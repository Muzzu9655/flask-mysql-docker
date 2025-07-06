from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = pymysql.connect(
            host='mysql-db',
            user='testuser',
            password='testpass',
            database='testdb'
        )
        return "Connected to MySQL from Flask via Docker!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
