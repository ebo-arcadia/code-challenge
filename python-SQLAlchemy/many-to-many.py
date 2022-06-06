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

# causing integrity error
# s1.benchmarks.append(b1)
# s2.benchmarks.append(b2)
# s3.benchmarks.append(b3)

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

# query and display data from the tables
