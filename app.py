from flask import Flask
import os
from dotenv import load_dotenv
import mindmaps

load_dotenv()

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return {'status': 'Server is running!'}

if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))