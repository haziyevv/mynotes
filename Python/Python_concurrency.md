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




## Asyncio

1. Asyncio is created to fix the context switching problem in threading. In threading each time one thread os stopped and context is switched to the other thread to do its task. 

1. Asynchronous means for example: you have 10 urls that you have to send request. You send one request and then cpu does not sleep and wait for the response, it goes to the second url and like this.

1. A **coroutine** is a function that can suspend its execution before reaching return and it can directly pass control to some other **coroutine** for some time.

1. What is an **event loop** ?

   - There is a queue of events and a loop that constantly pulls events off the queue and runs them. These events are called **coroutines**.

1. How to create an event loop and run a coroutine ?

   ```python
   import asyncio
   
   async def main():
   	print('salam qaqa')
   asyncio.run(main())
   ```

1. 
3. Runs in a single process and a single thread. 
4. Everything is happening within 1 thread and 1 process.
5. **Await** --> where it is safe for asyncio to go another coroutine. Generally it is where we are waiting for some io to complete.
6. **Coroutine** --> This is just a stateful subroutine, namely function. Its difference and advantage from  a function is that when you invoke a function again it does not remember anything and starts from beginning, but with coroutines it continues from where it left. 
7. When you use **await f()** -- **f** function should be awaitable. This means it is another coroutine, or an object defining an **\_\_await\_\_** dunder method.
6. 

