# backend/app/config.py
import os
from dotenv import load_dotenv

# Construct path to .env file located in the 'backend' directory
# This assumes config.py is in backend/app/
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print(f".env file not found at {dotenv_path}. Make sure it exists in the 'backend' directory.")


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'postgresql://user:password@localhost:5432/poker_cash_manager_db'
