import loadenv, os

# loadenv()


class Settings():
    DATABASE_URL = os.environ.get("DATABASE_URL", None)

settings = Settings()