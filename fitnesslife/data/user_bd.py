'''база данных где храниться данные пользователя'''
import sqlite3

with sqlite3.connect("users_bd.sqlite") as connection:
    cursor = connection.cursor()
    query = """
            CREATE TABLE users(
                id int,
                name varchar(30),
                lastname varchar(30),
                phone integer,
                age integer,
                sex varchar(10),
                bday dater
            )
        """

    cursor.execute(query)