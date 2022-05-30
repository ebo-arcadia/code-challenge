from sqlalchemy import Column, Integer, String, and_, or_, ForeignKey, text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query

# create a database along with a connectivity, a table, and mapped it to a python class object
db_engine = create_engine("sqlite:///polaris.db", echo=True)
Base = declarative_base()


class Fund(Base):
    __tablename__: str = 'fund'
    id = Column(Integer, primary_key=True)
    alternative_identifier = Column(Integer)
    name = Column(String)
    market_cap = Column(String)
    value = Column(String)


class Sleeve(Base):
    __tablename__: str = 'sleeve'
    id = Column(Integer, primary_key=True)
    alternative_identifier = Column(Integer)
    fund_relationship = Column('sleeve_id', ForeignKey('fund.id'), nullable=False)
    name = Column(String)


Base.metadata.create_all(db_engine)

# how to interact with the database?
# using another object but how to create one?
# how does this object bound to which object in order to performance database interaction?
# what functions or methods that are inherited to the Session class and subsequent session object?

Session = sessionmaker(bind=db_engine)
print("------what type is the Session class?------")
print(type(Session))
print(Session)
session = Session()
print("------what type is the session object?------")
print(type(session))
print(session)
print("------break------")

print("------add records or data to the table-------")
print("------add one record--------")
add_one = Fund(alternative_identifier=1040, name="vanguard SP500 spartan", market_cap="3%", value="300k")
add_one_sleeve = Sleeve(alternative_identifier=87, fund_relationship=1, name="growth 30 years")
session.add(add_one)
session.add(add_one_sleeve)
session.commit()

print("------add multiple records--------")
add_more = [
    Fund(alternative_identifier=2100, name="vanguard treasury 30 yrs", market_cap="20%", value="140k"),
    Fund(alternative_identifier=3512, name="vanguard tech index", market_cap="7%", value="50k"),
    Fund(alternative_identifier=6812, name="vanguard medical china region", market_cap="14%", value="30k"),
    Fund(alternative_identifier=7819, name="vanguard SP500 spartan", market_cap="3%", value="300k"),
    Fund(alternative_identifier=101, name="fidelity stable ST100", market_cap="88%", value="11k"),
    Fund(alternative_identifier=220, name="fidelity income growth", market_cap="99%", value="22k"),
    Fund(alternative_identifier=309, name="fidelity bullet prove", market_cap="77%", value="33k"),
    Fund(alternative_identifier=90909090, name="crypto", market_cap="88%", value="11k"),
]
session.add_all(add_more)
session.commit()

print("-------query a table using defined query object---------")
# how to execute SQL select statement to render and display record from a table?
# class, object, sql expression, print result
# object.query(mapped class).return_result
query_fund = session.query(Fund).all()
print("type of query_fund object is:", type(query_fund))
# iterate query_fund object
for record in query_fund:
    print("alt_id: ", record.alternative_identifier,
          "fund_name: ", record.name,
          "market_cap: ", record.market_cap,
          "fund_value: ", record.value
          )

print("-------query a table using Query class---------")
query_fund_table = Query(Fund, session)
print("type of query_fund_table is:", type(query_fund_table))
for record in query_fund_table:
    print(record.alternative_identifier, record.name, record.market_cap, record.value)

print("----using filter method to query a table-------")
filtered_fund = query_fund_table.filter(Fund.alternative_identifier > 3000).all()
# filtered_fund = session.query(Fund).filter(Fund.alternative_identifier > 3000).all()
print("type of filtered_fund object:", type(filtered_fund))
for record in filtered_fund:
    print(record.alternative_identifier, record.name, record.market_cap, record.value)

print("--------fetch an object corresponding to a row in a table using get()--------")
Handler = sessionmaker(bind=db_engine)
table_handler = Handler()
fetch_one = table_handler.query(Fund).get(1)
print(fetch_one)
print(fetch_one.alternative_identifier, fetch_one.name, fetch_one.market_cap, fetch_one.value)

# update values for this selected row
fetch_one.name = 'vanguard comprehensive package'
fetch_one.market_cap = '8%'
fetch_one.value = '800000k'

table_handler.commit()
fetch_one_updated = table_handler.query(Fund).first()
print(fetch_one_updated.alternative_identifier, fetch_one_updated.name, fetch_one_updated.market_cap,
      fetch_one_updated.value)

