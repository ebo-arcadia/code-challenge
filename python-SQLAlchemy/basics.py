from sqlalchemy import create_engine, \
    MetaData, Table, Column, Integer, \
    String, text, ForeignKey, join, \
    and_, or_, asc, desc, between, func, union, union_all, except_, except_all
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
students_obj = students.select()
db_connection = engine.connect()
select_result = db_connection.execute(students_obj)

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

print("-----verify if name is updated---------")
updated_students_obj = students.select()
updated_result = db_connection.execute(updated_students_obj)

for st in updated_result:
    print(st)

print("----delete all students using delete() object")
if updated_students_obj is not None:
    delete_all = students.delete()
    db_connection.execute(delete_all)
else:
    insert_result = db_connection.execute(students_to_inserts)
    connection.execute(students.insert(), [
        {'name': 'Rajiv', 'lastname': 'Khanna'},
        {'name': 'Komal', 'lastname': 'Bhandari'},
        {'name': 'Abdul', 'lastname': 'Sattar'},
        {'name': 'Priya', 'lastname': 'Rajhans'},
    ])
    print("--------------")
    print("update column with update() method")
    update_column = update(students).where(students.c.lastname == "Sattar").values(lastname="Penitentiary House")
    print(update_students)

# using multiple tables
# creating database
vg_db_engine = create_engine('sqlite:///vanguard.db', echo=True)
tb_metadata = MetaData()

advisors = Table(
    'advisors', tb_metadata,
    Column('portId', Integer, primary_key=True),
    Column('identifier', String),
    Column('content', String),
)

funds = Table(
    'funds', tb_metadata,
    Column('fundId', Integer, primary_key=True),
    Column('advisor_id', Integer, ForeignKey('advisors.portId')),
    Column('value', Integer),
)

tb_metadata.create_all(vg_db_engine)

# insert rows in the tables
vg_db_connection = vg_db_engine.connect()
vg_db_connection.execute(advisors.insert(), [
    {'identifier': 'personal all weather', 'content': 'most popular portfolio'},
    {'identifier': 'IVY', 'content': 'balanced long term allocation'},
])

vg_db_connection.execute(funds.insert(), [
    {'advisor_id': 1, 'value': 2000},
    {'advisor_id': 2, 'value': 123},
])

# fetch data from the two tables
fetch_stmt = select([advisors, funds]).where(advisors.c.portId == funds.c.advisor_id)
fetch_data = vg_db_connection.execute(fetch_stmt)

for row in fetch_data:
    print(row)

# update multiple tables using update() object and from and where clauses

vg_db_connection.execute(advisors.insert(), [
    {'identifier': 'conservative', 'content': '70% bond & 30% stocks'},
])
vg_db_connection.execute(funds.insert(), [
    {'advisor_id': 3, 'value': 999},
])

update_stmt = advisors.update().where(advisors.c.identifier == 'conservative') \
    .values(identifier='safe heaven') \
    .where(advisors.c.portId == select([funds.c.value])
           .where(funds.c.advisor_id == advisors.c.portId)
           .as_scalar()
           )

update_execution = vg_db_connection.execute(update_stmt)

# fetch data from the two tables to verify update
fetch_stmt_after_update = select([advisors, funds]).where(advisors.c.portId == funds.c.advisor_id)
fetch_data_with_update = vg_db_connection.execute(fetch_stmt_after_update)

print("----fetch data to verify update-----")
for row in fetch_data_with_update:
    print(row)

print("-------end of update multi tables execution------")

another_update_stmt = (
    advisors.update()
        .where(advisors.c.identifier == "conservative")
        .values(identifier="saver")
    # .returning(advisors.c.identifier, advisors.c.content)
)

print(another_update_stmt)
vg_db_connection.execute(another_update_stmt)

print("------update table using preserve parameter order-----")

update_stmt_with_param_order = (
    funds.update().ordered_values((funds.c.value, 150000))
)

print(update_stmt_with_param_order)
vg_db_connection.execute(update_stmt_with_param_order)

print("--------using join---------")
j1 = advisors.join(funds)
print(j1)
j2 = advisors.join(funds, advisors.c.portId == funds.c.advisor_id)
print(j2)
join_stmt = select([advisors]).select_from(j1)
print(join_stmt)
join_result = vg_db_connection.execute(join_stmt).fetchall()
print(join_result)

print("--------using and_() function to produce conjunctions of expressions joined by AND -------")
query_with_and = select([advisors]).where(and_(advisors.c.portId < 6, advisors.c.identifier == "IVY", advisors.c.portId == 5))
result_with_and = vg_db_connection.execute(query_with_and).fetchall()
print(result_with_and)

print("-----using or_() function to produce conjunctions of expression joined by OR ------")
query_with_or = select([advisors]).where(or_(advisors.c.content == "most popular portfolio", advisors.c.content == "xxx"))
result_with_or = vg_db_connection.execute(query_with_or).fetchall()
print(result_with_or)

print("----using asc() function to produce an ascending order_by clause----")
asc_order_by_stmt = select([advisors]).order_by(asc(advisors.c.identifier))
result_with_order_by_asc = vg_db_connection.execute(asc_order_by_stmt)

for row in result_with_order_by_asc:
    print(row)

print("----using desc() function to produce an descend order_by clause-----")
desc_order_by_stmt = select([advisors]).order_by(desc(advisors.c.content))
result_with_order_by_desc = vg_db_connection.execute(desc_order_by_stmt)

for row in result_with_order_by_desc:
    print(row)

print("----using between() function to produce a BETWEEN predicate clause to validate if column value fall in a range---")
between_stmt = select([advisors]).where(between(advisors.c.portId,1,3))
between_result = vg_db_connection.execute(between_stmt).fetchall()

for row in between_result:
    print(row)

print("----generic function or function passing parameters--------")
# how to implement/ render a generic function such as now()?
# functions are implemented by the usage of the func key word imported from sql-alchemy library
print("--------")
print("---using now()---")
generic_func_now_stmt = vg_db_connection.execute(select([func.now()])).fetchone()
print(generic_func_now_stmt)
print("--------")
print("---using count()---")
func_count_stmt = vg_db_connection.execute(select([func.count(advisors.c.portId)])).fetchone()
print(func_count_stmt)

print("---using max, min, avg functions ----")
# are these functions generic or requires parameters?
# rendered by the usage of func keyword
max_stmt = vg_db_connection.execute(select([func.max(advisors.c.portId).label("max_port_id")])).fetchone()
print(max_stmt)
min_stmt = vg_db_connection.execute(select([func.min(advisors.c.portId).label("min_port_id")])).fetchone()
print(min_stmt)
avg_stmt = vg_db_connection.execute(select([func.avg(advisors.c.portId).label("average_port_id")])).fetchone()
print(avg_stmt)


print("------using set operator union_all function-------")
stmt_1 = select([advisors]).where(advisors.c.portId < 3)
stmt_2 = select([advisors]).where(advisors.c.portId == 5)
union_all_stmt = union_all(stmt_1, stmt_2)
union_result = vg_db_connection.execute(union_all_stmt).fetchall()

for row in union_result:
    print(row)


# clean up!!!
print("------delete tables---------")
delete_advisors_tb_stmt = advisors.delete()
delete_funds_tb_stmt = funds.delete()
# if advisors is not None:
#     vg_db_connection.execute(delete_advisors_tb_stmt)
# else:
#     pass
# if funds is not None:
#     vg_db_connection.execute(delete_funds_tb_stmt)
# else:
#     pass