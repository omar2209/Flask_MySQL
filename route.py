from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        password="password123",
        database="MedicalImages"
    )

@app.route('/')
def home():
    return "<h1>Benvenuto all'API InsuranceData</h1><p>Usa le route disponibili per ottenere dati:</p><ul>" \
           "<li>/insurance</li>" \
           "<li>/insurance/region?name=region_name</li>" \
           "<li>/insurance/smokers/count</li>" \
           "<li>/insurance/bmi/stats</li></ul>"


@app.route('/insurance', methods=['GET'])
def get_insurance_data():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM InsuranceData LIMIT 10")
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'age': row[1],
            'sex': row[2],
            'bmi': row[3],
            'children': row[4],
            'smoker': row[5],
            'region': row[6],
            'charges': row[7]
        })
    return jsonify(data)

@app.route('/insurance/region', methods=['GET'])
def get_by_region():
    region = request.args.get('name')
    if not region:
        return jsonify({"error": "Parametro 'name' mancante"}), 400

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM InsuranceData WHERE region = %s LIMIT 10", (region,))
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'age': row[1],
            'sex': row[2],
            'bmi': row[3],
            'children': row[4],
            'smoker': row[5],
            'region': row[6],
            'charges': row[7]
        })
    return jsonify(data)

@app.route('/insurance/smokers/count', methods=['GET'])
def count_smokers():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT smoker, COUNT(*) FROM InsuranceData GROUP BY smoker")
    rows = cursor.fetchall()
    cursor.close()
    db.close()

    result = {row[0]: row[1] for row in rows}
    return jsonify(result)

@app.route('/insurance/bmi/stats', methods=['GET'])
def bmi_stats():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT AVG(bmi), MIN(bmi), MAX(bmi) FROM InsuranceData")
    avg_bmi, min_bmi, max_bmi = cursor.fetchone()
    cursor.close()
    db.close()

    stats = {
        "average_bmi": round(avg_bmi, 2),
        "min_bmi": round(min_bmi, 2),
        "max_bmi": round(max_bmi, 2)
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
