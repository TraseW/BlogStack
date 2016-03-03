

from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session
import os, datetime, json






app = Flask(__name__)


pageLocation = os.path.join(os.path.abspath(os.path.join(app.static_folder, '..')), 'pages')
import template
from admin import checkPassword

app.secret_key= 'test'


def checkCredentials(sessionInfo):
    try:
        timeDiff = (datetime.datetime.now() - sessionInfo['login_date']).days
        if sessionInfo['logged_in'] and timeDiff > 1:
            return False
        else:
            return True


    except:
        return False




@app.route('/')
def hello_world():

    return render_template('nav.html')


@app.route('/pages/<name>')
def getPage(name):
    content = template.getPage(name)
    print('here')
    print(content['content'])
    return render_template('post.html', post=content['content'])

@app.route('/api/pages/<name>/meta')
def apiGetPage(name):
    content = template.getPage(name)
    print(content)
    return json.dumps(content)

@app.route('/api/pages/<name>/meta/<tag>')
def apiGetTag(name, tag):
    page = template.getPage(name)[name]
    meta = page['meta']
    out = meta[tag]
    return out

@app.route('/api/pages')
def apiGetPages():

    return  json.dumps(os.listdir(pageLocation))


@app.route('/admin/create', methods=['POST', 'GET'])
def createPage():
    if (request.method == 'POST'):
        r = list(dict(request.form).keys())[0]
        pageDict = json.loads(str(r))
        print('test')
        print(pageDict)
        checkPage = template.createPage(pageDict)
        if checkPage != 'success':
            return checkPage
        return redirect(url_for('adminLogin'))
    else:
        return 'You should not be here!'

@app.route('/admin', methods=['POST', 'GET'])
def adminLogin():

    if checkCredentials(session):
        return render_template('panel.html')
    else:
        return redirect(url_for('logout'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    print(request.method)
    if (request.method == 'POST'):
        if checkPassword(request.form['password']):
            session['logged_in'] = True
            session['login_date'] = datetime.datetime.now()
            return redirect(url_for('adminLogin'))
    return render_template('adminLogin.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
