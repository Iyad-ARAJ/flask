from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("base.html",
                           title ="base")

@app.route("/play")
def play():
    return render_template("play.html",
                           title="play",
                           custom_css="play")

@app.route("/play/<num>")
def play_count(num):
    return render_template("playnum.html",
                           title="play_num",
                           num = int(num),
                           custom_css="play")

@app.route("/play/<num>/<color>")
def play_count_color(num,color):
    return render_template("playnum_color.html",
                           title="play_num_color",
                           num = int(num),
                           color=color,
                           custom_css="play")


if __name__ == "__main__":
    

    app.run(debug=True,port=5000)

