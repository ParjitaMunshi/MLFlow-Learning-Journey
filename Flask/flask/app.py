from flask import Flask


###WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. This should be an amazing code"

@app.route("/index")
def index():
    return "This should be an amazing code"

if __name__ == "__main__":
    app.run(debug=True)