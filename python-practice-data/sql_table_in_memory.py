import sqlite3

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

create_table_sql_stmt = """CREATE TABLE beatles (
            'fname' text,
            'lname' text,
            'nickname' text
        )
        """

# execute sql create schema stmt to create a table
cursor.execute(create_table_sql_stmt)

list_of_beatles = [('John', 'Lennon', 'The Smart One'),
                   ('Paul', 'McCartney', 'The Cute One'),
                   ('George', 'Harrison', 'The Funny One'),
                   ('Ringo', 'Starr', 'The Quiet One')
                   ]

insert_data_to_table = 'INSERT INTO beatles VALUES (?, ?, ?)'

# iterate each beatle and insert it into the schema
for beatles in list_of_beatles:
    cursor.execute(insert_data_to_table, beatles)

# insert a sequence of sequences, or, in this case, a list of beatles tuples, run once

another_list_of_beatles = [('Taylor', 'Swift', 'baby heart'),
                           ('Neo', 'Anderson', 'the one'),
                           ('Trinity', 'Anderson', 'the queen')
                           ]

cursor.executemany(insert_data_to_table, another_list_of_beatles)

# query the schema and retrieve data from the table
retrieve_beatles_from_schema = 'SELECT fname, lname, nickname from beatles'
cursor.execute(retrieve_beatles_from_schema)

# iterate the response and return data
results = cursor.fetchall()
cursor.close()
connection.close()

for beatles in results:
    print(beatles)
