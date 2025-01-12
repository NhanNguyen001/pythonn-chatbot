from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if __name__ == "__main__":
    openai = OpenAI()
    chat_log = []
    while True:
        user_input = input()
        if user_input.lower() == "stop":
            break

        chat_log.append({"role": "user", "content": user_input})

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=chat_log,
            temperature=0.6,
        )

        bot_response = response.choices[0].message.content

        chat_log.append({"role": "assistant", "content": bot_response})

        print(bot_response)
