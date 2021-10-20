1) What are generative and discriminative models ?

--> Discrimative models predicts the output directly **P(y|x)**, but generative models calculate other probabilities to find the output --> **P(y)P(x|y)**



2. What is residual ?

   --> Residual is the difference between **true value** and the **predicted value** :  **y - y_hat**

3. How does **Mean Squared Error** calculated ?
   $$
   \sum_{i=1}^m \frac{(y_i - y_{hat_i})^2}{m}
   $$

4. What is R-square score and how is it calculated ?

   * It is used for deciding how much does the relationship between two variables explains  the result.  Like you have one feature height and you predict the weight. If R  square is high, then you can say that knowing height you can predict the weight.

   * It is calculated by comparing the **sum of squares of residuals** for predicted model and a baseline model which uses mean score. 
     $$
     \frac{SS(mean) - SS(model)}{SS(mean)}
     $$
     

5. What is leave one label out and leave p labels out ?

   --> these are validation methods. For example dataset contains samples for different users. Leave some user data and train with others, then predicted the left users to how your model is generalasing ?

   

7. What is the easier way to calculate f1, precision and recall scores in scikit learn ? 

   ```python
   from sklearn.metrics import classification_report
   
   report = classification_report(y_hat, y, output_dict=True)
   result_df = pd.DataFrame(report)
   ```

8. How to encode categorical data in pandas ?

   ```python
   dummies = pd.get_dummies(df["salary"], prefix="salary")
   df = pd.concat([df, dummies], axis=1)
   ```
   
8. Apply feature scaling in all possible ways :

   * ```python
     from sklearn.preprocessing import StandardScaler
     scaler = StandardScaler()
     df["wages"] = scaler.fit_transform(df[["wages"]])
     ```

9. What is **bias/variance** tradeof ?

   --> Bias happens when the machine learning model is not able to capture the true relationship effectively.  High variance happens when ther is overfit.

10. Talk about **Supoort Vector Machines**:

    - Start with low dimensional data
    - Move into higher dimension
    - Find threshold that seperates the data into groups

11. Talk about **Decision Tree** : 

    - For each feature calculate gini impurity
    - Select the one with the smallest gini impurity
    - Then select others in terms of the one selected before. Select the smallest one. If its gini index is bigger than the parent node stop dividing.
    - Gini score: example : Patient has chest pain - yes, no.  Output is he has heart disease or not. 144 person has chest pain, of which 105 has heart disease and 39 has not. 159 person does not have chest pain, of which 34 has heart disease and 125 has not.
    - 

$$
\frac{144}{144+159} * (1-(\frac{105}{144})^2 - (\frac{39}{144})^2) + \frac{159}{144+159} *(1-(\frac{34}{159})^2 -(\frac{125}{159}^2))
$$





12. Talk about **Random Forest**

* Create 100s of different **bootstrapped** Datasets. Create **bootstrapped** datasets, by selecting the data randomly, same as the amount of data, but you can select the same item in each random selection. 
* Bootstrapped datasetlerin her biri üçün decision tree apply et. Decision tree apply ederken her stepde random feature subsamplı yaradırıq. Subsampe qeder featura baxaraq decision seçirik. Meselen: 4 feature var. Birinci stepde random 2-sin nezere al, ikinci stepde 3 deneden yalnız 2sin nezere al.
* Sonda 100 lerle decision tree yaratmış oluruq. Prediction etmek isteyende, her decision tree ile ayrı ayrı qerar verir ve en çox seçilen qerarı seçirik. 

  What is **Bagging** ?

  Bootstrapping data plus applying aggregation to make a decision is called **bagging**.

  What is **out of bag** data ?

  These are the data that are not selected in bootstrapped datasets.

  We can measue how accurate the random forest is by calculating the accuracy of the prediction of the **out of bag** data.

13. Talk about AdaBoost :

- In contrast to random forest, here created decision trees has one leaf nodes

- In contrast to random forest, some trees will have more saying than others. Because they will be weighted, in terms of the amount of misclassified outputs.

- In random forest, each tree is created independently. But in adaboost, one tree will affect the next tree. Because, items that are missclassified will be boosted, and so they will be selected more in the next bootstrap. 

14. Code and explain Expectation Maximization:

