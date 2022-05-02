1. TPU is 200 times faster than GPU **
2. PubSub:
   1. Topic: 
   2. Example: We have a *Human Resources* topic. 
      1. a new employe joins the company, so several applications in the company needs to be updated
3. Dataflow: a fully managed service for executing Apache Beam Pipelines within the google cloud echosystem
   1. is serverless and noops. Noops means no maintenance is needed. 





## BigQueryML

- How to create a model ?

  ```sql
  CREATE OR REPLACE MODEL
  	mydataset.mymodel
  OPTIONS
  	( model_type='linear_reg',
  input_label_cols='sales',
  ls_init_learn_rate=.15,
  l1_reg=1,
  max_iterations=5 ) AS
  ```

  ```sql
  CREATE OR REPLACE MODEL `ecommerce.classification_model`
  OPTIONS(model_type='logistic_reg', labels = ['will_buy_on_return_visit'])
  AS
  #standardSQL
  SELECT
    * EXCEPT(fullVisitorId)
  FROM
    # features
    (SELECT
      fullVisitorId,
      IFNULL(totals.bounces, 0) AS bounces,
      IFNULL(totals.timeOnSite, 0) AS time_on_site
    FROM
      `data-to-insights.ecommerce.web_analytics`
    WHERE
      totals.newVisits = 1
      AND date BETWEEN '20160801' AND '20170430') # train on first 9 months
    JOIN
    (SELECT
      fullvisitorid,
      IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit
    FROM
        `data-to-insights.ecommerce.web_analytics`
    GROUP BY fullvisitorid)
    USING (fullVisitorId)
  ;
  ```

  Labels -> input_label_cols

  Features -> 

- Inspect training process ?

  ```
  select * from ML.TRAINING_INFO(MODEL `mydataset.mymodel`)
  ```

- How to make evaluation ?

  ```
  select * from ML.EVALUATE(MODEL 'mydataset.mymodel')
  ```

- How to make prediction ?

  ```
  select * from ML.PREDICT(MODEL 'mydataset.mymodel', (<query>))
  ```

- To evaluate:

```sql
SELECT
  roc_auc,
  CASE
    WHEN roc_auc > .9 THEN 'good'
    WHEN roc_auc > .8 THEN 'fair'
    WHEN roc_auc > .7 THEN 'not great'
  ELSE 'poor' END AS model_quality
FROM
  ML.EVALUATE(MODEL ecommerce.classification_model,  (
SELECT
  * EXCEPT(fullVisitorId)
FROM
  # features
  (SELECT
    fullVisitorId,
    IFNULL(totals.bounces, 0) AS bounces,
    IFNULL(totals.timeOnSite, 0) AS time_on_site
  FROM
    `data-to-insights.ecommerce.web_analytics`
  WHERE
    totals.newVisits = 1
    AND date BETWEEN '20170501' AND '20170630') # eval on 2 months
  JOIN
  (SELECT
    fullvisitorid,
    IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit
  FROM
      `data-to-insights.ecommerce.web_analytics`
  GROUP BY fullvisitorid)
  USING (fullVisitorId)
));
```



- How to make prediction:

```sql
SELECT
*
FROM
  ml.PREDICT(MODEL `ecommerce.classification_model_2`,
   (
WITH all_visitor_stats AS (
SELECT
  fullvisitorid,
  IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit
  FROM `data-to-insights.ecommerce.web_analytics`
  GROUP BY fullvisitorid
)
  SELECT
      CONCAT(fullvisitorid, '-',CAST(visitId AS STRING)) AS unique_session_id,
      # labels
      will_buy_on_return_visit,
      MAX(CAST(h.eCommerceAction.action_type AS INT64)) AS latest_ecommerce_progress,
      # behavior on the site
      IFNULL(totals.bounces, 0) AS bounces,
      IFNULL(totals.timeOnSite, 0) AS time_on_site,
      totals.pageviews,
      # where the visitor came from
      trafficSource.source,
      trafficSource.medium,
      channelGrouping,
      # mobile or desktop
      device.deviceCategory,
      # geographic
      IFNULL(geoNetwork.country, "") AS country
  FROM `data-to-insights.ecommerce.web_analytics`,
     UNNEST(hits) AS h
    JOIN all_visitor_stats USING(fullvisitorid)
  WHERE
    # only predict for new visits
    totals.newVisits = 1
    AND date BETWEEN '20170701' AND '20170801' # test 1 month
  GROUP BY
  unique_session_id,
  will_buy_on_return_visit,
  bounces,
  time_on_site,
  totals.pageviews,
  trafficSource.source,
  trafficSource.medium,
  channelGrouping,
  device.deviceCategory,
  country
)
)
ORDER BY
  predicted_will_buy_on_return_visit DESC;
```







## Custom Training

1. **Vertex AI workbench** is a single development environment for entire data science project. From exploring to training and then deploying.

   There are two options, for the environment to use. Pre-built container and custom container

   

## MLOps
#### Kubernetes and Containers
1. Build a docker image in the google container registry:
```
gcloud builds submit --tag gcr.io/project_name/test_image .
```

2. Build a docker image with a build configuration file. example: cloudbuild.yml:
```
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
images:
- 'gcr.io/$PROJECT_ID/quickstart-image'
```

to create image like in part 1:
```
gcloud builds submit --config cloudbuild.yml .
```

3. Build a docker image with a build configuration file and run it to test if it is successful:
config_file:
```
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
- name: 'gcr.io/$PROJECT_ID/quickstart-image'
  args: ['fail']
images:
- 'gcr.io/$PROJECT_ID/quickstart-image
```

<br/><br/>

4. In the container config what does **Limit** and **Request** mean?
- Request means the minimum amount of resource needed by the container, so it will not be assigned to a node with less resources
- Limit means the highest amount of resource to be used by the container


6. **Blue-Green Deployment**: New version is created and as soon as it is ready server will be directed to it.
7. **Canary Deployment**: Passed to the new deployment gradually

8. Services can be configured as ClusterIP, NodePort or LoadBalancer types 

 
####  Pipelines
- **Kubeflow**: out of box support for top frameworks such as pytorch, caffe, tf and xgboost
- **TFX**: Google best practices on TF


#### AI Platform
1. How to add editor permission for your cloud build service account ?
```
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
CLOUD_BUILD_SERVICE_ACCOUNT="${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com"
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member serviceAccount:$CLOUD_BUILD_SERVICE_ACCOUNT \
  --role roles/editor
```

2. How to set the project ID to your Google Cloud Project ?
```
export PROJECT_ID=$(gcloud config get-value core/project)
gcloud config set project $PROJECT_ID
```

3. Ho create a GKE cluster ?
```
gcloud container clusters create cluster-1 --zone us-central1-a --machine-type n1-standard-2 --scopes=https://www.googleapis.com/auth/cloud-platform
```

4. 






