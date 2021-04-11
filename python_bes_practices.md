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
   
    

**_\_slots\_\_**  :    For classes that primarily serve as simple data structures, you can often greatly reduce the memory footprint of instances by adding the __slots__ attribute to the class definition. 

```
class Date:
  __slots__ = ['year', 'month', 'day']
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
```

When you define __slots__ , Python uses a much more compact internal representation
for instances. Instead of each instance consisting of a dictionary, instances are built
around a small fixed-sized array, much like a tuple or list. Attribute names listed in the
__slots__ specifier are internally mapped to specific indices within this array. A side
effect of using slots is that it is no longer possible to add new attributes to instances—
you are restricted to only those attribute names listed in the __slots__ specifier.



##### **Encapsulating names**:

1) Any name that starts with a single leading **underscore (_) should always be assumed to be internal implementation.** 

2) Any name starting with two leading **underscores (__) is called private implementation**. What private implementations give is that mainly they are also internal operations and should be approached carefully. Also, their difference from single underscore is that these implementations are not available in inheritance. Meaning, private methods and properties of the parent **class are not inherited by the child class.**

3) 





# PYCHARM

1. **ctrl+alt+s** --> goes to settings. In settings you can add documentation types **such as plain, google or numpy**.

2. 
