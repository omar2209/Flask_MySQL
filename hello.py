from flask import Flask, render_template # Uso Render Template per reindirizzare, è una funzione di Flask
import mysql.connector

app = Flask(__name__)

def get_db_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        password="password123",
        database="CLASH_ROYALE"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Clash_Unit")
    results = cursor.fetchall()
    cursor.close()
    mydb.close()
    return results

@app.route("/")
def show_units():
    units = get_db_data()
    return render_template("index.html", units=units)

if __name__ == "__main__":
    app.run(debug=True)
