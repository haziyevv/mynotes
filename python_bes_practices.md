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
source ./local/bin/virtualenwrapper.sh
```

first command installs virtualenvwrapper.

second command exports its main directory where all the created virtual environments will be installed.

third command activates the virtual environment wrapper

```
mkvirtualenv venv --> creates a virtual environment named venv in ENVS folder
workon venv --> activates the venv virtual environment
```


