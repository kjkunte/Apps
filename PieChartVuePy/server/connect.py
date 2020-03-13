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

# Error Handling has to be done
@app.route('/api/severity/', methods=['GET'])
def get_all_severity():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select severity, count(eventId) from severity group by severity")
    data=cursor.fetchall()
    # print(data)
    # return data
    return jsonify({'severity':data})


if __name__ == '__main__':
    app.run(debug=True)