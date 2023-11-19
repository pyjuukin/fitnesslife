'''база данных для входа (логин/пароль)'''
import sqlite3

with sqlite3.connect("login_bd.sqlite") as connection:
    cursor = connection.cursor()
    query = """
        CREATE TABLE login(
            email nvarchar(50),
            login varchar(50),
            password nvarchar(50)
        )
    """

    cursor.execute(query)