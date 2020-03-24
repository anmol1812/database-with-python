
import pandas as pd
from datetime import datetime
import psycopg2

no=0
#while True:
    
try:
    connection = psycopg2.connect(user="anmol",
                                  host="localhost",
                                  database="database")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO time_record (id, data_type, present_time) VALUES (%s,%s,%s)"""
    present_time = str(datetime.now())
    #print(type(present_time), present_time)
    #print(type(now), now)
    no+=1
    record_to_insert = ('inserted data type', present_time)
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
