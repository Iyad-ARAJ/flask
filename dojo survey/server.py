# from flask import Flask,render_template,request

# app= Flask(__name__)

# @app.route("/")
# def base():
#      return render_template("base.html")

# @app.route("/result",methods=['post'])
# def index():
#      location = request.form['location']
#      language = request.form['language']
#      comment =request.form['comment']

#      return render_template("index.html",name=name,location=location,language=language,comment=comment)
# if __name__ == "__main__":
#      app.run(debug=True,port=5000)
from flask import Flask,render_template,request,redirect,session
app= Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route("/")
def base():
     return render_template("base.html")

@app.route("/result",methods=['post'])
def index():
     session['username'] = request.form['name']
     session['location'] = request.form['location']
     session['language'] = request.form['language']
     session['comment'] = request.form['language']
     return redirect("/show")
@app.route("/show")
def show_results():
     return render_template("index.html",name =session['username'] ,location = session['location'],
                              language = session['language'] ,
                              comment =session['comment'])

if __name__ == "__main__":
     app.run(debug=True,port=5000)


