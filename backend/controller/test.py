from sqlalchemy import create_engine
import pandas as pd


def main():
    host = 'localhost'
    port = 3306
    username = 'root'
    # remember to replace @ sign with %40 for sqlalchemy to process if ur pw contains @
    password = 'Djj%4019950420'
    database = 'employees'
    # Connect to the database
    engine = create_engine("mysql+mysqlconnector://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + database)

    # Test the connection
    connection = engine.connect()
    sql_query = pd.read_sql_query("SELECT * FROM employees", connection)
    df = pd.DataFrame(sql_query)
    print(df)
    connection.close()


if __name__ == '__main__':
    main()
