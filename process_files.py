import os
import openai

# Get API key from environment variable
API_KEY = os.getenv('OPENAI_API_KEY')
CUSTOM_MODEL_ID = 'g-D5VNzVh5P-codexpress'  # Model ID for your custom GPT model

if not API_KEY:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = API_KEY

def get_custom_model_suggestions(prompt):
    response = openai.ChatCompletion.create(
        model=CUSTOM_MODEL_ID,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048
    )
    return response.choices[0].message["content"].strip()

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    prompt = f"Provide suggestions to improve the following code:\n\n{content}"
    suggestions = get_custom_model_suggestions(prompt)

    with open(file_path, 'a') as file:
        file.write("\n\n// CodeXpress Suggestions:\n")
        file.write(suggestions)

def main():
    repo_path = os.path.dirname(os.path.abspath(__file__))  # Use the current script location
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.cs'):  # Process only C# files, adjust as necessary
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    main()
