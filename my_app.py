from flask import Flask, jsonify
import logging
import random
import time

app = Flask(__name__)


logging.basicConfig(filename='system.log', level=logging.INFO)


@app.route('/check_updates')
def check_updates():
    updates_available = random.choice([True, False])  # 随机模拟是否有更新
    if updates_available:
        logging.info('Updates available.')
        return jsonify({'status': 'success', 'updates': 'Updates are available and ready to install.'}), 200
    else:
        logging.info('No updates available.')
        return jsonify({'status': 'success', 'updates': 'System is up to date.'}), 200


@app.route('/monitor_resources')
def monitor_resources():
    cpu_usage = random.randint(10, 90)
    memory_usage = random.randint(10, 90)
    logging.info(f'CPU usage: {cpu_usage}%, Memory usage: {memory_usage}%')
    return jsonify({'cpu': cpu_usage, 'memory': memory_usage}), 200


@app.route('/handle_failure')
def handle_failure():
    logging.error('System failure detected. Executing recovery procedures.')

    time.sleep(1)
    logging.info('System recovery completed successfully.')
    return jsonify({'status': 'recovered'}), 200

if __name__ == '__main__':
    app.run(debug=True)
