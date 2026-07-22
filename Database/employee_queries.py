class EmployeeQueries:

    @staticmethod
    def get_employee(employee_id):
        return """
        SELECT *
        FROM employee
        WHERE employee_id=%s
        """

    @staticmethod
    def delete_employee(employee_id):
        return """
        DELETE FROM employee
        WHERE employee_id=%s
        """