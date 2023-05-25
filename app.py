from flask import Flask, render_template, request, json
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route("/")
def index():
    return render_template(template_name_or_list="index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = SignUpForm()
    return render_template("cadastro.html", form=form)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()