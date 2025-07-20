from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    health_data = {
        "status": "healthy",
        "timestamp": time.time(),
        "message": "Service is running"
    }
    return jsonify(health_data), 200

@app.route('/')
def home():
    return "Hello! Visit /health to check service status"

if __name__ == '__main__':
    # Use environment variable for port (required for Render)
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
