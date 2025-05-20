# backend/manage.py
import os
import argparse
import psycopg2
from dotenv import load_dotenv

def initialize_database():
    # Load environment variables from .env file in the backend directory
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print(f"Loaded environment variables from {dotenv_path}")
    else:
        print(f".env file not found at {dotenv_path}. Attempting to use globally set environment variables.")

    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        print("Error: DATABASE_URL environment variable not set.")
        return

    # Construct path to schema.sql relative to this script's location
    # manage.py is in backend/, schema.sql is in database/
    # So, ../database/schema.sql from backend/
    schema_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'schema.sql')
    
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        return

    print(f"Found schema file at {schema_path}")
    print(f"Connecting to database using URL: {'*****'.join(db_url.split('@')) if '@' in db_url else 'similar to ' + db_url}") # Avoid printing password fully

    conn = None # Initialize conn to None for the finally block
    cur = None # Initialize cur to None
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        with open(schema_path, 'r') as f:
            sql_script = f.read()
        
        # Execute the entire script. psycopg2 can execute multi-statement strings.
        cur.execute(sql_script)
        conn.commit()
        
        print("Database initialized successfully. Tables created.")
        
    except psycopg2.Error as e:
        print(f"Error initializing database: {e}")
        if conn: # Rollback if connection was established
            conn.rollback()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Manage the Poker Cash Manager application.")
    parser.add_argument('command', choices=['initdb'], help="Command to execute.")
    
    args = parser.parse_args()
    
    if args.command == 'initdb':
        print("Initializing database...")
        initialize_database()
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()
