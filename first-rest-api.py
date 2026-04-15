from flask import Flask, jsonify
import mysql.connector

# Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    row_headers = [x[0] for x in mycursor.description]  # column names
    myresult = mycursor.fetchall()

    json_data = []
    for row in myresult:
        json_data.append(dict(zip(row_headers, row)))
    
    return jsonify(json_data)

@app.route("/air_transport")
def airTransport():
    query = "SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE transport = 'Air'"
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    units = mycursor.fetchall()

    json_data = []
    for row in units:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)

@app.route("/epic_units")
def epicUnits():
    query = "SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'Epic'"
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    units = mycursor.fetchall()

    json_data = []
    for row in units:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)

@app.route("/ground_target")
def groundTarget():
    query = "SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE target = 'Ground'"
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    units = mycursor.fetchall()

    json_data = []
    for row in units:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)

@app.route("/null_type")
def nullType():
    query = "SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE target = 'null'"
    mycursor.execute(query)
    row_headers = [x[0] for x in mycursor.description]
    units = mycursor.fetchall()

    json_data = []
    for row in units:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)
