from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

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
        funds=[Fund(name='fidelity FTSE spartan growth', type='stocks'),
               Fund(name='vanguard treasury 30 years', type='bond'),
               Fund(name='vanguard treasury 30 years', type='bond'),
               Fund(name='fidelity all weather growth', type='cylinder'),
               Fund(name='fidelity growth income', type='cryptocurrency')]
    )
]

# insert with a list of objects (multiple rows for the parent table)
add_multiple_advisors = [
    Advisor(
        name='Solid Snake', portfolio_identifier=2030, portfolio='HNS ER Doctor assistant group', fee=421,
        funds=[Fund(name='vanguard treasury 30 years', type='bond'),
               Fund(name='fidelity growth income', type='cryptocurrency'),
               Fund(name='fidelity blockchain new coins', type='cryptocurrency')]
    ),

    Advisor(
        name='Mave Rick', portfolio_identifier=2110, portfolio='Air Force One secretary', fee=380,
        funds=[Fund(name='vanguard gold and silver', type='commodity')]
    )
]

DB_connector = sessionmaker(bind=db_engine)
db_connector = DB_connector()
db_connector.add(add_one_advisor)
db_connector.add_all(add_one_advisor_with_constructor)
db_connector.add_all(add_multiple_advisors)
db_connector.commit()

# how to query the joined parent and child tables?
print('--------query two relational tables using filter---------')
for advisor, fund in db_connector.query(Advisor, Fund).filter(Advisor.id == Fund.advisor_id).all():
    print("Advisor name: {} Advisor fee: {} Fund name: {} Fund type: {}".format(advisor.name, advisor.fee, fund.name,
                                                                                fund.type))

# how to query joined parent and child tables with certain values in the child table?
# how to query the joined tables returns advisors with fund type as bond only?
print('------query relational tables using join()------')
bond_only = db_connector.query(Advisor).join(Fund).filter(Fund.type == "bond").all()
for advisor in bond_only:
    for fund in advisor.funds:
        print(advisor.name, advisor.fee, fund.name, fund.type)

# how does join() know how to join the tables?
# via the foreign key attributes
# what happens when there are no foreign key or there are more than one foreign keys?
# join() needs to be more explict


# 1. construct a python object with SQL statement with/without conditions specified used to query one table
# 2. pass this statement as a Table object with access to column via attribute 'c' along with the parent table to query()
# 3. store the above statement as an array of objects in a variable
# 4. iterate the array and print data passing correct attributes

# return a list of all advisors with a total of funds for each
# 1. construct a sql statement query the fund table
# 2. construct a sql statement query the advisor table passing the above statement
# 3. iterate returned result set

query_fund_stmt = db_connector.query(Fund.advisor_id, func.count('*')
                                     .label('fund_count')).group_by(Fund.advisor_id).subquery()

for advisor, fund_count in db_connector.query(Advisor, query_fund_stmt.c.fund_count)\
        .outerjoin(query_fund_stmt, Advisor.id == query_fund_stmt.c.advisor_id)\
        .order_by(Advisor.id):
    print('advisor name: {} advisor fee: {} fund count: {}'.format(advisor.name, advisor.fee, fund_count))


# using common relational operators
# find advisor with cryptocurrency type fund using relational operators

print('----get advisor with cryptocurrency in many-to-one relational tables----')
advisor_with_crypto = db_connector.query(Advisor).join(Fund).filter(Fund.type.__eq__('cryptocurrency'))
for advisor_fund in advisor_with_crypto:
    for fund in advisor_fund.funds:
        print(advisor_fund.name, advisor_fund.fee, fund.name, fund.type)


print('-----get advisor with fund that has advisor_id equal to 1 only-----')
advisor_with_crypto = db_connector.query(Advisor).join(Fund).filter(Fund.advisor_id.__eq__(1))
for advisor_fund in advisor_with_crypto:
    for fund in advisor_fund.funds:
        print(advisor_fund.name, advisor_fund.fee, fund.advisor_id, fund.name, fund.type)


