# Data Engineering Basics

1. **ETL** --> Extract, transform and Load

## Relational Databases

When to use and pros? 

1. Aggregations are possible, such as group by, join etc.

2. You can do joins.

3. ACID transactions.

4. Use with small data

5. You can add **secondary indexes** for fast querying.

ex: Your primary key is City but you see that most of the time you query using the country code. So you add the Country code as a secondary index, to make it faster for querying. 

| City   | Code | Country code |
| ------ | ---- | ------------ |
| Paris  | 011  | 1            |
| London | 013  | 2            |

### ACID transactions

- Properties of databases intended to guarantee their working even in problematic situations.

- **A**TOMICITY:  The whole transaction is processed or nothing is processed. ex: if a transaction consists of 3 operations and 1 one succeeds and second one does not succeed, then it should roll back to the start of the transaction and do not apply the first operation.

- **C**onsistency: Only valid data are added to database.

- **I**solation: One transaction should not affect the other transaction. 

- **D**urability: Completed transactions are saved to database, even if there is a system failure.

**When Not To Use Relational Databases**

- Large amounts of data.

- Need to do fast reads and writes. High throughput rate.

- Need to store different data formats

- Flexible schema. To add columns to some rows but not all.

- Horizontal scaling. Add new computers to the system. 

# MySQL

1. Installation: 

```
1. download mysql-apt-config_0.8.18-1_all.deb from mysql website
2. sudo dpkg -i /home/haziyevv/Downloads/mysql-apt-config_0.8.18-1_all.deb
3. sudo apt update
4. sudo apt install mysql-server
5. sudo apt install myslq-workbench-community
```

2. Create first database and tables in mysql:

```
mysql -p pasword

create database employees;
use employees;
create table employee_details (firstname varchar(20), lastname varchar(20),
                               birthday Date, salary decimal)
```

3. How to backup database in mysql ?

```
mysqldump -u root employees > employeesbackup.sql
```

4. How to backup only a table from a database ?

```
mysqldump --host=127.0.0.1 
          --port=3306 
          --user=root 
          --password 
          employees employee_details > employee_details.sql
```

5. How to restore the mysql database from the backup ?

```
mysql -u root restored_employees < employeesbackup.sql

other database in udacity:
mysql --host=127.0.0.1 
      --port=3306 
      --user=root 
      --password 
      sakila < sakila_mysql_dump.sql

if you are inside the mysql command line : source employeesbackup.sql
```

6. How to load data to a table in mysql ?

```
# using infile statement
load data infile 'employeesdata.csv' into table employees_details

# using mysqlimport utility
mysqlimport employees employees_details.csv
```

7. How to show all the tables of a database ? 

```
show full tables where table_type='BASE TABLE'
```

8. How to explore the structure of any table in mysql ?

```
describe table_name;
```





# Postgresql

1) Switching to postgres account:

```
sudo -i -u postgres
```

2. To access postgrees prompt type:

```
psql
```

3. To change postgres user to ask a password:

```
1)--> cd /etc/postgresql/12/main/
2)--> edit pg_hba.conf

change from

# TYPE DATABASE USER ADDRESS METHOD
local  all      all          md5

to

# TYPE DATABASE USER ADDRESS METHOD
local  all      all          trust

3) sudo service postgresql restart
4) psql -U postgres
5) alter user postgres with password 'password';
6) revert changes in pg_hba.conf from trust to md5
7) restart postgresql 
```

4. How to list databases in postgresql using psql command line?

```
\l
```

5. Create a database

```
sudo -u postgres createdb student_db
```

**Create user**

```
sudo -u postgres createuser student
psql
alter user student with encrypted password "kelem";
```

Create user student. Then enter **posgtgres** terminal and then give that user a password.

6. How to connect to a database in psql command line ?

```
\connect student_db
```

7. To connect to the database with the given creadentials

```
psql -h 127.0.0.1 --username student -d student_db --password
```

Here we connect to **hostname=localhost**,  **username=student** and **database=student_db**



8. How to restore a backed up database in psql ?

   using psql command:

   ```sql
   psql restored_employees < employeesbackup.sql
   ```

   inside the psql command line:

   ```sql
   \connect student_db;
   include student_db_dump.sql;
   ```

9.  How to list all the tables in a database ?

```sql
\dt;
```

10. How to explore the structure of a table named **store** inside the **student** database ?

```
\d store;
```



11. How to dump a database in postgres ?

```
pg_dump employees > employeesbackup.sql
pg_dump --username=postgres --host=localhost --password --dbname=sakila --table=store --format=plain > sakila_store_pgsql_dump.sql

```

12. In psql when you do not commit a query after executing there will be error and psql will not let us continue. To continue with new queries, we should either commit or reconnect. To solve this **autocommit** is used.

```
conn = psycopg2.connect("host=127.0.0.1 user=student 
                        dbname=student_db password=student")


conn.set_session(autocommit=True)
```

13. To give user priviliges to create database:

```
sudo -i -u postgres
psql
alter user student with createdb;
```



14. In psycopg2, how to connect to a database ?

