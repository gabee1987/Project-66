from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json
from db_connect import *

app = Flask(__name__)
app.secret_key = "Transmission commencing"


@app.route('/register', methods=['GET'])
def display_register():
    return render_template('register.html')


@app.route('/register_post', methods=['POST'])
def register_post():
    user_username = request.form['username']
    user_password = request.form['password']
    query = """SELECT username \
             FROM swusers \
             WHERE username = '{}'""".format(user_username)
    result = handle_database(query)
    if result == []:
        password = generate_password_hash(user_password)
        query = """INSERT INTO swusers (username, p4ssword) \
                    VALUES ('{}', '{}')""".format(user_username, password)
        handle_database(query)
        return redirect(url_for('login'))
    else:
        error = 'Username already in use.'
        return render_template('error.html', error=error)


@app.route('/login', methods=['GET'])
def display_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    user_username = request.form['username']
    query = """SELECT username \
             FROM swusers \
             WHERE username = '{}'""".format(user_username)
    result = handle_database(query)
    if result == []:
        error = 'Username not registered.'
        return render_template('error.html', error=error)
    if user_username in result[0][0]:
        user_password = request.form['password']
        query = """SELECT p4ssword \
                FROM swusers \
                WHERE username = '{}'""".format(user_username)
        result = handle_database(query)
        saved_password = result[0][0]
        if check_password_hash(saved_password, user_password):
            session['username'] = user_username
            print(session['username'])
            return redirect(url_for('index'))
        else:
            error = 'Authentification failed.'
            return render_template('error.html', error=error)
    else:
        error = 'Username not registered.'
        return render_template('error.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
    '''
        Displays the index page.
        Shows the planets as a table.
    '''
    table_headers = [
                    'Name',
                    'Diameter',
                    'Climate',
                    'Terrain',
                    'Surface water percentage',
                    'Population',
                    'Residents'
                    ]
    if 'username' in session:
        user_username = session['username']
        table_headers = [
                    'Name',
                    'Diameter',
                    'Climate',
                    'Terrain',
                    'Surface water percentage',
                    'Population',
                    'Residents',
                    'Vote'
                    ]
        return render_template('index.html', table_headers=table_headers, user_username=user_username)
    return render_template('index.html', table_headers=table_headers)


@app.route('/vote', methods=['POST'])
def voting():
    user_username = session['username']
    json_planet_id = request.json['votedPlanetId']
    voted_planet_id = json.loads(json_planet_id)
    planet_id = voted_planet_id['votedplanet']
    query = """SELECT id \
             FROM swusers \
             WHERE username = '{}';""".format(user_username)
    result = handle_database(query)
    user_id = result[0][0]
    query_vote_check = """SELECT user_id, planet_id
                          FROM planet_votes
                          WHERE user_id = '{}' AND planet_id = '{}';""".format(user_id, planet_id)
    vote_check = handle_database(query_vote_check)
    if vote_check == []:
        query = """INSERT INTO planet_votes (planet_id, user_id, submission_time) \
                    VALUES ('{}', '{}', '{}');""".format(planet_id, user_id, str(datetime.now())[:-7])
        handle_database(query)
    return redirect(url_for('index'))


@app.route('/statistics', methods=['POST'])
def statistics():
    query = """SELECT planet_id, COUNT(planet_id) \
                FROM planet_votes \
                GROUP BY planet_id \
                ORDER BY planet_id;"""
    result = handle_database(query)
    json_statistics = jsonify(result)
    return json_statistics


@app.route('/error')
def error():
    return render_template('error.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)