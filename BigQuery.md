1. ```bash
   gcloud auth login --> to login to a cloud account
   gcloud init --> to configure cloud login
   ```

2. ```bash
   bq mk testing --> create a bigquery dataset named testing
   ```

3.  To upload a table from csv to bigquery: 

   ```bash
   bq load --autodetect testing.jeopardy /home/farid/jeopardy.csv
   
   autodetect --> automatically detect the schema
   testing.jeopardy --> dataset name . table name
   /home/farid/jeuoardy.csv --> local file to upload
   ```

4. To export a table to cloud storage:

   ```bash
   bq extract Dataset.Table gs://Bucket/File
   ```

5. 