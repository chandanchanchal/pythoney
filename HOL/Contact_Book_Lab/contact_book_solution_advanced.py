"""
Contact Book - Advanced Reference (validation, pretty list, stable ids)
"""
import json, re, uuid
from datetime import datetime
from typing import Dict, List, Optional

Contact = Dict[str, object]
Book = Dict[str, Contact]

def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def _new_id(_: Book) -> str:
    # UUID for stability across sessions
    return uuid.uuid4().hex[:8]

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def _valid_email(email: Optional[str]) -> bool:
    return (email is None) or bool(EMAIL_RE.match(email))

def add_contact(book: Book, name: str, phones: List[str], email: Optional[str]=None, tags: Optional[List[str]]=None) -> str:
    if not name or not name.strip():
        raise ValueError("name is required")
    if not _valid_email(email):
        raise ValueError("invalid email")
    phones = [p.strip() for p in (phones or []) if p.strip()]
    tags = [t.strip().lower() for t in (tags or []) if t.strip()]
    # Optional: dedupe
    phones = list(dict.fromkeys(phones))
    tags = list(dict.fromkeys(tags))
    cid = _new_id(book)
    book[cid] = {
        "name": name.strip(),
        "phones": phones,
        "email": email,
        "tags": tags,
        "created_at": _now_iso(),
    }
    return cid

def _match_str(hay: str, needle: str) -> bool:
    return needle.lower() in hay.lower()

def search_contacts(book: Book, query: str) -> Book:
    q = (query or "").strip()
    if not q:
        return {}
    results: Book = {}
    for cid, c in book.items():
        fields = [c.get("name",""), c.get("email","") or ""]
        fields += c.get("phones", [])
        fields += c.get("tags", [])
        for f in fields:
            if _match_str(str(f), q):
                results[cid] = c
                break
    return results

def delete_contact(book: Book, contact_id: str) -> bool:
    return book.pop(contact_id, None) is not None

def list_contacts(book: Book) -> Book:
    return {cid: book[cid] for cid in sorted(book.keys(), key=lambda cid: (book[cid]["name"].lower(), book[cid].get("email","") or ""))}

def save_contacts(book: Book, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)

def load_contacts(path: str) -> Book:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {}
            return {str(k): v for k, v in data.items()}
    except FileNotFoundError:
        return {}

def _format_contact(cid: str, c: Contact) -> str:
    phones = ", ".join(c.get("phones", [])) or "-"
    email = c.get("email") or "-"
    tags = ", ".join(c.get("tags", [])) or "-"
    return f"[{cid}] {c['name']:<20} | {phones:<18} | {email:<24} | tags: {tags}"

def run_cli():
    book: Book = {}
    print("=== Contact Book (Advanced) ===")
    print("Commands: add | search | delete | list | save | load | quit")

    while True:
        cmd = input("> ").strip().lower()
        if cmd == "add":
            name = input("Name: ").strip()
            phones = [p.strip() for p in input("Phones (comma-separated): ").split(",") if p.strip()]
            email_raw = input("Email (optional): ").strip() or None
            if email_raw and not _valid_email(email_raw):
                print("Invalid email. Try again.")
                continue
            tags = [t.strip() for t in input("Tags (comma-separated): ").split(",") if t.strip()]
            try:
                cid = add_contact(book, name, phones, email_raw, tags)
                print(f"Added with id: {cid}")
            except Exception as e:
                print(f"Error: {e}")
        elif cmd == "search":
            q = input("Query: ").strip()
            results = search_contacts(book, q)
            if not results:
                print("No matches.")
            else:
                header = f"{'ID':<10} {'Name':<20} {'Phones':<20} {'Email':<26} Tags"
                print(header)
                print("-"*len(header))
                for cid, c in list_contacts(results).items():
                    print(_format_contact(cid, c))
        elif cmd == "delete":
            cid = input("Contact id: ").strip()
            ok = delete_contact(book, cid)
            print("Deleted." if ok else "Not found.")
        elif cmd == "list":
            header = f"{'ID':<10} {'Name':<20} {'Phones':<20} {'Email':<26} Tags"
            print(header)
            print("-"*len(header))
            for cid, c in list_contacts(book).items():
                print(_format_contact(cid, c))
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
