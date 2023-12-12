from collections import defaultdict
import secret
import pymysql
import data #contains secret data


dict1=defaultdict(int)
for i in range(11,31):
    val=f"{i}-Sep-2023"
    dict1[val]=[0,0,0,0,0,0,0]

for i in range(1,32):
    val=f"{i}-Oct-2023"
    dict1[val]=[0,0,0,0,0,0,0]

for i in range(1,31):
    val=f"{i}-Nov-2023"
    dict1[val]=[0,0,0,0,0,0,0]

for i in range(1,23):
    val=f"{i}-Dec-2023"
    dict1[val]=[0,0,0,0,0,0,0]







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

create_table_query = """
CREATE TABLE IF NOT EXISTS timetable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    first_period VARCHAR(255),
    second_period VARCHAR(255),
    third_period VARCHAR(255),
    fourth_period VARCHAR(255),
    fifth_period VARCHAR(255),
    sixth_period VARCHAR(255),
    seventh_period VARCHAR(255)
)
"""

cursor.execute(create_table_query)

for date, periods in dict1.items():
    insert_query = f"""
    INSERT INTO timetable (date, first_period, second_period, third_period, 
                            fourth_period, fifth_period, sixth_period, seventh_period)
    VALUES ('{date}', '{periods[0]}', '{periods[1]}', '{periods[2]}', '{periods[3]}',
            '{periods[4]}', '{periods[5]}', '{periods[6]}')
    """
    cursor.execute(insert_query)

connection.commit()
print("Data inserted successfully")




data=data.data()

details_list=list(data.split('\n'))
details_list = list(map(lambda x: x.split("\t"), details_list))


for i in details_list:
    
    userid=i[0]
    password=i[1]
    #print(uid,password)
    dict1=secret.check_attendence(userid,password,dict1)
    print(userid," over")
    print("DATE".ljust(25),"period")
    print("-"*16)
    for k,j in dict1.items():
        try:
            update_query = f"""
                            UPDATE timetable
                            SET
                                first_period = '{j[0]}',
                                second_period = '{j[1]}',
                                third_period = '{j[2]}',
                                fourth_period = '{j[3]}',
                                fifth_period = '{j[4]}',
                                sixth_period = '{j[5]}',
                                seventh_period = '{j[6]}'
                            WHERE
                                date = '{k}'
                            """

            cursor.execute(update_query)
            connection.commit()
        except:
            pass

        try:
            print(f"{k}".ljust(25),j[0:])
        except:
            pass