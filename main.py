from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"hello {name} and your age is {number}"



if __name__ == "__main__":
    app.run(debug = True)