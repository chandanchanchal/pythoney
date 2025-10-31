# OOP Mini-Curriculum: Classes, Inheritance, Polymorphism (Python)

**Duration:** 120 minutes  
**Audience:** Python freshers who just learned core data structures  
**Focus:** Classes/objects, encapsulation, inheritance, polymorphism, composition

---

## What’s included
- **Lab 1:** Employee Management Classes (starter + solution)
- **Quiz:** OOP Principles (with answer key)
- **Mini Project:** Library Management System using OOP
  - Starter with TODOs
  - Reference solution (clean)
  - Advanced solution (more inheritance/polymorphism)
  - Unit tests

---

## Suggested 120-minute agenda
1. **Kickoff (10 min)** — Recap OOP pillars & show end goal (Library app).
2. **Lab 1 (25 min)** — Employee classes: base/derived, payroll polymorphism.
3. **Mini Project Part A (45 min)** — Core Library features (add/search/checkout/return).
4. **Quiz (10 min)** — OOP principles (formative).
5. **Mini Project Part B (20 min)** — Extend with inheritance/polymorphism (items & fees).
6. **Wrap (10 min)** — Run tests, discuss design choices & trade-offs.

---

## Learning outcomes
- Model a domain with classes and objects.
- Use **inheritance** to share behavior and **polymorphism** to vary behavior.
- Encapsulate state with instance attributes and private helpers.
- Write small, cohesive methods and basic validations.
- Create a simple, testable command-style API (no heavy UI required).

---

## Rubric (10 pts)
- Correct class design & relationships: **3 pts**
- Core features working (add/search/checkout/return): **4 pts**
- Use of inheritance/polymorphism beyond trivial: **2 pts**
- Code quality (naming, docstrings, small methods): **1 pt**

---

## How to run
```bash
# Employee lab
python employee_lab_starter.py
# or
python employee_lab_solution.py

# Library mini project (starter/solutions)
python library_system_starter.py
# or
python library_system_solution.py
# or
python library_system_solution_advanced.py

# Run tests
python -m unittest tests_library_system.py -v
```
