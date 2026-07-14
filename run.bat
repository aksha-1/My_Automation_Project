@echo off

cd /d %WORKSPACE%

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python -m pytest -v -s Test_cases -m regression --browser=edge --html=Reports\report.html --self-contained-html