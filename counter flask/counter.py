from flask import Flask ,render_template,redirect,session,request
app = Flask(__name__)
app.secret_key ="super_secret_key"


@app.route("/")
def index():
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit']=1
    return render_template("index.html")
@app.route('/destroy_session')
def destroy():
    session.clear()
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)



