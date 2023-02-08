

| Train data    | Test_data         | fscore   | precision | recall   | Accuracy  |
| ------------- | ----------------- | -------- | --------- | -------- | --------- |
| Not augmented | Not augmented     | 47.5     | 51.8      | 46.97    | 76.4      |
| Not augmented | Augmented         | 45.5     | 51.3      | 44.5     | 73.8      |
| **Augmented** | **Not augmented** | **50.5** | **55.8**  | **49.8** | **77.99** |
| Augmented     | Augmented         | 49.9     | 55.4      | 48.9     | 77.3      |



## New MLP with energy
Model type | Train data    | Test_data         | fscore   | precision | recall   | Accuracy  |
| ------------- | ----------------- | -------- | --------- | -------- | --------- | -------- |
| MLP laser encoder| augmented | augmented     | 52.4     | 57.14     | 51.9    | 77.8      |
| MLP laser encoder| augmented | not-augmented     | 53.5     | 58.57     | 52.7    | 77.14      |
| MLP laser encoder| not-augmented | not-augmented     | 46.55     | 51.65  | 45.87    | 74.03      |
| MLP laser encoder| not-augmented | augmented     | 53.36     | 57.46  | 52.25    | 77.44      |




## New MLP with only anaphoric test data
Model type | Train data    | Test_data         | fscore   | precision | recall   | Accuracy  |
| ------------- | ----------------- | -------- | --------- | -------- | --------- | -------- |
| MLP laser encoder| augmented | only anaphoric     | 52.24     | 56.51     | 52.8    | 77.81      |
| MLP laser encoder| not-augmented | only anaphoric     | 46.65    | 54.49     | 45.2    | 71.3     |
| MLP laser encoder| augmented | not-augmented     | 53.5     | 58.57     | 52.7    | 77.14      |
| MLP laser encoder| not-augmented | not-augmented     | 46.55     | 51.65  | 45.87    | 74.03      |
| MLP distilbert encoder| augmented | only anaphoric     | 52.16    | 56.98     | 52.88    | 74.0     |
 MLP distilbert encoder| not-augmented | only anaphoric     | 46.68    | 53.67    | 46.92   | 68.7    |    
 MLP distilbert encoder| augmented | not-augmented     | 53.82    | 58.15    | 53.1   | 74.27    |    
 MLP distilbert encoder| not-augmented | not-augmented     | 53.76    | 58.31    | 53.2   | 74.62    |