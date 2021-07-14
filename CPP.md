1. What is a preprocessor ?
2. What should be returned in the **main** to show that program is run correctly ?
3. What is the size of the **short** integer ?
4. How to get the size of any variable ?
5. What is the size of **char** variable ?
6. What is typedef and how to define it ? 
7. What happens when a variable for example **int** is declared more than its maximum value ?
8.  What is literal constant and symbolic constant ?
9.  How to create **enum** and how it works
10.  
11.  
12.  
13.  
14.  
15.  
16.  
17.  
18.  
19.  
20.  
21.  
22.  
23.  
24.  
25.  
26.  
27.  
28.  
29.  
30. 
31. User input:

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

8. Constructors and Destructors

```
Cat()
~Cat()
```

in cat.h just type the code above

```
Cat::Cat(){
    happy = true;
    cout << "cat is created" << endl;
}


Cat::~Cat(){
    cout << 'cat is destroyed'
}
```

9. String Streams

```
#include <sstream>

stringstream info;
string name = "Farid";
int age = 29;

info << "My name is" << name << " I am " << age << " years old";
cout << info.str() << endl;
```

10. Using this pointer

```
Person::Person(string name, int age){
    this->name = name;
    this->age = age;
}
```

11. Constructor initialization lists:

```
Person::Person(string name, int age): name(name), age(age){};
```

12. **Pointers**:

```
int* pnValue --> this is a pointer to int
& --> gets the addres of a variable
int val = 5
&val --> returns the addres of val variable 
*pnValue --> returns the value where pnValue pointer refers to
```

13. Casting 

```
cast to double
double val1 = (double)7/2
```

14. Inheritance

```
class Cat: public Animal{

}

--> here class cat inherits from class Animal
```

# Advanced C++

1. **Typedef**  --> used to create an alias for an existing data type.

```
typedef double distance_t;
distance_t milesTo = 3.3;

--> here distance_t is used instead of double as the data type
```

2. **Type alias** is a more improved version of typedef

```
using distance_t = double;
```

3. How to write to a file:

```
include <fstream>

ofstream myfile("exmaple.txt");
if(myfile.is_open()){
    myfile << "This is life" << endl;
    myfile.close()
}
```

4. How to read from a file:

```
include <fstream>


ifstream myfile("example.txt");
if(myfile.is_open()){
    string line;
    while(myfile){
        getline(myfile, line)
        cout << line << endl;
    }
    myfile.close()
}
```

5. Explain vectors briefly :
- They are different from normal array in that they are resizable like python lists. You can start without defining its length and push as much as objects you want.

```
vector<string> strings;
strings.push_back("one");
strings.push_back("two");
```

6. Explain two dimensional vectors:

```
vector< vector<int> > grid(3, vector<int>(4, 12));

this will create a vector (3,4) and fit it with 12s
```

7. 



# Answers

9. ```
   enum Days = { Monday, Tuesday, Wednesday, Thursday, Friday};
   
   Days day1 = Friday;
   ```
