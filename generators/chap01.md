## Python generators to expand understanding.

### Let's go dive deeper into some specific aspects

### 1. **Using `yield` to Maintain State**
   - When you use `yield`, the generator function remembers its state. Each time it’s resumed, it picks up exactly where it left off. This is ideal for sequences where each element depends on the previous one.

   Here’s a more complex example: a generator that yields prime numbers indefinitely.

   ```python
   def generate_primes():
       num = 2
       while True:
           is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
           if is_prime:
               yield num
           num += 1

   prime_gen = generate_primes()
   for _ in range(5):
       print(next(prime_gen))  # Outputs the first 5 prime numbers
   ```

### 2. **Generator Expressions with Conditional Logic**
   - Generator expressions can include conditions, allowing for filtered, lazy evaluation.

   ```python
   even_squares = (x * x for x in range(20) if x % 2 == 0)
   for square in even_squares:
       print(square)  # Outputs squares of even numbers up to 20
   ```

### 3. **Pipelining with Generators**
   - Generators can be combined in a pipeline, where each generator processes and passes its output to the next one. This pattern is useful in data processing.

   For example, let’s build a simple pipeline that:
   1. Generates numbers from 1 to 10.
   2. Filters even numbers.
   3. Squares each even number.

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

   # Creating the pipeline
   numbers = number_generator()
   even_numbers = even_filter(numbers)
   squared_evens = square_mapper(even_numbers)

   for result in squared_evens:
       print(result)  # Outputs squares of even numbers: 4, 16, 36, 64, 100
   ```

### 4. **Using `send()` and `yield` Together**
   - You can send values back into a generator using `send()`. This is useful when you want to communicate with the generator while it’s running.

   Here’s an example where a generator calculates a running total, and you can adjust the number it adds on each iteration:

   ```python
   def running_total():
       total = 0
       while True:
           num = yield total
           total += num if num is not None else 0

   accumulator = running_total()
   next(accumulator)  # Prime the generator

   print(accumulator.send(5))  # Outputs: 5
   print(accumulator.send(10))  # Outputs: 15
   print(accumulator.send(-3))  # Outputs: 12
   ```

### 5. **Using `yield from` for Subgenerators**
   - The `yield from` expression allows a generator to delegate part of its operations to another generator. This is handy for breaking up complex generators into smaller parts.

   Here’s an example of using `yield from`:

   ```python
   def child_generator():
       yield "Hello"
       yield "World"

   def parent_generator():
       yield from child_generator()
       yield "!"

   for item in parent_generator():
       print(item)  # Outputs: Hello, World, !
   ```

### 6. **Using Generators for File Processing**
   - Generators are perfect for handling large files since they don’t load the entire file into memory.

   Here’s a generator that reads a file line by line:

   ```python
   def read_file_line_by_line(filename):
       with open(filename, 'r') as file:
           for line in file:
               yield line.strip()

   for line in read_file_line_by_line("large_file.txt"):
       print(line)  # Processes one line at a time, efficiently handling large files
   ```

### 7. **Advanced Example: Infinite Sequence with Custom Stop Condition**
   - Here’s a generator that yields values indefinitely until it hits a custom stop condition (like reaching a maximum).

   ```python
   def countdown(start):
       while start > 0:
           yield start
           start -= 1

   for number in countdown(5):
       print(number)  # Outputs: 5, 4, 3, 2, 1
   ```

