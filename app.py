from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template("index.html")


@app.route('/about')
def about():
    return  render_template("about.html")

@app.route('/services')
def services():
    return  render_template("service.html")

@app.route('/why')
def why():
    return  render_template("why.html")

@app.route('/team')
def team():
    return  render_template("team.html")

@app.route("/register")
def register():
    return  render_template("register.html")

@app.route('/login')
def login():
    return  render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

