from datetime import datetime
import psycopg2
import pandas.io.sql as sqlio

def get_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="x",
                                  host="35.205.119.160",
                                  port="5432",
                                  database="computer-vision-project")
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
    return(connection)

def get_data():

    connection = get_connection()
    cursor = connection.cursor()

    postgreSQL_select_Query = "select * from overcrowding_alerts order by id desc "
    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchall()

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(mobile_records)

def get_daily_data():
    connection = get_connection()
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT date_part('hour', logtime) as hour,object_type, count(id) FROM public.detected_people_coordinates group by object_type, hour order by hour"
    daily_summary = sqlio.read_sql_query(postgreSQL_select_Query, connection)

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(daily_summary)

def get_monthly_data():
    connection = get_connection()
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT date_part('month', logtime) as month,object_type, count(id) FROM public.detected_people_coordinates group by object_type, month order by month"
    monthly_summary = sqlio.read_sql_query(postgreSQL_select_Query, connection)

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(monthly_summary)

def get_time_series_data():
    connection = get_connection()
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT date(logtime) as date,object_type, count(id) FROM public.detected_people_coordinates group by object_type, date order by date"
    time_series_summary = sqlio.read_sql_query(postgreSQL_select_Query, connection)

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(time_series_summary)

def delete_data():
    connection = get_connection()
    cursor = connection.cursor()
    postgreSQL_select_Query = "delete from overcrowding_alerts  "
    cursor.execute(postgreSQL_select_Query)

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

def get_bydayofweek_data():
    connection = get_connection()
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT EXTRACT(DOW FROM logtime) as dow,object_type, count(id) FROM public.detected_people_coordinates group by object_type, dow order by dow"
    dow_data = sqlio.read_sql_query(postgreSQL_select_Query, connection)

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(dow_data)

def get_coord_data2():
    connection = get_connection()
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT x,y,height, logtime FROM public.detected_people_coordinates "
    coord_data = sqlio.read_sql_query(postgreSQL_select_Query, connection)

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return(coord_data)
