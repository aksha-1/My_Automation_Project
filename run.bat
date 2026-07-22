@echo off

cd /d E:\Akshay\2026_Job_Document\My_Automation_Project

call .venv\Scripts\activate

python -m pytest -v -s Test_cases ^
-m regression ^
--browser=chrome ^
--html=Reports\report.html
exit /b 0