from flask import Flask, request, render_template
from flask_mysqldb import MySQL 
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

mysql = MySQL(app)
#conexion base de datos 

app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")


@app.route("/")
def index():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)