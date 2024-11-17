from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Endpoint to fetch all session data
@app.route("/api/sessions", methods=["GET"])
def get_sessions():
    conn = sqlite3.connect("network_traffic.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions")
    sessions = cursor.fetchall()
    conn.close()

    # Return data in JSON format
    return jsonify([
        {
            "session_key": session[0],
            "src_ip": session[1],
            "dst_ip": session[2],
            "protocol": session[3],
            "src_port": session[4],
            "dst_port": session[5],
            "packet_count": session[6],
            "total_volume": session[7],
        } for session in sessions
    ])

if __name__ == "__main__":
    app.run(debug=True)