```
conn = psycopg2.connect("""host=127.0.0.1
                           user=student
                           dbname=student_db
                           password=student""")
```

15. In psycopg2 how to create a cursor ?

```
cursor = conn.cursor()
```

16. How to create a table **music\_library** with columns **album\_name**, **artist\_name**, **year**. 

```
try:
    cursor.execute("""create table if not exists music_library
                                    (album_name varchar,
                                     artist_name varchar,
                                     year int)""")
except psycopg2.Error as e:
    print(e)
```

17. How to insert into **music\_library** ?

```
insert_query = "insert into music_library (album_name, artist_name, year)
                values (%s,%s,%s)"
values = ["fosforlu cevriyem", "ibo", 1983]


cursor.execute(insert_query, values)
```

18. Data Types:

**text**: text data with unlimited size

**varchar**: text data with limited number of characters, at most 250, default 80

**bigint**: like long -> integer with 64 bit precision

**numeric**: floating point number. can be initialised like this numeric(7,3)-> here 7 is the total number of digits, 3 is the number of digits after comma. but if we initialize only numeric, it will take as much digit as it can.

**decimal**: same thing as numeric.

19. Explain **views** in postgres:
    - Views are alternative way of representing one or more tables or views.
    - You can keep some info from different tables in a view.
    - You can protect some info like private customer informations by not putting them on view.
    - You can use it as a copy of a table, to not interact with the main table directly each time.

20. Explain **materialized views** in postgres:
    * It is created similar to the normal view, but you can not insert, update or delete to it.
    * It is faster than the normal view but you can not change it.
21. 

# NoSql Databases

1) Common types of NoSQL databases:
   
   1) **Apache Cassandra** --> Partition raw store. Data is distributed as partitions, accross nodes or servers. Data is organised in a columns and rows format. 
   
   2) **MongoDb** --> Document Store. In addition to key lookups performed by key value, this databases offer a query that retrieves document based on its contents. Easy to do search on documents.
   
   3) **DynamoDb** --> Key value store. Data is represented as a collection of key value pairs.
   
   4) **ApacheHbase** --> Wide column Store. Also uses tables, rows and collumns like a relational database. But unlike a relational database, the names and formats of columns can vary from row to row.
   
   5) **Neo4J** --> Graph Database. Data is represented as nodes and edges.

# Basics of Apache Cassandra

* **Keyspace** --> like a database in a relational database.
  
  * Collection of tables.

* **Table** --> A group of partitions.

* **Rows** --> A single item.

* **Partition** --> Is a fundamental unit of access. Collection of rows. How the data is distributed.

* **Primary key**--> Made up of a partition key and clustering columns

* **Columns** --> Consists of **Clustering Columns**  and **Data Columns**. Labeled Element.

<img title="" src="file:///home/haziyevv/Documents/mynotes/figures/casandra_basics.png" alt="">

Uses its own query language **CQL** (cassandra query language)

1. What is scale-up linearity ? 

    It means the more nodes you add to your system the more it grows linearly.

2. When not to use NoSQL?
   
   1. Need ACID transactions
   
   2. Need to do **JOINS**
   
   3. Need to do aggregations and analysis.
   
   4. When you need changing business requirements.
   
   5. With NoSql you can not do ad hoc queries. You should know the queries in advance and build your data model for those queries.

3. To install cassandra driver to python ?

```
pip3 install cassandra-driver
```

4. How to connect to import  cassandra library to python ?

```
import cassandra
from cassandra.cluster import Cluster
```

5. How to connect to cassandra cluster in local ?

```
try:
    cluster = Cluster.connect(['127.0.0.1'])
    session = cluster.connect()
except Exception as e:
    print(e)
```

6. How to create a **keyspace** ?

```
query = """create keyspace if not exists udacity
           with replication={'class':'SimpleStrategy',
            'replication_factor':1}"""
```

7. How to connect to a keyspace ? 

```
session.set_keyspace('udacity')
```

8. How to create a table ?

```
query = ""create table if not exists (song text, artist_name text,
                           album_name text, year int, single boolean,
                            PRIMARY_KEY(year, artist_name))""
```

# Relational Data Models

1. Divided to two broad categories **OLAP** and **OLTP**
   
   **OLAP**: online analytical processing. Used for data analysis. More aggregations and complex queries. 
   
   **OLTP**: online transactional processing. Used for daily requests and queries. 

2. Normalisation and denormalisation

**Normalisation** is the process of removing copies and redundacies in the table to make it fast for insrt, update and delete operations.

**Denormalisation** is the process for making read queries faster at the cost of copies in the table. 

3. **Fact** and **Dimension** tables. Fact tables are about measurements, metrics and facts. The rest are dimension tables.

4. **Star** and **Snowflake** schemas are used for creating fact and dimension tables.

5. **Composite** key is where group of columns are used as primary key.

6. **Upsert** : this means insert or update the row if it already exists. In postgresql:
- Check if exists and do nothing:

```
insert into customer_address (customer_id, customer_street)
values (1, "dadash dadashov")
on conflict (customer_id)
do nothing;
```

* Check if exists and update:

