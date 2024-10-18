from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from models.model import probe_model_5l_profit

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    if not request.json or 'data' not in request.json:
        return jsonify({'error': 'No data provided'}), 400
    
    data = request.json['data']
    result = probe_model_5l_profit(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, request, render_template, jsonify
# import json
# from models.model import probe_model_5l_profit

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part'})
#         file = request.files['file']
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'})
#         if file:
#             data = json.load(file)
#             result = probe_model_5l_profit(data['data'])
#             return jsonify(result)
#     return render_template('uploads.html')

# @app.route('/results')
# def results():
#     return render_template('results.html')

# if __name__ == '__main__':
#     app.run(debug=True)