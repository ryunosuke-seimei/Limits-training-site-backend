from flask import Flask, request, render_template
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
    return 'Hello World!'


@app.route("/rin_jin/insert", methods=["POST"])
def insert_db():
    name= request.form["name"]
    sentences = request.form["sentences"]
    return "ok"


if __name__ == '__main__':
    app.run()

