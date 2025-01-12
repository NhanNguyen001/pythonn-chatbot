from typing import Annotated

from dotenv import load_dotenv
from fastapi import FastAPI, Form
from openai import OpenAI

load_dotenv()

app = FastAPI()

chat_log = []

client = OpenAI()


@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
    chat_log.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_log,
        temperature=0.6,
    )

    bot_response = response.choices[0].message.content

    chat_log.append({"role": "assistant", "content": bot_response})

    return bot_response