```
insert into customer_address (customer_id, customer_street)
values (1, "dadash dadashov")
on conflict (customer_id)
do update 
    set customer_street = EXCLUDED.customer_street;
```

Excluded -- means the row that is not inserted because of conflict. Here excluded.customer\_street is "dadash dadashov"

# NoSQL Data Models

1. Primary keys in Cassandra
* May consist of partition key and cluster key or only partition key.

* If you want to query the table you should always add the **partition key** to the **where** clause  Clustering keys can also be added to query but in the **sorted order**.

* You should select the primary key carefully, because data is distributed in nodes by the primary key. If you select **city id** as the primary key, then more data will be on Baku than Kalbajar for example. That is why **primary** key should be selected carefully to dsitribute data evenly.

* Cassandra sorts data for partition and clustering keys in descending order.

# Questions

### Querying data

1. Retrieve the next 3 film names distinctly after first 5 films released in 2015 ?
   
   ```
   select distinct title from films where releasedyear=2015 limit 3 offset 5;
   ```

2. How to select the distinct person names from the table ?

   ```
   select distinct name from person_table;
   ```

3. How to count the distinct person names from the table ?

   ```
   select count(distinct name) from person_table;
   ```

4. How to calculate the standard deviation of **age** column in the table ?

   ```
   select stddev(age) from person_table;
   ```

5. How to find the number of person from each age ?

   ```
   select count(name) from person groupby age;
   ```

6. How to update the surname of a person named "farid" in person table ?

   ```
   update persons
   set surname='haziyev'
   where name='farid';
   ```

7. What is the difference between **OLTP** and **OLAP**. Give examples to each of them.

8. What are some factors that you will take into account while building a data infrastructure ? 

9. What is data model ?

   Data model is a blueprint of a database system

10. What are **Entities** and **Attributes** in **Entity Relationship Model** ?

   - Entities are tables and Attributes are the columns of the table.

11. What is **Relational schema** in a relational model ?

    * It shows the names of the table attributes with their data type.

12. What is **Relational instance** in a relational model ?

    * It is the actual table created in database

13. What does **degree** refer in a relational model ?

    * Number of attributes in a table

14. What does **cardinality** refer in a relational model ?

    * Number of rows in a table

15. What are **DDL** and **DML** statements ?

    * **DDL** used for defining tables
      
      * create, alter, truncate, drop

    * **DML** used for manipulating data in tables
      
      * **CRUD** operations: insert, select, update, delete

16. How to add **telephone\_number** with data type bigint column to **author** table ?

```
Alter table author
    add column telephone_number bigint;
```

15. How to alter the data type of the **telephone\_number** column from bigint to varchar(20) ?

```
Alter table author
    alter column telephone_numner set data type varchar(20)
```

16. How to drop the column **telephone\_number** ?

```
Alter table author
    drop column telephone_number
```

17. What is the difference between char(20) and varchar(20) ?

> With char(20) 20 byte will be stored even if the inputed text is less than 20 characters. But with varchar if you store 15 characters, then it will take 15 bytes. But varchar also stores 1-2 bytes for storing varying lenthg input.

18. How to drop a table ?

```
drop table author;
```

19. How to remove all the raws from a table immediately ?

```
truncate table author immediate;
```

20. How to assign a primary key, while creating a table ?

```
Create table Author 
    (author_id int not null, name varchar, surname varchar
    Primary Key(author_id));
```

21. How to add a primary key, after the table is already created ?

```
Alter table author
    Add primary key(author_id)
```

22. How to create foreign key, while creating a table ?

```
Create table Book 
    (book_id int not null, name varchar, author_id int)
    Primary Key(book_id)
    Constraint fk_copy_author Foreign Key(author_id)
        References author(author_id)
        On Delete Cascade);
```

-- > will create a table with primary key **book\_id** and foreign key **author\_id**. 

--> **on delete cascade** means if the author id is deleted in the parent class this row will be deleted.

23. How to add foreign key after the table is created ?
    
    ```
    ALTER TABLE BookShop
    ADD CONSTRAINT fk_BookShop FOREIGN KEY (AUTHOR_ID)
        REFERENCES BookShop_AuthorDetails(AUTHOR_ID)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION;
    ```

24. How to create an index in a **RDBMS** ?

```
Create Unique Index unique_book_id On book(book_id);
```

24. What are the disadvantages of **indexing** in **RDBMS** ?
* Use disk space

* Decreased performance on insert, update and delete queries.
25. What are first, second and third normal forms ?
* **First form:** 1) Each row should be unique 2) Each cell should contain a single value.

* **Second form**: 1) Same value should not be repeated in different rows.

* **Third form**: 
26. How to create **Author Details** table from a **Bookshop** table ?

```
Create table BookShop_AuthorDetails as (
select distinct AUTHOR_ID, AUTHOR_NAME, AUTHOR_BIO from BOOKSHOP
) with data;
```

27. How to select **Authors** from **authors** table whose name start with ma ?

```
SELECT * FROM authors where author_name like 'ma%'
```

28. How to create a view ?

```
CREATE VIEW testing (firstname, lastname) as 
SELECT first_name, last_name from person_table
```

29. Explain stored procedures:

> 
