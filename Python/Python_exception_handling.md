# Exception Handling

**Index Error**: When the integer index is not in the range

**Key Error**: When the key does not exist in the lookup

**Value Error:** Object is of the right type, but contains inapropriate value for the operation. In the example below we can see that. Input type is correct, it is a string but a string that can not be converted to integer.

```
def converter(s: str) -> int:
    x = int(s)
    return x



In [2]: converter("alma")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-684f7a9b4202> in <module>
----> 1 converter("alma")

<ipython-input-1-f8f112efece0> in converter(s)
      1 def converter(s: str) -> int:
----> 2     x = int(s)
      3     return x

ValueError: invalid literal for int() with base 10: 'alma'
```

**Type Error**: Object is not of the right type. In the example below, string or byte or int is expected, but input was a list.

```
In [3]: converter([1,2,3,4])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-c417cd5701e1> in <module>
----> 1 converter([1,2,3,4])

<ipython-input-1-f8f112efece0> in converter(s)
      1 def converter(s: str) -> int:
----> 2     x = int(s)
      3     return x

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
```

- [x] Avoid doing this:

```
try:
    do_something
except:
pass
```

or

```
try:
    do_something
except Exception as e
    print(e)
```

If you pass, or catch any exception, the you will not know what causes the error.
