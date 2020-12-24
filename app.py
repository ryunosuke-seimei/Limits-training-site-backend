from flask import Flask, request, render_template, redirect
from flask_cors import CORS
import mysql.connector as db

app = Flask(__name__, instance_relative_config=True)
CORS(app)

# instance/config.cfg と指定しなくてよい
# cfg は全て大文字
app.config.from_pyfile('config.cfg')


# mariadb_connection = db.connect(host='localhost', user='ryu', password='reina001', database='ryu_db')
# cursor = mariadb_connection.cursor()
# cursor.execute(
#     "INSERT INTO temp_sentence(LINE_id, sentence) values(%s, %s)", (user_id, message))
# mariadb_connection.commit()


@app.route('/rin_jin/')
def hello_world():
    print(app.config["SERVER"])
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"], database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from word_table")
    word_table = cursor.fetchall()

    return render_template("index.html", word_table=word_table)


@app.route('/rin_jin/create/', methods=["GET"])
def get_some_path():
    return render_template("form.html")


@app.route("/rin_jin/insert/", methods=["POST"])
def insert_db():
    name = request.form["name"]
    sentences = request.form["sentences"]
    print(name)
    print(sentences)
    # インサート
    return redirect("https://reina-raft.xyz/rin_jin/", code=302)


@app.route("/rin_jin/edit/<Id>", methods=["GET"])
def edit_show(Id):
    print(Id)
    ID = int(Id)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"], database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from word_table where id ={}".format(ID))
    word_table = cursor.fetchone()
    return render_template("form.html", word_table=word_table)


@app.route("/rin_jin/update", methods=["POST"])
def update_db():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"], database=app.config["DATABASES"])
    ID = request.form["id"]
    name = request.form["name"]
    sentences = request.form["sentences"]

    # cursor = db_connection.cursor()
    # cursor.execute(
    #     "update word_table set  where id ={}".format(ID))

    return redirect("https://reina-raft.xyz/rin_jin/", code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
