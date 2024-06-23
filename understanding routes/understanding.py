from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "hello world!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return f"HI {name}"

@app.route("/repeat/<int:num>/<name>")
def repeat(num,name):
    return f"{num * name}"

@app.errorhandler(404)
def page_not_found(e):
    return "sorry , the page not found.Error 404"

if __name__ == "__main__":
    app.run(debug=True,port=5000)