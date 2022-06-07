from sqlalchemy import create_engine, Table, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

db_engine = create_engine('sqlite:///fund_launch_UI_DB.db', echo=True)
Table_Base = declarative_base()


class Association(Table_Base):
    __tablename__ = 'association'
    benchmark_id = Column(Integer, ForeignKey('benchmarks.id'), primary_key=True)
    sleeve_id = Column(Integer, ForeignKey('sleeves.id'), primary_key=True)


class Benchmark(Table_Base):
    __tablename__: str = 'benchmarks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sleeves = relationship('Sleeve', secondary='association', back_populates='benchmarks')


class Sleeve(Table_Base):
    __tablename__: str = 'sleeves'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    benchmarks = relationship('Benchmark', secondary='association', back_populates='sleeves')


Table_Base.metadata.create_all(db_engine)

# insert data into tables
b1 = Benchmark(name='benchmark gold')
s1 = Sleeve(name='sleeve stock')
b1.sleeves.append(s1)

b2 = Benchmark(name='benchmark silver')
s2 = Sleeve(name='sleeve bond')
b2.sleeves.append(s2)

b3 = Benchmark(name='benchmark bronze')
s3 = Sleeve(name='sleeve cylinder')
b3.sleeves.append(s3)

<<<<<<< HEAD
# above objects are in transient state saved in the memory only

=======
>>>>>>> 28af19b3b970c1d83f7130b05dfb670a32853b31
# causing integrity error
# s1.benchmarks.append(b1)
# s2.benchmarks.append(b2)
# s3.benchmarks.append(b3)

<<<<<<< HEAD
# cascading objects into session object
=======
>>>>>>> 28af19b3b970c1d83f7130b05dfb670a32853b31
Session = sessionmaker(bind=db_engine)
db_connector = Session()
# db_connector.add(b1)
# db_connector.add(b2)
# db_connector.add(b3)
db_connector.add_all([b1, b2, b3])
# causing integrity error
# db_connector.add(s1)
# db_connector.add(s2)
# db_connector.add(s3)
db_connector.commit()

<<<<<<< HEAD
# query, loading and display data from the tables
# get all the rows from the two tables
for data in db_connector.query(Benchmark, Sleeve). \
        filter(Association.benchmark_id == Benchmark.id, Association.sleeve_id == Sleeve.id). \
        order_by(Benchmark.id).all():
    print(type(data))
    print('--------')
    print("benchmark name: {}; sleeve name: {};".format(data.Benchmark.name, data.Sleeve.name))

# further practice and understanding
# what is the concept of dialects in ORM?
# it is used to communicate with different types of database
# each database requires a DBAPI wrapper; each wrapper requries a driver
# SQL alchemy uses create_engine class to construct and passing parameters including username, DB names, etc

=======
# query and display data from the tables
>>>>>>> 28af19b3b970c1d83f7130b05dfb670a32853b31
