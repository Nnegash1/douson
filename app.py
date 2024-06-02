from flask import Flask, render_template
#from form import RegistrationForm
app = Flask(__name__)

# @app.route("/temp")
# def temp():
#     return render_template("temp.html")
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/form")
def form():
    return render_template("form.html")

# @app.route("/register")
# def RegistrationForm():
#     form = RegistrationForm()
#     return render_template("registerForm.html", title='Register', form=form)
#
# @app.route("/Login")
# def RegistrationForm():
#     form = LoginForm()
#     return render_template("Login.html", title='Login', form=form)

if __name__== "__main__":
    app.run(debug=True)
    #db.create_all()
