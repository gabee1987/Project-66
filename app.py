from flask import Flask, render_template, request, redirect, session
import requests
import bll
import hashlib
import credentials
from datetime import datetime

app = Flask(__name__)
app.secret_key = credentials.secret_key


@app.route('/')
def main_page():
    planet_data = requests.get('https://swapi.co/api/planets').json()
    if 'username' in session:
        user = session['username']
    else:
        user = None
    return render_template('index.html', planet_data=planet_data, username=user)


@app.route('/login', methods=['GET'])
def show_login():
    return render_template('form.html', action='Login', route='/login', title='Login')


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    rebel = request.form.get('rebel')
    hashed_password = hashlib.sha256(str.encode(password)).hexdigest()
    user_id = bll.validate_user(username, hashed_password)
    if not rebel:
        return render_template('rebellion.html')
    if user_id:
        session['username'] = username
        session['userid'] = user_id
        return redirect('/')
    else:
        return render_template('form.html', action='Login', route='/login', title='Login',
                               login_error=True, username=username)


@app.route('/register', methods=['GET'])
def show_register():
    return render_template('form.html', action='Register', route='/register', title='Registration')


@app.route('/register', methods=['POST'])
def do_register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.sha256(str.encode(password)).hexdigest()
    user_id = bll.register_user(username, hashed_password)
    if user_id > 0:
        return redirect('/login')
    else:
        return render_template('form.html', action='Register', route='/register', title='Registration',
                               reg_error=True, username=username)


@app.route('/logout')
def do_logout():
    session.pop('username', None)
    session.pop('userid', None)
    return redirect(request.referrer)


@app.route('/login_status')
def check_login_status():
    if 'username' in session:
        return session['username']
    return ''


@app.route('/vote', methods=['GET'])
def do_vote():
    planet_url = request.args.get('planet-url')
    planet_id = planet_url.split('/')[-2]
    submission_time = datetime.now().replace(microsecond=0)
    user_id = session['userid']
    bll.insert_vote(planet_id, user_id, submission_time)
    return 'Ok'


@app.route('/voted-planets')
def get_voted_planets():
    voted_planets = bll.get_voted_planets()
    return voted_planets


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=None)
