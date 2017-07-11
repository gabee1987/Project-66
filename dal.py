import psycopg2
import json
from credentials import connection_data
from psycopg2.extras import RealDictCursor


def establish_connection():
    try:
        connect_str = "dbname={} user={} host={} password={} port={}".format(connection_data['dbname'],
                                                                             connection_data['user'],
                                                                             connection_data['host'],
                                                                             connection_data['password'],
                                                                             connection_data['port'])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_data_from_table(sql_string, sql_variables=None):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(sql_string, sql_variables)
    result_set = cursor.fetchall()
    cursor.close()
    conn.close()
    return result_set


def get_json_from_table(sql_string, sql_variables=None):
    conn = establish_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(sql_string, sql_variables)
    result = json.dumps(cursor.fetchall(), indent=2)
    cursor.close()
    conn.close()
    return result


def modify_table(sql_string, sql_variables=None):
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(sql_string, sql_variables)
    cursor.close()
    conn.close()
