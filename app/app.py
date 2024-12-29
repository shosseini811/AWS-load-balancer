from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return jsonify({
        'message': 'Hello from AWS Load Balancer Demo!',
        'hostname': hostname
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
