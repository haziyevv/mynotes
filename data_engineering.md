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

- <img title="" src="kubernetes.png" alt="">

**Kubernetes** consists of a number of **node instances** and each node instance can be named as **Pod**. Each Pod is consisting of several **containers**.