## **Some Basic commands for Dockerfile**

1) **FROM** --> used to define the parent image

2) **RUN** --> before running any command in terminal:

```
RUN apt-get update
RUN pip install -r requirements.txt
RUN python3 hellp.py
```

3. **ADD** --> add everything in the current directory into a directory that will be created inside the image.

```
ADD . /frodo_baggins
```

Everything inside the current folder will be added into the froddo_baggins folder in the created image.



4. **WORKDIR** --> selects the working directory in the docker container.

```
WORKDIR /frodo_baggins
```



## Some basic commands for Docker-compose

1. **version** --> Used to define the compose file format

2. **services** --> we should define the services that we want to use

3. 










