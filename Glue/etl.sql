-- Glue Studio → Visual ETL → Transform: SQL Query
-- Parent node alias (Node name): raw_orders
-- This is the only code learners write in Lab 2.

SELECT
  CAST(order_id AS STRING) AS order_id,
  CAST(order_ts AS TIMESTAMP) AS order_ts,
  CAST(TO_DATE(order_ts) AS DATE) AS order_date,
  UPPER(TRIM(region)) AS region,
  LOWER(TRIM(channel)) AS channel,
  LOWER(TRIM(category)) AS category,
  CAST(sku AS STRING) AS sku,
  CAST(qty AS INT) AS qty,
  CAST(unit_price AS DOUBLE) AS unit_price,
  CAST(currency AS STRING) AS currency,
  LOWER(TRIM(status)) AS status,
  CASE
    WHEN campaign IS NULL OR TRIM(campaign) = '' THEN 'unattributed'
    ELSE LOWER(TRIM(campaign))
  END AS campaign,
  CAST(customer_id AS STRING) AS customer_id,
  CAST(qty AS INT) * CAST(unit_price AS DOUBLE) AS line_amount,
  CASE
    WHEN LOWER(TRIM(status)) = 'paid' THEN CAST(qty AS INT) * CAST(unit_price AS DOUBLE)
    WHEN LOWER(TRIM(status)) = 'refunded' THEN -1 * CAST(qty AS INT) * CAST(unit_price AS DOUBLE)
    ELSE 0.0
  END AS gmv_usd
FROM raw_orders
WHERE order_id IS NOT NULL
  AND TRIM(CAST(order_id AS STRING)) <> ''
  AND qty IS NOT NULL
  AND TRIM(CAST(qty AS STRING)) <> ''
  AND unit_price IS NOT NULL
  AND TRIM(CAST(unit_price AS STRING)) <> ''
  AND TRIM(CAST(unit_price AS STRING)) <> 'N/A'
  AND CAST(qty AS INT) > 0
  AND CAST(unit_price AS DOUBLE) > 0
