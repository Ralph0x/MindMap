from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

mind_map = {}

@app.route('/status', methods=['GET'])
def status():
    app.logger.info("Checking server status")
    return {'status': 'Server is running!'}

@app.route('/mindmap', methods=['GET', 'POST'])
def handle_mind_map():
    if request.method == 'POST':
        data = request.json
        if not data or not isinstance(data, dict):
            app.logger.warning("Invalid or missing data in POST request")
            return jsonify({"error": "Invalid or missing data"}), 400
        
        for key, value in data.items():
            mind_map[key] = value
        app.logger.info("Mind map updated via POST request")
        return jsonify({"message": "Mind map updated", "current_map": mind_map}), 200
    
    elif request.method == 'GET':
        app.logger.info("Mind map retrieved via GET request")
        return jsonify(mind_map), 200

if __name__ == '__main__':
    app_port = os.getenv('PORT', 5000)
    app.run(port=int(app_port))