import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-key')
    CITY_NAME = os.getenv('CITY_NAME', 'Karachi')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', '')
    DATABASE = os.path.join('instance', 'cityfinder.db')