from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='testPython'
app.config['MYSQL_DATABASE_HOST']='localhost'

mysql = MySQL(app)
CORS(app)

@app.route('/api/severity', methods['GET'])
def get_all_severity():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select * from severity")
    data=cursor.fetchall()
    # console.log(data)
    print(data)