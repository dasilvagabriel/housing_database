from datetime import date
from create import Office, estate_agent, House_listing, house_buyer, Sales, engine, Base
from sqlalchemy.orm import sessionmaker

# start session before inserting data
Session = sessionmaker(bind=engine)
session = Session()

# insert office, real estate agent, listings and buyers information
offices = [
    Office(officename = 'Morumbi'),
    Office(officename = 'Jardins 1'),
    Office(officename = 'Morumbi 2'),
    Office(officename = 'Jardins 2'),
    Office(officename = 'Jardins 3'),
]

agents = [
    estate_agent(officeid=2,firstname = 'Joanna',lastname='Silva',phone='415-2134455',email='Joanna.Silva@realestate.com'),
    estate_agent(officeid=1,firstname = 'Jose',lastname='Luis',phone='213-76334877',email='Jose@realestate.com'),
    estate_agent(officeid=1,firstname = 'Luiza',lastname='couto',phone='763-5231455',email='lcouto@realestate.com'),
    estate_agent(officeid=2,firstname = 'Alberto',lastname='souza',phone='623-5122731',email='Alberto.souza@realestate.com'),
    estate_agent(officeid=3,firstname = 'Celia',lastname='couto',phone='512-5436172',email='Celia@realestate.com'),
    estate_agent(officeid=4,firstname = 'Novaes',lastname='Jefe',phone='723-6537122',email='Novaes.Jefe@realestate.com'),
    estate_agent(officeid=5,firstname = 'Tereza',lastname='Linda',phone='623-5122731',email='Tereza@realestate.com'),
    estate_agent(officeid=3,firstname = 'Olivia',lastname='Rodrigo',phone='623-5122731',email='olivia@realestate.com'),
    estate_agent(officeid=4,firstname = 'Patrick',lastname='Pantaleao',phone='567-7123455',email='Patrick@realestate.com'),
    estate_agent(officeid=5,firstname = 'Frederico',lastname='Silveira',phone='831-4567122',email='fSilveira@realestate.com'),
]

downtownListings = [
    House_listing(listingname='1 bedroom in Morumbi', bedroom_no=1, bathroom_no=1, address='431 1st Ave, Sao Paulo', zipcode='10009', listing_price=185700.00, listing_date=date(2022,8,15), listing_month=202208, listing_agent=2, listing_office=1),
    House_listing(listingname='2 bedrooms in Avenida Brazil', bedroom_no=2, bathroom_no=1, address='38 E 28th Street , Sao Paulo', zipcode='10016', listing_price=255000.00, listing_date=date(2021,10,12), listing_month=202110, listing_agent=3, listing_office=1),
    House_listing(listingname='Unit 4C 101 Oeste 2nd Street', bedroom_no=3, bathroom_no=2, address='101 Oeste 2nd Street, Sao Paulo', zipcode='10009', listing_price=890000.00, listing_date=date(2022,9,3), listing_month=202209, listing_agent=2, listing_office=1),
    House_listing(listingname='Cozy 1 bedroom apartment in Morumbi', bedroom_no=1, bathroom_no=1, address='414 Oeste 10th Street, Sao Paulo', zipcode='10009', listing_price=335000.00, listing_date=date(2022,9,1), listing_month=202209, listing_agent=3, listing_office=1),
    House_listing(listingname='Two bedroom apartment in Morumbi', bedroom_no=2, bathroom_no=2, address='268 Oeste 4th Street, Sao Paulo', zipcode='10009', listing_price=53000.00, listing_date=date(2022,8,12), listing_month=202208, listing_agent=2, listing_office=1),
    House_listing(listingname='Four bedroom Condo', bedroom_no=4, bathroom_no=2, address='383 Oeste 10th Street, Sao Paulo', zipcode='10009', listing_price=1360000.00, listing_date=date(2022,7,10), listing_month=202207, listing_agent=2, listing_office=1),
    House_listing(listingname='Glamorous 4 bedroom condo', bedroom_no=4, bathroom_no=2, address='149 Avenue C, Sao Paulo', zipcode='10009', listing_price=599000.00, listing_date=date(2022,7,23), listing_month=202207, listing_agent=3, listing_office=1),
    House_listing(listingname='Rustic 3 bedroom apartment', bedroom_no=3, bathroom_no=1, address='633 Oeste 11th Street, Sao Paulo', zipcode='10009', listing_price=385000.00, listing_date=date(2022,6,10), listing_month=202206, listing_agent=2, listing_office=1),
]

