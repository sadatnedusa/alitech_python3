### Start with beginner-friendly examples and build up to more advanced uses of generators.
#### Each example will demonstrate different generator techniques, advancing gradually.

#### Beginner Level

1. **Basic Generator Function**
   - This example introduces a simple generator that yields values one by one.

   ```python
   def simple_generator():
       yield "Python"
       yield "is"
       yield "fun"

   for word in simple_generator():
       print(word)
   ```

   **Output**:
   ```
   Python
   is
   fun
   ```

2. **Counting Generator**
   - This generator yields numbers in a sequence, useful for understanding how generators can replace basic loops.

   ```python
   def count_up_to(limit):
       count = 1
       while count <= limit:
           yield count
           count += 1

   for number in count_up_to(5):
       print(number)
   ```

   **Output**:
   ```
   1
   2
   3
   4
   5
   ```

### Intermediate Level

3. **Generator for Filtering Even Numbers**
   - This generator function yields only even numbers from a given sequence, introducing conditionals within a generator.

   ```python
   def even_numbers(seq):
       for num in seq:
           if num % 2 == 0:
               yield num

   numbers = [1, 2, 3, 4, 5, 6, 7, 8]
   for even in even_numbers(numbers):
       print(even)
   ```

   **Output**:
   ```
   2
   4
   6
   8
   ```

4. **Generator Expression**
   - This example uses a generator expression, which is a concise way to create a generator.

   ```python
   squares = (x * x for x in range(5))
   for square in squares:
       print(square)
   ```

   **Output**:
   ```
   0
   1
   4
   9
   16
   ```

   - Step-by-step explanation of code in **layman's terms**:
      
      ### Code Overview:
      ```python
      squares = (x * x for x in range(5))
      for square in squares:
          print(square)
      ```
      
      ### What the Code Does:
      1. **Creates a "generator" that calculates squares of numbers in a range (`squares`)**.
      2. **Iterates over the generator using a `for` loop**.
      3. **Prints each squared value**.
      
      ### Step-by-Step Breakdown:
      #### **Step 1: `range(5)`**
      - `range(5)` generates numbers from 0 to 4 (5 is excluded). 
        - Output: `0, 1, 2, 3, 4`.
      
      #### **Step 2: `(x * x for x in range(5))`**
      - This is called a **generator expression**.
      - **What it does**:
        - For every number `x` in `range(5)`, it computes `x * x` (i.e., the square of `x`).
        - The result is not computed all at once; instead, it calculates one square at a time when needed. This is called **lazy evaluation**.
      - **Why use a generator?**
        - Saves memory because it computes each value on demand rather than creating a large list in memory.
      
      - Example:
        - When you ask the generator for a value, it gives:
          - \( 0^2 = 0 \)
          - \( 1^2 = 1 \)
          - \( 2^2 = 4 \)
          - \( 3^2 = 9 \)
          - \( 4^2 = 16 \)
      
      #### **Step 3: `for square in squares`**
      - This loops through the generator.
      - Each time the loop runs:
        - The generator calculates the next square.
        - The value of the square is stored in the variable `square`.
      
      #### **Step 4: `print(square)`**
      - Each `square` is printed to the console.

      
      ### Key Concept: What is Lazy Evaluation?
      - Instead of creating all squares at once (like in a list `[x * x for x in range(5)]`), the generator calculates one square at a time when the `for` loop asks for it.
      - This makes generators efficient for handling large datasets, as they don’t use unnecessary memory.
   
      
      ### Final Output:
      Here’s how the loop executes step by step:
      1. `squares` generator is created but doesn’t calculate anything yet.
      2. The `for` loop asks the generator for the first value:
         - \( x = 0 \), calculates \( 0^2 = 0 \), prints `0`.
      3. Loop asks for the next value:
         - \( x = 1 \), calculates \( 1^2 = 1 \), prints `1`.
      4. Repeats for \( x = 2, 3, 4 \), printing `4`, `9`, and `16`.
      
      **Output:**
      ```
      0
      1
      4
      9
      16
      ```


      ### Why is This Useful?
      - **Efficiency**: Generators are memory-efficient because they calculate values one by one instead of storing them all at once.
      - **Example**: If you needed squares of a billion numbers, a generator would calculate them one by one, whereas a list would consume a huge amount of memory.


5. **File Reading Generator**
   - This generator reads a file line-by-line, saving memory by not loading the entire file at once.

   ```python
   def read_file(file_path):
       with open(file_path, 'r') as file:
           for line in file:
               yield line.strip()

   # Assume 'sample.txt' contains lines of text
   for line in read_file('sample.txt'):
       print(line)
   ```

### Advanced Level

6. **Infinite Generator**
   - This generator creates an infinite sequence, useful when the end condition isn’t known beforehand.

   ```python
   def infinite_numbers():
       num = 1
       while True:
           yield num
           num += 1

   gen = infinite_numbers()
   for _ in range(5):
       print(next(gen))
   ```

   **Output**:
   ```
   1
   2
   3
   4
   5
   ```

7. **Using `send()` with Generators**
   - This example demonstrates how to send values to a generator, creating a generator that maintains a running total.

   ```python
   def running_total():
       total = 0
       while True:
           num = yield total
           total += num

   accumulator = running_total()
   next(accumulator)  # Prime the generator

   print(accumulator.send(10))  # Outputs: 10
   print(accumulator.send(5))   # Outputs: 15
   print(accumulator.send(-3))  # Outputs: 12
   ```

8. **`yield from` to Delegate to a Subgenerator**
   - `yield from` allows a generator to delegate part of its operations to another generator, useful for simplifying code structure.

   ```python
   def nested_generator():
       yield "Nested"
       yield "generator"

   def main_generator():
       yield "This is a"
       yield from nested_generator()
       yield "example"

   for word in main_generator():
       print(word)
   ```

   **Output**:
   ```
   This is a
   Nested
   generator
   example
   ```

9. **Pipelining with Multiple Generators**
   - Generators can be used in a pipeline, where each generator performs a transformation and passes results to the next.

   ```python
   def number_generator():
       for i in range(1, 11):
           yield i

   def even_filter(numbers):
       for number in numbers:
           if number % 2 == 0:
               yield number

   def square_mapper(numbers):
       for number in numbers:
           yield number * number

   # Using the pipeline
   numbers = number_generator()
   even_numbers = even_filter(numbers)
   squared_evens = square_mapper(even_numbers)

   for result in squared_evens:
       print(result)
   ```

   **Output**:
   ```
   4
   16
   36
   64
   100
   ```

10. **Simulating a Coroutine with Generators**
    - Generators can be used to simulate coroutines by maintaining and updating internal state.

    ```python
    def average_calculator():
        total, count = 0, 0
        average = None
        while True:
            num = yield average
            total += num
            count += 1
            average = total / count

    calc = average_calculator()
    next(calc)  # Prime the generator

    print(calc.send(10))  # Outputs: 10.0
    print(calc.send(20))  # Outputs: 15.0
    print(calc.send(30))  # Outputs: 20.0
    ```

    **Explanation**:
    - The generator `average_calculator` maintains a running average by storing the total and count of numbers sent to it. Each call to `send` provides a new number, updates the average, and yields it.

