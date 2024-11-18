import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')

def set_up():
    load_dotenv()

    config = {
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "port": os.getenv("DB_PORT"),
    }
    return config


if __name__ == "__main__":
    print(set_up())
