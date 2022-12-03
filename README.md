# Real Estate Database
A SQLAlchemy implementation of a real estate company's Database. I used data normalization to reduce redundancy and indexes to retrieve data faster.

## Running the database
**Mac**
```
python3.6 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 insert_data.py
python3 query_data.py
```
**Windows**
```
python3.6 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 create.py
python3 insert_data.py
python3 query_data.py
```
## Notes on Data Normalization
*First Normal Form:*
1. The order in which data is stored does not matter
2. Each attribute in each table takes only one value and its domain remains unchanged
3. Each attribute has a unique name within the tablespace

*Second Normal Form:*
1. All other attributes of each table depend on the primary key (i.e. ID).

*Third Normal Form:*
1. No transitive dependencies as there are no non-primary key attributes dangling beyond the primary key of its own table
	- Example: An agent's last name does not depend on the agent's first name, only on the agent's agentID.
## Thank you notes
Thank you Ha Trang and Eugene Chan with the help especially on creating the queries that wrapped sales table and the listings table simultenously. 