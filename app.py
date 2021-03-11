from flask import Flask, request, render_template, redirect, url_for, jsonify
# from flask_cors import CORS
import mysql.connector as db

app = Flask(__name__, instance_relative_config=True)
# CORS(app)

# instance/config.cfg と指定しなくてよい
# cfg は全て大文字
app.config.from_pyfile('config.cfg')


@app.route('/rin_jin/')
def hello_world():
    return render_template("develop/home.html")


@app.route('/rin_jin/item')
def index_item():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select id, name from word_table where delete_flag = 0")
    word_table = cursor.fetchall()

    return render_template("develop/item.html", lists=word_table)


@app.route('/rin_jin/roulette')
def index_roulette():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select id, name from word_table where delete_flag = 0")
    word_table = cursor.fetchall()

    return render_template("develop/roulette.html", lists=word_table)


@app.route('/rin_jin/item-api', methods=["GET"])
def API_get():
    # ID = request.form["id"]
    # db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
    #                            database=app.config["DATABASES"])
    # cursor = db_connection.cursor()
    # cursor.execute("select * from word_table where id = {}".format(ID))
    # word_table = cursor.fetchone()
    # return jsonify(word_table)
    return jsonify("ok")


@app.route("/rin_jin/item-api", methods=["POST"])
def API_insert():
    #     name = request.form["name"]
    #     words = [name]
    #     for number in range(10):
    #         words.append(request.form["form{}".format(number)])
    #     join_point = ",".join(words)
    #     data_format = ",".join(["%s"] * 11)
    #     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
    #                                database=app.config["DATABASES"])
    #     cursor = db_connection.cursor()
    #     cursor.execute(
    #         "INSERT INTO word_table(name,flag0,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9) values({})".format(
    #             data_format), tuple(join_point.split(",")))
    #     db_connection.commit()
    return jsonify("ok")


@app.route('/rin_jin/item-api', methods=["PUT"])
def API_update():
    # data = request.json
    # ID = data["id"]
    # name = data["name"]
    # words = data["words"]
    # words.insert(0, name)
    # data_format = ""
    # for number in range(len(words)):
    #     if number == 0:
    #         data_format += "name='" + words[number] + "'"
    #     else:
    #         data_format += ",flag{}='".format(str(number - 1)) + words[number] + "' "
    #
    # db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
    #                            database=app.config["DATABASES"])
    # cursor = db_connection.cursor()
    # cursor.execute(
    #     "update word_table set {} where id ={}".format(data_format, ID))
    # db_connection.commit()

    return jsonify("ok")


@app.route('/rin_jin/item-api', methods=["DELETE"])
def API_delete():
    # db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
    #                            database=app.config["DATABASES"])
    # ID = request.form["id"]
    # cursor = db_connection.cursor()
    # cursor.execute(
    #     "update word_table set delete_flag=TRUE where id ={}".format(ID))
    # db_connection.commit()
    return jsonify("ok")


if __name__ == '__main__':
    app.run(host=app.config["HOST"])
