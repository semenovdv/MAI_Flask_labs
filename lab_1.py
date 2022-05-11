from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world_print():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
