from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!'


@app.route('/testing/')
def testing():
    return '<h1>Testing, bitch!!!</h1>'

if __name__ == '__main__':
    app.run()
