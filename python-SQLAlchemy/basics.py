from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.sql import select, alias
from sqlalchemy.sql.expression import update

# create db engine object
# create metadata to stores db info

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()
meta.bind = engine

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

meta.create_all(engine)

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


text_obj = text("select students.name, students.lastname from students where students.name between :x and :y")
db_connection.execute(text_obj, x='A', y='L').fetchall()
print("----------", sep=" ")
print("query database using alias")
st = students.alias("s")
s = select([st]).where(st.c.id > 2)
st_with_alias = db_connection.execute(s).fetchall()

print(st_with_alias)

# update a value in a column
print("--------------")
print("update column with update object")
conn = engine.connect()
update_stmt = students.update().where(students.c.name == "Ravi").values(name="Leon")
conn.execute(update_stmt)
updated_students_obj = students.select()
update_students = db_connection.execute(updated_students_obj).fetchall()
print(update_students)

print("--------------")
print("update column with update() method")
update_column = update(students).where(students.c.name == "Ravi").values(name="Snake")






