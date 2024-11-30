---

# docs/TUTORIALS.md

# USL Tutorials

Welcome to the USL Tutorials! This document provides a series of tutorials designed to help you learn and master the Universal Scripting Language (USL). Whether you're a beginner just starting out, an intermediate developer looking to enhance your skills, or an advanced user aiming to leverage USL's full potential, these tutorials have something for you.

---

 Table of Contents

1. [Beginner Tutorial: Getting Started with USL](#1-beginner-tutorial-getting-started-with-usl)
    - [1.1 Introduction to USL](#11-introduction-to-usl)
    - [1.2 Setting Up Your Environment](#12-setting-up-your-environment)
    - [1.3 Writing Your First USL Script](#13-writing-your-first-usl-script)
    - [1.4 Running USL Scripts](#14-running-usl-scripts)
    - [1.5 Basic Syntax and Concepts](#15-basic-syntax-and-concepts)
    - [1.6 Summary](#16-summary)
2. [Intermediate Tutorial: Building Applications](#2-intermediate-tutorial-building-applications)
    - [2.1 Working with Functions](#21-working-with-functions)
    - [2.2 Managing Data with Collections](#22-managing-data-with-collections)
    - [2.3 Object-Oriented Programming in USL](#23-object-oriented-programming-in-usl)
    - [2.4 Error Handling and Debugging](#24-error-handling-and-debugging)
    - [2.5 File I/O Operations](#25-file-io-operations)
    - [2.6 Summary](#26-summary)
3. [Advanced Tutorial: USL for System Programming](#3-advanced-tutorial-usl-for-system-programming)
    - [3.1 Asynchronous Programming with USL](#31-asynchronous-programming-with-usl)
    - [3.2 Creating and Managing Threads](#32-creating-and-managing-threads)
    - [3.3 Building a Simple Web Server](#33-building-a-simple-web-server)
    - [3.4 Extending USL with Custom Modules](#34-extending-usl-with-custom-modules)
    - [3.5 Reflection and Meta-programming](#35-reflection-and-meta-programming)
    - [3.6 Summary](#36-summary)

---

 1. Beginner Tutorial: Getting Started with USL

 1.1 Introduction to USL

Universal Scripting Language (USL) is a powerful and versatile programming language designed to unify the syntax and features of over 400 programming languages. USL aims to provide a consistent and intuitive scripting experience, making it easier for developers to write, read, and maintain code across different platforms and use cases.

Key Features:

- Unified Syntax: Simplifies learning by providing a consistent syntax derived from multiple languages.
- Extensibility: Easily extendable through custom modules and plugins.
- Cross-Platform: Runs seamlessly on Windows, macOS, and Linux.
- Rich Standard Library: Offers a comprehensive set of built-in modules for various functionalities.

 1.2 Setting Up Your Environment

Before you can start writing and running USL scripts, you need to set up your development environment.

Prerequisites:

- Python 3.6 or Higher: USL is implemented in Python, so you need Python installed on your system.
- Git: For cloning the USL interpreter repository.

Installation Steps:

1. Install Python:
   - Download the latest version from [python.org](https://www.python.org/downloads/).
   - Follow the installation instructions for your operating system.
   - Verify the installation:
     ```bash
     python --version
     ```
     Should display `Python 3.6.x` or higher.

2. Install Git:
   - Download from [git-scm.com](https://git-scm.com/downloads).
   - Follow the installation instructions for your operating system.
   - Verify the installation:
     ```bash
     git --version
     ```
     Should display `git version x.y.z`.

3. Clone the USL Interpreter Repository:
   ```bash
   git clone https://github.com/yourusername/usl_interpreter.git
   ```
   Replace `yourusername` with your actual GitHub username.

4. Navigate to the Project Directory:
   ```bash
   cd usl_interpreter
   ```

5. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Add USL to PATH (Optional):
   - Follow the instructions in the [Installation Guide](INSTALLATION.md) to add USL to your system PATH for easy access.

 1.3 Writing Your First USL Script

Let's write a simple "Hello, World!" script to get you started.

1. Create a New File:
   - Name the file `hello_world.usl`.

2. Add the Following Code:
   ```usl
   // hello_world.usl
   // This script prints "Hello, World!" to the console.

   // Function definition for main execution.
   function main() {
       // Use the built-in print function to output text.
       print("Hello, World!");
   }

   // Call the main function to start the program.
   main();
   ```

3. Save the File.

 1.4 Running USL Scripts

To execute your USL script, use the following command:

```bash
usl run hello_world.usl
```

Expected Output:

```
Hello, World!
```

 1.5 Basic Syntax and Concepts

Understanding the basic syntax and concepts is crucial for writing effective USL scripts.

# 1.5.1 Comments

- Single-line Comments: Use `//` to start a single-line comment.
  ```usl
  // This is a single-line comment
  ```

- Multi-line Comments: Use `/*` to start and `*/` to end a multi-line comment.
  ```usl
  /*
    This is a multi-line comment.
    It spans multiple lines.
  */
  ```

# 1.5.2 Variables and Constants

- Variables: Declared using the `var` keyword and can be reassigned.
  ```usl
  var count = 10;
  count = 20; // Reassignment is allowed
  ```

- Constants: Declared using the `const` keyword and cannot be reassigned.
  ```usl
  const PI = 3.14159;
  // PI = 3.14; // This will cause an error
  ```

# 1.5.3 Data Types

USL supports various data types, including:

- Primitive Types: `int`, `float`, `bool`, `char`, `string`
- Composite Types: `List`, `Set`, `Map`, `Queue`, `Stack`

# 1.5.4 Control Flow

- Conditional Statements: `if`, `else if`, `else`, `switch`
- Loops: `for`, `while`, `do...while`, `forEach`
- Jump Statements: `break`, `continue`

# 1.5.5 Functions

Functions are declared using the `function` keyword and can accept parameters and return values.

```usl
function add(a, b) {
    return a + b;
}

var result = add(5, 3); // result is 8
```

# 1.5.6 Object-Oriented Programming

USL supports classes, inheritance, and interfaces.

```usl
class Person {
    var name;
    var age;

    function constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    function greet() {
        print("Hello, my name is " + this.name);
    }
}

var person = new Person("Alice", 30);
person.greet(); // Outputs: Hello, my name is Alice
```

 1.6 Summary

In this beginner tutorial, you've learned how to set up your USL development environment, write and run your first USL script, and understood the basic syntax and core concepts of USL. You're now ready to dive deeper into more advanced topics and build more complex applications using USL.

---

 2. Intermediate Tutorial: Building Applications

 2.1 Working with Functions

Functions are fundamental building blocks in USL, allowing you to encapsulate reusable code.

# 2.1.1 Function Declaration and Usage

Syntax:

```usl
function functionName(parameter1, parameter2) {
    // Function body
    return result;
}
```

Example:

```usl
// Function to calculate the area of a rectangle
function calculateArea(width, height) {
    return width * height;
}

var area = calculateArea(5, 10);
print("Area: " + area); // Outputs: Area: 50
```

# 2.1.2 Function Overloading

USL allows you to define multiple functions with the same name but different parameters.

Example:

```usl
// Function to add two integers
function add(a: int, b: int) {
    return a + b;
}

// Function to add two floats
function add(a: float, b: float) {
    return a + b;
}

var sumInt = add(5, 3);       // Calls add(int, int)
var sumFloat = add(5.5, 3.2); // Calls add(float, float)
```

# 2.1.3 Anonymous Functions (Lambdas)

Anonymous functions are functions without a name, often used as arguments to other functions.

Example:

```usl
// Using an anonymous function with forEach
var numbers = [1, 2, 3, 4, 5];

collections.forEach(numbers, function(number) {
    print(number * 2);
});
/*
Outputs:
2
4
6
8
10
*/
```

# 2.1.4 Higher-Order Functions

Functions that accept other functions as parameters or return them as results.

Example:

```usl
// Function that takes another function as a parameter
function applyOperation(a, b, operation) {
    return operation(a, b);
}

var sum = applyOperation(5, 3, function(a, b) {
    return a + b;
});

print("Sum: " + sum); // Outputs: Sum: 8
```

 2.2 Managing Data with Collections

USL provides a robust `collections` module for managing groups of data efficiently.

# 2.2.1 Lists

Lists are ordered, dynamic collections that can hold elements of any type.

Example:

```usl
import collections;

var fruits = new collections.List();
collections.add(fruits, "Apple");
collections.add(fruits, "Banana");
collections.add(fruits, "Cherry");

print("Fruits: " + fruits); // Outputs: Fruits: ["Apple", "Banana", "Cherry"]

// Accessing elements
var firstFruit = collections.get(fruits, 0);
print("First Fruit: " + firstFruit); // Outputs: First Fruit: Apple
```

# 2.2.2 Sets

Sets are unordered collections of unique elements.

Example:

```usl
import collections;

var uniqueNumbers = new collections.Set();
collections.add(uniqueNumbers, 1);
collections.add(uniqueNumbers, 2);
collections.add(uniqueNumbers, 2); // Duplicate, won't be added

print("Unique Numbers: " + uniqueNumbers); // Outputs: Unique Numbers: {1, 2}
```

# 2.2.3 Maps

Maps are collections of key-value pairs.

Example:

```usl
import collections;

var userAges = new collections.Map();
collections.add(userAges, "Alice", 30);
collections.add(userAges, "Bob", 25);

print("Alice's Age: " + collections.get(userAges, "Alice")); // Outputs: Alice's Age: 30
```

# 2.2.4 Queues

Queues follow the First-In-First-Out (FIFO) principle.

Example:

```usl
import collections;

var taskQueue = new collections.Queue();
collections.enqueue(taskQueue, "Task 1");
collections.enqueue(taskQueue, "Task 2");
collections.enqueue(taskQueue, "Task 3");

while (!collections.isEmpty(taskQueue)) {
    var task = collections.dequeue(taskQueue);
    print("Processing: " + task);
}
/*
Outputs:
Processing: Task 1
Processing: Task 2
Processing: Task 3
*/
```

# 2.2.5 Stacks

Stacks follow the Last-In-First-Out (LIFO) principle.

Example:

```usl
import collections;

var callStack = new collections.Stack();
collections.push(callStack, "Function A");
collections.push(callStack, "Function B");
collections.push(callStack, "Function C");

while (!collections.isEmpty(callStack)) {
    var func = collections.pop(callStack);
    print("Exiting: " + func);
}
/*
Outputs:
Exiting: Function C
Exiting: Function B
Exiting: Function A
*/
```

 2.3 Object-Oriented Programming in USL

USL supports object-oriented programming (OOP) paradigms, including classes, inheritance, and interfaces.

# 2.3.1 Classes and Objects

Defining a Class:

```usl
class Car {
    var make;
    var model;
    var year;

    function constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    function displayInfo() {
        print("Car: " + this.year + " " + this.make + " " + this.model);
    }
}

var myCar = new Car("Toyota", "Corolla", 2020);
myCar.displayInfo(); // Outputs: Car: 2020 Toyota Corolla
```

# 2.3.2 Inheritance

Inheritance allows a class to inherit properties and methods from another class.

Example:

```usl
class Vehicle {
    var make;
    var model;

    function constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    function startEngine() {
        print(this.make + " " + this.model + "'s engine started.");
    }
}

class Motorcycle extends Vehicle {
    var type;

    function constructor(make, model, type) {
        super(make, model);
        this.type = type;
    }

    function displayType() {
        print("Motorcycle Type: " + this.type);
    }
}

var bike = new Motorcycle("Harley-Davidson", "Street 750", "Cruiser");
bike.startEngine(); // Outputs: Harley-Davidson Street 750's engine started.
bike.displayType(); // Outputs: Motorcycle Type: Cruiser
```

# 2.3.3 Interfaces

Interfaces define a contract that implementing classes must adhere to.

Example:

```usl
interface Drivable {
    function drive();
    function stop();
}

class Car implements Drivable {
    var make;
    var model;

    function constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    function drive() {
        print(this.make + " " + this.model + " is driving.");
    }

    function stop() {
        print(this.make + " " + this.model + " has stopped.");
    }
}

var myCar = new Car("Honda", "Civic");
myCar.drive(); // Outputs: Honda Civic is driving.
myCar.stop();  // Outputs: Honda Civic has stopped.
```

 2.4 Error Handling and Debugging

Proper error handling is essential for building robust applications.

# 2.4.1 Try-Catch-Finally

Syntax:

```usl
try {
    // Code that may throw an exception
} catch (ExceptionType e) {
    // Error handling code
} finally {
    // Code that runs regardless of whether an exception occurred
}
```

Example:

```usl
function divide(a, b) {
    if (b == 0) {
        throw new DivideByZeroError("Cannot divide by zero.");
    }
    return a / b;
}

function main() {
    var numerator = 10;
    var denominator = 0;

    try {
        var result = divide(numerator, denominator);
        print("Result: " + result);
    } catch (DivideByZeroError e) {
        print("Error: " + e.message);
    } finally {
        print("Division operation completed.");
    }
}

main();
/*
Outputs:
Error: Cannot divide by zero.
Division operation completed.
*/
```

# 2.4.2 Debugging Techniques

- Using `print` Statements: Insert `print` statements to trace variable values and program flow.
  
  ```usl
  function factorial(n) {
      print("Calculating factorial of " + n);
      if (n <= 1) {
          return 1;
      }
      return n * factorial(n - 1);
  }

  var result = factorial(5);
  print("Factorial Result: " + result); // Outputs intermediate steps
  ```

- Handling Exceptions: Use `try-catch` blocks to gracefully handle unexpected errors.

- Logging Modules: Utilize logging modules to record events, errors, and other significant actions.

  ```usl
  import logging;

  logging.setLevel(logging.DEBUG);

  function main() {
      logging.debug("Program started.");
      // Your code here
      logging.debug("Program ended.");
  }

  main();
  ```

 2.5 File I/O Operations

Managing files is a common task in programming. USL provides the `io` module for handling file operations.

# 2.5.1 Reading Files

Example:

```usl
import io;

function main() {
    var filePath = "data.txt";

    try {
        var content = io.readFile(filePath);
        print("File Contents:\n" + content);
    } catch (FileNotFoundError e) {
        print("Error: " + e.message);
    }
}

main();
```

# 2.5.2 Writing Files

Example:

```usl
import io;

function main() {
    var filePath = "output.txt";
    var data = "This is a sample text.";

    try {
        io.writeFile(filePath, data);
        print("Data written to " + filePath);
    } catch (PermissionError e) {
        print("Error: " + e.message);
    }
}

main();
```

# 2.5.3 Appending to Files

Example:

```usl
import io;

function main() {
    var filePath = "output.txt";
    var additionalData = "\nAppended line.";

    try {
        io.appendFile(filePath, additionalData);
        print("Data appended to " + filePath);
    } catch (PermissionError e) {
        print("Error: " + e.message);
    }
}

main();
```

 2.6 Summary

In this intermediate tutorial, you've explored more advanced features of USL, including working with functions, managing data using collections, implementing object-oriented programming paradigms, handling errors gracefully, and performing file I/O operations. These skills are essential for building more complex and feature-rich applications using USL.

---

 3. Advanced Tutorial: USL for System Programming

 3.1 Asynchronous Programming with USL

Asynchronous programming allows your applications to perform non-blocking operations, improving efficiency and responsiveness.

# 3.1.1 Understanding Asynchronous Concepts

- Asynchronous Function (`async`): Declares a function that can perform asynchronous operations.
- Await Keyword (`await`): Pauses the execution of an asynchronous function until the awaited operation completes.
- Promises: Objects representing the eventual completion or failure of an asynchronous operation.

# 3.1.2 Example: Fetching Data Asynchronously

```usl
import http;
import io;

async function fetchData(url) {
    try {
        var response = await http.get(url);
        if (response.statusCode == 200) {
            return response.body;
        } else {
            throw new HttpError("Failed to fetch data. Status Code: " + response.statusCode);
        }
    } catch (HttpError e) {
        io.print("Error: " + e.message);
        return null;
    }
}

async function main() {
    var url = "https://api.example.com/data";
    var data = await fetchData(url);
    
    if (data != null) {
        io.print("Fetched Data: " + data);
    }
}

main();
```

# 3.1.3 Handling Multiple Asynchronous Operations

Example:

```usl
import http;
import io;

async function fetchUserData(userId) {
    var url = "https://api.example.com/users/" + userId;
    var response = await http.get(url);
    return response.body;
}

async function fetchPostData(postId) {
    var url = "https://api.example.com/posts/" + postId;
    var response = await http.get(url);
    return response.body;
}

async function main() {
    var userPromise = fetchUserData(1);
    var postPromise = fetchPostData(101);

    var user = await userPromise;
    var post = await postPromise;

    io.print("User Data: " + user);
    io.print("Post Data: " + post);
}

main();
```

 3.2 Creating and Managing Threads

Threads allow your application to perform multiple operations concurrently.

# 3.2.1 Creating a New Thread

Example:

```usl
import threading;
import io;

function backgroundTask() {
    for (var i = 1; i <= 5; i++) {
        io.print("Background Task Iteration: " + i);
        sleep(1); // Pause for 1 second
    }
}

function main() {
    var thread = new Thread(backgroundTask);
    thread.start();

    // Main thread continues executing
    for (var i = 1; i <= 3; i++) {
        io.print("Main Thread Iteration: " + i);
        sleep(2); // Pause for 2 seconds
    }

    thread.join(); // Wait for the background thread to finish
    io.print("All tasks completed.");
}

main();
/*
Possible Output:
Background Task Iteration: 1
Main Thread Iteration: 1
Background Task Iteration: 2
Main Thread Iteration: 2
Background Task Iteration: 3
Main Thread Iteration: 3
Background Task Iteration: 4
Background Task Iteration: 5
All tasks completed.
*/
```

# 3.2.2 Synchronizing Threads

To prevent race conditions and ensure thread-safe operations, use synchronization primitives like mutexes.

Example:

```usl
import threading;
import io;

var counter = 0;
var mutex = new Mutex();

function incrementCounter() {
    for (var i = 0; i < 1000; i++) {
        mutex.lock();
        counter += 1;
        mutex.unlock();
    }
}

function main() {
    var thread1 = new Thread(incrementCounter);
    var thread2 = new Thread(incrementCounter);

    thread1.start();
    thread2.start();

    thread1.join();
    thread2.join();

    io.print("Final Counter Value: " + counter); // Expected: 2000
}

main();
```

 3.3 Building a Simple Web Server

Creating a web server demonstrates USL's capability in system programming and network operations.

Example:

```usl
import net;
import threading;
import io;

function handleClient(client) {
    var request = client.read();
    io.print("Received request:\n" + request);

    var response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nWelcome to the USL Web Server!";
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

Testing the Web Server:

1. Run the Server:
   ```bash
   usl run simple_web_server.usl
   ```
   Output:
   ```
   USL Web Server is running on port 8080
   ```

2. Access the Server via Browser or cURL:
   ```bash
   curl http://localhost:8080
   ```
   Output:
   ```
   Welcome to the USL Web Server!
   ```

 3.4 Extending USL with Custom Modules

USL allows you to create custom modules to encapsulate and reuse code across different projects.

# 3.4.1 Creating a Custom Module

1. Create a New File:
   - Name the file `math_utils.usl`.

2. Add Functions to the Module:
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

3. Import and Use the Custom Module:
   ```usl
   import math_utils;
   import math;
   import io;

   function main() {
       var number = 5;
       var fact = math_utils.factorial(number);
       io.print("Factorial of " + number + " is " + fact); // Outputs: Factorial of 5 is 120

       var primeCheck = math_utils.isPrime(7);
       io.print("Is 7 prime? " + primeCheck); // Outputs: Is 7 prime? true
   }

   main();
   ```

# 3.4.2 Packaging Custom Modules

For larger projects, it's beneficial to organize custom modules into packages.

Example:

1. Create a Package Directory:
   - Directory structure:
     ```
     my_package/
     ├── __init__.usl
     ├── math_utils.usl
     └── string_utils.usl
     ```

2. Initialize the Package:
   ```usl
   // my_package/__init__.usl
   export * from 'math_utils';
   export * from 'string_utils';
   ```

3. Add Functions to Submodules:
   ```usl
   // my_package/math_utils.usl
   export function square(n) {
       return n * n;
   }
   ```

   ```usl
   // my_package/string_utils.usl
   export function capitalize(str) {
       if (string.length(str) == 0) {
           return str;
       }
       return string.toUpperCase(string.substring(str, 0, 1)) + string.substring(str, 1);
   }
   ```

4. Import and Use the Package:
   ```usl
   import my_package;
   import io;

   function main() {
       var num = 4;
       var squared = my_package.square(num);
       io.print("Square of " + num + " is " + squared); // Outputs: Square of 4 is 16

       var text = "hello";
       var capitalized = my_package.capitalize(text);
       io.print("Capitalized Text: " + capitalized); // Outputs: Capitalized Text: Hello
   }

   main();
   ```

 3.5 Reflection and Meta-programming

Reflection allows your program to inspect and modify its own structure and behavior at runtime. Meta-programming involves writing programs that can generate or manipulate other programs or themselves.

# 3.5.1 Using Reflection

Example: Inspecting Class Methods:

```usl
import io;

class Calculator {
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
        return a / b;
    }
}

function main() {
    var calc = new Calculator();
    var calcType = typeof(calc);

    io.print("Class Name: " + calcType.name); // Outputs: Class Name: Calculator

    var methods = calcType.getMethods();
    io.print("Methods:");
    for (var method in methods) {
        io.print("- " + method.name);
    }
    /*
    Outputs:
    Methods:
    - add
    - subtract
    - multiply
    - divide
    */
}

main();
```

# 3.5.2 Meta-programming with `eval`

Example: Dynamically Generating and Executing Code:

```usl
import io;

function generateGreeting(greeting) {
    return "function greet(name) { print('" + greeting + ", ' + name + '!'); }";
}

function main() {
    var code = generateGreeting("Hi");
    eval(code); // Dynamically defines the greet function

    greet("Alice"); // Outputs: Hi, Alice!
}

main();
```

# 3.5.3 Using Annotations

Annotations allow you to add metadata to classes, methods, or functions.

Example: Marking Deprecated Functions

```usl
// Define a custom annotation: @Deprecated
annotation Deprecated(message) {
    var message;

    function constructor(message) {
        this.message = message;
    }
}

// Using the @Deprecated annotation
@Deprecated("Use newFunction instead.")
function oldFunction() {
    print("This function is deprecated.");
}

function newFunction() {
    print("This is the new function.");
}

function main() {
    var funcType = typeof(oldFunction);
    var annotations = funcType.getAnnotations();

    for (var annotation in annotations) {
        if (annotation instanceof Deprecated) {
            print("Deprecated: " + annotation.message);
        }
    }

    oldFunction(); // Outputs: This function is deprecated.
}

main();
/*
Outputs:
Deprecated: Use newFunction instead.
This function is deprecated.
*/
```

 3.6 Summary

In this advanced tutorial, you've delved into the more sophisticated aspects of USL, including asynchronous programming, multithreading, building a web server, extending USL with custom modules, and utilizing reflection and meta-programming techniques. These skills empower you to build complex, efficient, and dynamic applications using USL.

---
