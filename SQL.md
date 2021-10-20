1. What happens when you select **count(name)** from persons table ?

   --> It will return the number of rows where name is not null

2.  What is **CASE** and how to use it ?

   ```sql
   SELECT player_name,
          height,
          CASE WHEN height > 74 THEN 'over 74'
               WHEN height > 72 AND height <= 74 THEN '73-74'
               WHEN height > 70 AND height <= 72 THEN '71-72'
               ELSE 'under 70' END AS height_group
     FROM benn.college_football_players
   ```

3. How to concatenate two columns in bigquery and add word between. For example column name is "Marry" and column gender is "F". New column should be "Marry is a girl"

```sql
SELECT CONCAT(name, ' is ', case when gender = 'F' then 'girl' else 'boy' end) as intro FROM `baby_names`
```

4. 