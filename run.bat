@echo off

echo ====================================
echo Starting Automation Execution
echo ====================================

cd /d E:\Akshay\2026_Job_Document\My_Automation_Project

call .venv\Scripts\activate
@REM chrome

@REM pytest -s -v  --html=Reports/regression_chrome.html Test_cases -n=2 -m regression  --browser=chrome
@REM pytest -s -v  --html=Reports/smoke_chrome.html Test_cases -n=2  -m "smoke" --browser=chrome

@REM edge 
pytest -s -v  --html=Reports/regression_edge.html Test_cases -n=2 -m regression  --browser=edge
@REM pytest -s -v  --html=Reports/smoke_edge.html Test_cases -n=2  -m "smoke" --browser=edge
echo.
echo ====================================
echo Automation Execution Completed
echo ====================================

pause