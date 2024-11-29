1. What are the common methods to type at first ?

```python
pd.set_option("display.max_columns", 80) --> max number of columns 
                                                    to display

pd.set_option("display.max_rows", 85) --> max number of rows to display

df = pd.read_csv()
df.head()
df.shape()
df.info()  --> info about columns data type, 
               number of nulls and total number of rows.
df.describe() --> shows statistical infos about numberic columns
```

2. How to convert a column's data type to int in pandas:

   ```python
   df['year'] = df['year'].astype('int')
   ```

3. How to read a spreadsheet file:

   ```python
   file_name = 'file.xlsx'
   
   xls = pd.ExcelFile(file)
   print(xls.sheet_name) # will show all the sheets in the excel file
   
   # load a sheet named 2003
   df = xls.parse('2003')
   ```

4. Show all string columns in the data frame:

   ```python
   non_numeric = df.select_dtypes("object") # will return df with only string columns
   
   
   df_item_risk.select_dtypes(include=['object']).columns
   ```

5. Importing date time:

   ```python
   df = pd.read_csv('file.csv', parse_dates='date-column')
   ```

6. How to convert data to date time:

   ```python
   df['date-col'] = pd.to_datetime(df['date-col'])
   ```

7. How to extract `day`, `month` or `year` from date time:

   ```python
   df['day'] = df['date-col'].dt.day
   ```

8. Given `Salary_USD` in salaries dataframe, which shows the salary of each employee. We need to create a column named `salary_level` which groups the employees accroding to their salaries. There are two ways to do this, either using `np.select` or `pd.cut`

   ```python
   salary_labels = ["entry", "mid", "senior", "exec"]
   salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]
   
   conditions = [((salaries['Salary_USD'] > 0) & (salaries['Salary_USD'] <= twenty_fifth)), ((salaries['Salary_USD'] > twenty_fifth) & (salaries['Salary_USD'] <= salaries_median)), ((salaries['Salary_USD'] > salaries_median) & (salaries['Salary_USD'] <= seventy_fifth)), (salaries['Salary_USD'] > seventy_fifth) & (salaries['Salary_USD'] < salaries["Salary_USD"].max())]
   
   # using np select
   salaries['salary_level'] = np.select(conditions, salary_labels, default='Other')
   
   # using pd.cut
   salaries['salary_level'] = pd.cut(salaries['Salary_USD'], bins=salary_ranges, labels=salary_labels) 
   ```

9. loc and iloc explained:

   ```markdown
   **loc** and **iloc** both selects the row. 
   **iloc** selects by the place of the index, but **loc** by the label of the index. 
   df.loc[3] --> will give the raw whose index is 3. But if the index is not a number then **df.loc[3]** will not work, instead we should give the name of the index of the wanted row.
   ```

10. How to sort a data frame:

   ```python
   # to sort for index
   df.sort_index()
   
   # to sort by columns
   df.sort_values(by=["name", "surname"]) # sorts for name and surname
   
   # to sort in an order
   df.sort_values(by=["name", "surname"], ascending=[False, True]) # name descending and surname ascending
   ```

11. Aggregate function:

   ```python
   # a custom inter quartile range function
   def iqr(column):
         return column.quantile(0.75) - column.quantile(0.25)
   df['sales'].agg(iqr)
   ```

   ```python
   # find the iqr of sales and unemployment columns
   df[['sales', 'unemployment']].agg(iqr)
   
   # find the iqr and median of sales and unemployment columns
   import numpy as np
   df[['sales', 'unemployment']].agg([iqr, np.median])
   ```

11. How to drop the duplicates:

    ```python
    # from one column
    df.drop_duplicates('name') # will remove duplicates in name column
    
    # from more than one column
    df.drop_duplicates(['name', 'surname']) # will remove duplicates for the combination of name, surname
    ```

12. Value Counts:

    ```python
    # Count the number of each unique item passing in a column
    df['name'].value_counts() # will count all the different names. how many times each passing
    
    # sort them
    df['name'].value_counts(sort=True)
    
    # sort and also normalize to [0,1]
    df['name'].value_counts([sort=True, normalize=True])
    ```

