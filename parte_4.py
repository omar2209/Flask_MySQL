import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS MedicalImages")
mycursor.execute("USE MedicalImages")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS InsuranceData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    sex VARCHAR(10),
    bmi FLOAT,
    children INT,
    smoker VARCHAR(10),
    region VARCHAR(20),
    charges FLOAT
);
""")

# Pulisco tabella
mycursor.execute("DELETE FROM InsuranceData")
mydb.commit()

# Leggo CSV aggiornato (con header)
csv_path = '/workspaces/MySQL-Flask/insurance.csv'
data = pd.read_csv(csv_path)

print("Prime 10 righe del CSV:")
print(data.head(10))

insert_sql = """
INSERT INTO InsuranceData (age, sex, bmi, children, smoker, region, charges)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
for _, row in data.iterrows():
    mycursor.execute(insert_sql, (
        int(row['age']),
        row['sex'],
        float(row['bmi']),
        int(row['children']),
        row['smoker'],
        row['region'],
        float(row['charges'])
    ))
mydb.commit()

print("Dati inseriti con successo.")

mycursor.execute("SELECT * FROM InsuranceData LIMIT 10")
results = mycursor.fetchall()
for r in results:
    print(r)
