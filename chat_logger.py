from flask import Flask, request, jsonify
from data_bot_logger import FILE_NAME

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_message():
    data = request.get_json(force=True)
    message = (data.get('message') or '').strip()
    if not message:
        return jsonify({'error': 'Empty message'}), 400
    with open(FILE_NAME, 'a', encoding='utf-8') as f:
        f.write(message + '\n')
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
