1. **r** before a regex pattern makes it a raw string. 

   ```python
   re.search(rf'"{kw}": "\d+.\d+"')
   ```

2. pattern = "the (.\*)er they (.\*), the \1er we \2"

   This patern will match:

   the faster they ran, the faster we ran

   but will not match:

   the faster they ran, the faster we catch

3. If you do not want to capture a group:

   pattern = (?:some|a few) (people|cats) like some \1

   This pattern will match:

   some cats like some cats

   but not:

   some cats like some some

4. ```python
   re.findall("(un)?expected", "a few unexpected words are to be expected")
   ```

   this will return ["un", ""]. Because python will try to capture the groups.

   to fix this:

   ```python
   re.findall("(?:un)?expected", "a few unexpected words are to be expected")
   ```

   This will make group non capturable. This will return ["unexpected", "expected"]

5. To match the string in the end of a sentence:

   ```python
   re.match("example$", "there is an example in the end of example")
   ```

   

