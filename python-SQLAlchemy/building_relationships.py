from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlalchemy.orm import subqueryload, selectinload, joinedload

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
    advisor_id = Column(Integer, ForeignKey('advisors.id', ondelete='CASCADE'))
    advisor = relationship('Advisor', back_populates='funds')


Advisor.funds = relationship('Fund', order_by=Fund.id, back_populates='advisor', cascade='all, delete-orphan')
Base_for_table.metadata.create_all(db_engine)

# insert data into the parent table
add_one_advisor = Advisor(name='Leon Kennedy', portfolio_identifier=1001, portfolio='Apple ML engineers', fee=700)
add_one_advisor.funds = [Fund(name='vanguard S&P standard', type='stocks')]

# insert via construct an advisor object providing mapped funds attribute in the constructor
add_one_advisor_with_constructor = [
    Advisor(
        name='Ada Wong', portfolio_identifier=2010, portfolio='Slack front-end developers', fee=850,
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
        name='Solid Snake', portfolio_identifier=3330, portfolio='HNS ER Doctor assistant group', fee=421,
        funds=[Fund(name='vanguard treasury 30 years', type='bond'),
               Fund(name='fidelity growth income', type='cryptocurrency'),
               Fund(name='fidelity blockchain new coins', type='cryptocurrency')]
    ),

    Advisor(
        name='Mave Rick', portfolio_identifier=4190, portfolio='Air Force One secretary', fee=380,
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

print('------------------')
print('----get advisor and funds from relational tables linked with foreign key 2------')
fund_alias = aliased(Fund)
# above aliased has no effect preventing cartesian warning nor does using the first filter
advisor_with_crypto = db_connector.query(Advisor).filter(Advisor.id == fund_alias.id).filter(Fund.advisor_id.__eq__(2))
for advisor_fund in advisor_with_crypto:
    for fund in advisor_fund.funds:
        print(advisor_fund.name, advisor_fund.fee, fund.name, fund.type)


print('------------------')
print('----get advisor and funds from relational tables linked with foreign key 3------')
# __eq__ only works with many-to-one --> Fund.advisor_id
advisor_with_crypto = db_connector.query(Advisor).join(Fund, Advisor.id == Fund.advisor_id).filter(Fund.advisor_id.__eq__(3))
for advisor_fund in advisor_with_crypto:
    for fund in advisor_fund.funds:
        print(advisor_fund.name, advisor_fund.fee, fund.advisor_id, fund.name, fund.type)


print('------------------')
print('----get advisor and funds from relational tables linked NOT with foreign key 4------')
# __ne__ only works with many-to-one --> Fund.advisor_id
advisor_with_no_bond = db_connector.query(Advisor).join(Fund, Advisor.id == Fund.advisor_id).filter(Fund.advisor_id.__ne__(4)).group_by(Advisor.name)
for advisor in advisor_with_no_bond:
    for fund in advisor.funds:
        print('advisor name: {}, fund name: {}, fund type: {}...'.format(advisor.name, fund.name, fund.type))


# contains()
print('------------------')
print('-----find cryptocurrency that is not vanguard-----')
vanguard_funds_only = db_connector.query(Fund).\
    filter(Fund.type.contains("cryptocurrency")).\
    filter(not_(Fund.name.contains("vanguard%")))

for fund in vanguard_funds_only:
    print(fund.name, fund.type, fund.advisor_id)

# any()
print('------------------')
print('------find any advisor with fund type stocks-----')
advisor_any_fund_cylinder = db_connector.query(Advisor).filter(Advisor.funds.any(Fund.type == 'stocks'))
for advisor in advisor_any_fund_cylinder:
    for fund in advisor.funds:
        print(advisor.name, advisor.fee, fund.name, fund.type)

# has()
print('------------------')
print('-----find fund and associate advisor with name Ada Wong----')
fund_with_a_name = db_connector.query(Fund).filter(Fund.advisor.has(Advisor.name == 'Ada Wong'))
for fund in fund_with_a_name:
    print(fund.name, fund.type, fund.advisor_id, fund.advisor.name)


# relationship loading techniques
# lazy loading
# eager loading
# no loading

print('------eager loading-------')
print('-----reduces queries save runtime-------')
print('------load object of collections or scalar association upfront-------')
print('-----return a particular advisor with associate funds using eager loading technique------')


eager_load_advisor = db_connector.query(Advisor).\
    options(subqueryload(Advisor.funds)).\
    filter(Advisor.name == "Leon Kennedy")
print(type(eager_load_advisor))
for advisor in eager_load_advisor:
    print('advisor name: {}; advisor fee: {}; advisor id: {};'.format(advisor.name, advisor.fee, advisor.id))
    for fund in advisor.funds:
        print("fund name: {}; fund type: {}. ".format(fund.name, fund.type))


print('---use selectinload() to solve disadvantages of using subqueryload() technique----')
eager_load_advisor_improved = db_connector.query(Advisor).\
    options(selectinload(Advisor.funds)).\
    filter(Advisor.name == "Leon Kennedy")

print(type(eager_load_advisor_improved))

for advisor in eager_load_advisor_improved:
    print('advisor name: {}; advisor fee: {}; advisor id: {};'.format(advisor.name, advisor.fee, advisor.id))
    for fund in advisor.funds:
        print("fund name: {}; fund type: {}. ".format(fund.name, fund.type))


print('-------------------------------------------')
print('-----use joinedload eager loading technique-----')
print('------used often for many-to-one relationship-----')
joined_load_advisor = db_connector.query(Advisor).options(joinedload(Advisor.funds)).filter(Advisor.name == "Ada Wong")

print(type(joined_load_advisor))

for advisor in joined_load_advisor:
    print('advisor name: {}; advisor fee: {}; advisor id: {};'.format(advisor.name, advisor.fee, advisor.id))
    for fund in advisor.funds:
        print("fund name: {}; fund type: {}. ".format(fund.name, fund.type))


# delete operation
# delete an object of a mapped class from a session and the commit the transaction
# verify in the table
# delete related object using cascade rules when defining the table

# 1. select the row to delete
# 2. delete the the row object
# 3. commit the delete operation
# 4. verify if the row is still in the table

print('--------------------')
print("------delete operation---------")
# example: delete all advisor named Ada Wong
advisor_ada_wong = db_connector.query(Advisor).get(2)
db_connector.delete(advisor_ada_wong)
db_connector.commit()
ada_wong_advisor_count = db_connector.query(Advisor).filter_by(name='Ada Wong').count()
print('how many advisor ada wong is left after deletion? ', ada_wong_advisor_count)

ada_fund = db_connector.query(Fund).filter(Fund.advisor_id == 2).count()
print('how many ada wong funds are left after deletion? ', ada_fund)


