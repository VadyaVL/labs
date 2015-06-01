import json
import requests
from flask import render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import SubmitField

from flask import Flask, redirect, url_for, session, request
from flask_oauthlib.client import OAuth

#region initialisation
app = Flask(__name__)

app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

github = oauth.remote_app(
    'github',
    #consumer_key='f39faf739e75161ecd41',
    #consumer_secret='f396b078ef0aa875393be9952edfc0d4568f6882',
    consumer_key='3367efadc12fd02f2d5e',
    consumer_secret='9d116dc625f17260d2ecebdbd69ebcfbbdc103fd',
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

WTF_CSRF_ENABLED = False
#endregion

# region Form
class EncumbranceForm(Form):
    numberStatement = StringField('numberStatement')
    dateStatement = StringField('dateStatement')
    type_id = IntegerField('type_id')
    object_id = IntegerField('object_id')
    person_id = IntegerField('person_id')

    submit = SubmitField('submit')
# endregion

# region API routing
@app.route('/')
def index():
    print 'index'
    form = EncumbranceForm(csrf_enabled=False)
    r = requests.get('http://127.0.0.1:5010/api/encumbrance')
    data = json.loads(r.text)
    if 'github_token' in session:
        return render_template('authorized.html', objects=data["objects"], form=form)
    return render_template('unauthorized.html', objects=data["objects"], form=form)


@app.route('/delete/<int:encumbrance_id>')
def delete(encumbrance_id):
    r = requests.delete('http://127.0.0.1:5010/api/encumbrance/' + str(encumbrance_id))
    return index()


@app.route('/update/<int:encumbrance_id>')
def update(encumbrance_id):
    form = EncumbranceForm(csrf_enabled=False)
    r = requests.get('http://127.0.0.1:5010/api/encumbrance/'+str(encumbrance_id))
    data = json.loads(r.text)

    form.numberStatement.data = data['numberStatement']
    form.dateStatement.data = data['dateStatement']
    form.type_id.data = data['type_id']
    form.object_id.data = data['object_id']
    form.person_id.data = data['person_id']

    return render_template('update.html', encumbrance=data, form=form)


@app.route('/send_update/<int:encumbrance_id>', methods=['POST'])
def send_update(encumbrance_id):
    print encumbrance_id
    id = encumbrance_id
    numberStatement = request.form['numberStatement']
    dateStatement = request.form['dateStatement']
    type_id = int(request.form['type_id'])
    object_id = int(request.form['object_id'])
    person_id = int(request.form['person_id'])

    header = {'Content-Type':'application/json'}

    data = json.dumps({
                       "id": id,
                       "numberStatement": numberStatement,
                       "dateStatement": dateStatement,
                       "type_id":type_id,
                       "object_id":object_id,
                       "person_id":person_id
                       })

    r = requests.patch('http://127.0.0.1:5010/api/encumbrance/' + str(encumbrance_id), data=data, headers=header)
    return index()


@app.route('/add', methods=['POST'])
def add():
    numberStatement = request.form['numberStatement']
    dateStatement = request.form['dateStatement']
    type_id = int(request.form['type_id'])
    object_id = int(request.form['object_id'])
    person_id = int(request.form['person_id'])

    # creation_date = request.form['creation_date']
    # approval_date = request.form['approval_date']
    header = {'Content-Type':'application/json'}
    data = json.dumps({
                       "numberStatement": numberStatement,
                       "dateStatement": dateStatement,
                       "type_id":type_id,
                       "object_id":object_id,
                       "person_id":person_id
                       })
    r = requests.post('http://127.0.0.1:5010/api/encumbrance', headers=header, data=data)
    return index()
# endregion

# region OAuth routing
@app.route('/login')
def login():
    return github.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('github_token', None)
    return redirect(url_for('index'))


@app.route('/login/authorized')
def authorized():
    resp = github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )
    session['github_token'] = (resp['access_token'], '')
    me = github.get('user')
    return index()


@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')
#endregion

#region PDF

@app.route('/print')
def print_form():
    r = requests.get('http://127.0.0.1:5010/api/method')
    method_data = json.loads(r.text)
    r = requests.get('http://127.0.0.1:5010/api/author')
    author_data = json.loads(r.text)
    r = requests.get('http://127.0.0.1:5010/api/category')
    category_data = json.loads(r.text)
    return render_template('print.html',
                           methods=method_data["objects"],
                           authors=author_data["objects"],
                           categories=category_data["objects"])


# @app.route('/pdf/<string:name>')
# def generate_pdf(name):
#     pdfkit.from_url('http://127.0.0.1:5000/print', name + ".pdf")
#     return name + ".pdf generated"

#endregion




if __name__ == '__main__':
    app.run()
