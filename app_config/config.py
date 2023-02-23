import sys
sys.path.append("../.env")

from pydantic import BaseSettings

class Settings(BaseSettings):
    app_org : str = "org-fbZKeNIBMA7bM7bNIj96xYk7"
    open_api : str = "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"

