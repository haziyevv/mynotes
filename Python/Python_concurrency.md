1. What does Thread-safe mean ?

2. Research about deadlock ?

3. task\_que.get(block=False) ?

4. In cpython no 2 threads can run at the same time 

5. sys.getrefcount(a) --> shows number of references to the object "a"

**Reference count** --> obyekte olan müraciet sayıdır. Eger bu sıfır olarsa **garbage collector** bu obyekti silir yaddaşdan.

IO bound vs cpu bound -- > with io bound you can use multithreading. But with cpu bound functions multithreading is not working. 





6.  Most high level and easy to use parallel processing features are given by **concurrent.futures**

```
from concurrent.futures import , ProcessPoolExecutor


with ThreadPoolExecutor() as exec:
    exec.map(func, arguments_list)
```

example:

```
def error_calc(audio_file):
    key_ = audio_file.split("/")[-1].split(".")[0]
    error_ = get_error_rate(audio_file, texts[key_])
    return error_

with ThreadPoolExecutor() as exec:
    exec.map(func, audio_files)
```









Gedeye Amazon account yaratdım. Onun accountuna s3e acces verdim bu işe yaramadı.

S3 iam role yaratdım ve ec2 ye verdim. bu işledi.









## Asyncio

1. Runs in a single process and a single thread. 

2. Everything is happening within 1 thread and 1 process.

3. **Await** --> where it is safe for asyncio to go another coroutine. Generally it is where we are waiting for some io to complete.

4. **Coroutine** --> This is just a stateful subroutine, namely function. Its difference and advantage from  a function is that when you invoke a function again it does not remember anything and starts from beginning, but with coroutines it continues from where it left. 

5. When you use **await f()** -- **f** function should be awaitable. This means it is another coroutine, or an object defining an **\_\_await\_\_** dunder method.

6. 

