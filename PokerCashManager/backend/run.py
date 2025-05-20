# backend/run.py
import os
# Assuming 'app' directory is at the same level as 'run.py'
from app import create_app 
from dotenv import load_dotenv

# Load .env file from the 'backend' directory (where run.py is)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print(f".env file not found at {dotenv_path}. Make sure it exists. Using default or environment-set DATABASE_URL.")

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5001))
    # Set debug=False if FLASK_ENV is 'production', otherwise True
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
