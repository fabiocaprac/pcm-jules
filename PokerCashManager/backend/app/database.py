# backend/app/database.py
import psycopg2
import psycopg2.extras # For dictionary cursor
from flask import current_app, g, Flask

def get_db_connection(): # Renamed to avoid conflict if 'db' is used for something else in g
    if 'db_conn' not in g:
        try:
            g.db_conn = psycopg2.connect(current_app.config['DATABASE_URL'])
        except psycopg2.OperationalError as e:
            print(f"Database connection error: {e}")
            raise
    return g.db_conn

def close_db_connection(e=None): # Renamed
    db_conn = g.pop('db_conn', None)
    if db_conn is not None:
        db_conn.close()

def init_app_db(app: Flask):
    app.teardown_appcontext(close_db_connection)
    try:
        # Test connection during app initialization
        # This requires an app context
        with app.app_context():
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT 1;")
            cur.fetchone()
            cur.close()
            # Don't close the connection here, teardown_appcontext will do it
            print("Database connection successful on app init.")
    except Exception as e:
        print(f"Failed to connect to database on app init: {e}")
        # Depending on the desired behavior, you might want to re-raise the exception
        # or prevent the app from starting if the DB is critical.

def query_db(query, args=(), one=False):
    db_conn = get_db_connection()
    # Always create a new cursor for each operation with 'with' statement for proper resource management
    try:
        with db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(query, args)
            if cur.description: # Check if query returns rows (e.g. SELECT)
                results = cur.fetchall()
                if one:
                    return results[0] if results else None
                return results
            else: # For INSERT, UPDATE, DELETE that might not return rows
                return None 
        # The commit should happen after the cursor is used, typically before closing the connection
        # or as part of a transaction management strategy.
        # For simplicity, committing after each successful query_db call if it's not a SELECT.
        # More robust transaction management might be needed for complex operations.
        if not query.strip().upper().startswith("SELECT"):
             db_conn.commit()
    except psycopg2.Error as e: # Catch psycopg2 specific errors
        if db_conn:
            db_conn.rollback() # Rollback on error
        print(f"Database query error: {e}")
        raise
    # The connection is managed by g and closed by teardown_appcontext
