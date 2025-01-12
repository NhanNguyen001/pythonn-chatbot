from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if __name__ == "__main__":
    openai = OpenAI()
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the CEO of Apple."},
            # {
            #     "role": "assistant",
            #     "content": "The Spurs won the 2005 NBA Championship.",
            # },
            {
                "role": "user",
                "content": "Who was on the team?",
            },
        ],
    )
    # response.choices[0].message.content

    print(response.choices[0].message.content)
