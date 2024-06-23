from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html",
                           rows=8,
                           cols=8)

@app.route("/<num>")
def homepage4(num):
        return render_template("index.html",rows =int(num),
                               cols=int(num))

@app.route("/<rows>/<cols>")
def x_and_y(rows,cols):
     return render_template("index.html",rows =int(rows),
                            cols=int(cols))







if __name__ == "__main__":
    app.run(debug=True,port=5000)