# In your app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Toe San, Flask App Successfully Deployed update 2.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Important: host='0.0.0.0'
