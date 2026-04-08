from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="Notification Service is Up"), 200

@app.route('/notify')
def send_notify():
    return jsonify(message="Notification sent successfully!"), 200

if __name__ == '__main__':
    app.run(port=5003)
