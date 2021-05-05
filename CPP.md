1. User input:

```
cout << "Please enter your name:" << flush;
string name;
cin >> name;
```

2. In c++ comparing flaots is problematic :

```
float f1 = 1.1
if(f1==1.1){
    cout << "They are equal" << endl;
}
else{
    cout << "They are not equal" << endl;
}

output--> They are not equal
```

3. **const** --> when you declare variable with const you can not change it in the program.

```
const string password = "hello"
```

So you can not change password variable elsewhere.

4. Multidimensional arrays:

```
string animals[2][3] = {
            {"fox", "dog", "cat"}, 
            {"mouse", "squirrel", "parrot"}
};
```
