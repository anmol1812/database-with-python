
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

    postgres_insert_query = """ INSERT INTO time_record (id, game_code, data_type, last_time, present_time) VALUES (%s,%s,%s,%s,%s)"""
    present_time = str(datetime.now())
    #print(type(present_time), present_time)
    #print(type(now), now)
    no+=1
    record_to_insert = ('ByGqEfCXa', 'inserted data type', past_time, present_time)
    cursor.execute(postgres_insert_query, record_to_insert)
    #past_time = present_time
    print(past_time, present_time)

    connection.commit()
    count = cursor.rowcount

    print(count, "Record inserted successfully into time_record table")
    
    cursor.execute('SELECT * from time_record')
    x=cursor.fetchall()
    print(type(x), x[0][4])
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into time_record table: ", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
