from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' #kendi sifresin gir
app.config['MYSQL_DATABASE_DB'] = 'sakila'  #database adı
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

def executeCommand(command):
    cursor.execute("SELECT * from sakila.actor where actor_id = 10")
    data = cursor.fetchall()
    return data
