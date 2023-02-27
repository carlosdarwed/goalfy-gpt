import os
import sys

from pydantic import BaseSettings

class Settings(BaseSettings):
    app_org : str = os.environ["ORG_KEY"]
    open_api : str = os.environ["OPENAI_KEY"]

