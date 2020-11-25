from application import app
from flask  import session, render_template ,flash,json, request,redirect,url_for
from flask_wtf import FlaskForm
import os.path
from werkzeug.utils import secure_filename

@app.route('/',methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/url',methods=['GET','POST'])
def url():
    if request.method == 'POST':
        urls={}

        if os.path.exists('urls.json'):
            with open('urls.json') as urlfile:
                urls=json.load(urlfile)
    
        

        if request.form['short'] in urls.keys():
            flash('short name is choosen ,think another one','info')
            return render_template('main.html')
        if 'url' in request.form.keys():
            urls[request.form['short']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            filename=request.form['short']  + secure_filename(f.filename)
            f.save('C:\\flaskprojects\\flaskproject2\\'+filename)
            urls[request.form['short']] =  {'url':filename}
        with open('urls.json','w') as urlfile:
            json.dump(urls,urlfile)
    return redirect('/')


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('errorpage.html'),404