import dal
import psycopg2


def register_user(username, password):
    sql_string = "INSERT INTO swuser (username, password) VALUES (%s, %s);"
    sql_variables = (username, password)
    try:
        dal.modify_table(sql_string, sql_variables)
    except psycopg2.IntegrityError:
        return -1
    else:
        sql_string = "SELECT ID FROM swuser WHERE username = %s;"
        sql_variable = (username, )
        user_id = dal.get_data_from_table(sql_string, sql_variable)[0][0]
        return user_id


def validate_user(username, password):
    sql_string = "SELECT ID FROM swuser WHERE username = %s AND password = %s;"
    sql_variables = (username, password)
    user_id = dal.get_data_from_table(sql_string, sql_variables)
    if user_id:
        user_id = user_id[0][0]
    return user_id


def insert_vote(planet_id, user_id, submission_time):
    sql_string = "INSERT INTO planet_votes (planet_id, user_id, submission_time) VALUES (%s, %s, %s);"
    sql_variables = (planet_id, user_id, submission_time)
    dal.modify_table(sql_string, sql_variables)


def get_voted_planets():
    sql_string = "SELECT planet_id, count(planet_id) AS votes FROM planet_votes\
                 GROUP BY planet_id ORDER BY votes desc;"
    result = dal.get_json_from_table(sql_string)
    return result
