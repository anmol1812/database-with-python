
import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "root",
                                  password = "kzmtmq1WzP8z3PdgcELzVQVX",
                                  host = "localhost",
                                  database = "ml")
    cursor = connection.cursor()
    create_table_query = """CREATE TABLE time_record (
            id    SERIAL PRIMARY KEY,
            game_code    VARCHAR NOT NULL,
            data_type    VARCHAR NOT NULL,
            last_sync_time    TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            present_sync_time    TIMESTAMP WITHOUT TIME ZONE NOT NULL);"""
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table: ", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")