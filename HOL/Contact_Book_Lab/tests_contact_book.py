import unittest
import os
import json

# Try to import student starter (functions may be NotImplemented).
# Also test the reference solution to show expected behavior.
import importlib.util

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

BASE = os.path.dirname(__file__)
starter_path = os.path.join(BASE, "contact_book_starter.py")
solution_path = os.path.join(BASE, "contact_book_solution.py")

S = load_module(starter_path, "student")
R = load_module(solution_path, "reference")

class ContactBookTests(unittest.TestCase):
    def setUp(self):
        self.book = {}

    def test_add_and_list_solution(self):
        cid1 = R.add_contact(self.book, "Alice", ["111"], "alice@example.com", ["friend"])
        cid2 = R.add_contact(self.book, "Bob", ["222"], None, ["work"])
        self.assertIn(cid1, self.book)
        self.assertIn(cid2, self.book)
        listed = list(R.list_contacts(self.book).keys())
        self.assertEqual(listed, sorted(listed, key=lambda i: self.book[i]["name"].lower()))

    def test_search_solution(self):
        R.add_contact(self.book, "Alice", ["111"], "alice@example.com", ["friend"])
        R.add_contact(self.book, "Bob", ["222"], None, ["work"])
        self.assertTrue(R.search_contacts(self.book, "ali"))
        self.assertTrue(R.search_contacts(self.book, "222"))
        self.assertTrue(R.search_contacts(self.book, "work"))
        self.assertFalse(R.search_contacts(self.book, "zzz"))

    def test_delete_solution(self):
        cid = R.add_contact(self.book, "Charlie", ["333"], None, [])
        ok = R.delete_contact(self.book, cid)
        self.assertTrue(ok)
        self.assertNotIn(cid, self.book)
        self.assertFalse(R.delete_contact(self.book, "does-not-exist"))

    def test_persistence_solution(self):
        R.add_contact(self.book, "Dana", ["444"], "d@example.com", ["vip"])
        path = os.path.join(BASE, "test_contacts.json")
        try:
            R.save_contacts(self.book, path)
            loaded = R.load_contacts(path)
            self.assertEqual(len(loaded), len(self.book))
        finally:
            if os.path.exists(path):
                os.remove(path)

    # Optional: starter smoke tests (won't fail if NotImplemented)
    def test_starter_functions_exist(self):
        for fn in ("add_contact", "search_contacts", "delete_contact", "list_contacts"):
            self.assertTrue(hasattr(S, fn))

if __name__ == "__main__":
    unittest.main()
