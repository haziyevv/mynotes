

Example:

There is a restaurant that serves only 3 foods: **hamburger**, **pizza** and **hot-dog**. 

If you know what they have served today, you can predict what they will serve tomorrow.

|      | ha   | pi   | ho   |
| ---- | ---- | ---- | ---- |
| ha   | 0.2  | 0.6  | 0.2  |
| pi   | 0.3  | 0    | 0.7  |
| ho   | 0.5  | 0    | 0.5  |



Mathematically speaking **markovian property** can be shown like this:
$$
P(x_{n+1}|x_{1}, x_{2}, ..., x_{n}) = P(x_{n+1}|x_{n})
$$
If we noted the served foods for infinite number of days then we will come to an equilibrium state, which is called **stationary distribution** which can be simulated.



_______



**TO DO** random walku appy et

______



## n-step transition matrix

2. What is the probability of the restaurant to cook hot dog after two days if they cooked hamburger today ?

   this could be calculated by finding the dot product of the transition matrix to himself. If we want to calculate fir third day, we have to find the dot product again.

   If **A** is the transition matrix A . A . A will show the probabilities to start and end in each food in third day.

   A . A . A . A will show in the fourth day etc.

​		

​		So in mathematical terms we can show the probability of riching to state **j** from state **i** in n stages as follows:
$$
P_{ij}(n) = A_{ij}^n
$$
If calculate this for infinitely many steps then the found matrix will be:

|      | ha    | pi    | ho    |
| ---- | ----- | ----- | ----- |
| ha   | 0.352 | 0.211 | 0.436 |
| Pi   | 0.352 | 0.211 | 0.436 |
| ho   | 0.352 | 0.211 | 0.436 |

We can see that in which state we start, we will end up in the jth state with the same probability in the long run. Of course the relationship between the items should be **irreducible**.



