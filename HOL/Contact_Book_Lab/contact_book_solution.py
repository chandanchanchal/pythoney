"""
Contact Book - Reference Solution (Core + JSON persistence)
"""
import json
from datetime import datetime
from typing import Dict, List, Optional

Contact = Dict[str, object]
Book = Dict[str, Contact]

def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def _new_id(book: Book) -> str:
    # Simple incremental id as string
    return str(len(book) + 1)

def add_contact(book: Book, name: str, phones: List[str], email: Optional[str]=None, tags: Optional[List[str]]=None) -> str:
    if not name:
        raise ValueError("name is required")
    if phones is None:
        phones = []
    if tags is None:
        tags = []
    cid = _new_id(book)
    book[cid] = {
        "name": name,
        "phones": list(phones),
        "email": email,
        "tags": list(tags),
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
    return {cid: book[cid] for cid in sorted(book.keys(), key=lambda cid: book[cid]["name"].lower())}

# --- Persistence ---
def save_contacts(book: Book, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)

def load_contacts(path: str) -> Book:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Basic validation
            if not isinstance(data, dict):
                return {}
            return {str(k): v for k, v in data.items()}
    except FileNotFoundError:
        return {}
    
# --- CLI ---
def _prompt_list(label: str) -> List[str]:
    raw = input(f"{label} (comma-separated, leave empty for none): ").strip()
    if not raw:
        return []
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
