import os
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        if email == "siti@gmail.com" and password == "r" :
            return redirect('/sukses')
        else:
            return redirect("/gagal")
    return render_template('index.html')

@application.route('/gagal')
def gagal():
    return render_template("home.html")

@application.route('/sukses')
def sukses():
    return render_template("sukses.html")

@application.route('/home')
def Beranda():
    return render_template("home.html")

@application.route('/proses',methods = ['GET','POST'])
def upload():
    if request.method=='POST':
        file = request.file['file']
        file.save(os.path.join("static/uploads", file.filename))
        return render_template('upload.html', message="Berhasil")
    return render_template('sukses.html')


@application.route('/signup')
def signup():
    return render_template("Signup.html")
if __name__ == '__main__':
    application.run(debug=True)