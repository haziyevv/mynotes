## Request and Response

**Request Message**

| Request Start line | get/index.html HTTP/1.0                                              |
| ------------------ | -------------------------------------------------------------------- |
| **Request Header** | User-Agent: python-requests/2.21.0\n Accept-Encoding: gzip,deflate : |

**Response Message**

| Response Start line | HTTP/1.0 200 OK                                             |
| ------------------- | ----------------------------------------------------------- |
| **Response Header** | Server: Apache-Cache: UNCACHEABLE                           |
| **Response Body**   | <!DOCTYPE html><html><body><h1>My first heading</h1></html> |



**Status Code**

| 1XX | Informational           |
| --- | ----------------------- |
| 100 | Everything is so far ok |
| 2xx | Success                 |
| 200 | Ok                      |
| 3xx | Redirection             |
| 300 | Multiple Choices        |



| 4XX | Client Error   |
| --- | -------------- |
| 401 | Unathorized    |
| 403 | Forbidden      |
| 404 | Not Found      |
| 500 | Server Error   |
| 501 | No Implemented |





* How to send request to http://httpbin.org/get   using name = farid and id=123 with **get request** ?

```
requests.get("https://httpbin.org/get", 
              params={"name":"Farid", "id":123})
```

* How to send **post request** to http://httpbin.org/get using name=farid and id=123 ?

```
requests.post("https://httpbin.org/get",
               params={"name":"Farid", "id":123})
```





## Overview of HTTP

* **Scheme:** http://,  https:://

* **Internet adress or Base URL:** used to find the location, for example: www.ibm.com or www.gitlab.com

* **Route:** location on the web server, example: /images/IDNlogo.png
  
  
  
  
  
  
  
  
