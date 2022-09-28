import sqlite3
import log

conn = sqlite3.connect('orders.db')


def create_user_table():
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS users (
                                           id integer PRIMARY KEY,
                                           name text NOT NULL,
                                           lastname text NOT NULL,
                                           birthday TEXT,
                                           phone text
                                       ); """

    # create a database connection
    conn = create_connection("orders.db")

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def write_data(data):
    print(data)
    try:
        sqliteConnection = sqlite3.connect('orders.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO users
                                 ( name, lastname, birthday, phone) 
                                 VALUES (?, ?, ?, ?);"""

        data_tuple = (data.get("name"), data.get("lastname"), data.get("birthday"), data.get("phone"))
        count = cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Record inserted successfully into users table ", cursor.rowcount)
        cursor.close()
        log.write_log(data, "POST")
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def find_data(query):
    con = create_connection("orders.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE ? in (name, lastname, birthday, phone)", (query.get("find_value")[0],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    log.write_log(query, "GET")
    return row
