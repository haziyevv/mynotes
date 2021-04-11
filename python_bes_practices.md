**Fork on github:** To copy someone elses project and make your changes to that project. You can also start with someone else's project by forking it, then add their licence. 

## Python implementations:

Cpython:  reference implementation, written in C. This is the standard python implementation

PyPy: Faster implementation compared to the cpython

Jython: Python implementation to work with java

IronPython: Python implementation to work with .net 

PythonNet: Python implementation to work with .net

## Pipenv and Virtual Environments

### **Pipenv**:

Dependency manager for python projects. 

Manages dependencies on a per-project basis. 

```
 pipenv install requests
```

--> this command will install requests library and create a Pipfile file where all the dependencies will be added.

```
pipenv run python main.py 
```

--> this way we run the main script. We add pipenv before, to ensure installed pipenv packages are available to the python script. İf we do not add pipenv before, libraries installed by pipenv for this project will not be accessible to the python script.

### **Virtualenv**

```
pip install virtualenv
virtualenv testing
```

--> installs virtualenv and creates a virtualenv named testing in the given directory.

```
to activate: source testing/bin/activate
```

### VirtualEnvWrapper

```
pip install virtualenvwrapper
export WORKON_HOME=~/ENVS
source ./local/bin/virtualenvwrapper.sh
```

first command installs virtualenvwrapper.

second command exports its main directory where all the created virtual environments will be installed.

third command activates the virtual environment wrapper

```
mkvirtualenv venv --> creates a virtual environment named venv in ENVS folder
workon venv --> activates the venv virtual environment
```





# Classes in Python

  **String representation of instances**: 

1.   **\_\_str\_\_**  --> result when we call **print(object)** .  

2. **\_\_repr\_\_** --> Printable representation of the class. 
   
   These two are mainly similar and have the purpose of showing the printable representation of the class
   
    

**_\_slots\_\_**  :    When the instances are created a lot like more than 1000 instances will be created and this class keeps some data that will not be changed, it is better to keep them  in tupple instead of dictionary. Using __slots__ wil do this for us and decrease the memory usage. **So use this whenever the instances are created a lot**.

```
class Date:
  __slots__ = ['year', 'month', 'day']
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
```



##### **Encapsulating names**:

1) Any name that starts with a single leading **underscore (_) should always be assumed to be internal implementation.** 

2) Any name starting with two leading **underscores (__) is called private implementation**. What private implementations give is that mainly they are also internal operations and should be approached carefully. Also, their difference from single underscore is that these implementations are not available in inheritance. Meaning, private methods and properties of the parent **class are not inherited by the child class.**



##### Class Method and Static Method

**Class Method**: These methods are used like alternative constructors.

**Static Method**: To attach to the class, the utility functions somehow related to the class.

**\_\_init\_\_** : is not a constructor  



# PYCHARM

1. **ctrl+alt+s** --> goes to settings. In settings you can add documentation types **such as plain, google or numpy**.

2. 
