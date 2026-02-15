import mysql.connector
from django.conf import settings

def get_db_connection():
    connection = mysql.connector.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        database=settings.DATABASES['default']['NAME'],
        port=settings.DATABASES['default']['PORT']
    )
    return connection

def execute_query(query, params=None, fetch=False):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True) #Send SQL queries to the database,Receive results from the database
    
    try:
        cursor.execute(query, params or ()) #only sends the sql queries to mysql
        
        if fetch:  #fetchs data from the database (likely a select query)
            result = cursor.fetchall()
            return result
        else:     #if fetch= False (likely an insert, update or delete query)
            connection.commit()
            return cursor.lastrowid
    
    except Exception as e:
        connection.rollback()
        raise e
    
    finally:
        cursor.close()
        connection.close()