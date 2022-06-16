1. TPU is 200 times faster than GPU
2. PubSub:
   1. Topic: 
   2. Example: We have a *Human Resources* topic. 
      1. a new employe joins the company, so several applications in the company needs to be updated
3. Dataflow: a fully managed service for executing Apache Beam Pipelines within the google cloud echosystem
   1. is serverless and noops. Noops means no maintenance is needed. 

**Apache Beam** is used to create the pipeline and **DataFlow** is the execution engine used to implement that pipeline




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



## Optimizers
1. Stochastic Gradient Descent
2. Momentum: Adding old weights with a coefficient to the new weight update. This stops us being stuck in local minimum. 
3. Nesterov Accelerated Gradients: Calculate gradients with respect to future weight values. 
``W_{future} = n*v_{old} + W_{old}``
``v_{new} = n*v_{old} - \sigma*\frac{d_{Loss}}{d_{W_{future}}}``

4. Adaptive Optimization: Learning rate and momentum coefficient will not stay constant throughout the training process. These values will adapt to each weight in the network.
5. Adagrad: (Adaptive gradients) - Decrease learning rate if weight is being updated too much in short time and it will increase if the weight is not updated much.
6. RMSProp: additionally to adagrad decay rate is added. 
7.  Adam: combination of RMSProp and Momentum. 



## ROC AUC
- It is a performance measurement for classification problems at various threshold settings.
- It tells how much the model is capable of distinguishing between classes.
- Higher the AUC, better the model at predicting class 0 as 0 and class 1 as 1
- Use it when you only care about ranking predictions and not outputting well calibrated probabilities
- Not use it when your data is heavily inbalanced
- Use it when you care about true positive and true negative the same


## Prediction Bias
- Prediction bias = average of predictions - average of labels in dataset


#### Question
- What is feedback loop ?
A model predicts university rankings based on the scores of the students. Then students will see the results and good students will go to those universities, increasing their scores further.
- 

## Types of Bias
1. Reporting Bias
2. Automation Bias
3. Selection Bias
    1. Coverage bias
    2. Non-response bias
    3. Sampling Bias
4. Group Attribution Bias
    1. In-group Bias
    2. Out-group Bias
5. **Implicit Bias**: When assumptions are made by ones own beliefs rather than the actual. ex: An engineer training a gesture classification takes head shake as no, but it is actually yes in some cultures



## TOOLS
1. **Dataproc**: 
2. Service Types:
    1. IAAS: infrastructure as a service(compute engine)
    2. PAAS: Platform as a service (app engine)
3.     
 


## Data Management
- Unstructured data are usually stored in Cloud Storage
- **Cloud Storage** has four primary storage classes:
    - Standard Storage (for frequently accessed or data stored for a brief period of time)
    - Nearline Storage: Data read or modified once per month
    - Coldline Storage: Once every 90 days
    - Archive Storage: Once every year
- Structured data:
    - Transactional data: Fast data inserts and updates are required. If you acces your data with sql : **Cloud SQL** or **Cloud Spanner** is needed. If no sql **Firestore** is the option.
    - Analytical data: Used when entire data needed to read. If sql is needed use **BiqQuery**. If no sql use **Cloud BigTable**



## Data Ingestion and Process
1. Pub Sub
2. Data Flow
3. Dataproc
4. Cloud Data Fusion

## Data Storage
1. Cloud Storage
2. CloudSQL
3. Cloud Big Table
4. Cloud Spanner
5. Firestore

## Analytics
1. BigQuery
2. Data Studio
3. Looker

# ML
1. Vertex AI:
    1. AutoML
    2. Vertex AI Workbench
    3. Tensorflow

AI Solutions
1. Document AI
2. Contact Center AI
3. Retail Product Discovery
4. Healthcare Data Engine


## Inbalanced Data
1. **Downsampling**: Training on a low subset of the majority class
2.**Upweighting**: Adding an example weight to the downsampled class equal to the factor by which you downsampled

 
 ## Kubeflow
 1. Describe Kubeflow pipeline ?
     1. Create the ops - (kubeflow tasks). These ops are docker containers, that are executed when the tasks are run
     2. Compose the ops - specify the order of these tasks. output of one op is inputed to other op
 2. How to instantiate an op ?
     - mlengine_train_op()
     - evaluate_model_op()
 3. What is func_to_container_op ?
     - It is used to convert a simple python function to a container op


 
 
 ## Reinforcement Learning
 - The purpose is to find the suitable action model that would maximize the total cumulative reward of the agent.
 
 
 ## Recommendations AI
 - Avaiable Recommendation types:
     - Others you may like: Product detailde qoyursan ki bunlari da beyene bilersen.
     - **Frequently bought together**: Add to card edib artiq productu. Orda hemin product benzer produktlari gosterib, frequently bought together deyirsen.
     - **Recommended for you**: Home pagede gosterilir ki bunlara baxa bilersen.
     - Recently viewed

     
    