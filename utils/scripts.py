import os
import csv
import pymysql

from flask import current_app


def init_database():
    """
    when application start, insert csv data into database
    :return:
    """

    try:
        connection = pymysql.connect(host=os.getenv("DB_HOST"),
                                     database=os.getenv("DB_DATABASE"),
                                     user=os.getenv("DB_USER"),
                                     password=os.getenv("DB_PASSWORD"),
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cur:
            f = open(file=os.path.abspath(os.path.join(os.path.dirname(__file__), "./wanted_temp_data.csv")), mode="r")
            reader = list(csv.reader(f))
            header = reader[0]

            for row in reader[1:]:
                cur.execute(query=f"""INSERT INTO companies ({', '.join(header)}) VALUES ({str(row).replace('[', '').replace(']', '').replace("''", "NULL")});""")

        connection.commit()

    except Exception as e:
        current_app.logger.error(e)
        return False

    return True