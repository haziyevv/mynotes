# Secure Software Development Lifecycle
Application Security Base Principles
1. Confidentiality: preserve authorized restrictions on information access
2. Integrity: guarding against impromer information modification or destruction
3. Availability:
4. Usability

To achieve Aplication Security Base Principles:
1. Identification: user tells the system who he is, by usernmae
2. Authentication: process of verifying the users claimed identity
3. Authorization: After the user is permited to enter, what he has access to do
4. Auditing: evaluation of product or system


Three approaches to build an appliation
1. intuitive approach: elinden geleni elemek
2. Reactive approach: One security gate before the application rollout.
3. Proactive Approach

Parts od development before SDLC:
Planning --> Defining --> Designing --> Building --> Testing --> Deployment and Maintenance 

Access control policies MAC, RBAC, DAC

10 Famous Vulnerabilities
1. SQL injection: username ve passworda sql command yazib login olurlar veya databasei silirler


**Salting**:
Append random data to the password that is different every time
in the database keep username, pasword_hash and pasword_salt as seperate columns. 
**Pepper**: random data added everyones password. Kept secret and is same for every user
