from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="Chat Service is Up"), 200

@app.route('/messages')
def get_messages():
    return jsonify(messages=[{"from": "Harry", "text": "Hello Jenkins!"}]), 200

if __name__ == '__main__':
    app.run(port=5002)
