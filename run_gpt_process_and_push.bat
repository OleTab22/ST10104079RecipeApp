@echo off
SET REPO_PATH=%cd%
SET PYTHON_SCRIPT=%REPO_PATH%\process_files.py
SET GITHUB_BRANCH=main

REM Set the OpenAI API key environment variable
SET OPENAI_API_KEY=sk-proj-gwMinQlCp2w3PKEjkNfYT3BlbkFJc7FyuSQB7kSmuU3x1HeS  # Replace with your actual API key

REM Run the Python script to process files and get suggestions from CodeXpress
python %PYTHON_SCRIPT%

REM Navigate to the repository
cd %REPO_PATH%

REM Stage the changes
git add .

REM Commit the changes
git commit -m "Apply CodeXpress suggestions to the code"

REM Push the changes
git push origin %GITHUB_BRANCH%

echo Changes pushed successfully!
pause
