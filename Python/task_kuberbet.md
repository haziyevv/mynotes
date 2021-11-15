**Task:** Build a Docker container image from provided code and a Dockerfile using Cloud Build. Then upload the container to Container Registry.

**Objectives**: Use Cloud Build to build and push containers. Use Container Registry to store and deploy containers.





1. create a Dockerfile:

   ```bash
   FROM alpine
   COPY quickstart.sh /
   CMD ["/quickstart.sh"]
   ```

2. - In Cloud Shell, run the following command to build the Docker container image in Cloud Build.

     ```bash
     gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/quickstart-image .
     ```

   - Other possible way is:

     create a yaml file cloudbuild.yaml:

     ```bash
     steps:
     - name: 'gcr.io/cloud-builders/docker'
       args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
     images:
     - 'gcr.io/$PROJECT_ID/quickstart-image'
     ```

     then:

     ```bash
     gcloud builds submit --config cloudbuild.yaml .
     ```

   - Another possible yaml that tests the container:

     ```bash
     steps:
     - name: 'gcr.io/cloud-builders/docker'
       args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
     - name: 'gcr.io/$PROJECT_ID/quickstart-image'
       args: ['fail']
     images:
     - 'gcr.io/$PROJECT_ID/quickstart-image
     ```

     

