"""
Log Analyzer (Starter)
---------------------
Build a tool that reads web server access logs and prints useful summaries.

Input: one or more log files (plain text). Example format (common/combined log-like):
127.0.0.1 - - [31/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.0.10 - - [31/Oct/2025:10:01:03 +0000] "POST /login HTTP/1.1" 401 512

Part A (core):
- Implement parse_line(line) -> dict with keys: ip, method, path, status, bytes, ts
- Analyze a file:
  - total requests
  - status code counts (e.g., 200, 404, 500)
  - top 5 IPs by request count
- Handle malformed lines: skip and count how many; print a warning at end

Part B (extensions):
- Support reading multiple files
- Export summary to CSV
- Optional: read .gz files transparently

Be sure to use try/except around file I/O and parsing.
"""

import re, csv, os, gzip
from datetime import datetime
from typing import Dict, List, Iterable

LOG_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<bytes>\d+|-)\s*$'
)

class ParseError(Exception):
    """Raised when a log line cannot be parsed."""

def parse_line(line: str) -> Dict[str, object]:
    """Parse a single line into fields. Raise ParseError on failure. (TODO)"""
    # TODO: implement using LOG_RE
    raise NotImplementedError

def open_maybe_gz(path: str):
    """Open text file or .gz file with utf-8 decoding. (TODO)"""
    # TODO
    raise NotImplementedError

def analyze_files(paths: List[str]) -> Dict[str, object]:
    """
    Return a summary dict with keys:
    total, status_counts (dict), top_ips (list of (ip, count)), malformed (int)
    """
    # TODO: implement accumulation with try/except for parsing
    raise NotImplementedError

def export_summary_csv(path: str, summary: Dict[str, object]) -> None:
    """Write a compact CSV with status_counts and top_ips. (TODO)"""
    # TODO
    raise NotImplementedError

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer_starter.py <logfile> [<logfile2> ...]")
        return
    try:
        summary = analyze_files(sys.argv[1:])
        print("Total requests:", summary["total"])
        print("Malformed lines:", summary["malformed"])
        print("Status counts:", summary["status_counts"])
        print("Top IPs:", summary["top_ips"][:5])
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
