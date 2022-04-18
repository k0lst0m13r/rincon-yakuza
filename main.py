from flask import Flask
from flask import render_template
import forms

app = Flask(__name__)

@app.route("/")
def index():
    name = 'index'
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/sala")
def sala():
    return render_template("base/sala.html")

@app.route("/peli")
def peli():
    return render_template("peli.html")

@app.route('/form')
def formu():
    comment_form = forms.CommentForm()
    return render_template('form.html', form = comment_form)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
