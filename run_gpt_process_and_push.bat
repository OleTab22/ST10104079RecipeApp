@echo off
SET REPO_PATH=%cd%
SET PYTHON_SCRIPT=%REPO_PATH%\process_files.py
SET GITHUB_BRANCH=main

REM Run the Python script to process files and get suggestions from the custom GPT model
python %PYTHON_SCRIPT%

REM Navigate to the repository
cd %C:\TabaneTechSolutions\CustomAi\ST10104079RecipeApp%

REM Stage the changes
git add .

REM Commit the changes
git commit -m "Apply custom GPT model suggestions to the code"

REM Push the changes
git push origin %GITHUB_BRANCH%

echo Changes pushed successfully!
pause
