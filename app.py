from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

mysql = MySQL(app)
# conexion base de datos
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
app.secret_key = os.getenv("CAC_PYTHON_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        try:
            data = request.form
            email = data["email"]
            password = data["password"]

            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM users WHERE email = %s AND password = %s",
                (email, password),
            )
            user = cur.fetchone()

            if user:
                print(user)
                session["userId"] = user[0]
                session["username"] = user[1]
                return redirect(url_for("index"))

            else:
                return redirect("/login")

        except Exception as e:
            return jsonify({"message": str(e)}), 500

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        try:
            data = request.form
            name = data["name"]
            email = data["email"]
            password = data["password"]

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password),
            )
            mysql.connection.commit()
            cur.close()
            return redirect(url_for("login"))
        except Exception as e:
            return jsonify({"message": str(e)}), 500
    return render_template("register.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    session.pop("role", None)
    return redirect("/login")


@app.route("/agregar", methods=["POST"])
def agregar_pelicula():
    if request.method == "POST":
        try:
            data = request.form
            titulo = data["titulo"]
            anio = data["anio"]
            descripcion = data["descripcion"]
            portada = data["portada"]
            categoria = data["categoria"]

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO peliculas (titulo,anio,descripcion,portada,categoria) VALUES (%s, %s, %s, %s,%s)",
                (titulo, anio, descripcion, portada, categoria),
            )
            mysql.connection.commit()
            cur.close()
            return redirect("/peliculas")
        except Exception as e:
            return jsonify({"message": str(e)}), 500


@app.route("/peliculas")
def get_peliculas():
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM peliculas")
        data = cur.fetchall()
        cur.close()
        return render_template("peliculas.html", data=data)
    else:
        return redirect("/login")


@app.route("/peliculas/<int:id>")
def get_pelicula(id):
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM peliculas WHERE id = %s", (id,))
        data = cur.fetchone()
        cur.close()
        return render_template("pelicula.html", data=data)
    else:
        return redirect("/login")


@app.route("/peliculas/<int:id>/delete")
def delete_pelicula(id):
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM peliculas WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return redirect("/peliculas")
    else:
        return redirect("/login")


@app.route("/peliculas/<int:id>/update", methods=["POST"])
def update_pelicula(id):
    if "username" in session:
        if request.method == "POST":
            try:
                data = request.form
                titulo = data["titulo"]
                anio = data["anio"]
                descripcion = data["descripcion"]
                portada = data["portada"]
                categoria = data["categoria"]

                cur = mysql.connection.cursor()
                cur.execute(
                    "UPDATE peliculas SET titulo = %s, anio = %s, descripcion = %s, portada = %s, categoria = %s WHERE id = %s",
                    (titulo, anio, descripcion, portada, categoria, id),
                )
                mysql.connection.commit()
                cur.close()
                return redirect("/peliculas")
            except Exception as e:
                return jsonify({"message": str(e)}), 500
    else:
        return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
