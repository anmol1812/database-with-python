
import pandas as pd
from datetime import datetime
import psycopg2
past_time = '2020-01-16 06:13:07.872064'
no=0
#while True:
    
try:
    connection = psycopg2.connect(user="root",
                                  password="kzmtmq1WzP8z3PdgcELzVQVX",
                                  host="localhost",
                                  #port="5432",
                                  database="ml")
    cursor = connection.cursor()

    query = '''ALTER TABLE Time_record
    ADD COLUMN run_time TIMESTAMP WITHOUT TIME ZONE;'''

    cursor.execute(query)
    #past_time = present_time
    #print(past_time, present_time)

    connection.commit()
    count = cursor.rowcount

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into time_record table: ", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