subListings = [
    House_listing(listingname='3 bedroom with nice city views', bedroom_no=3, bathroom_no=1, address='345 Oeste 93rd Street, Sao Paulo', zipcode='10128', listing_price=680000.00, listing_date=date(2022,7,10), listing_month=202207, listing_agent=1, listing_office=2),
    House_listing(listingname='Luxurious condo in Jardins', bedroom_no=4, bathroom_no=2, address='340 Oeste 80th Street, Sao Paulo', zipcode='10075', listing_price=1665000.00, listing_date=date(2022,7,28), listing_month=202207, listing_agent=4, listing_office=2),
    House_listing(listingname='Luxurious condo in Park Avenue', bedroom_no=5, bathroom_no=3, address='925 Park Avenue, Sao Paulo', zipcode='10028', listing_price=3900000.00, listing_date=date(2022,8,15), listing_month=202208, listing_agent=4, listing_office=2),
    House_listing(listingname='Family-friendly apartment in Jardins', bedroom_no=5, bathroom_no=2, address='8 Oeste 83rd Street, Sao Paulo', zipcode='10028', listing_price=1699000.00, listing_date=date(2022,8,20), listing_month=202208, listing_agent=1, listing_office=2),
    House_listing(listingname='Affordable 3 bedroom apartment for young people', bedroom_no=3, bathroom_no=1, address='448 Oeste 84th Street, Sao Paulo', zipcode='10028', listing_price=425000.00, listing_date=date(2022,6,15), listing_month=202206, listing_agent=4, listing_office=2),
    House_listing(listingname='Artistic 3 bedroom condo', bedroom_no=3, bathroom_no=3, address='420 Oeste 72nd Street, Sao Paulo', zipcode='10028', listing_price=2100000.00, listing_date=date(2022,9,1), listing_month=202209, listing_agent=1, listing_office=2),
    House_listing(listingname='Triple Duplex on Park Avenue', bedroom_no=5, bathroom_no=3, address='730 Park Avenue, Sao Paulo', zipcode='10021', listing_price=35000000.00, listing_date=date(2022,6,23), listing_month=202206, listing_agent=1, listing_office=2),
]

buyers = [
    house_buyer(firstname='Alice',lastname='Petrovio',email='alice@gmail.com',phone='213-4132566'),
    house_buyer(firstname='Carlos',lastname='Simpson',email='csouza@gmail.com',phone='412-5634155'),
    house_buyer(firstname='Daniel',lastname='Couto',email='daniel.couto@gmail.com',phone='617-4223587'),
    house_buyer(firstname='Frederico',lastname='Souza',email='Frederico@gmail.com',phone='567-7123455'),
    house_buyer(firstname='Gregorio',lastname='Pedro',email='Gregorio.pedro@gmail.com',phone='719-5234612'),
]

session.add_all(offices)
session.add_all(agents)
session.add_all(downtownListings)
session.add_all(subListings)
session.add_all(buyers)
session.commit()

# Wrap the sales in a "transaction" function that can update the sales table and the listings table simultaneously.
def add_sales(house_buyer, house_listing, price, date_list, month, estate_agent):
    try:
        sale = Sales(buyerid=house_buyer,listingid=house_listing,sales_price=price,sales_date=date(date_list[0],date_list[1],date_list[2]), sales_month = month, agentid=estate_agent)
        session.add(sale)
        sale_listing = session.query(House_listing).get(house_listing)
        sale_listing.sold = True
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

add_sales(1,1,180000.00,(2022,8,12),202208,3)
add_sales(2,2,250000.00,(2022,8,28),202208,3)
add_sales(3,3,900000.00,(2022,8,15),202208,2)
add_sales(4,4,300000.00,(2022,8,3),202208,5)
add_sales(2,6,1200000.00,(2022,8,28),202208,2)
add_sales(3,7,600000.00,(2022,8,14),202208,8)
add_sales(2,8,400000.00,(2022,8,14),202208,5)
add_sales(1,9,750000.00,(2022,8,12),202208,4)
add_sales(4,10,1800000.00,(2022,8,10),202208,4)
add_sales(3,11,2500000.00,(2022,8,5),202208,1)
add_sales(2,13,450000.00,(2022,8,15),202208,7)
add_sales(4,14,1800000.00,(2022,8,12),202208,6)
add_sales(4,15,20000000.00,(2022,8,10),202208,10)
add_sales(1,12,1250000.00,(2022,8,8),202208,9)