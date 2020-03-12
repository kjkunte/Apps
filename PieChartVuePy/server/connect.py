from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='testPython'
app.config['MYSQL_DATABASE_HOST']='localhost'

mysql = MySQL(app)
CORS(app)
api = Api(app)


@app.route('/api/severity', methods=['GET'])
def get_all_severity():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select * from severity")
    data=cursor.fetchall()
    # print()
    # return data
    return jsonify({'data':data})


# @app.route('/api/severityWeekly', methods=['GET'])
# def get_week_severity():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("select * from severity where ")
#     data=cursor.fetchall()
#     # print()
#     # return data
#     return jsonify({'data':data})

# @app.route('/api/severityMonthly', methods=['GET'])
# def get_today_severity():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("select * from severity where ")
#     data=cursor.fetchall()
#     # print()
#     # return data
#     return jsonify({'data':data})

if __name__ == '__main__':
    app.run(debug=True)