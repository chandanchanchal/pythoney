# Mini Project Lab: Contact Book (Search, Add, Delete)

**Duration:** 120 minutes  
**Audience:** Python freshers (covered: lists, tuples, sets, dicts)  
**Goal:** Build a menu-driven Contact Book CLI that lets users add, search, delete, and list contacts. Use core data structures and (optionally) JSON persistence.

---

## Learning outcomes
- Choose appropriate data structures for real-world data.
- Implement CRUD operations with dictionaries, lists, and sets.
- Write modular functions and basic input validation.
- (Stretch) Save & load contacts from a JSON file.

---

## Time plan (120 minutes)
1. **Warm-up & brief (10 min)** — Explain data model and demo expected behavior.
2. **Part A: Core features (45 min)** — Add, search, delete, list (in-memory).
3. **Checkpoint & quick test (5 min)** — Verify with provided test script.
4. **Part B: Persistence (30 min)** — Save/Load to `contacts.json` (JSON).
5. **Stretch & polish (20 min)** — Partial search, tags, multiple phones, sorting.

---

## Data model
Use a dictionary keyed by a generated contact id (string). Each contact is a dictionary:
```python
{
  "name": "Ada Lovelace",
  "phones": ["+44-1234-567"],
  "email": "ada@example.com",
  "tags": ["friend", "work"],
  "created_at": "2025-10-30T10:00:00"
}
```
- `phones`: list of strings  
- `tags`: list or set; store as list in JSON, cast to `set` in memory if desired.

---

## Milestones & checks
- **M1:** Add contact returns contact id and stores the contact.
- **M2:** Search supports case-insensitive substring on name/email/phones/tags.
- **M3:** Delete removes by id; return `True/False`.
- **M4:** List shows all contacts in a stable sorted order by name.
- **M5 (Stretch):** Save/Load round-trips all fields to `contacts.json`.

---

## Files in this bundle
- `contact_book_starter.py` — skeleton with TODOs.
- `contact_book_solution.py` — reference solution (core + JSON persistence).
- `contact_book_solution_advanced.py` — adds input validation & nicer printing.
- `tests_contact_book.py` — quick unit tests (run with `python -m unittest`).
- `contacts_sample.json` — sample data you can load.
- This README.

---

## How to run
```bash
# 1) Run the app (starter or solution)
python contact_book_starter.py
# or
python contact_book_solution.py

# 2) Run tests
python -m unittest tests_contact_book.py -v
```

---

## Suggested rubric (10 pts)
- Data model & functions (add/search/delete/list): **4 pts**
- Menu & UX flow: **2 pts**
- Search quality (partial & case-insensitive): **2 pts**
- Persistence (save/load): **1 pt**
- Code quality (naming, small functions, docstrings): **1 pt**

---

## Stretch ideas
- Prevent duplicate names (or merge strategy).
- Export to CSV.
- Pretty table output.
- Support birthday and search by month.
- Undo last delete (keep a stack/list).
- Import from CSV with simple parsing.
