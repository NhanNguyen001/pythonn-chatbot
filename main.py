from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    openai = OpenAI()
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."}]
    )

    print(response)