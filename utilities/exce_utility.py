import openpyxl
from openpyxl import load_workbook

class DDT:
    @staticmethod
    def get_login_data():
        workbook = load_workbook(".\\TestData\\DDT.xlsx")
        sheet = workbook["Sheet1"]
        data = []
        for row in sheet.iter_rows(min_row=2,values_only=True):
            data.append(row)
        return data
    

