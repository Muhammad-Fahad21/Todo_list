from flask import Flask, request, jsonify
from flask_cors import CORS  
import psycopg2

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host='db-container',
        database='postgres',
        user='postgres',
        password='secret'
    )
    return conn

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        task = data['task']
        cur.execute("INSERT INTO tasks (description) VALUES (%s)", (task,))
        conn.commit()
        message = {'message': 'Task added'}
        status = 201
    else:
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
        message = [{'id': row[0], 'task': row[1]} for row in rows]
        status = 200

    cur.close()
    conn.close()
    return jsonify(message), status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
