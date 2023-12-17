
import pymysql


def percentage(sub):
    host = "localhost"
    user = "root"
    password = "careerconnect"
    database = "college"

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    sum=0

    query1=f"select count(*) from timetable where first_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a
    query1=f"select count(*) from timetable where second_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a

    query1=f"select count(*) from timetable where third_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a
    query1=f"select count(*) from timetable where fourth_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a

    query1=f"select count(*) from timetable where fifth_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a

    query1=f"select count(*) from timetable where sixth_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a

    query1=f"select count(*) from timetable where seventh_period = '{sub}'"
    cursor.execute(query1)
    a=cursor.fetchall()[0][0]
    sum+=a
    print(sub,sum)

    return sum