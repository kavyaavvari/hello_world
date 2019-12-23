from flask import Flask, render_template
app = Flask(__name__)


app.route("/")
def hello():
    return "Hello World!"


@app.route("/kavya")
def hello_kavya():
    return render_template('hello_kavya.html')


if __name__ == "__main__":
    app.run()



