from flask import Flask, jsonify
from flask_cors import CORS # Critical for frontend-backend communication

app = Flask(__name__)
CORS(app) # This allows the stylish frontend to fetch data from this API

@app.route("/api/status")
def get_status():
    # Sending real data to the terminal
    return jsonify({
        "status": "OPERATIONAL",
        "uptime": "99.9%",
        "message": "Connection to Backend established via Flask 🚀"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
