import os, sys
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template

UPLOAD_FOLDER = 'uploads/'

#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sys.path.append(os.path.abspath('PINet'))

def predict(img_path):
    from PINet.test import PINet_Tester
    tester = PINet_Tester()
    output_path = tester.test_image(img_path)
    return output_path

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/templates/<fname>', methods=['GET'])
def template(fname):
    return render_template(fname)

# Upload API
@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print("saved file successfully")
        # send file name as parameter to downlad

        # predict the result
        _ = predict(filepath)
        return redirect('/downloadfile/'+ filename)

    return render_template('upload_file.html')

# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    input_filename = filename
    prediction_filename = os.path.splitext(filename)[0] + '_output.png'
    return render_template('download.html', origin=input_filename, output=prediction_filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))
