from flask import Flask, request, render_template, redirect, url_for, jsonify
# from flask_cors import CORS
import mysql.connector as db
import json

app = Flask(__name__, instance_relative_config=True)
# CORS(app)

# instance/config.cfg と指定しなくてよい
# cfg は全て大文字
app.config.from_pyfile('config.cfg')


@app.route('/rin_jin/item-api', methods=["GET"])
def API_get():
    flag = request.args.get("flag")
    print(flag)
    if flag == "0":
        # print("All")
        db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                                   database=app.config["DATABASES"])
        cursor = db_connection.cursor()
        cursor.execute("select id, name from word_table where delete_flag = 0")
        word_table = cursor.fetchall()

    elif flag == "1":
        # print("A")
        ID = request.args.get("id")
        db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                                   database=app.config["DATABASES"])
        cursor = db_connection.cursor()
        cursor.execute("select id,name,flag0,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9 from word_table where id = {}".format(ID))
        word_table = cursor.fetchone()

    elif flag == "2":
        db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                                   database=app.config["DATABASES"])
        cursor = db_connection.cursor()
        cursor.execute("select name,flag0,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9 from word_table where delete_flag = 0")
        word_table = cursor.fetchall()
        result = []
        for word in word_table:
            temp_result = {"title": word[0], "value": word[1:]}
            result.append(temp_result)
        word_table = result
    else:
        word_table = "non data"

    return jsonify(word_table)


@app.route("/rin_jin/item-api", methods=["POST"])
def API_insert():
    data = json.loads(request.json["data"])
    title = data["title"]
    form_list = data["data"]
    values = [title]
    for form in form_list:
        values.append(form["value"])

    data_format = ",".join(["%s"] * 11)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO word_table(name,flag0,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8,flag9) values({})".format(
            data_format), tuple(values))
    db_connection.commit()
    return jsonify("ok")


@app.route('/rin_jin/item-api', methods=["PUT"])
def API_update():
    print(request.get_data())
    data = json.loads(request.json["data"])
    form_list = data["data"]
    ID = data["id"]
    title = data["title"]
    values = [title]
    for form in form_list:
        values.append(form["value"])

    data_format = ""
    for number in range(len(values)):
        if number == 0:
            data_format += "name='" + values[number] + "'"
        else:
            data_format += ",flag{}='".format(str(number - 1)) + values[number] + "'"

    print("update word_table set {} where id = {}".format(data_format, ID))

    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "update word_table set {} where id ={}".format(data_format, ID))
    db_connection.commit()

    return jsonify("ok")


@app.route('/rin_jin/item-api', methods=["DELETE"])
def API_delete():
    ID = json.loads(request.get_data())["id"]
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "update word_table set delete_flag=TRUE where id ={}".format(ID))
    db_connection.commit()
    return jsonify("ok")


if __name__ == '__main__':
    app.run(host=app.config["HOST"])
