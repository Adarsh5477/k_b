from flask import Flask, request, jsonify
from flask_cors import CORS
from .models.model import probe_model_5l_profit  # Updated import path

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    if not request.json or 'data' not in request.json:
        return jsonify({'error': 'No data provided'}), 400
    
    data = request.json['data']
    result = probe_model_5l_profit(data)
    return jsonify(result)

# Required for Vercel
app.debug = False
