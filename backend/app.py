from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running successfully"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/db-check")
def db_check():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = connection.cursor()
        cursor.execute("SELECT version();")

        db_version = cursor.fetchone()

        cursor.close()
        connection.close()
        
        return jsonify({
            "database": "connected",
            "version": db_version
        })

    except Exception as e:
        return jsonify({
            "database": "failed",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    print("Starting Flask backend...")
    app.run(host="0.0.0.0", port=5000)



