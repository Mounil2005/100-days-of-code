from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from Tkinter (localhost)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_text = data.get('task')
    if task_text:
        tasks.append({'task': task_text, 'done': False})
        return jsonify({'message': 'Task added successfully'}), 201
    return jsonify({'error': 'No task provided'}), 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        data = request.get_json()
        tasks[task_id]['done'] = data.get('done', tasks[task_id]['done'])
        return jsonify({'message': 'Task updated'}), 200
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
