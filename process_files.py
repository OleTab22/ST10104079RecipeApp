import os
import openai

# Replace with your OpenAI API key and custom model ID
API_KEY = 'sk-svcacct-AMXsEyVqynpMpZi3ZLqzT3BlbkFJhcJ6wnx7qAnd3j7il7dx'
CUSTOM_MODEL_ID = 'your_custom_model_id'  # Model ID for your custom GPT model

def get_custom_model_suggestions(prompt):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        model=CUSTOM_MODEL_ID,  # Use your custom model ID
        prompt=prompt,
        max_tokens=2048  # Increase this value to the maximum tokens you require
    )
    return response.choices[0].text.strip()

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    prompt = f"Provide suggestions to improve the following code:\n\n{content}"
    suggestions = get_custom_model_suggestions(prompt)

    with open(file_path, 'a') as file:
        file.write("\n\n# GPT-4 Suggestions:\n")
        file.write(suggestions)

def main():
    repo_path = os.path.dirname(os.path.abspath(__file__))  # Use the current script location
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):  # Process only Python files, adjust as necessary
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    main()
