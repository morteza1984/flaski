from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello CI/CD", 200


def my_sum(a: int, b: int) -> int:
    return a+b


if __name__ == "__main__":
    app.run(debug=True)
