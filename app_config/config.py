import os
import sys
sys.path.append("../.env")

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_org : str = os.getenv("ORG_KEY")
    open_api : str = os.getenv("OPENAI_KEY")

