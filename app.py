from flask import Flask, request, render_template, redirect
# from flask_cors import CORS
import mysql.connector as db

app = Flask(__name__, instance_relative_config=True)
# CORS(app)

# instance/config.cfg と指定しなくてよい
# cfg は全て大文字
app.config.from_pyfile('config.cfg')


@app.route('/rin_jin/')
def hello_world():
    return render_template("top.html")


@app.route('/rin_jin/index/')
def index():
    # print(app.config["SERVER"])
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from word_table")
    word_table = cursor.fetchall()

    return render_template("index.html", word_table=word_table)



@app.route("/rin_jin/insert/", methods=["POST"])
def insert_db():
    name = request.form["name"]
    words = [name]
    for number in range(10):
        words.append(request.form["form{}".format(number)])
    join_point = ",".join(words)
    data_format = ",".join(["%s"] * 11)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO word_table(name,flag0,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9) values({})".format(
            data_format), tuple(join_point.split(",")))
    db_connection.commit()
    # インサート
    return redirect("https://reina-raft.xyz/rin_jin/index/", code=302)


@app.route("/rin_jin/edit/<Id>/", methods=["GET"])
def edit_show(Id):
    print(Id)
    ID = int(Id)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from word_table where id ={}".format(ID))
    word_table = cursor.fetchone()
    print(word_table)
    return render_template("form.html", word_table=word_table)


@app.route("/rin_jin/update/", methods=["POST"])
def update_db():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    ID = request.form["id"]
    name = request.form["name"]
    words = [name]
    for number in range(10):
        words.append(request.form["form{}".format(number)])
    data_format = ""
    for number in range(len(words)):
        if number == 0:
            data_format += "name='" + words[number] + "'"
        else:
            data_format += ",flag{}='".format(str(number - 1)) + words[number] + "' "

    cursor = db_connection.cursor()
    cursor.execute(
        "update word_table set {} where id ={}".format(data_format, ID))
    db_connection.commit()

    return redirect("https://reina-raft.xyz/rin_jin/index/", code=302)


@app.route("/rin_jin/delete/", methods=["POST"])
def delete_db():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    ID = request.form["id"]
    print(ID)
    cursor = db_connection.cursor()
    cursor.execute(
        "update word_table set delete_flag=TRUE where id ={}".format(ID))
    db_connection.commit()

    return redirect("https://reina-raft.xyz/rin_jin/index/", code=302)


@app.route("/rin_jin/limits/", methods=["GET"])
def limits():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from word_table")
    word_table = cursor.fetchall()

    return render_template("limits.html", word_table=word_table)


@app.route("/rin_jin/limits/start/", methods=["POST"])
def limits_start():
    left = request.form["left"]
    right = request.form["right"]
    word_table = [left, right]
    print(word_table)
    return render_template("start.html", word_table=word_table)


if __name__ == '__main__':
    app.run(host=app.config["HOST"])
