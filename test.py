import os
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect, secure_filename

UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):  
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@application.route('/sukses', methods=['GET', 'POST'])
def sukses():
    if request.method == 'POST':        
        if 'file' not in request.files:
            return render_template('sukses.html')
        file = request.files['file']
        
        if file.filename == '':
            return render_template('sukses.html')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            return render_template('result.html',
                    msg='Sukses Upload, Thankyou!',
                    img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('sukses.html')


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