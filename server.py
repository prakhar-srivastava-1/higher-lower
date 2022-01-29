from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Guess a number between 0 and 9!</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:guess>")
def guess_number(guess):
    return f"{guess}"


if __name__ == "__main__":
    app.run(debug=True)
