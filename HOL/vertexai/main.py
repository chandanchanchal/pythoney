from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)
client = bigquery.Client()

@app.route('/getClaimStatus')
def get_claim():
    claim_id = request.args.get('claim_id')

    query = f"""
    SELECT * FROM `YOUR_PROJECT_ID.insurance_ds.claims`
    WHERE claim_id = '{claim_id}'
    LIMIT 1
    """

    results = client.query(query).result()

    for row in results:
        return jsonify({
            "claim_id": row.claim_id,
            "status": row.status,
            "amount": row.amount,
            "next_steps": "No action needed" if row.status=="Approved" else "Under review"
        })

    return jsonify({"error": "Claim not found"})
