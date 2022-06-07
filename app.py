from flask import Flask, request

app = Flask(__name__)


@app.route("/echo", methods=['POST'])
def echo():
    return request.json


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
