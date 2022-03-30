1. **How to build a docker image ?**

   - from a dockerfile in the same directory and the image with name testing and version v1.3.0

   ```bash
   docker build -t testing:v1.3.0 .
   ```

   - from a dockerfile in the specified path and build the docker image in this directory:

   ```bash
   docker build -t testing:v1.3.0 -f docker/Dockerfile .
   ```

   

1. How to run docker container and open its terminal ?

   ```bash
   docker run -it busybox sh
   ```

3. Example 1:

   ```dockerfile
   FROM python:3
   ENV PYTHONUNBUFFERED 1
   RUN mkdir /code
   WORKDIR /code
   COPY requirements.txt /code
   RUN pip install -r requirements.txt
   COPY . /code
   CMD python run.py
   ```

4. If you are dockerizing a flask script, change the host ip addres from "192.1.0.0" to "0.0.0.0".

   ```python
   app.run(host="0.0.0.0", port=5000, debug=os.environ.get("debug")=='1')
   ```

   here we also give port address and take debug variable from environment

5. If you dockerize flask, when you run the command expose the flask port to outside computer.

   ```bash
   docker run -p 5000:5000 -e DEBUG=1 flask_app_dev
   
   # -e DEBUG gives the environment variable DEBUG a value of 1
   ```

6. How to stop a container ?

   ```bash
   docker stop 838456456
   ```

   stops the docker container with the given id

7. How to look at the logs in the container ?

   ```bash
   docker logs container_id
   #or
   docker logs container_name 
   ```

8. How to create a container with a name given by you ?

   ```bash
   docker run --name kelbecer redis:latest
   ```

9. How to open a running container's shell ?

   ```bash
   docker exec -it container_id /bin/bash
   ```

10. What is the difference between `docker run` and `docker start` ?

    --> `docker run` creates a container from an image

    --> `docker start` is for starting a container, that is already created

11. What is `docker network` and how to create a `docker network` ?

    ```bash
    # Docker network allows two containers inside a dockerfile to connect with each other
    docker network create mongo-network
    
    # this will create a docker network named mongo-network
    ```

12. To create a mongo container with environmental variables and also connect it to a network:

    ```bash
    docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password --name mongodb --net mongo-network mongo
    
    # here:
    # -e  is used to give environmental variables
    # --net is used to connect to a network
    ```

13. How to remove a docker image ?

    ```bash
    docker rmi image_id
    ```

14. How to start a docker-compose from a file ?

    ```bash
    docker-compose -f docker-compose.override.yml up
    ```

15. How to debug in docker-compose ?

    1. add **stdin_open:true** and **tty:true** inside the service

    ```dockerfile
    services:
      autocorrect:
        stdin_open: true
        tty: true
        command:
    ```

    2. start the docker-compose:

    ```bash
    docker compose -f test.yml up
    ```

    3. Call the started container:

    ```bash
    docker attach container_id
    ```

16. How to assign the port of the container to the local machine ?

    ```bash
    docker run -p 3000:3000 test_image
    ```

17. 















```
docker build -t gcr.io/bghntr-speech-recognition/testing .
docker push gcr.io/bghntr-speech-recognition/testing

gcloud ai-platform jobs submit training mytestingmodell --region us-west1 --master-image-uri 'gcr.io/bghntr-speech-recognition/testing:latest' --scale-tier=CUSTOM --master-machine-type=n1-standard-8 --master-accelerator=type=nvidia-tesla-t4,count=2 --job-dir gs://my-test-models/mytestingmodell -- --model-name='finetuned-bert-classifier'
```

gcloud ai-platform jobs submit training indianwav2vec --region us-west1 --master-image-uri 'gcr.io/bghntr-speech-recognition/testspeechbig:latest' --scale-tier=CUSTOM --master-machine-type=n1-standard-8 --master-accelerator=type=nvidia-tesla-t4,count=4 --job-dir gs://my-test-models/indianwav2vec -- --model-name='wav2vecindian'

```bash
docker build -t sepen --build-arg data_path=gs://stt_train_data --build-arg train_data_path=indian_train_data.csv --build-arg audio_path=gs://voiceloft_amazon_data/media --build-arg test_data_path=indian_test_data.csv .
```

