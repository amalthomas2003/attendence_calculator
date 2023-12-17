def extra():    
    import pymysql
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
    insert_query1 = """
                        UPDATE timetable
            SET second_period = "101009/IT500A",
                third_period = "101009/IT500A",
                fifth_period = "101009/EN500E",
                sixth_period = "101009/EN500E"
            WHERE date = "7-Dec-2023"

                """
    cursor.execute(insert_query1)
    insert_query1 = """
                            UPDATE timetable
                SET 
                first_period="101009/IT522T",
                second_period = "101009/IT522T",
                    third_period = "101009/IT522T",
                    fourth_period="101009/IT522T",
                    fifth_period = "101009/IT522T",
                    sixth_period = "101009/IT522T"
                WHERE date = "16-Nov-2023"

                    """
    cursor.execute(insert_query1)

    insert_query1 = """
                        UPDATE timetable
            SET second_period = "101009/MS500C",
                third_period = "101009/MS500C",
                fifth_period = "101009/IT500B",
                sixth_period = "101009/IT500B"
            WHERE date = "8-Dec-2023"

                """
    cursor.execute(insert_query1)

    insert_query1 = """
                        UPDATE timetable
            SET second_period = "101009/IT503F",
                third_period = "101009/IT503F",
                fifth_period = "101009/MS500D",
                sixth_period = "101009/MS500D"
            WHERE date = "11-Dec-2023"

                """
    cursor.execute(insert_query1)

    connection.commit()
    print("Extra.py Executed 100%")