# rollback previous operation
# table_handler.rollback()

# how to execute bulk updates?
print('-------update multiple common values-----')
selected_funds = table_handler.query(Fund).filter(Fund.name.like('fidelity%'))
for fund in selected_funds:
    print(fund.alternative_identifier, fund.name)

print('------print updated row or column values-------')
selected_funds.update({Fund.name: Fund.name + " Investment"}, synchronize_session="fetch")
for fund in selected_funds:
    print(fund.alternative_identifier, fund.name)

print('-----commit change to persistently update the table in the database-------')
table_handler.commit()

print("------applying filter method to retrieve rows and columns from result set----")
filtered_result_set = table_handler.query(Fund).filter(Fund.name.like('vanguard%'), Fund.value == '300k')

for filtered_funds in filtered_result_set:
    print(filtered_funds.alternative_identifier, filtered_funds.name, filtered_funds.market_cap, filtered_funds.value)

print('------apply filter operators-----')
# what goes into filter()?
# ==, !=, and_(), or_(), in_(), like(), etc

obj_to_retrieve_a_fund_by_id = table_handler.query(Fund).filter(Fund.alternative_identifier == 1040)
print('fund with id 1040 is: ')
for fund in obj_to_retrieve_a_fund_by_id:
    print(fund.alternative_identifier, fund.name)
print('---------------')

obj_to_retrieve_non_fidelity_funds = table_handler.query(Fund).filter(Fund.name != "crypto")
print('fund set without crypto: ')
for fund in obj_to_retrieve_non_fidelity_funds:
    print(fund.alternative_identifier, fund.name)
print('---------------')

obj_to_retrieve_fidelity_and_crypto = table_handler.query(Fund).filter(
    and_(Fund.name.like('fidelity%'), Fund.name.like('crypto%')))
print('result only contains fidelity and crypto')
for fund in obj_to_retrieve_fidelity_and_crypto:
    print(fund.alternative_identifier, fund.name)

obj_to_retrieve_vanguard_or_fidelity = table_handler.query(Fund).filter(
    or_(Fund.name.like('fidelity%'), Fund.name.like('vanguard%')))
print('result only contains fidelity and crypto')
for fund in obj_to_retrieve_vanguard_or_fidelity:
    print(fund.alternative_identifier, fund.name)
print('---------------')

obj_to_retrieve_funds_in_altIds = table_handler.query(Fund).filter(Fund.alternative_identifier.in_([1000, 2000]))
print('result only contains funds with alt ids between 1000 and 2000')
for fund in obj_to_retrieve_funds_in_altIds:
    print(fund.alternative_identifier, fund.name)
print('---------------')

print('------returning list immediately upon SQL execution-------')
all_fidelity_funds = table_handler.query(Fund).filter(Fund.name.like('fidelity%')).all()
print('------returns list of all fidelity funds-------')
for fund in all_fidelity_funds:
    print(fund.alternative_identifier, fund.name)

print('---------------')
print('-------using one() or scalar() to check no rows error-------')
# check_if_rows_exist_in_sleeve_table = table_handler.query(Sleeve).one()
# only_one_sleeve = table_handler.query(Sleeve).scalar()
# print(only_one_sleeve.alternative_identifier, only_one_sleeve.fund_relationship, only_one_sleeve.name)

print('------using text() construct to link SQL stmt to mapped ORM ----------')
for textually_filtered_funds in table_handler.query(Fund).filter(text("alternative_identifier>2000")):
    print(textually_filtered_funds.name, textually_filtered_funds.market_cap, textually_filtered_funds.value)

print('---specify filtering with binding parameters when querying-----')
find_one = table_handler.query(Fund).filter(text("alternative_identifier = :value").params(value=1040)).all()
for fund in find_one:
    print(fund.id, fund.alternative_identifier, fund.name, fund.value)


print('----use from_statement to construct and execute entire string-based SQL statement-----')
string_based__filter_fund = table_handler.query(Fund).from_statement(text("SELECT * FROM fund")).first()
print(string_based__filter_fund.name, string_based__filter_fund.value)


print('----passing columns expression as positional arguments-----')
statement = text("SELECT alternative_identifier, name, market_cap, value FROM fund")
statement = statement.columns(Fund.alternative_identifier, Fund.name)
result = table_handler.query(Fund.alternative_identifier, Fund.name).from_statement(statement).first()
print(result)
