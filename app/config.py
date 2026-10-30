import os
from dotenv import load_dotenv


load_dotenv()


class Settings():
    DATABASE_URL = os.environ.get("DATABASE_URL", None)

settings = Settings()