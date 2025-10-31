"""
CSV Lab (Starter)
-----------------
Tasks:
1) Read products from `products_input.csv`. Each row: id,name,price,qty
2) Validate: id is non-empty; price & qty are numbers and >= 0
3) Compute: total_value = price * qty per row; and grand totals
4) Write cleaned rows to `products_clean.csv` with new column total_value
5) Handle errors:
   - File not found -> print friendly message and exit
   - Malformed row -> skip it, log to `errors.log` with the reason
Use csv module and context managers.
"""

import csv
from typing import List, Tuple

INPUT_PATH = "products_input.csv"
OUTPUT_PATH = "products_clean.csv"
ERROR_LOG = "errors.log"

def read_products(path: str) -> List[Tuple[str, str, float, int]]:
    """Return list of valid rows as tuples; skip invalid with logging (TODO)."""
    # TODO: implement with proper try/except, csv.reader, and validation
    raise NotImplementedError

def write_products(path: str, rows: List[Tuple[str, str, float, int]]) -> None:
    """Write rows with a computed total_value column (TODO)."""
    # TODO
    raise NotImplementedError

def main():
    try:
        rows = read_products(INPUT_PATH)
        write_products(OUTPUT_PATH, rows)
        print(f"Wrote {len(rows)} cleaned rows to {OUTPUT_PATH}")
    except FileNotFoundError:
        print(f"Input file not found: {INPUT_PATH}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
