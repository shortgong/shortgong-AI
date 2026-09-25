import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'vic6969!!')
DB_DATABASE = os.getenv('DB_DATABASE', 'shortgong1')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'none')