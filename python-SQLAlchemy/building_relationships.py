from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

db_engine = create_engine('sqlite:///eip.db', echo=True)
Base_for_table = declarative_base()


# create two tables, mapped classes, and establish relationships between the two
class Advisor(Base_for_table):
    __tablename__: str = 'advisors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    portfolio_identifier = Column(Integer)
    portfolio = Column(String)
    fee = Column(Integer)


class Fund(Base_for_table):
    __tablename__: str = 'funds'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    advisor_id = Column(Integer, ForeignKey('advisors.id'))
    advisor = relationship('Advisor', back_populates='funds')


Advisor.funds = relationship('Fund', order_by=Fund.id, back_populates='advisor')
Base_for_table.metadata.create_all(db_engine)


# insert data into the parent table
add_one_advisor = Advisor(name='Leon Kennedy', portfolio_identifier=1001, portfolio='Apple ML engineers', fee=700)
add_one_advisor.funds = [Fund(name='vanguard S&P standard', type='stocks')]

# insert via construct an advisor object providing mapped funds attribute in the constructor
add_one_advisor_with_constructor = [
    Advisor(
        name='Ada Wong', portfolio_identifier=1010, portfolio='Slack front-end developers', fee=850,
        funds=[Fund(name='fidelity FTSE spartan growth', type='stocks')]
    )
]

# insert with a list of objects (multiple rows for the parent table)
add_multiple_advisors = [
    Advisor(
        name='Solid Snake', portfolio_identifier=2030, portfolio='HNS ER Doctor assistant group', fee=421,
        funds=[Fund(name='vanguard treasury 30 years', type='bond')]
    ),

    Advisor(
        name='Mave Rick', portfolio_identifier=2110, portfolio='Air Force One secretary', fee=380,
        funds=[Fund(name='vanguard gold and silver', type='commodity')]
    )
]


DB_connector = sessionmaker(bind=db_engine)
db_connector = DB_connector()
# db_connector.add(add_one_advisor)
# db_connector.add_all(add_one_advisor_with_constructor)
db_connector.add_all(add_multiple_advisors)
db_connector.commit()
