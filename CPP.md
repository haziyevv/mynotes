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

5. **Prototype:** define a function befor creating it.

```
void doSomething();
int main(){
    doSomething();
    return 0;
}

void doSomething(){
    cout << "Hello World" << endl;
}
```

6. Headers --> files where you put the prototypes

```
#include "utils.sh"
```

include that header file named **utils.sh** like that

7. Classes: 

Lets create a class named **Cat.cpp**, then we also should create **Cat.h**. We will create the class and its variables in **Cat.h**, but applications are in **Cat.cpp**:

cat.h --> 

```
class Cat{
public:
    void speak();
    void jump();
}
```

cat.cpp -->

```
#include "Cat.h"

void Cat::speak(){
    cout << "Meouuuuw" << endl;
}

void Cat::jump(){
    cout << "A cat has jumped" << endl;
}
```
