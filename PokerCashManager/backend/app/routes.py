# backend/app/routes.py
from flask import Blueprint, jsonify
# Ensure correct import from your database module
from .database import get_db_connection 

main_bp = Blueprint('main', __name__)

@main_bp.route('/health', methods=['GET'])
def health_check():
    db_status = "disconnected"
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1;')
        cur.fetchone()
        cur.close()
        # Connection is managed by g, no need to close here
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return jsonify(status="ok", database=db_status), 200
