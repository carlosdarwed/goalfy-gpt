# sys imports
import os
import sys 
sys.path.append("../.")
sys.path.append("../config")
sys.path.append(".")

# imports
from functools import lru_cache
import openai
import json
from fastapi import FastAPI
from app_config.config import Settings
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request model declaration
class TextPrompt(BaseModel):
    prompt : str

# cache so the settings don't reload every new request
@lru_cache()
def get_settings():
    return Settings()

@app.get("/")
async def status():
    return  {"status" : "all good !"}

@app.post("/generate_prompt")
async def generate_prompt(userInput : TextPrompt):

    ''' The "generate_prompt" route takes the user_input and
    sends it to the open-ai api, once done, it formats a json and return.'''

    openai.organization = get_settings().app_org
    openai.api_key = get_settings().open_api
    resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=userInput.prompt,
        max_tokens=500,
        temperature=0
    )
    result = (resp.choices[0].text).replace("\n", '').replace("/", '')
    return json.loads(result)