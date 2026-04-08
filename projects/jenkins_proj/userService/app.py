from flask import Flask, jsonify
# jus added commento test parallel execution of stages
app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="User Service is Up"), 200

@app.route('/users')
def get_users():
    return jsonify(users=["Harry", "Gemini", "DevOps-Bot"]), 200

if __name__ == '__main__':
    app.run(port=5001)
