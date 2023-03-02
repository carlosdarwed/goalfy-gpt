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
from fastapi import FastAPI, HTTPException, status
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
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role" : "user", "content" : userInput.prompt}],
        temperature=0
    )
    result = (resp.choices[0].message.content).replace("\n", '').replace("/", '')
    try:
        return json.loads(result) 
    except:
        raise HTTPException(
        status_code=400,
        detail=f'[err-api]: the current prompt is not a valid JSON object')

        
    