from __future__ import annotations
from typing import List

class Employee:
    # TODO: define init with emp_id:int, name:str, base_pay:float
    # TODO: property validation for base_pay >= 0
    # TODO: method compute_pay(self) -> float (raise NotImplementedError)
    # TODO: __str__ to show "<Employee id name pay>"
    pass

class FullTimeEmployee(Employee):
    # TODO: add annual_salary: float; compute_pay returns monthly salary
    pass

class PartTimeEmployee(Employee):
    # TODO: hourly_rate: float; hours: float; compute_pay = rate * hours
    pass

class Manager(FullTimeEmployee):
    # TODO: team: List[Employee]; bonus_pct: float (0..1)
    # compute_pay = monthly + monthly * bonus_pct
    pass

def demo():
    pass

if __name__ == "__main__":
    demo()
