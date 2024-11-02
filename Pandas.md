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

2. loc and iloc explained:

   ```markdown
   **loc** and **iloc** both selects the row. 
   **iloc** selects by the place of the index, but **loc** by the label of the index. 
   df.loc[3] --> will give the raw whose index is 3. But if the index is not a number then **df.loc[3]** will not work, instead we should give the name of the index of the wanted row.
   ```

3. How to select the rows between 2 and 6 and columns between 3 and 7 in pandas ?

   ```python
   df.iloc[2:6,3:7]
   ```

4. How to change the index ?

   ```python
   df.set_index("kelem")
   ```

6. How to get back to the number index again ?

   ```python
   df.reset_index()
   ```

7. How to set the index column while loading csv in pandas ?

   ```python
   pd.read_csv("kelem.csv", index_col="email") # --> if header has a name
   pd.read_csv("kelem.csv", index_col=0) # --> select the first 
   # column as index
   ```

8. How to sort df according to the index ?

   ```python
   df.sort_index()
   ```

9. How to filter rows whose nationality is in ["azerbaijan", "turkey", "italy"] ? 

   ```python
   df[df["nationality"].isin(["azerbijain", "tuekry", "italy"])]
   ```

10. How to filter rows whose nationality contains string "stan" ?

    ```python
    df[df["nationality"].str.contains("stan", na=False)]
    ```

11. How to change all column names to be underscore seperated instead of empty space seperated ?

    ```python
    df.columns.str.replace(" ", "_")
    ```

12. How to change some column names ?

    ```python
    df.rename(columns={"first_name":"first", "second_name":"second"})
    ```

13. How to turn all **Yes** value to **True** and **No** values to **False** in a column ?

    ```python
    df["col"].map({"Yes":True, "No":False})
    ```

14. How to apply a function to all the items in a dataframe ?

    ```python
    df.apply_map(func)
    ```

15. How to drop columns **name** and **email** ?

    ```python
    df.drop(columns=["name", "email"])
    ```

16. Given a colmn name **fullname**, how to divide it to 2 columns **name** and **surname** ?

    ```python
    df[["name", "surname"]] = df["fullname"].str.split(" ", expand=True)
    ```

17. How to append a dataframe to another ?

    ```python
    df.append(df2, ignore_index=True)
    ```

18. How to sort dataframe by **name** and **surname** ?

    ```python
    df.sort_values(by=["name", "surname"])
    ```

19. How to sort dataframe by **name** and **surname** by **descending** order for name and **ascending** order for **surname** ? 

    ```python
    df.sort_values(by=["name", "surname"], ascending=[False, True])
    ```

20. Select top **n** largest rows in **age** column ?

    ```python
    df["age"].nlargest(10)
    ```

21. Select **top n** largest rows in the datafraame according to the **age** column ?

    ```python
    df.nlargest(10, "Age")
    ```

22. How to scale the output of **.value\_counts** to 0-1 ?

    ```python
    df["country"].value_counts(normalize=True)
    ```

23. **GroupBy**

```
groups = df.groupby(["Country"]) --> to group df for countries
groups.get_group("Azerbaijan") --> gets the Azerbaijan group


groups["Salary"].median() --> group with country and then aggreagate 
                                by median for the salary


groups["Salary"].agg(["mean", "median"])  --> group with country and then
                                            aggregate by median and mean
                                            for the salary
```

24. How to convert series to dataframe ?

    ```python
    series.to_frame().reset_index()
    ```

25. How to combine many series to form a dataframe ?

    ```python
    ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
    ser2 = pd.Series(np.arange(26))
    
    df = pd.concat([ser1, ser2], axis=1)
    ```

26.  How to plot a scatter plot in pandas ?

    ```python
    df.plot(kind="scatter",
            x="Weight",
            y="Height",
            title="Weight and height in adults")
    
    ```

27. Build a basic one layer linear regression model in keras ?

    ```bash
    model = Sequential()
    model.add(Dense(1, input_shape=(1,)))
    model.compile(Adam(learning_rate=0.1), "mean_squared_error")
    model.fit(x,y,epochs=10)
    ```

28. How to merge two dataframes ?

    ```python
    data = pd.merge(ratings, users)
    ```

    Here users has a 1-m relationship to ratings.

29. What is pivot table and how it is used ?

    --> It is like grouping by two features and aggregating by a third features. But it is better than group by in terms of visualization. Here we can show one feature in column and other in row as a table.

    ```python
    pivott = df.pivot_table("rating", index="title", 
    						column="gender", aggfunc="mean")
    						
    --> rating is the values feature
    --> index is the row and column is the column feature
    ```

30. How to drop `na` rows only for some columns ? 

    ```python
    df.dropna(subset=["name", "toy"])
    ```
