from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

Base = declarative_base()
engine = create_engine("sqlite://", echo=True, future=True)
session = Session(engine)

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

def create_objects_and_persist():
    with Session(engine) as session:
        spongebob = User(
        name = "spongebob",
        fullname = "Spongebob Squarepants",
        addresses = [Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
        name = "sandy",
        fullname = "Sandy Cheeks",
        addresses = [Address(email_address="sandy@sqlalchemy.org"),
                     Address(email_address="sandy@squirrelpower.org"),],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()


def query_db_with_select():
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    for user in session.scalars(stmt):
        print(user)


def query_db_with_select_join():
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name == "sandy")
        .where(Address.email_address == "sandy@sqlalchemy.org")
        )
    sandy_address = session.scalars(stmt).one()
    print(sandy_address)


def make_changes_in_db():
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()

    patrick.addresses.append(
        Address(email_address="patrickstar@sqlalchemy.org")
    )
    session.commit()


def delete_from_db_using_remove():
    sandy = session.get(User, 2)
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name == "sandy")
        .where(Address.email_address == "sandy@sqlalchemy.org")
        )
    sandy_address = session.scalars(stmt).one()
    sandy.addresses.remove(sandy_address)


def delete_from_db_using_flush():
    session.flush()
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()
    session.delete(patrick)
    session.commit()


if __name__ == "__main__":
    user = User()
    address = Address()
    print(user, address)
    Base.metadata.create_all(engine)
    create_objects_and_persist()
    query_db_with_select()
    query_db_with_select_join()
    make_changes_in_db()
    delete_from_db_using_remove()
    delete_from_db_using_flush()

