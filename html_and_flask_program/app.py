from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/profile')
def profile():
    if "response" in session:
        return render_template("profile.html")
    return "<h1>Please Login First</h1>"


@app.route('/login')
def login():
    if "response" in session:
        return render_template("already_logined.html")
    return render_template("login.html")


@app.route('/success', methods= ["POST"])
def success():
    name = request.form.get("name")
    password = request.form.get("password")
    if name == "aditya" and password == "aditya":
        session["response"] = "aditya"
        return render_template("logined_successfully.html")
    return render_template("error.html")


@app.route("/logout")
def log_out():
    if "response" in session:
        session.clear()
        return render_template("log_out.html")
    return "<h1>You have'nt Logined to Log Out. So first login.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
