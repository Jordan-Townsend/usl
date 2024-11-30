---

# docs/STANDARD_LIBRARY.md

# USL Standard Library Documentation

The Universal Scripting Language (USL) comes equipped with a robust Standard Library that provides a wide range of built-in modules and functions. These modules facilitate common programming tasks such as input/output operations, mathematical computations, string manipulation, data structure management, date and time handling, and system interactions. This documentation serves as a comprehensive guide to understanding and utilizing the USL Standard Library effectively.

---

 Table of Contents

1. [Introduction](#introduction)
2. [Core Modules](#core-modules)
   - [1. IO Module](#1-io-module)
   - [2. Math Module](#2-math-module)
   - [3. String Module](#3-string-module)
   - [4. Collections Module](#4-collections-module)
   - [5. DateTime Module](#5-datetime-module)
   - [6. System Module](#6-system-module)
3. [Module Usage](#module-usage)
   - [Importing Modules](#importing-modules)
   - [Using Module Functions](#using-module-functions)
4. [Advanced Features](#advanced-features)
   - [Custom Modules](#custom-modules)
   - [Extending the Standard Library](#extending-the-standard-library)
5. [Examples](#examples)
6. [Best Practices](#best-practices)
7. [Appendix](#appendix)

---

 Introduction

The USL Standard Library is designed to provide developers with essential tools to perform a variety of tasks efficiently. By leveraging these built-in modules, you can avoid reinventing the wheel and focus on building the unique aspects of your applications.

---

 Core Modules

USL's Standard Library consists of several core modules, each tailored to specific functionalities. Below is an overview of each core module, including their available functions, classes, constants, and usage examples.

 1. IO Module

 Overview

The `io` module provides functionalities for input and output operations, including reading from and writing to files, handling user input, and interacting with the console.

 Functions

- `print(value)`
  - Description: Outputs the given value to the console.
  - Example:
    ```usl
    import io;
    io.print("Hello, World!");
    ```

- `read()`
  - Description: Reads a line of input from the user and returns it as a string.
  - Example:
    ```usl
    import io;
    io.print("Enter your name:");
    var name = io.read();
    io.print("Hello, " + name + "!");
    ```

- `readFile(path)`
  - Description: Reads the entire content of a file specified by the path and returns it as a string.
  - Example:
    ```usl
    import io;
    var content = io.readFile("data.txt");
    io.print(content);
    ```

- `writeFile(path, data)`
  - Description: Writes the provided data to a file at the specified path. Overwrites the file if it already exists.
  - Example:
    ```usl
    import io;
    var data = "This is a sample text.";
    io.writeFile("output.txt", data);
    ```

- `appendFile(path, data)`
  - Description: Appends the provided data to the end of the file at the specified path. Creates the file if it does not exist.
  - Example:
    ```usl
    import io;
    var additionalData = "\nAppended line.";
    io.appendFile("output.txt", additionalData);
    ```

 Classes

- `File`
  - Description: Represents a file and provides methods for more granular file operations.
  - Constructor:
    ```usl
    var file = new File("path/to/file.txt");
    ```
  - Methods:
    - `open(mode)`
      - Description: Opens the file in the specified mode (`"r"` for read, `"w"` for write, `"a"` for append).
      - Example:
        ```usl
        file.open("r");
        ```
    - `close()`
      - Description: Closes the file.
      - Example:
        ```usl
        file.close();
        ```
    - `readLine()`
      - Description: Reads the next line from the file.
      - Example:
        ```usl
        var line = file.readLine();
        io.print(line);
        ```
    - `write(data)`
      - Description: Writes data to the file.
      - Example:
        ```usl
        file.write("Writing to the file.");
        ```

 Constants

- `EOF`
  - Description: Represents the end-of-file marker.
  - Usage Example:
    ```usl
    import io;
    
    var file = new File("data.txt");
    file.open("r");
    
    while (true) {
        var line = file.readLine();
        if (line == io.EOF) {
            break;
        }
        io.print(line);
    }
    
    file.close();
    ```

---

 2. Math Module

 Overview

The `math` module offers a collection of mathematical functions and constants to perform complex calculations, trigonometric operations, and more.

 Constants

- `PI`
  - Description: Represents the mathematical constant π (3.14159...).
  - Example:
    ```usl
    import math;
    io.print("Value of PI: " + math.PI);
    ```

- `E`
  - Description: Represents Euler's number (2.71828...).
  - Example:
    ```usl
    import math;
    io.print("Value of E: " + math.E);
    ```

 Functions

- `abs(value)`
  - Description: Returns the absolute value of the given number.
  - Example:
    ```usl
    import math;
    var number = -10;
    io.print("Absolute value: " + math.abs(number)); // Outputs: Absolute value: 10
    ```

- `ceil(value)`
  - Description: Returns the smallest integer greater than or equal to the given number.
  - Example:
    ```usl
    import math;
    var number = 3.14;
    io.print("Ceiling: " + math.ceil(number)); // Outputs: Ceiling: 4
    ```

- `floor(value)`
  - Description: Returns the largest integer less than or equal to the given number.
  - Example:
    ```usl
    import math;
    var number = 3.99;
    io.print("Floor: " + math.floor(number)); // Outputs: Floor: 3
    ```

- `round(value)`
  - Description: Rounds the given number to the nearest integer.
  - Example:
    ```usl
    import math;
    var number = 2.5;
    io.print("Rounded: " + math.round(number)); // Outputs: Rounded: 3
    ```

- `sqrt(value)`
  - Description: Returns the square root of the given number.
  - Example:
    ```usl
    import math;
    var number = 16;
    io.print("Square root: " + math.sqrt(number)); // Outputs: Square root: 4
    ```

- `pow(base, exponent)`
  - Description: Raises the base to the power of the exponent.
  - Example:
    ```usl
    import math;
    var base = 2;
    var exponent = 3;
    io.print("Power: " + math.pow(base, exponent)); // Outputs: Power: 8
    ```

- `sin(angle)`
  - Description: Returns the sine of the given angle (in radians).
  - Example:
    ```usl
    import math;
    var angle = math.PI / 2;
    io.print("Sine of PI/2: " + math.sin(angle)); // Outputs: Sine of PI/2: 1
    ```

- `cos(angle)`
  - Description: Returns the cosine of the given angle (in radians).
  - Example:
    ```usl
    import math;
    var angle = 0;
    io.print("Cosine of 0: " + math.cos(angle)); // Outputs: Cosine of 0: 1
    ```

- `tan(angle)`
  - Description: Returns the tangent of the given angle (in radians).
  - Example:
    ```usl
    import math;
    var angle = math.PI / 4;
    io.print("Tangent of PI/4: " + math.tan(angle)); // Outputs: Tangent of PI/4: 1
    ```

- `log(value)`
  - Description: Returns the natural logarithm (base e) of the given number.
  - Example:
    ```usl
    import math;
    var number = math.E;
    io.print("Natural Logarithm of E: " + math.log(number)); // Outputs: Natural Logarithm of E: 1
    ```

- `exp(value)`
  - Description: Returns e raised to the power of the given number.
  - Example:
    ```usl
    import math;
    var number = 1;
    io.print("Exponential of 1: " + math.exp(number)); // Outputs: Exponential of 1: 2.71828...
    ```

- `min(a, b)`
  - Description: Returns the smaller of two numbers.
  - Example:
    ```usl
    import math;
    io.print("Min of 10 and 20: " + math.min(10, 20)); // Outputs: Min of 10 and 20: 10
    ```

- `max(a, b)`
  - Description: Returns the larger of two numbers.
  - Example:
    ```usl
    import math;
    io.print("Max of 10 and 20: " + math.max(10, 20)); // Outputs: Max of 10 and 20: 20
    ```

 Classes

- `Random`
  - Description: Provides methods to generate random numbers.
  - Constructor:
    ```usl
    var rng = new math.Random();
    ```
  - Methods:
    - `nextInt(min, max)`
      - Description: Returns a random integer between `min` (inclusive) and `max` (exclusive).
      - Example:
        ```usl
        var randomNumber = rng.nextInt(1, 100);
        io.print("Random Integer: " + randomNumber);
        ```
    - `nextFloat(min, max)`
      - Description: Returns a random floating-point number between `min` and `max`.
      - Example:
        ```usl
        var randomFloat = rng.nextFloat(0.0, 1.0);
        io.print("Random Float: " + randomFloat);
        ```

 Constants

- `math.PI`
  - Description: The mathematical constant π (3.141592653589793).
  - Example:
    ```usl
    import math;
    io.print("PI: " + math.PI); // Outputs: PI: 3.141592653589793
    ```

- `math.E`
  - Description: Euler's number (2.718281828459045).
  - Example:
    ```usl
    import math;
    io.print("E: " + math.E); // Outputs: E: 2.718281828459045
    ```

---

 3. String Module

 Overview

The `string` module offers a suite of functions for string manipulation, enabling operations such as concatenation, searching, slicing, and formatting.

 Functions

- `length(str)`
  - Description: Returns the length of the given string.
  - Example:
    ```usl
    import string;
    var message = "Hello, USL!";
    io.print("Length: " + string.length(message)); // Outputs: Length: 11
    ```

- `substring(str, start, end)`
  - Description: Extracts a substring from `str` starting at index `start` and ending before index `end`.
  - Example:
    ```usl
    import string;
    var text = "Hello, World!";
    var sub = string.substring(text, 7, 12);
    io.print("Substring: " + sub); // Outputs: Substring: World
    ```

- `indexOf(str, substring)`
  - Description: Returns the index of the first occurrence of `substring` in `str`. Returns `-1` if not found.
  - Example:
    ```usl
    import string;
    var text = "Hello, USL!";
    var index = string.indexOf(text, "USL");
    io.print("Index of 'USL': " + index); // Outputs: Index of 'USL': 7
    ```

- `toUpperCase(str)`
  - Description: Converts all characters in `str` to uppercase.
  - Example:
    ```usl
    import string;
    var text = "Hello, USL!";
    var upper = string.toUpperCase(text);
    io.print("Uppercase: " + upper); // Outputs: Uppercase: HELLO, USL!
    ```

- `toLowerCase(str)`
  - Description: Converts all characters in `str` to lowercase.
  - Example:
    ```usl
    import string;
    var text = "Hello, USL!";
    var lower = string.toLowerCase(text);
    io.print("Lowercase: " + lower); // Outputs: Lowercase: hello, usl!
    ```

- `replace(str, old, new)`
  - Description: Replaces all occurrences of `old` in `str` with `new`.
  - Example:
    ```usl
    import string;
    var text = "Hello, World!";
    var newText = string.replace(text, "World", "USL");
    io.print(newText); // Outputs: Hello, USL!
    ```

- `split(str, delimiter)`
  - Description: Splits `str` into an array based on the specified `delimiter`.
  - Example:
    ```usl
    import string;
    var csv = "apple,banana,cherry";
    var fruits = string.split(csv, ",");
    for (var fruit in fruits) {
        io.print(fruit);
    }
    /*
    Outputs:
    apple
    banana
    cherry
    */
    ```

- `trim(str)`
  - Description: Removes whitespace from both ends of `str`.
  - Example:
    ```usl
    import string;
    var messy = "   Hello, USL!   ";
    var clean = string.trim(messy);
    io.print("'" + clean + "'"); // Outputs: 'Hello, USL!'
    ```

- `concat(str1, str2, ...)`
  - Description: Concatenates multiple strings into one.
  - Example:
    ```usl
    import string;
    var greeting = "Hello";
    var name = "Alice";
    var message = string.concat(greeting, ", ", name, "!");
    io.print(message); // Outputs: Hello, Alice!
    ```

 Classes

- `StringBuilder`
  - Description: Efficiently constructs and manipulates large strings.
  - Constructor:
    ```usl
    var sb = new string.StringBuilder();
    ```
  - Methods:
    - `append(str)`
      - Description: Appends `str` to the current string.
      - Example:
        ```usl
        sb.append("Hello, ");
        sb.append("USL!");
        io.print(sb.toString()); // Outputs: Hello, USL!
        ```
    - `toString()`
      - Description: Returns the concatenated string.
      - Example:
        ```usl
        var result = sb.toString();
        io.print(result); // Outputs: Hello, USL!
        ```
    - `clear()`
      - Description: Clears the current string.
      - Example:
        ```usl
        sb.clear();
        io.print(sb.toString()); // Outputs an empty string
        ```

 Constants

- `string.EMPTY`
  - Description: Represents an empty string.
  - Usage Example:
    ```usl
    import string;
    var empty = string.EMPTY;
    io.print("Is empty: " + (empty == "")); // Outputs: Is empty: true
    ```

---

 4. Collections Module

 Overview

The `collections` module provides data structures such as lists, sets, maps, queues, and stacks, along with associated functions to manipulate these structures efficiently.

 Data Structures

- `List`
  - Description: An ordered, dynamic collection of elements.
  - Example:
    ```usl
    import collections;
    var fruits = new collections.List();
    collections.add(fruits, "Apple");
    collections.add(fruits, "Banana");
    collections.add(fruits, "Cherry");
    io.print("Fruits: " + fruits); // Outputs: Fruits: ["Apple", "Banana", "Cherry"]
    ```

- `Set`
  - Description: An unordered collection of unique elements.
  - Example:
    ```usl
    import collections;
    var uniqueNumbers = new collections.Set();
    collections.add(uniqueNumbers, 1);
    collections.add(uniqueNumbers, 2);
    collections.add(uniqueNumbers, 2); // Duplicate, won't be added
    io.print("Unique Numbers: " + uniqueNumbers); // Outputs: Unique Numbers: {1, 2}
    ```

- `Map`
  - Description: A collection of key-value pairs.
  - Example:
    ```usl
    import collections;
    var ageMap = new collections.Map();
    collections.add(ageMap, "Alice", 30);
    collections.add(ageMap, "Bob", 25);
    io.print("Age Map: " + ageMap); // Outputs: Age Map: {"Alice": 30, "Bob": 25}
    ```

- `Queue`
  - Description: A first-in-first-out (FIFO) collection.
  - Example:
    ```usl
    import collections;
    var taskQueue = new collections.Queue();
    collections.enqueue(taskQueue, "Task 1");
    collections.enqueue(taskQueue, "Task 2");
    collections.enqueue(taskQueue, "Task 3");
    
    while (!collections.isEmpty(taskQueue)) {
        var task = collections.dequeue(taskQueue);
        io.print("Processing: " + task);
    }
    /*
    Outputs:
    Processing: Task 1
    Processing: Task 2
    Processing: Task 3
    */
    ```

- `Stack`
  - Description: A last-in-first-out (LIFO) collection.
  - Example:
    ```usl
    import collections;
    var callStack = new collections.Stack();
    collections.push(callStack, "Function A");
    collections.push(callStack, "Function B");
    collections.push(callStack, "Function C");
    
    while (!collections.isEmpty(callStack)) {
        var func = collections.pop(callStack);
        io.print("Exiting: " + func);
    }
    /*
    Outputs:
    Exiting: Function C
    Exiting: Function B
    Exiting: Function A
    */
    ```

 Functions

- `add(collection, item)`
  - Description: Adds an item to the specified collection (`List`, `Set`, or `Map`).
  - Example:
    ```usl
    import collections;
    var list = new collections.List();
    collections.add(list, "Item 1");
    collections.add(list, "Item 2");
    io.print(list); // Outputs: ["Item 1", "Item 2"]
    
    var set = new collections.Set();
    collections.add(set, "A");
    collections.add(set, "B");
    collections.add(set, "A"); // Duplicate, won't be added
    io.print(set); // Outputs: {"A", "B"}
    
    var map = new collections.Map();
    collections.add(map, "Key1", "Value1");
    collections.add(map, "Key2", "Value2");
    io.print(map); // Outputs: {"Key1": "Value1", "Key2": "Value2"}
    ```

- `remove(collection, item)`
  - Description: Removes an item from the specified collection.
  - Example:
    ```usl
    import collections;
    var list = new collections.List();
    collections.add(list, "Item 1");
    collections.add(list, "Item 2");
    collections.remove(list, "Item 1");
    io.print(list); // Outputs: ["Item 2"]
    
    var set = new collections.Set();
    collections.add(set, "A");
    collections.add(set, "B");
    collections.remove(set, "A");
    io.print(set); // Outputs: {"B"}
    
    var map = new collections.Map();
    collections.add(map, "Key1", "Value1");
    collections.remove(map, "Key1");
    io.print(map); // Outputs: {}
    ```

- `contains(collection, item)`
  - Description: Checks if the collection contains the specified item.
  - Example:
    ```usl
    import collections;
    var list = new collections.List();
    collections.add(list, "Apple");
    collections.add(list, "Banana");
    io.print(collections.contains(list, "Apple")); // Outputs: true
    io.print(collections.contains(list, "Cherry")); // Outputs: false
    ```

- `size(collection)`
  - Description: Returns the number of elements in the collection.
  - Example:
    ```usl
    import collections;
    var list = new collections.List();
    collections.add(list, "A");
    collections.add(list, "B");
    io.print("List size: " + collections.size(list)); // Outputs: List size: 2
    ```

- `clear(collection)`
  - Description: Removes all elements from the collection.
  - Example:
    ```usl
    import collections;
    var set = new collections.Set();
    collections.add(set, "X");
    collections.add(set, "Y");
    collections.clear(set);
    io.print(set); // Outputs: {}
    ```

 Classes

- `List`
  - Description: Represents an ordered, dynamic collection of elements.
  - Methods:
    - `append(item)`: Adds an item to the end of the list.
    - `remove(item)`: Removes the first occurrence of the item.
    - `get(index)`: Retrieves the item at the specified index.
    - `set(index, item)`: Sets the item at the specified index.
    - `contains(item)`: Checks if the item exists in the list.
    - `size()`: Returns the number of elements.
    - `clear()`: Removes all elements.
  - Example:
    ```usl
    import collections;
    var fruits = new collections.List();
    fruits.append("Apple");
    fruits.append("Banana");
    io.print("Fruits: " + fruits); // Outputs: Fruits: ["Apple", "Banana"]
    ```

- `Set`
  - Description: Represents an unordered collection of unique elements.
  - Methods:
    - `add(item)`: Adds an item to the set.
    - `remove(item)`: Removes the item from the set.
    - `contains(item)`: Checks if the item exists in the set.
    - `size()`: Returns the number of elements.
    - `clear()`: Removes all elements.
  - Example:
    ```usl
    import collections;
    var uniqueNumbers = new collections.Set();
    uniqueNumbers.add(1);
    uniqueNumbers.add(2);
    uniqueNumbers.add(2); // Duplicate, won't be added
    io.print("Unique Numbers: " + uniqueNumbers); // Outputs: Unique Numbers: {1, 2}
    ```

- `Map`
  - Description: Represents a collection of key-value pairs.
  - Methods:
    - `add(key, value)`: Adds a key-value pair to the map.
    - `remove(key)`: Removes the key-value pair by key.
    - `get(key)`: Retrieves the value associated with the key.
    - `contains(key)`: Checks if the key exists in the map.
    - `size()`: Returns the number of key-value pairs.
    - `clear()`: Removes all key-value pairs.
  - Example:
    ```usl
    import collections;
    var ageMap = new collections.Map();
    ageMap.add("Alice", 30);
    ageMap.add("Bob", 25);
    io.print("Alice's Age: " + ageMap.get("Alice")); // Outputs: Alice's Age: 30
    ```

- `Queue`
  - Description: Implements a first-in-first-out (FIFO) queue.
  - Methods:
    - `enqueue(item)`: Adds an item to the end of the queue.
    - `dequeue()`: Removes and returns the item at the front of the queue.
    - `isEmpty()`: Checks if the queue is empty.
    - `size()`: Returns the number of elements.
    - `clear()`: Removes all elements.
  - Example:
    ```usl
    import collections;
    var taskQueue = new collections.Queue();
    taskQueue.enqueue("Task 1");
    taskQueue.enqueue("Task 2");
    taskQueue.enqueue("Task 3");
    
    while (!taskQueue.isEmpty()) {
        var task = taskQueue.dequeue();
        io.print("Processing: " + task);
    }
    /*
    Outputs:
    Processing: Task 1
    Processing: Task 2
    Processing: Task 3
    */
    ```

- `Stack`
  - Description: Implements a last-in-first-out (LIFO) stack.
  - Methods:
    - `push(item)`: Adds an item to the top of the stack.
    - `pop()`: Removes and returns the item at the top of the stack.
    - `peek()`: Returns the item at the top without removing it.
    - `isEmpty()`: Checks if the stack is empty.
    - `size()`: Returns the number of elements.
    - `clear()`: Removes all elements.
  - Example:
    ```usl
    import collections;
    var callStack = new collections.Stack();
    callStack.push("Function A");
    callStack.push("Function B");
    callStack.push("Function C");
    
    while (!callStack.isEmpty()) {
        var func = callStack.pop();
        io.print("Exiting: " + func);
    }
    /*
    Outputs:
    Exiting: Function C
    Exiting: Function B
    Exiting: Function A
    */
    ```

 Utility Functions

- `add(collection, item)`
  - Description: Adds an item to a collection (`List`, `Set`, or `Map`).
  - Example:
    ```usl
    import collections;
    var list = new collections.List();
    collections.add(list, "Item 1");
    collections.add(list, "Item 2");
    io.print(list); // Outputs: ["Item 1", "Item 2"]
    ```

- `remove(collection, item)`
  - Description: Removes an item from a collection.
  - Example:
    ```usl
    import collections;
    var set = new collections.Set();
    collections.add(set, "A");
    collections.add(set, "B");
    collections.remove(set, "A");
    io.print(set); // Outputs: {"B"}
    ```

- `contains(collection, item)`
  - Description: Checks if a collection contains the specified item.
  - Example:
    ```usl
    import collections;
    var map = new collections.Map();
    collections.add(map, "Key1", "Value1");
    io.print(collections.contains(map, "Key1")); // Outputs: true
    io.print(collections.contains(map, "Key2")); // Outputs: false
    ```

- `size(collection)`
  - Description: Returns the number of elements in the collection.
  - Example:
    ```usl
    import collections;
    var queue = new collections.Queue();
    collections.enqueue(queue, "Task 1");
    collections.enqueue(queue, "Task 2");
    io.print("Queue size: " + collections.size(queue)); // Outputs: Queue size: 2
    ```

- `clear(collection)`
  - Description: Removes all elements from the collection.
  - Example:
    ```usl
    import collections;
    var stack = new collections.Stack();
    collections.push(stack, "Item A");
    collections.push(stack, "Item B");
    collections.clear(stack);
    io.print(stack); // Outputs: []
    ```

 Iteration Helpers

- `forEach(collection, function(item))`
  - Description: Iterates over each element in the collection and executes the provided function.
  - Example:
    ```usl
    import collections;
    
    var fruits = new collections.List();
    collections.add(fruits, "Apple");
    collections.add(fruits, "Banana");
    collections.add(fruits, "Cherry");
    
    collections.forEach(fruits, function(item) {
        io.print("Fruit: " + item);
    });
    /*
    Outputs:
    Fruit: Apple
    Fruit: Banana
    Fruit: Cherry
    */
    ```

---

 5. DateTime Module

 Overview

The `datetime` module provides functionalities to handle dates, times, and durations, enabling developers to perform operations such as getting the current date and time, formatting dates, parsing date strings, and manipulating date and time values.

 Functions

- `now()`
  - Description: Returns the current date and time.
  - Example:
    ```usl
    import datetime;
    var currentDateTime = datetime.now();
    io.print("Current Date and Time: " + datetime.format(currentDateTime, "YYYY-MM-DD HH:MM:SS"));
    ```

- `format(date, formatString)`
  - Description: Formats a `date` object into a string based on the provided `formatString`.
  - Format Specifiers:
    - `YYYY`: 4-digit year
    - `MM`: 2-digit month
    - `DD`: 2-digit day
    - `HH`: 2-digit hour (24-hour format)
    - `MM`: 2-digit minute
    - `SS`: 2-digit second
  - Example:
    ```usl
    import datetime;
    var date = datetime.now();
    var formatted = datetime.format(date, "YYYY-MM-DD");
    io.print("Formatted Date: " + formatted); // Outputs: Formatted Date: 2024-04-27
    ```

- `parse(dateString, formatString)`
  - Description: Parses a `dateString` into a `date` object based on the provided `formatString`.
  - Example:
    ```usl
    import datetime;
    var dateString = "2024-12-31";
    var date = datetime.parse(dateString, "YYYY-MM-DD");
    io.print("Parsed Date: " + datetime.format(date, "DD/MM/YYYY")); // Outputs: Parsed Date: 31/12/2024
    ```

- `addDays(date, days)`
  - Description: Adds a specified number of days to a `date` object.
  - Example:
    ```usl
    import datetime;
    var today = datetime.now();
    var futureDate = datetime.addDays(today, 10);
    io.print("Date after 10 days: " + datetime.format(futureDate, "YYYY-MM-DD"));
    ```

- `addHours(date, hours)`
  - Description: Adds a specified number of hours to a `date` object.
  - Example:
    ```usl
    import datetime;
    var now = datetime.now();
    var later = datetime.addHours(now, 5);
    io.print("Time after 5 hours: " + datetime.format(later, "HH:MM:SS"));
    ```

- `diffInDays(date1, date2)`
  - Description: Calculates the difference in days between two dates.
  - Example:
    ```usl
    import datetime;
    var startDate = datetime.parse("2024-01-01", "YYYY-MM-DD");
    var endDate = datetime.parse("2024-01-15", "YYYY-MM-DD");
    var difference = datetime.diffInDays(endDate, startDate);
    io.print("Difference in Days: " + difference); // Outputs: Difference in Days: 14
    ```

 Classes

- `Date`
  - Description: Represents a specific date and time.
  - Constructor:
    ```usl
    var date = new datetime.Date(year, month, day, hour, minute, second);
    ```
  - Methods:
    - `toString(formatString)`
      - Description: Returns the date as a formatted string.
      - Example:
        ```usl
        var date = new datetime.Date(2024, 12, 25, 10, 30, 0);
        io.print(date.toString("YYYY-MM-DD HH:MM:SS")); // Outputs: 2024-12-25 10:30:00
        ```
    - `addDays(days)`
      - Description: Adds a specified number of days to the date.
      - Example:
        ```usl
        date.addDays(5);
        io.print(date.toString("YYYY-MM-DD")); // Outputs: 2024-12-30
        ```
    - `addHours(hours)`
      - Description: Adds a specified number of hours to the date.
      - Example:
        ```usl
        date.addHours(3);
        io.print(date.toString("HH:MM:SS")); // Outputs: 13:30:00
        ```
    - `differenceInDays(otherDate)`
      - Description: Returns the difference in days between this date and `otherDate`.
      - Example:
        ```usl
        var anotherDate = new datetime.Date(2025, 1, 1);
        var diff = date.differenceInDays(anotherDate);
        io.print("Difference: " + diff + " days"); // Outputs: Difference: 2 days
        ```

 Constants

- `datetime.EPOCH`
  - Description: Represents the Unix epoch time (January 1, 1970).
  - Usage Example:
    ```usl
    import datetime;
    var epoch = datetime.EPOCH;
    io.print("Unix Epoch: " + datetime.format(epoch, "YYYY-MM-DD HH:MM:SS")); // Outputs: Unix Epoch: 1970-01-01 00:00:00
    ```

---

 6. System Module

 Overview

The `system` module allows interaction with the underlying operating system, providing functionalities such as environment variable management, executing system commands, and handling program termination.

 Functions

- `getEnv(variable)`
  - Description: Retrieves the value of the specified environment variable.
  - Example:
    ```usl
    import system;
    var path = system.getEnv("PATH");
    io.print("System PATH: " + path);
    ```

- `setEnv(variable, value)`
  - Description: Sets the value of the specified environment variable.
  - Example:
    ```usl
    import system;
    system.setEnv("MY_VAR", "SomeValue");
    var myVar = system.getEnv("MY_VAR");
    io.print("MY_VAR: " + myVar); // Outputs: MY_VAR: SomeValue
    ```

- `exec(command)`
  - Description: Executes a system command and returns the output.
  - Example:
    ```usl
    import system;
    var output = system.exec("echo Hello from the system!");
    io.print(output); // Outputs: Hello from the system!
    ```

- `exit(code)`
  - Description: Terminates the program with the specified exit code. If no code is provided, defaults to `0`.
  - Example:
    ```usl
    import system;
    io.print("Exiting the program.");
    system.exit(0);
    ```

 Classes

- `Process`
  - Description: Represents a system process, allowing for more advanced process management.
  - Constructor:
    ```usl
    var proc = new system.Process("command", ["arg1", "arg2"]);
    ```
  - Methods:
    - `start()`
      - Description: Starts the process.
      - Example:
        ```usl
        proc.start();
        ```
    - `kill()`
      - Description: Terminates the process.
      - Example:
        ```usl
        proc.kill();
        ```
    - `isRunning()`
      - Description: Checks if the process is currently running.
      - Example:
        ```usl
        io.print("Is running: " + proc.isRunning());
        ```
    - `getOutput()`
      - Description: Retrieves the standard output of the process.
      - Example:
        ```usl
        var output = proc.getOutput();
        io.print("Process Output: " + output);
        ```

 Constants

- `system.OS_WINDOWS`
  - Description: Represents the Windows operating system.
  - Usage Example:
    ```usl
    import system;
    if (system.currentOS() == system.OS_WINDOWS) {
        io.print("Running on Windows.");
    }
    ```

- `system.OS_MACOS`
  - Description: Represents the macOS operating system.
  - Usage Example:
    ```usl
    import system;
    if (system.currentOS() == system.OS_MACOS) {
        io.print("Running on macOS.");
    }
    ```

- `system.OS_LINUX`
  - Description: Represents the Linux operating system.
  - Usage Example:
    ```usl
    import system;
    if (system.currentOS() == system.OS_LINUX) {
        io.print("Running on Linux.");
    }
    ```

 Utility Functions

- `currentOS()`
  - Description: Returns the current operating system as a constant (`OS_WINDOWS`, `OS_MACOS`, `OS_LINUX`).
  - Example:
    ```usl
    import system;
    var os = system.currentOS();
    if (os == system.OS_WINDOWS) {
        io.print("You are using Windows.");
    } else if (os == system.OS_MACOS) {
        io.print("You are using macOS.");
    } else if (os == system.OS_LINUX) {
        io.print("You are using Linux.");
    } else {
        io.print("Unknown operating system.");
    }
    ```

---

 Module Usage

Understanding how to properly import and utilize modules is crucial for leveraging the full capabilities of the USL Standard Library. Below are guidelines and examples on how to import modules and use their functions effectively.

 Importing Modules

To use a module's functions, classes, or constants, you must first import the module into your USL script. There are two primary ways to import modules:

1. Import the Entire Module

   ```usl
   import moduleName;
   ```
   
   Example:
   
   ```usl
   import math;
   var area = math.PI * math.pow(radius, 2);
   io.print("Area: " + area);
   ```

2. Import Specific Submodules or Functions

   ```usl
   import moduleName.subModule;
   ```
   
   Example:
   
   ```usl
   import collections.List;
   var fruits = new List();
   collections.add(fruits, "Apple");
   ```

 Using Module Functions

Once a module is imported, you can access its functions, classes, and constants using the dot (`.`) notation.

Example: Using the `math` Module

```usl
import math;

// Using a function from the math module
var squareRoot = math.sqrt(25);
io.print("Square Root of 25: " + squareRoot); // Outputs: Square Root of 25: 5

// Using a constant from the math module
io.print("Value of PI: " + math.PI); // Outputs: Value of PI: 3.141592653589793
```

Example: Using the `collections` Module

```usl
import collections;

// Creating a new list
var colors = new collections.List();
collections.add(colors, "Red");
collections.add(colors, "Green");
collections.add(colors, "Blue");

// Iterating over the list
collections.forEach(colors, function(color) {
    io.print("Color: " + color);
});
/*
Outputs:
Color: Red
Color: Green
Color: Blue
*/
```

Example: Using the `datetime` Module

```usl
import datetime;

// Getting the current date and time
var now = datetime.now();
io.print("Current Date and Time: " + datetime.format(now, "YYYY-MM-DD HH:MM:SS"));

// Adding days to the current date
var future = datetime.addDays(now, 7);
io.print("Date after 7 days: " + datetime.format(future, "YYYY-MM-DD"));
```

Example: Using the `system` Module

```usl
import system;

// Getting an environment variable
var path = system.getEnv("PATH");
io.print("System PATH: " + path);

// Executing a system command
var output = system.exec("echo Hello from the system!");
io.print(output); // Outputs: Hello from the system!
```

---

 Advanced Features

 Custom Modules

USL allows developers to create their own custom modules to encapsulate and reuse code across different projects.

Creating a Custom Module

1. Create a New Module File

   Create a new `.usl` file, for example, `math_utils.usl`.

2. Define Functions and Classes

   ```usl
   // math_utils.usl
   // A custom module for additional mathematical functions.
   
   export function factorial(n) {
       if (n <= 1) {
           return 1;
       }
       return n * factorial(n - 1);
   }
   
   export function isPrime(num) {
       if (num <= 1) {
           return false;
       }
       for (var i = 2; i <= math.sqrt(num); i++) {
           if (num % i == 0) {
               return false;
           }
       }
       return true;
   }
   ```

3. Import and Use the Custom Module

   ```usl
   import math_utils;
   import math;
   
   var number = 5;
   var fact = math_utils.factorial(number);
   io.print("Factorial of " + number + " is " + fact); // Outputs: Factorial of 5 is 120
   
   var primeCheck = math_utils.isPrime(7);
   io.print("Is 7 prime? " + primeCheck); // Outputs: Is 7 prime? true
   ```

 Extending the Standard Library

Developers can extend the USL Standard Library by adding new modules or enhancing existing ones. This is particularly useful for adding domain-specific functionalities or integrating with external systems.

Steps to Extend the Standard Library

1. Identify the Functionality Needed

   Determine what additional functions or modules are required for your application.

2. Create a New Module

   Similar to creating a custom module, create a new `.usl` file with the desired functions.

3. Define and Export Functions

   ```usl
   // network_utils.usl
   // A custom module for network-related functions.
   
   export function ping(host) {
       var result = system.exec("ping -c 1 " + host);
       return result.contains("1 packets transmitted");
   }
   
   export function getIPAddress() {
       var ip = system.exec("hostname -I");
       return string.trim(ip);
   }
   ```

4. Import and Use the Extended Module

   ```usl
   import network_utils;
   
   var host = "google.com";
   var isReachable = network_utils.ping(host);
   io.print(host + " is reachable: " + isReachable); // Outputs: google.com is reachable: true
   
   var ipAddress = network_utils.getIPAddress();
   io.print("Your IP Address: " + ipAddress);
   ```

---

 Examples

Below are some practical examples demonstrating how to use various modules and functions from the USL Standard Library to build useful applications.

 Example 1: File Reader

```usl
// file_reader.usl
// Reads and displays the contents of a file.

import io;

function main() {
    io.print("Enter the path to the file:");
    var filePath = io.read();
    
    try {
        var content = io.readFile(filePath);
        io.print("File Contents:\n" + content);
    } catch (FileNotFoundError e) {
        io.print("Error: " + e.message);
    }
}

main();
```

 Example 2: Basic Calculator

```usl
// basic_calculator.usl
// Performs basic arithmetic operations based on user input.

import io;
import math;

function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b == 0) {
        throw new DivideByZeroError("Cannot divide by zero.");
    }
    return a / b;
}

function main() {
    io.print("Enter first number:");
    var num1 = parseFloat(io.read());
    
    io.print("Enter an operator (+, -, *, /):");
    var operator = io.read();
    
    io.print("Enter second number:");
    var num2 = parseFloat(io.read());
    
    var result;
    
    try {
        if (operator == "+") {
            result = add(num1, num2);
        } else if (operator == "-") {
            result = subtract(num1, num2);
        } else if (operator == "*") {
            result = multiply(num1, num2);
        } else if (operator == "/") {
            result = divide(num1, num2);
        } else {
            io.print("Invalid operator.");
            return;
        }
        io.print("Result: " + result);
    } catch (DivideByZeroError e) {
        io.print("Error: " + e.message);
    }
}

main();
```

 Example 3: Simple Web Server

```usl
// simple_web_server.usl
// A basic web server that responds with a welcome message.

import net;
import threading;
import io;

function handleClient(client) {
    var request = client.read();
    io.print("Received request:\n" + request);
    
    var response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nWelcome to USL Web Server!";
    client.write(response);
    client.close();
}

function main() {
    var server = net.createServer(8080);
    io.print("USL Web Server is running on port 8080");
    
    while (true) {
        var client = server.accept();
        var thread = new Thread(() => handleClient(client));
        thread.start();
    }
}

main();
```

---

 Best Practices

Adhering to best practices ensures that your USL code is efficient, readable, and maintainable. Below are some recommended practices for working with the USL Standard Library.

 1. Consistent Naming Conventions

- Variables and Functions: Use `camelCase` for naming.
  ```usl
  var userName = "Alice";
  function calculateTotal(price, tax) { /* ... */ }
  ```

- Classes and Interfaces: Use `PascalCase` for naming.
  ```usl
  class UserAccount { /* ... */ }
  interface Drivable { /* ... */ }
  ```

- Constants: Use `UPPER_SNAKE_CASE` for naming.
  ```usl
  const MAX_USERS = 100;
  ```

 2. Code Formatting

- Indentation: Use 4 spaces for indentation to enhance readability.
- Line Length: Keep lines within 80-120 characters to avoid horizontal scrolling.
- Spacing: Add spaces around operators and after commas.
  ```usl
  var total = price + tax;
  function add(a, b) { /* ... */ }
  ```

 3. Modular Programming

- Encapsulation: Group related functions and classes into modules.
- Reusability: Avoid duplicating code by utilizing modules and functions.
- Separation of Concerns: Each module should handle a specific aspect of the application.

 4. Error Handling

- Graceful Degradation: Use `try-catch-finally` blocks to handle potential errors without crashing the program.
- Informative Messages: Provide clear and descriptive error messages to aid in debugging.
- Resource Cleanup: Use `finally` blocks to ensure resources are released properly.

 5. Documentation and Comments

- Inline Comments: Explain complex logic or important steps within the code.
  ```usl
  // Calculate the factorial of a number recursively
  function factorial(n) { /* ... */ }
  ```

- Function Documentation: Describe the purpose, parameters, and return values of functions.
  ```usl
  /*
    Function: add
    Description: Adds two numbers and returns the sum.
    Parameters:
      a (int): The first number.
      b (int): The second number.
    Returns:
      int: The sum of a and b.
  */
  function add(a, b) {
      return a + b;
  }
  ```

- Module Documentation: Provide an overview of what each module does and how to use its functions.

 6. Performance Optimization

- Efficient Algorithms: Use appropriate algorithms and data structures for your tasks.
- Avoid Unnecessary Computations: Cache results of expensive operations when possible.
- Memory Management: Be mindful of memory usage, especially when handling large datasets.

 7. Security Considerations

- Input Validation: Always validate and sanitize user inputs to prevent injection attacks.
- Secure Coding Practices: Avoid using `eval` unless absolutely necessary and ensure that any dynamically generated code is safe.

---

 Appendix

 Appendix A: Standard Library Reference

Refer to the individual module sections above for detailed information on the Standard Library's functionalities.

 Appendix B: Glossary

- Variable: A storage location identified by a name that holds a value.
- Function: A reusable block of code that performs a specific task.
- Class: A blueprint for creating objects, encapsulating data and behavior.
- Object: An instance of a class containing data (fields) and behavior (methods).
- Exception: An error event that disrupts the normal flow of the program and can be handled using error handling constructs.
- Module: A file containing definitions of functions, classes, or variables that can be imported and used in other scripts.
- Thread: A sequence of executable instructions that can run concurrently with other threads.
- Interface: A contract that defines a set of methods that implementing classes must provide.
- Annotation: Metadata added to code elements like classes or functions to provide additional information or directives.

---

End of STANDARD_LIBRARY.md

---

