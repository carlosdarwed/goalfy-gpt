# sys imports

import os
import sys 
sys.path.append("../.")
sys.path.append("../config")
sys.path.append("../request")

# imports

from functools import lru_cache
import openai
import json
from fastapi import FastAPI
from app_config.config import Settings
from request.body_request import TextPrompt

app = FastAPI()

# cache so the settings don't reload every new request

@lru_cache()
def get_settings():
    return Settings()

@app.get("/")
async def status():
    return  {"status" : "all good !"}

@app.post("/generate_prompt")
async def generate_prompt(userInput : TextPrompt):
    openai.organization = "org-fbZKeNIBMA7bM7bNIj96xYk7"
    openai.api_key = get_settings().open_api
    resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=userInput.prompt,
        max_tokens=500,
        temperature=0
    )
    result = (resp.choices[0].text).replace("\n", '').replace("/", '')
    return json.loads(result)
    
# yey that was a very complex program