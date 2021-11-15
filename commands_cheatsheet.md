# Vim Cheatsheet

**ctrl+r** --> redo action

**/def** --> def sözünü search edir , alternative to **?def**

**:%s/hi/hilo/g** --> to search word "hi" and replace it with "hilo". here g means, do this for all occurences.

**ctrl + n** --> default autocompletion on vim

# Linux Cheatsheet

1. What are the some common shell commands for getting information?

   - **whoami** --> shows the username 
   - **id** --> user id and group_id
   - **uname** --> operating system
   - **uname -a** --> returns all informations about operating system
   - **ps** --> running processes
   - **top** --> 
   - **df** --> mounted file systems
   - **man** --> reference manual
   - **date**

2.  What are the some common shell commands for working with files ?

    * cp
    * mv
    * rm
    * touch
    * chmod
    * wc
    * **grep** --> return lines in a file matching a given pattern 

3. How to search for files in a directory ?

   ```bash
   find /etc -name '*.txt'
   find -type f -name '*.txt' | wc -l
   ```

4. How to select and remove empty files in a directory ?

   ```bash
   find -type f -empty -delete
   ```
   
   

5. How to apply operations in for loop in terminal ?

   ```bash
   for f in *.pdf; do echo rm "$f"; done
   ```

   

6. How to use **tar** to archive folders ?

   | Option | Description                    |
   | ------ | ------------------------------ |
   | -c     | Create new archive file        |
   | -v     | Verbosely list files processed |
   | -f     | Archive file name              |

7. Tar a folder named **bin** to bin.tar:

   ```bash
   tar -cvf bin.tar /bin
   ```

8. List all the files inside the **bin.tar** archive:

   ```bash
   tar -tvf bin.tar
   ```

9. Untar the archive **bin.tar** :

   ```bash
   tar -xvf bin.tar
   ```

10. How to compress entire folder with **zip** ?

   ```bash
   zip -r bin.zip /bin
   ```

11. How to list all the files inside the **zip** archive ?

   ```bash
   unzip -l bin.zip
   ```

11. How to unzip all the files inside the **zip** archive ?

    ```bash
    unzip bin.zip
    ```

12. How to remove read permission from all users on **test.txt** ?

    ```bash
    chmod -r test.txt
    ```

13. How to add read permission to all users on **test.txt** ?

    ```bash
    chmod +r test.txt
    ```

14. How to remove the read permission for **others** category ?

    ```bash
    chmod o-r test.txt
    ```

15. How to find the number of lines, words and characters in a file name **test.txt** ?

    ```bash
    wc test.txt
    ```

16. How to display file contents line by line ?

    ```bash
    more test.txt
    ```

17. How to find only number of lines, or words or characters in a file named **test.txt** ?

    ```bash
    wc -l test.txt
    wc -w test.txt
    wc -c test.txt
    ```

18. How to get all the lines in file **test.txt** that contain word people ?

    ```bash
    grep people test.txt
    ```

19. How to get all the lines in file **test.txt** that do not contain word people ?

    ```bash
    grep -v people test.txt
    ```

20. How to get all the lines in the file **test.txt** that matches word **people** as whole word ?

    ```bash
    grep -w people test.txt
    ```

21. How to display the **ethernet adapter configuration** ?

    ```bash
    ifconfig eth0
    ```

22. How to view the permissions of a file ?

    ```bash
    ls -ld file
    ```

23. How to display files in a folder in ascending order of their access times ?

    ```bash
    ls -ltr /folder
    ```

24. Show the path of the command **python3**: 

    ```bash
    which python3
    ```

25. How to redirect error outputs to a file ?

    ```bash
    python3 sayhello.py 2> file.txt
    ```

    This will write the errors happened in executing the **sayhello.py** script to the file.txt instead of the standard output

26. How to assign another variable to a variable ?

    ```bash
    here=$(pwd)
    ```

27. Convert all the characters to capital letter :

    ```bash
    cat filename.txt | tr "[a-z]" "[A-Z]"
    ```

28. 

29. What are the commands for printing file and string contents ?

    * **more** --> prints file content page by page

30. What are the common networking commands ?

    * **hostname** --> 
    * **ifconfig** --> display or configure system network interfaces
    * **curl** --> display the contents of a file located in a url
    * 

31. How to extract and untar files inside .tar.gz to current directory .

```
tar xzf frodo.tar.gz
```

2. Where are the programs installed in ubuntu ?

```
/us/local
or
/opt
```

3.  Where all external storage are mounted ? 

```
/media
```

4. **/bin** --> contains all binary(program) files

5. How to search file named thisfile.txt in home folder ?

```
find /home -name thisfile.txt
```

6. How to open a pdf file from terminal ?

```
xdg-open filename 
```

7. How to play audios from terminal ?

```
play file.mp3
```

8. Count the number of lines that ends with 1 in candidates.csv file ? 

```
grep ",1$" candidates.csv | wc -l
```

9. How to create a symbolic link of a file named sepen.txt to the current folder ?

```
ln -s ../sepen.txt sepen
```



# **Awk**

1. ```bash
   awk -F ','  '{print "gs://voiceloft_amazon_data/media/" $2}' indian_test_data.csv > sepen.txt
   ```

   divides the lines in the given file with comma, and then selects the second column.

2. ```bash
   awk  -F ','  '{if (NR!=1) { print "gs://voiceloft_amazon_data/media/" $2}}' indian_test_data.csv > sepen.txt
   ```

   this will allso ignore the first row

3. 
