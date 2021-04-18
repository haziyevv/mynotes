#### Modules, Scripts and Programs

**Module**: Any .py code is a module. Mainly modules are convenient to import with api.

**Script**: any simple python code, that is more compatible to run from terminal rather than using it in an api.

**Program**: Composed of many modules.

##### Modules:

- ```
  from word import (fetch_words, print_words) --> we can import several 
                              functions from the word module like this
  ```

- **CODE OF ZEN**: Sparse is better than Dense. You should put two blank lines between the functions.

- **Docstring**: (documentation of the module)
  
  - In the first line use it as an information about what the module do in general, and how to run it
  
  - ```
    """
    What this module does in general, what is its purpose?
    Usage: python3 module_frodo.py "frodo baggıns"
    """
    ```
  
  - In each function add docstring, explaining the purpose of the function, what it does, input arguments and what it will return
  
  - ```
    """
    This function will make the life a better place for us.
    Args:
        url: the url you want to connect
        age: your age
    Returns:
        A list of movies that u could watch
    """
    ```
