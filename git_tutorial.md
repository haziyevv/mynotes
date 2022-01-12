1. What is **git fetch** ?

   Like **git pull** it downloads data from the remote to local repository but does not merge them to the local repository unlike **git pull**. Usefull to check for changes, before doing a pull.

2. To create a branch from another branch:

   ```bash
   git checkout -b testbranch mainbranch
   ```

3. ```bash
   git fetch origin
   git reset --hard origin/master
   ```

   This will get the latest history from the server and point you  local branch at it

4. To show the commit history

   ```bash
   git log
   ```

5.  to delete a local branch

   ```bash
   git branch -d mybranch
   ```

6. to remove the last commit

   ```bash
   git reset --soft HEAD~1
   ```

3. 