```
def calc_p(ta, tb, hc):
    tc = 10 - hc
    pa = math.pow(ta, hc) * math.pow((1-ta), tc)
    pb = math.pow(tb, hc) * math.pow((1-tb), tc)
    psa = pa/(pa+pb)
    psb = pb/(pa+pb)
    return psa, psb


def maximization(results):
    heads = sum([x[0] for x in results])
    tails = sum([x[1] for x in results])

    e_after = heads / (heads + tails)
    return e_after


experiments = [5,9,8,4,7]
ea, eb = 0.2, 0.1
iterations = 100


def expectations(experiments):
    coina_res, coinb_res = [], []
    for exp in experiments:
        psa, psb = calc_p(ea, eb, exp)
        coina_res.append((exp*psa, (10-exp)*psa))
        coinb_res.append((exp*psb, (10-exp)*psb))
    return coina_res, coinb_res

for i in range(iterations):
    expa, expb = expectations(experiments)
    ea, eb = maximization(expa), maximization(expb)
    print(i, ea, eb)
```



15. Explain L2 regularization ?

- As our main task is to minimize the cost function, adding sum of the squares of all the weights to the cost function will decrease the weights

$$
L = min(\sum(y_{hati} - y_i)^2 + \lambda*\sum(w_j)^2)
$$

- When we calculate gradient for **w1** it will take **lambda** into account. This will affect the **w1** by making it smaller than it would be without regularization. Lets show:

```
y = wx + b

--> normal cost function
L = (y_hat - y)^2
dL/dw = 2*(y_hat - y)*x
w = w - alpha*dl/dw
w = w - alpha*2*(y_hat-y)*x

--> regularized cost function
L = (y_hat - y)^2 + lambda*w^2
dL/dW = 2*(y_hat-y)*x + 2*lambda*w
w = w - alpha*2*(y_hat-y)*x - 2*alpha*lambda*w
w = w(1-2*alpha*lambda) - alpha*2*(y_hat-y)*x
```

It can be seen that w is multiplied by **(1-2\*alpha\*lambda)** . This makes weight to shrink. Increasing **lambda** makes weight even smaller.





16. What are **precision** and **recall** ?

<img title="" src="file:///home/haziyevv/Documents/mynotes/figures/Precisionrecall.svg.png" alt="" width="418">

- To clearly explain this, an example from a book is used. We have two dogs. One barks to everything as if it is a burglar and second one hardly ever barks but whenever he barks it is definitely a burglar. First dog has high recall, and second one has high precision. But first one has very bad precision, because it has very high False Positive. 

- We can say that **recall** is calculated by dividing the correctly found positives to actual number of positives. 

- **Precision** is calculated by dividing the correctly classified positives to anything that is classified as positive.



17. What can be done to cope with inbalanced dataset ?

* Change performance metric to f1, precision, recall instead of accuracy

* Apply over sampling and under sampling

* Try decision tree which is better on inbalanced dataset



18. Explain Batch Normalisation:

In very deep neural networks, sometimes one output from an activation layer can be very high compared to the other. Although we make normalisation in input layer, we need to do it for each layer too. So, we apply batch normalisation by normalising the output of the activation function or the input to the activation function with the mean and variance of the given batch.

19. What is the **ROC-AUC** curve ? 

-> It is a performance measurement for the classification problems at various threshold levels.

-> **ROC** is a probability curve with x axis  **false positive rate**(fp/(fp+tn)) and y axis **true positive rate**(tp/(tp+fn))

-> **AUC** shows the degree of class separability. Higher the **AUC** better the model predicts cancer as cancer and non cancer as non cancer. 1 AUC is the best 0 is the worst. 0 means we say positive to negative and negative to positive. 

20. What is **feature crosses** ?

-> Creating new features by multiplying different features with each other.

-> This way we can add nonlinearity to our linear model.

example: Housing price prediction. lattitude*num_bedrooms.

21. What is **l1** regularization ?

    -> It is similar to L2 regularization, but here we add absolute value of weights instead of square to the loss function
    $$
    L = min(\sum(y_{hati} - y_i)^2 + \lambda*\sum abs(w_j)
    $$
    -> This is effective on decreasing the size of the model by making weights of irrelevant features exactly zero.

22. What is **candidate sampling** ?

    -> It is used in softmax. Instead of finding output for all the classes, find for the true class and some of the random negative classes.

23. 



