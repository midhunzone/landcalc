from flask import Flask, render_template, request, jsonify
import csv
from io import StringIO

app = Flask(__name__)
data = []

@app.route('/')
def index():
    total_are = sum(row['area_in_are'] for row in data)
    total_cents = sum(row['area_in_cents'] for row in data)
    return render_template('index.html', data=data, total_are=total_are, total_cents=total_cents)

@app.route('/add', methods=['POST'])
def add_row():
    survey_number = request.form['survey_number']
    area_in_are = float(request.form['area_in_are'])
    area_in_cents = area_in_are * 2.47105
    data.append({
        'survey_number': survey_number,
        'area_in_are': area_in_are,
        'area_in_cents': round(area_in_cents, 2)
    })
    return jsonify(success=True)

@app.route('/delete', methods=['POST'])
def delete_row():
    index = int(request.form['index'])
    if 0 <= index < len(data):
        data.pop(index)
    return jsonify(success=True)

@app.route('/download')
def download_csv():
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Survey Number', 'Area in Are', 'Area in Cents'])
    for row in data:
        cw.writerow([row['survey_number'], row['area_in_are'], row['area_in_cents']])
    output = si.getvalue()
    return output, 200, {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment;filename=land_data.csv'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
