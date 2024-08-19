from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def pod_name():
    # Get the pod name from the environment variable 'HOSTNAME'
    pod_name = os.environ.get('HOSTNAME', 'Pod name not found')
    return f'Hello from pod: {pod_name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

