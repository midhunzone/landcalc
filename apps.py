from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    survey_number = data['survey_number']
    are_value = float(data['are_value'])
    cents_value = round(are_value * 2.47105, 2)
    return jsonify({'survey_number': survey_number, 'are_value': are_value, 'cents_value': cents_value})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
