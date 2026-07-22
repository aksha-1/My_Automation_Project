import pytest
from Database.employee_queries import EmployeeQueries


class TestEmployeeDatabase:
    @pytest.mark.skip
    def test_verify_employee_exists(self, db):

        query = EmployeeQueries.get_employee()

        employee = db.fetch_one(query, (101,))

        assert employee is not None
    @pytest.mark.skip
    def test_verify_employee_name(self, db):

        query = EmployeeQueries.get_employee()

        employee = db.fetch_one(query, (101,))

        assert employee["first_name"] == "Akshay"
    @pytest.mark.skip
    def test_verify_employee_department(self, db):

        query = EmployeeQueries.get_employee()

        employee = db.fetch_one(query, (101,))

        assert employee["department"] == "QA"