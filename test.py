from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        if email == "rizki@gmail.com" and password == "r" :
            return render_template('sukses.html')
        else:
            return redirect("/gagal")
    return render_template('index.html')
@application.route('/gagal')
def gagal():
    return render_template("home.html")
if __name__ == '__main__':
    application.run(debug=True)