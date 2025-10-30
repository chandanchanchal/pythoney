"""
Contact Book - Starter
----------------------
Finish the TODOs. Run `python -m unittest tests_contact_book.py -v` to check progress.

Recommended steps:
1) Implement core functions: add_contact, search_contacts, delete_contact, list_contacts.
2) Wire them into the CLI menu (see `run_cli`).
3) (Stretch) Implement save_contacts and load_contacts for JSON persistence.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

Contact = Dict[str, object]   # Convenience alias
Book = Dict[str, Contact]     # contact_id -> contact

def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def add_contact(book: Book, name: str, phones: List[str], email: Optional[str]=None, tags: Optional[List[str]]=None) -> str:
    """
    TODO: Create a new contact id (e.g., using timestamp+counter or len(book)).
    Store a contact dict with keys: name, phones, email, tags, created_at.
    Return the contact id as a string.
    """
    raise NotImplementedError

def search_contacts(book: Book, query: str) -> Book:
    """
    TODO: Case-insensitive substring match over name, email, phones, and tags.
    Return a dict of {id: contact} for matches.
    Tip: Convert everything to strings and compare with `in`.
    """
    raise NotImplementedError

def delete_contact(book: Book, contact_id: str) -> bool:
    """
    TODO: Remove contact by id. Return True if deleted, False if not found.
    """
    raise NotImplementedError

def list_contacts(book: Book) -> Book:
    """
    TODO: Return a new dict of contacts sorted by contact['name'] (ascending).
    Hint: sort keys using `sorted(..., key=lambda cid: book[cid]['name'].lower())`
    """
    raise NotImplementedError

# --- Stretch: persistence ---
def save_contacts(book: Book, path: str) -> None:
    """
    TODO: Save contacts to JSON file. Make sure sets are turned into lists.
    """
    raise NotImplementedError

def load_contacts(path: str) -> Book:
    """
    TODO: Load contacts from JSON file. Ensure missing file returns empty dict.
    """
    raise NotImplementedError

# --- CLI ---
def _prompt_list(label: str) -> List[str]:
    raw = input(f"{label} (comma-separated, leave empty for none): ").strip()
    if not raw:
        return []
    # split by comma and strip spaces
    return [p.strip() for p in raw.split(",") if p.strip()]

def run_cli():
    book: Book = {}
    print("=== Contact Book ===")
    print("Commands: add | search | delete | list | save | load | quit")

    while True:
        cmd = input("> ").strip().lower()
        if cmd == "add":
            name = input("Name: ").strip()
            phones = _prompt_list("Phones")
            email = input("Email (optional): ").strip() or None
            tags = _prompt_list("Tags")
            try:
                cid = add_contact(book, name, phones, email, tags)
                print(f"Added with id: {cid}")
            except Exception as e:
                print(f"Error: {e}")
        elif cmd == "search":
            q = input("Query: ").strip()
            results = search_contacts(book, q)
            if not results:
                print("No matches.")
            else:
                for cid, c in list_contacts(results).items():
                    print(f"[{cid}] {c['name']} | {', '.join(c.get('phones', []))} | {c.get('email','-')} | tags: {', '.join(c.get('tags', []))}")
        elif cmd == "delete":
            cid = input("Contact id: ").strip()
            ok = delete_contact(book, cid)
            print("Deleted." if ok else "Not found.")
        elif cmd == "list":
            for cid, c in list_contacts(book).items():
                print(f"[{cid}] {c['name']} | {', '.join(c.get('phones', []))} | {c.get('email','-')} | tags: {', '.join(c.get('tags', []))}")
        elif cmd == "save":
            path = input("Path to save (default contacts.json): ").strip() or "contacts.json"
            try:
                save_contacts(book, path)
                print(f"Saved to {path}")
            except Exception as e:
                print(f"Error saving: {e}")
        elif cmd == "load":
            path = input("Path to load (default contacts.json): ").strip() or "contacts.json"
            book = load_contacts(path)
            print(f"Loaded {len(book)} contacts from {path}")
        elif cmd in ("quit", "exit"):
            print("Bye!")
            break
        elif not cmd:
            continue
        else:
            print("Unknown command. Try: add | search | delete | list | save | load | quit")

if __name__ == "__main__":
    run_cli()
