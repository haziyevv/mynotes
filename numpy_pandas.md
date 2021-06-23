# PANDAS

1. What is loc and iloc differrence ? 
   
   - loc is preferred for selecting by labels and also it permits to boolean indexing:
   
   - iloc is preferred when selecting by index. So in general if you want to index the columns by number use this.
   
   ```
   df.loc[df["Age"] > 15] --> will give all the rows where column age > 15
   df.loc[df["Age"], "County"] --> will give all rows where column age >15 
                                   but will only return column Country  
   ```

```
df.iloc[:11, 1:5] --> will return rows until 11 and 
                        columns between 1 and 5
```

2. How to handle missing values ?

Sklearn has a library name **SimpleImputer** for this task.

```
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
```

3. How to encode the categorical data ?

```
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], 
                                      remainder="passthrough")
X = np.array(ct.fit_transform(X))
```

4. How to encode the labels ?

```
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
```

5. How to do feature scaling ?

```
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
```

# Numpy

1. What is the use case of np.convolve ?
   
   - Typical like use case in computer vision:
   
   ```
   a1 = np.array([1,2,3,4])
   a2 = np.array([0.5, 1, -0.5])
   ```
   
   np.convolve(a1, a2, mode="valid")

2. Get the indices where value is greater than a threshold ?
   
   ```
   np.argwhere(arr > 0)
   ```

3. What is **np.select** and how do we use it ?

```

```

4. What is **np.where** and how to use it ?

```
np.where(condition, x, y) --> depending on the condition
                              return either x or y
```

5. How to convert date to datetime type ?

```
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
```

6. 
