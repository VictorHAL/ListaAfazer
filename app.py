from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
import uuid
from datetime import datetime

app = Flask(__name__, template_folder='templates')
CORS(app)

TASKS_FILE = 'tasks.json'
MAX_TASKS = 10

# ──────────────────────────────────────────
# Helpers de persistência
# ──────────────────────────────────────────

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def capitalize_first(text: str) -> str:
    return text[0].upper() + text[1:] if text else text

# ──────────────────────────────────────────
# Rotas
# ──────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()

    # Validação de entrada
    if not text:
        return jsonify({'error': 'O texto da tarefa não pode estar vazio.'}), 400

    tasks = load_tasks()

    # Regra de negócio: limite de 10 tarefas
    if len(tasks) >= MAX_TASKS:
        return jsonify({'error': f'Limite máximo de {MAX_TASKS} tarefas atingido.'}), 400

    # Regra de negócio: formatação automática
    text = capitalize_first(text)

    task = {
        'id': str(uuid.uuid4()),
        'text': text,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }

    tasks.append(task)
    save_tasks(tasks)

    return jsonify(task), 201

@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    original_len = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]

    if len(tasks) == original_len:
        return jsonify({'error': 'Tarefa não encontrada.'}), 404

    save_tasks(tasks)
    return jsonify({'success': True})

@app.route('/api/tasks/<task_id>', methods=['PATCH'])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({'error': 'Tarefa não encontrada.'}), 404

# ──────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────

if __name__ == '__main__':
    print("\n  ✦  TODO LIST — Backend rodando em http://localhost:5000\n")
    app.run(debug=True, port=5000)