13. Group by:

    ```python
    # to group df for one column
    groups = df.groupby("Country")
    
    # to group for a column and aggregate for one column
    df.groupby('Country')['Salary'].mean()
    
    # to group for a column and aggregate for another column for more than one feature
    df.groupby('Country')['Salary'].agg(["mean", "min", "median"])
    
    books.groupby("genre").agg(
      mean_rating=("rating", "mean"),
      std_rating=("rating", "std"),
      mean_year=("year", "median")
    )
    ```

    ![Screenshot 2024-11-22 at 10.13.28](https://p.ipic.vip/z8a25v.png)

    Given this dataframe:
    ![Screenshot 2024-11-22 at 10.15.54](https://p.ipic.vip/nnj54u.png)

    - Print the mean and standard deviation of the unemployment rates for each year (in that order).

    ```python
    df.agg(['mean', 'std'])
    ```

    ![Screenshot 2024-11-22 at 10.17.18](https://p.ipic.vip/t4um7o.png)

14. What is pivot table and how it is used ?

   --> It is like grouping by two features and aggregating by a third features. But it is better than group by in terms of visualization. Here we can show one feature in column and other in row as a table.

   ```python
   pivott = df.pivot_table(values="rating", index="title", 
   						column="gender", aggfunc="mean")
   						
   # index is the row and column is the column feature
   # values is like the aggregated values in groupby
   ```

11. index and working with it:

   ```python
   # how to set an index
   df.set_index('full_name') # now full name will be the index
   
   # to reset an index to keep only the number indices
   df.reset_index() # this will put the index value as a column and create a numeric index
   
   # to reset an index and removing its content
   df.reset_index(drop=True) # this will completely remove the current index and create a numeric index
   
   # to set the index column while loading the csv
   pd.read_csv("kelem.csv", index_col="email") # --> if header has a name
   pd.read_csv("kelem.csv", index_col=0) # --> select the first 
   ```

11. Slicing:

   ```python
   # How to select the rows between 2 and 6 and columns between 3 and 7 in pandas ?
   df.iloc[2:6,3:7]
   
   # index is country, city
   df.set_index(['country', 'city'])
   df.loc['China':'Russia'] # items from China to Russia
   
   df.loc[('China', 'Pekin'): ('Russia', 'Moskow')] 
   ```

11. Missing values:

    ```python
    # to detect all NAN values in all the columns of the dataframe
    df.isna()
    
    # to check if there is any NAN value in all of the columns. will return True or False for all the columns
    df.isna().any()
    
    # to return all the NAN values in all of the columns
    df.isna().sum()
    
    # to remove all the rows where NAN exist
    df.dropna()
    
    # to fill NAN values with a value
    df.fillna(0)
    
    
    ```

12. Joining data in Pandas:

    ```python
    # inner join two dataframes df_student and df_teacher 
    df_joined = df_student.merge(df_teacher, on='teacher_id')
    
    # add suffixes in order to distinguish between the columns of the joined tables
    df_joined = df_student.merge(df_teacher, on='teacher_id', suffixes=['_student', '_teacher'])
    
    # to do left join
    df_joined = df_student.merge(df_teacher, on='teacher_id', suffixes=['_student', '_teacher'], how='left')
    
    # when joining primary key and foreign key can have different names. Then do
    df_joined = df_student.merge(df_teacher, left_on='teacher_id', right_on='id', suffixes=['_student', '_teacher'])
    ```

    

13. How to filter rows whose nationality is in ["azerbaijan", "turkey", "italy"] ? 

    ```python
    df[df["nationality"].isin(["azerbijain", "tuekry", "italy"])]
    ```

14. How to filter rows whose nationality contains string "stan" ?

    ```python
    df[df["nationality"].str.contains("stan", na=False)]
    ```

15. Extract n samples from a dataframe with and without replacement:

    ```python
    df.sample(4, replace=False)
    df.sample(4, replace=True)
    ```

    

16. How to change all column names to be underscore seperated instead of empty space seperated ?

    ```python
    df.columns.str.replace(" ", "_")
    ```

17. How to change some column names ?

    ```python
    df.rename(columns={"first_name":"first", "second_name":"second"})
    ```

18. How to turn all **Yes** value to **True** and **No** values to **False** in a column ?

    ```python
    df["col"].map({"Yes":True, "No":False})
    ```

19. How to apply a function to all the items in a dataframe ?

    ```python
    df.apply_map(func)
    ```

20. How to drop columns **name** and **email** ?

    ```python
    df.drop(columns=["name", "email"])
    ```

21. Given a colmn name **fullname**, how to divide it to 2 columns **name** and **surname** ?

    ```python
    df[["name", "surname"]] = df["fullname"].str.split(" ", expand=True)
    ```

22. How to append a dataframe to another ?

    ```python
    df.append(df2, ignore_index=True)
    ```

23. Select top **n** largest rows in **age** column ?

    ```python
    df["age"].nlargest(10)
    ```

24. Select **top n** largest rows in the datafraame according to the **age** column ?

    ```python
    df.nlargest(10, "Age")
    ```

25. How to convert series to dataframe ?

    ```python
    series.to_frame().reset_index()
    ```

26. How to combine many series to form a dataframe ?

    ```python
    ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
    ser2 = pd.Series(np.arange(26))
    
    df = pd.concat([ser1, ser2], axis=1)
    ```

27. How to plot a scatter plot in pandas ?

    ```python
    df.plot(kind="scatter",
            x="Weight",
            y="Height",
            title="Weight and height in adults")
    
    ```

28. How to merge two dataframes ?

    ```python
    data = pd.merge(ratings, users)
    ```

    Here users has a 1-m relationship to ratings.

29. How to drop `na` rows only for some columns ? 

    ```python
    df.dropna(subset=["name", "toy"])
    ```
