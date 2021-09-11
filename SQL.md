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

3. 