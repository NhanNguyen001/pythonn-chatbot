from typing import Annotated

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chat_log = [
    {
        "role": "system",
        "content": "You are a Python tutor AI, completely dedicated to teach users how to learn \
                        Python from scratch. Please provide clear instructions on Python concepts, \
                        best practices and syntax. Help create a path of learning for users to be able \
                        to create real life, production ready python applications.",
    }
]

client = OpenAI()


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


chat_responses = []


@app.post("/")
async def chat(request: Request, user_input: Annotated[str, Form()]):
    chat_log.append({"role": "user", "content": user_input})
    chat_responses.append(user_input)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_log,
        temperature=0.6,
    )

    bot_response = response.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    chat_responses.append(bot_response)

    return templates.TemplateResponse(
        "home.html", {"request": request, "chat_responses": chat_responses}
    )
