1. In order to draw a scatter plot with a regression line fitted to it:

   ```python
   sns.regplot(data=df, x='age', y='weight')
   ```

2. In order to plot a histogram of a column of a data frame:

   ```python
   import seaborn as sns
   
   # given male and female students at school. create a histogram for the males.
   # binwidth = 1 will make each bin's length 1 
   sns.histplot(data=school_df, x='male', binwidth=1)
   ```

3. Create a boxplot using seaborn:

   ```python
   # Create a boxplot of 2021 unemployment rates (on the x-axis), broken down by continent (on the y-axis).
   sns.boxplot(data=df, x='2021', y='continent')
   ```

   ![Screenshot 2024-11-21 at 23.29.23](https://p.ipic.vip/5jeb29.png)

4. To show the correlation between the columns in a dataframe:

   ```python
   sns.pairplot(data=df) # shows all the correlations between the columns
   
   sns.pairplot(data=df, vars=['income_mane', 'income_woman', 'marriage_duration'])
   ```

   ![Screenshot 2024-11-25 at 18.19.52](https://p.ipic.vip/k105ft.png)

5. If you want to plot a graph for how many times a value is passing in a data, use `sns.countplot`:

   ```python
   sns.countplot(y=region) # with region being a list
   
   sns.countplot(y='region', data=df) # with region being a column in a dataframe
   ```

   ![Screenshot 2024-11-27 at 23.31.55](/Users/farid/Desktop/Screenshot 2024-11-27 at 23.31.55.png)

6. 