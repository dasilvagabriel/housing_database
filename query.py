from create import Office, estate_agent, House_listing, house_buyer, Sales, Commission, engine, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, insert, select
from sqlalchemy.schema import Index

# start the session to query data into the database
Session = sessionmaker(bind=engine)
session = Session()

# function for printing results
def print_result(results):
    for result in results:
        print (result)

report_month = 202208 # specifying the month we want to report. 08 was the month with the most listings.

# Q1. find top 5 offices with the most sales for that month
Index('idx_agent_to_price',Sales.agentid, Sales.sales_price) # composite index to facilitate grouping sales price by agent
Index('idx_agent_to_office',estate_agent.agentid,estate_agent.officeid) # composite index to facilitate grouping office by agent
top_office_sales = session.query(
    Office.officename,
    func.sum(Sales.sales_price)
).\
    join(estate_agent,Sales.agentid==estate_agent.agentid).\
    join(Office,estate_agent.officeid==Office.officeid).\
    group_by(Office.officeid).\
    order_by(func.sum(Sales.sales_price).desc()).\
    limit(5)

print('Top 5 office by sales:')
print_result(top_office_sales)
print('==========================\n')

# Q2. top 5 agents with the most sales (inc. contact details)
top_agent = session.query(
    estate_agent.firstname,
    estate_agent.lastname,
    estate_agent.email,
    estate_agent.phone,
    func.sum(Sales.sales_price)
).\
    join(estate_agent,Sales.agentid == estate_agent.agentid).\
    group_by(estate_agent.agentid).\
    order_by(func.sum(Sales.sales_price).desc()).\
    limit(5)

print('Top 5 real estate agent by sales:')
print_result(top_agent)
print('==========================\n')

# Q3a. calculate commission for each agent and store in separate table
Index('idx_agent_sales',Sales.agentid) # Index to facilitate group by agent
commission = session.query(
    Sales.agentid,
    func.sum(Sales.comission),
    Sales.sales_month
).filter(Sales.sales_month==report_month).group_by(Sales.agentid)

i = insert(Commission).from_select(['agentid','commission','commission_month'],select=commission)
session.execute(i)
session.commit()

Index('idx_agent_agent', estate_agent.agentid) # Index to facilitate joining agent for the query on Commission table below
commission_by_agent = session.query(
    estate_agent.firstname,
    estate_agent.lastname,
    Commission.commission
).filter(Commission.commission_month == report_month).join(estate_agent, Commission.agentid == estate_agent.agentid)

print('Commission by agent:')
print_result(commission_by_agent)
print('==========================\n')

# Q3b. Number of days on the market
days_on_market = session.query(
    func.avg(func.julianday(Sales.sales_date)-func.julianday(House_listing.listing_date))
).filter(Sales.sales_month == report_month).join(House_listing,Sales.listingid == House_listing.listingid)

print(f'Average lead time for houses sold this month: {days_on_market[0][0]:.0f} days')
print('==========================\n')

# Q4. Average selling price
average_selling_price = session.query(
    func.avg(Sales.sales_price)
).filter(Sales.sales_month == report_month)

print(f'Average sale price for houses sold this month: ${average_selling_price[0][0]:.2f}')
print('==========================\n')