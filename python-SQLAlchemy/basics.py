from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.sql import select, subquery

# create db engine object
# create metadata to stores db info

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()
meta.create_all(engine)

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

# insert columns in db
students_to_inserts = students.insert().values(name='Ravi', lastname='Kapoor')
connection = engine.connect()
insert_result = connection.execute(students_to_inserts)
connection.execute(students.insert(), [
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])


# query db using select()
students = students.select()
db_connection = engine.connect()
select_result = db_connection.execute(students)

for row in select_result:
    print(row, sep=" ")

print("-------------------")
print("using text clause to execute sql expression querying db directly")

# using test clause representing textual SQL string directly and query db with it
sql_query_text = text("SELECT * FROM students")
text_query_result = db_connection.execute(sql_query_text)

for row in text_query_result:
    print(row, sep=" ")



