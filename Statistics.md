1. What is **Null hypothesis** ?

   -> The hypothesis that there is no difference between two things.

2. What is **alternative hypothesis** ?

   -> Opposite of null hypothesis.

3. What is **p value** ?

   -> Number between 0 and 1 to quantify how confident we should be that **drug-a** is different than **drug-b**. 

   -> The closer a **p-value** to 0, the more confidence we have that, **drug-a** and **drug-b** are different.

   -> A commonly used threshold for **p-value** is 0.05. 

4. What is **standard deviation** ?

   -> The standard deviation defines the width of the normal curve.

5. What are continuous, ordinal and categorical values ?

   - **Continuous**, is where there is a strict ordering and difference between values has a strict meaning. ex: 1,2,3,4,5,6
   - **Ordinal**, is where there is ordering but difference between values has no meaning.  ex: small, medium, large
   - **Categorical**, is where there is no ordering and difference between values does not make sense. ex: sport, economy, trade.

6. What are the **population parameters** ?

   -> They are the parameters in the whole population. For example: Counting apple in each and every grocery store. All the grocery stores is the population.

7. What is **pareto chart** ?

   -> Represents categories in descending order and adds a line showing the cumulative sum.

8. What is **covariance** ?

   -> Covariance tells us if 2 values are moving in the same direction ?
   $$
   COV = \frac{\sum (x_i - x_{hat})*(y_i - y_{hat})}{n-1}
   $$

   -> There is a positive trend, meaning these values move together: if **cov > 0**

   -> There is a negative trend: if **cov < 0**

   -> They are independent: if **cov = 0**

9. What is correlation ?

   -> It adjusts covariance to see the relationship
   $$
   r = \frac{cov(x,y)}{std(x)*std(y)}
   $$
   -> r will be between -1 and +1

   -> r closer to 1 means there is a correlation

   -> closer to -1 means negative correlation

   -> closer to 0 means they are independent.

10. What is **Z-score** ?

    -> It shows how usual or unusual data point is

    -> It shows how many standard deviations a data point is away from the mean
    $$
    Z = \frac{x-mean}{std}
    $$

11. What is central limit theorem ?

    - Whatever the population distribution is (binomıal, unıform, exponential etc.,) distribution of the means of several (1000 for example) samples from this distribution is gonna be normal
    - 

12. What is sampling distribution ?

    - a statistic computed from a lot of samples drawn from the same population

13. What is standard error ?

    - it is the standard deviation of the sampling distribution divided by square root of sample size. 

    - $$
      Standard\ error = \frac{s}{\sqrt{n}}
      $$

    - how about standard deviation:

    - $$
      s = \frac{\sum{(x_i - \hat{x})}}{n-1}
      $$

      here n is the number of samples

14. What is the bootstrap ?

    - Create additional samples by replacement from the given sample
    - Calculate the statistic using that samples

15. What is the difference between a random variable and a variable ?

    - a variable can be assigned a number but a random variable can take many numbers with different probabilities

16. 
