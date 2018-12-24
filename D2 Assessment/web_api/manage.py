import os
from dotenv import load_dotenv

from app import create_app, db

dotenv_path = os.path.join(os.path.dirname(__name__), '.env')
load_dotenv(dotenv_path)

app = create_app(os.environ.get('FLASK_CONFIG') or 'development')
