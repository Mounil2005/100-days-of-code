# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Boolean, default=False)

# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     tasks = Task.query.all()
#     return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks])

# @app.route('/tasks', methods=['POST'])
# def add_task():
#     data = request.json
#     new_task = Task(title=data['title'])
#     db.session.add(new_task)
#     db.session.commit()
#     return jsonify({"message": "Task added"}), 201

# @app.route('/tasks/<int:id>', methods=['PUT'])
# def update_task(id):
#     task = Task.query.get_or_404(id)
#     task.completed = not task.completed
#     db.session.commit()
#     return jsonify({"message": "Task updated"})

# @app.route('/tasks/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task = Task.query.get_or_404(id)
#     db.session.delete(task)
#     db.session.commit()
#     return jsonify({"message": "Task deleted"})

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)



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
