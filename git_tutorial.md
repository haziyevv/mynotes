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

7. Will show the description about the command ?

   ```bash
   git help "command"
   ex: 
   	git help reset
   ```

8. To remove individual files by name from the staging area:

   ```bash
   git reset filename
   ```

9. To remove all the staged files from staging area:

   ```bash
   git reset
   ```

10. To see the remote repository:

    ```bash
    git remote -v
    ```

11. How to stash and then get back to your latest changes:

    ```bash
    git stash # stashes your current changes
    git stash list # show all the stashes hostory
    git stash pop # restores your file to the latest stash and removes that stash
    ```

12. How to remove a stash

    ```bash
    git stash drop stash@1
    ```

12. How to remove a local branch ?

    ```bash
    git branch -d <branch_name>
    ```

13. If you started working on a new branch and there is a change in the develop branch meanwhile?

    ```bash
    # merge develop to your branch
    git checkout my_branch
    git merge develop
    ```

    

