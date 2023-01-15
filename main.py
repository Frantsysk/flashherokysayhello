from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = '12345678'


@app.route("/")
def index():
    flash("Wanna get a greet?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")


# app.run(debug=True, port=33500)