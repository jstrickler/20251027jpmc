from itertools import islice
import sqlite3

# conn = sqlite3.Connection(...)
with sqlite3.connect("../DATA/presidents.db") as conn:  # connect to the database

    s3_cursor = conn.cursor()  # get a cursor object

    # select specified columns from all presidents
    s3_cursor.execute('''
        select termnum, firstname, lastname, party
        from presidents
    ''')  # execute a SQL statement

    # first_record = s3_cursor.fetchone()
    # print("FIRST:", first_record)

    # row_7 = islice(s3_cursor, 6, 7)
    # print(list(row_7))
    # s3_cursor.execute('delete from presidents where termnum = 47')

    for term, firstname, lastname, party in s3_cursor: # .fetchall():
        print(f"{term:2d} {firstname:25} {lastname:20} {party}")
    print()
    s3_cursor.execute("select * from presidents where 1 = 0")
    # print(s3_cursor.description)
    column_names = [column[0] for column in s3_cursor.description]
    print(column_names)

