1) Create cloud instance from cloud shell. This will create a cloud instance named **testc** on **us-central1-a** zone.

```
gcloud compute instances create testc --zone us-central1-a
```

2) Config from cloud shell the default zone to **us-central1-b**. 

```
gcloud config set compute/zone us-central1-b
```

If we create an instance by default it will be assigned to zone **us-central1-b**

3) To connect to an instance through ssh:

```
gcloud compute ssh testc
```

If the instance is in another zone --> then it will not ssh. So you should give the zone name:

```
gcloud compute ssh testc --zone us-central1-a
```

4. To create a persistent disk:
   
   ```
   gcloud compute disks create disk-2 --size=100gb --zone=us-central1-a
   ```

5. To attach a disk to an instance:
   
   ```
   gcloud compute instances attach-disk testc --disk disk-2 --zone=us-central1-a
   ```

    to see if it is attached ssh to the instance and :

```
gcloud compute ssh testc


ls -la /dev/disk/by-id/
```

## Kubernetes

- Virtual Machines have their own operation systems, but in containers you do not need an operation system, you use the main machine's system.

- Kubernetes is a container cluster, where lots containers work.

- <img title="" src="figures/kubernetes.png" alt="">

**Kubernetes** consists of a number of **node instances** and each node instance can be named as **Pod**. Each Pod is consisting of several **containers**.

To create kubernetes cluster with one node instance

```
gcloud container clusters create my-first-cluster --num-nodes 1
```

To deploy a wordpress docker container to our kubernetes cluster. 

```
kubectl run wordpress --image=tutum/wordpress --port=80
```

tutum/wordpress is an out-of-the box docker image that includes eveything to run the site. Applying the code above a pod is created. 

```
kubectl get pods
=>
NAME        READY   STATUS    RESTARTS   AGE
wordpress   1/1     Running   0          3m6s
```

By default a pod is accessible to only other machines in the cluster. 

We should expose the pod as a service so it can be accessed externally. 

## App Engine

2 different App Engine choices exist:

1) **Standard**: Preconfigured with os and programs

2) **Flexible**: More like a compute engine. You can chose os and even create docker files to run.

**Cloud Functions**

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

## Postgresql

1) Switching to postgres account:

```
sudo -i -u postgres
```

2. To access postgrees prompt type:

```
psql
```

3. Create a database

```
sudo -u postgres createdb student_db
```

4. Create user

```
sudo -u postgres createuser student
psql
alter user student with encrypted password "kelem";
```

Create user student. Then enter posgtgres terminal and then give that user a password.

5. To connect to the database with the given creadentials

```
psql -h 127.0.0.1 --username student -d student_db --password
```

Here we connect to **hostname=localhost**,  **username=student** and **database=student_db**

6. In psql when you do not commit a query after executing there will be error and psql will not let us continue. To continue with new queries, we should either commit or reconnect. To solve this **autocommit** is used.

```
conn = psycopg2.connect("host=127.0.0.1 user=student 
                        dbname=student_db password=student")


conn.set_session(autocommit=True)
```

7. To give user priviliges to create database:

```
sudo -i -u postgres
psql
alter user student with createdb;
```

8. In psycopg2, how to connect to a database ?

```
conn = psycopg2.connect("""host=127.0.0.1
                           user=student
                           dbname=student_db
                           password=student""")
```

9. In psycopg2 how to create a cursor ?

```
cursor = conn.cursor()
```

10. How to create a table **music\_library** with columns **album\_name**, **artist\_name**, **year**. 

```
try:
    cursor.execute("""create table if not exists music_library
                                    (album_name varchar,
                                     artist_name varchar,
                                     year int)""")
except psycopg2.Error as e:
    print(e)
```

11. How to insert into **music\_library** ?

```
insert_query = "insert into music_library (album_name, artist_name, year)
                values (%s,%s,%s)"
values = ["fosforlu cevriyem", "ibo", 1983]


cursor.execute(insert_query, values)
```

12. 
