import pytest
from Database.employee_queries import EmployeeQueries


class TestEmployeeDatabase:

    def test_verify_employee_exists(self, db):

        query = EmployeeQueries.get_employee()

        employee = db.fetch_one(query, (101,))

        assert employee is not None

    def test_verify_employee_name(self, db):

        query = EmployeeQueries.get_employee()

        employee = db.fetch_one(query, (101,))

        assert employee["first_name"] == "Akshay"

    def test_verify_employee_department(self, db):

        query = EmployeeQueries.get_employee()

        employee = db.fetch_one(query, (101,))

        assert employee["department"] == "QA"