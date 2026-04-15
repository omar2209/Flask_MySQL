import mysql.connector
from flask import Flask

#Connect to mysql
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
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

@app.route("/air_transport")
def airTransport():
    query = "SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE transport = 'Air'"
    mycursor.execute(query)
    units = mycursor.fetchall()
    return str(units)

@app.route("/epic_units")
def epicUnits():
    query = "SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE rarity = 'Epic'"
    mycursor.execute(query)
    units = mycursor.fetchall()
    return str(units)

