from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'mysql_db'  # or your MySQL host
app.config['MYSQL_DATABASE_USER'] = 'testuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'testpass'
app.config['MYSQL_DATABASE_DB'] = 'testdb'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def hello():
    return "Flask-MySQL App Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
