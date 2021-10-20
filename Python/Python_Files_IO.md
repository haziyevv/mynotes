# Python Files - I/O

1. Explain **os.walk**:
- It lets you run through every directory and file inside a given path:

```
import os

for root, dirnames, filenames in os.walk("mynotes"):
    
```

--> Here at first, **root** will be the **mynotes** and **dirnames** will be all the directories inside **mynotes** folder, and **filenames** will be all the files inside **mynotes** folder directly, not inside any folder in the **mynotes**. 

--> In next iteration it will enter the first **dirname** inside the **root**. This time **root** will be that dirname.

2. Explain **pathlib**:
* Object Oriented, makes it more clean than os.path

```python
from pathlib import Path

path = Path("Documents") / "mynotes"
```

* It has **glob** and **rglob** methods available. **glob** will return files matching the pattern in the given directory, but **rglob** will return files that match the pattern in any directory inside the given directory.

```python
[x for x in path.rglob("*.md")]  --> will return all the files with 
--> .md extension inside the path and in all of its subdirectories
```

3. Parse xml:
   * One possible solution is **ElementTree**

```python
import xml.etree.ElementTree as ET

tree = ET.parse("some_data.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
```

4. 

