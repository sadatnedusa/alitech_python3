# Generators in Python

## A powerful tool for creating iterators in a memory-efficient way, especially useful when working with large datasets or streams of data.
## They allow you to define an iterator with minimal code using the `yield` keyword instead of `return`.

### Overview:

### 1. **Defining a Generator**
   - A generator function is defined like a normal function but uses `yield` to return a value, pausing the function and saving its state. When the generator is called again, it resumes from where it left off.

   ```python
   def simple_generator():
       yield 1
       yield 2
       yield 3
   ```

   - Calling `simple_generator()` returns a generator object. You can iterate over it using a `for` loop or `next()`.

   ```python
   gen = simple_generator()
   print(next(gen))  # Outputs: 1
   print(next(gen))  # Outputs: 2
   print(next(gen))  # Outputs: 3
   ```

### 2. **Why Use Generators?**
   - **Memory Efficiency**: Generators yield items one at a time, which means you don’t need to store the entire sequence in memory.
   - **Lazy Evaluation**: Generators produce items only as needed, making them ideal for handling large or infinite sequences.
   - **Pipelines**: You can use them to create data pipelines, where data flows through several steps without needing intermediate storage.

### 3. **Example: Fibonacci Sequence**

   Here’s a generator that yields an infinite sequence of Fibonacci numbers:

   ```python
   def fibonacci():
       a, b = 0, 1
       while True:
           yield a
           a, b = b, a + b

   fib_gen = fibonacci()
   for _ in range(10):
       print(next(fib_gen))  # Outputs the first 10 Fibonacci numbers
   ```

### 4. **Using Generators with `for` Loops**
   - You can iterate over a generator using a `for` loop, which handles `StopIteration` (the error raised when there are no more items) automatically.

   ```python
   def countdown(n):
       while n > 0:
           yield n
           n -= 1

   for number in countdown(5):
       print(number)  # Outputs: 5, 4, 3, 2, 1
   ```

### 5. **Generator Expressions**
   - Python also supports generator expressions, similar to list comprehensions but enclosed in parentheses. These expressions create generators directly.

   ```python
   gen_exp = (x * x for x in range(10))
   print(sum(gen_exp))  # Outputs the sum of squares from 0 to 9
   ```
