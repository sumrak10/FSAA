import os

from dotenv import load_dotenv

load_dotenv()

# DATABASE
DB=os.environ.get("DB")
DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_NAME=os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")


# ALL
DATETIME_FORMAT='%Y-%m-%dT%H:%M:%S.%f'