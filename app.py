from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/test-route')
def hello_world():
    return "I'd added test route"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
