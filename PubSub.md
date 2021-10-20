1. There are three terms in Pub/Sub that appear often: `topics`,  `publishing`  , `subscribing`. 

2. `Topic` is a shared string that allows applications to connect with one another through a common thread.

3. `Publishers` push a message to a Cloud Pub/Sub topic

4. `Subscribers` make a subscription to a topic where they will either pull messages from the subsciption or configure webhooks for push subscriptions.

5. How to create a topic ?

   ```bash
   gcloud pubsub topics create myTopic
   ```

6. How to create a subscription to a given topic ?

   ```bash
   gcloud pubsub subscriptions create --topic myTopics mysub
   ```

7. How to publish a message to a topic ?

   ```bash
   gcloud pubsub topics publish myTopic --message "Hello"
   ```

8. How to pull the published messages ?

   ```bash
   gcloud pubsub subscriptions pull mySubscription --auto-ack
   ```

9. 