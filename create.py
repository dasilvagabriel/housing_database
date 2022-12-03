import sqlalchemy
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///realestate.db', echo=True)
engine.connect()

# connect to the database
# create a database in case it doesn't exist
engine = create_engine('sqlite:///realestate.db', echo=True)
engine.connect()

# declarative method for creation of tables
Base = declarative_base()

class Office(Base):
    __tablename__ = 'office'
    officeid = Column(Integer, primary_key=True)
    officename = Column(Text)
    listings = relationship("House_listing")
    agents = relationship("estate_agent")

    def __repr__(self):
        return "<Office(ID={}, Office Name={})>".format(self.officeid, self.officename)

class estate_agent(Base):
    __tablename__ = 'estate_agent'
    agentid = Column(Integer, primary_key=True)
    officeid = Column(Integer,ForeignKey('office.officeid'))
    firstname = Column(Text)
    lastname = Column(Text)
    phone = Column(Text)
    email = Column(Text)
    listings = relationship("House_listing")
    sales = relationship("Sales")

    def __repr__(self):
        return "<Agent(ID={}, Name={} {}, Phone={}, Email={})>".format(self.agentid, self.firstname, self.lastname, self.phone, self.email)

class House_listing(Base):
    __tablename__ = 'House_listing'
    listingid = Column(Integer, primary_key=True)
    listingname = Column(Text)
    bedroom_no = Column(Integer)
    bathroom_no = Column(Integer)
    address = Column(Text)
    zipcode = Column(Text)
    listing_price = Column(Float)
    listing_date = Column(Date)
    listing_month = Column(Integer)
    listing_agent = Column(Integer, ForeignKey('estate_agent.agentid'))
    listing_office = Column(Integer, ForeignKey('office.officeid'))
    sold = Column(Boolean, default=False)
    sales = relationship("Sales")

    def __repr__(self):
        return "<Listing(ID={}, Name={}, Listing Price={}, Listing Date={}, Listing Agent={}, Listing Office={})>".format(self.listingid, self.listingname, self.listing_price, self.listing_date, self.listing_agent, self.listing_office)

class house_buyer(Base):
    __tablename__ = 'house_buyer'
    buyerid = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    sales = relationship("Sales")

# utility function to calculate the comission
def calc_comission(context):
    sales_price = context.get_current_parameters()['sales_price']
    if sales_price < 100000.00:
        return sales_price*0.1
    if sales_price <= 200000.00:
        return sales_price*0.075
    if sales_price <= 500000.00:
        return sales_price*0.06
    if sales_price <= 1000000.00:
        return sales_price*0.05
    return sales_price*0.04 

class Sales(Base):
    __tablename__ = 'sales'
    saleid = Column(Integer, primary_key=True)
    buyerid = Column(Integer, ForeignKey('house_buyer.buyerid'))
    listingid = Column(Integer, ForeignKey('House_listing.listingid'))
    sales_price = Column(Float)
    sales_date = Column(Date)
    sales_month = Column(Integer)
    agentid = Column(Integer, ForeignKey('estate_agent.agentid'))
    comission = Column(Float, default=calc_comission, onupdate=calc_comission) # utilize default and onupdate to insert and update comission data based on sales price

class Commission(Base):
    __tablename__ = 'commission'
    commissionid = Column(Integer, primary_key=True)
    agentid = Column(Integer, ForeignKey('estate_agent.agentid'))
    commission = Column(Float)
    commission_month = Column(Integer)

# create all the tables from above 
Base.metadata.create_all(bind=engine)