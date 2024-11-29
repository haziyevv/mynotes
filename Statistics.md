1. #### What are outliers:

   ```
   data < Q_1 - 1.5*IQR
   or
   data > Q3 + 1.5*IQR
   ```

2. What is `Ordinary Least Squares` ?

   - It is just based on minimizing the sum of the squared differences between the observations and the predictions.
   
7. Continuous Uniform Distribution:

   - To generate random numbers according to uniform distribution:

     ```python
     from scipy.stats import uniform
     uniform.rvs(0, 5, size=10)
     ```

   - To know the probability of waiting less than 7 minutes. If minimium wait time is 0 and max is 30

     ```python
     from scipy.stats import uniform
     
     prob = uniform.cdf(7, 0, 30)
     ```

8. Binomial Distribution:

   > Probability distribution of the number of successes in a sequence of independent trials.

   > e.g. Number of heads in a sequence of coin flips

   ```python
   # calculate the probability of 7 heads in 10 flips of fair coin
   binom.pmf(7, 10, 0.5)
   
   # calculate the probability of less than or equal to 7 heads in 10 flips of fair coin
   binom.cdf(7, 10, 0.5)
   ```

   example: GS usually plays 3 games per week and overall, they win 90% of this games.

   ```python
   # simulate one game
   binom.rvs(1, 0.9, size=1)
   
   # simulate a week
   binom.rvs(3, 0.9, size=1)
   
   # simulate a year, where there are 52 weeks
   binom.rvs(3, 0.9, size=52)
   ```

9. Normal Distribution 

   ```python
   # Given a women height data which is normal distributed
   # mean is 161 and std is 7
   
   # find the percent of women shorter than 154 cm.
   norm.cdf(154, 161, 7)
   
   # what height are 90% of women shorter than?
   z_score = norm.ppf(0.9) # this will return the z score
   height = 161 + z_score * 7
   # or just 
   height = norm.ppf(0.9, 161, 7)
   
   # generate 10 random variables
   norm.rvs(161, 7, size=10)
   ```

10. Poisson distribution:

   \# of events happening in a given time interval. Ex: Number of dogs adopted in a year. Number of hours Farid studies in a week. Number of products sold each week.

   ```python
   # Probability that Farid studied 5 hours in a day given his average is 8 hours
   poisson.pmf(5, 8)
   ```

11. Exponential distribution:

    > Amount of time until the next customer makes a purchase
    >
    > Amount of time until someone pays their loan

    ```python
    # on average operator responds to 1 request every 2.5 minutes
    # what is the probability that takes him 3 minutes to respond to a request
    from scipy.stats import expon
    
    expon.cdf(3, scale=2.5)
    ```

    

12. What is **Null hypothesis** ?

   -> The hypothesis that there is no difference between two things.

11. What is **alternative hypothesis** ?

   -> Opposite of null hypothesis.

11. What is **p value** ?

    -> Number between 0 and 1 to quantify how confident we should be that **drug-a** is different than **drug-b**. 

    -> The closer a **p-value** to 0, the more confidence we have that, **drug-a** and **drug-b** are different.

    -> A commonly used threshold for **p-value** is 0.05. 

12. What is **standard deviation** ?

   -> The standard deviation defines the width of the normal curve.

11. What are continuous, ordinal and categorical values ?

   - **Continuous**, is where there is a strict ordering and difference between values has a strict meaning. ex: 1,2,3,4,5,6
   - **Ordinal**, is where there is ordering but difference between values has no meaning.  ex: small, medium, large
   - **Categorical**, is where there is no ordering and difference between values does not make sense. ex: sport, economy, trade.

11. What are the **population parameters** ?

    -> They are the parameters in the whole population. For example: Counting apple in each and every grocery store. All the grocery stores is the population.

12. What is **pareto chart** ?

    -> Represents categories in descending order and adds a line showing the cumulative sum.

13. What is **covariance** ?

   -> Covariance tells us if 2 values are moving in the same direction ?
$$
   COV = \frac{\sum (x_i - x_{hat})*(y_i - y_{hat})}{n-1}
$$

   -> There is a positive trend, meaning these values move together: if **cov > 0**

   -> There is a negative trend: if **cov < 0**

   -> They are independent: if **cov = 0**

11. What is correlation ?

    -> It adjusts covariance to see the relationship
    $$
    r = \frac{cov(x,y)}{std(x)*std(y)}
    $$
    -> r will be between -1 and +1

    -> r closer to 1 means there is a correlation

    -> closer to -1 means negative correlation

    -> closer to 0 means they are independent.

12. What is **Z-score** ?

    -> It shows how usual or unusual data point is

    -> It shows how many standard deviations a data point is away from the mean
    $$
    Z = \frac{x-mean}{std}
    $$

13. What is central limit theorem ?

    - Whatever the population distribution is (binomıal, unıform, exponential etc.,) distribution of the means of several (1000 for example) samples from this distribution is gonna be normal
    - 

14. What is sampling distribution ?

    - a statistic computed from a lot of samples drawn from the same population

15. What is standard error ?

    - it is the standard deviation of the sampling distribution divided by square root of sample size. 

    - $$
      Standard\ error = \frac{s}{\sqrt{n}}
      $$

    - how about standard deviation:

    - $$
      s = \frac{\sum{(x_i - \hat{x})}}{n-1}
      $$

      here n is the number of samples

16. What is the bootstrap ?

    - Create additional samples by replacement from the given sample
    - Calculate the statistic using that samples

17. What is the difference between a random variable and a variable ?

    - a variable can be assigned a number but a random variable can take many numbers with different probabilities

18. 
