# Vim Cheatsheet

**ctrl+r** --> redo action

**/def** --> def sözünü search edir , alternative to **?def**

**:%s/hi/hilo/g** --> to search word "hi" and replace it with "hilo". here g means, do this for all occurences.

**ctrl + n** --> default autocompletion on vim

# Linux Cheatsheet

1.  How to extract and untar files inside .tar.gz to current directory .

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

10. 
