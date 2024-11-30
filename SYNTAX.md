---

 docs/SYNTAX.md

# USL Syntax Guide

 Introduction

The Universal Scripting Language (USL) is designed to provide a consistent and unified syntax that abstracts common programming constructs found in over 400 programming languages. This syntax guide serves as a comprehensive reference to help you understand and effectively use USL.

---

 Table of Contents

1. [Basic Elements](#1-basic-elements)
   - [Comments](#11-comments)
   - [Identifiers](#12-identifiers)
2. [Data Types](#2-data-types)
   - [Primitive Data Types](#21-primitive-data-types)
   - [Composite Data Types](#22-composite-data-types)
3. [Variables and Constants](#3-variables-and-constants)
   - [Variables](#31-variables)
   - [Constants](#32-constants)
4. [Operators](#4-operators)
   - [Arithmetic Operators](#41-arithmetic-operators)
   - [Comparison Operators](#42-comparison-operators)
   - [Logical Operators](#43-logical-operators)
   - [Assignment Operators](#44-assignment-operators)
5. [Control Flow](#5-control-flow)
   - [Conditional Statements](#51-conditional-statements)
   - [Switch Statement](#52-switch-statement)
   - [Loops](#53-loops)
6. [Functions](#6-functions)
   - [Function Declaration](#61-function-declaration)
   - [Function Overloading](#62-function-overloading)
   - [Anonymous Functions (Lambdas)](#63-anonymous-functions-lambdas)
7. [Classes and Objects](#7-classes-and-objects)
   - [Class Definition](#71-class-definition)
   - [Inheritance](#72-inheritance)
   - [Interfaces](#73-interfaces)
8. [Modules and Packages](#8-modules-and-packages)
   - [Importing Modules](#81-importing-modules)
   - [Exporting Modules](#82-exporting-modules)
9. [Error Handling](#9-error-handling)
   - [Try-Catch-Finally](#91-try-catch-finally)
   - [Throwing Exceptions](#92-throwing-exceptions)
10. [Generics and Templates](#10-generics-and-templates)
    - [Generic Functions](#101-generic-functions)
    - [Generic Classes](#102-generic-classes)
11. [Concurrency](#11-concurrency)
    - [Threads](#111-threads)
    - [Async/Await](#112-asyncawait)
12. [File I/O](#12-file-io)
    - [Reading Files](#121-reading-files)
    - [Writing Files](#122-writing-files)
13. [Networking](#13-networking)
    - [HTTP Requests](#131-http-requests)
    - [WebSocket](#132-websocket)
14. [Advanced Topics](#14-advanced-topics)
    - [Reflection](#141-reflection)
    - [Meta-programming](#142-meta-programming)
15. [Best Practices](#15-best-practices)
16. [Appendix A: Standard Library Reference](#16-appendix-a-standard-library-reference)
17. [Appendix B: Glossary](#17-appendix-b-glossary)

---

 1. Basic Elements

 1.1 Comments

- Single-line Comments

  Use `//` to start a single-line comment.

  ```usl
  // This is a single-line comment
  ```

- Multi-line Comments

  Use `/*` to start and `*/` to end a multi-line comment.

  ```usl
  /*
    This is a multi-line comment.
    It spans multiple lines.
  */
  ```

 1.2 Identifiers

- Naming Rules
  - Must start with a letter (a-z, A-Z) or underscore (`_`)
  - Can contain letters, digits (0-9), and underscores
  - Case-sensitive
- Examples

  ```usl
  var myVariable;
  const MAX_VALUE = 100;
  ```

---

 2. Data Types

 2.1 Primitive Data Types

- Integer (`int`)

  Whole numbers without a decimal point.

  ```usl
  int count = 42;
  ```

- Floating-point (`float`, `double`)

  Numbers with decimal points.

  ```usl
  float price = 19.99;
  double largeNumber = 1.23456789;
  ```

- Boolean (`bool`)

  Represents `true` or `false`.

  ```usl
  bool isActive = true;
  ```

- Character (`char`)

  A single Unicode character.

  ```usl
  char initial = 'A';
  ```

- String (`string`)

  A sequence of characters.

  ```usl
  string name = "John Doe";
  ```

 2.2 Composite Data Types

- Array

  Fixed-size collection of elements of the same type.

  ```usl
  int[] numbers = [1, 2, 3, 4, 5];
  ```

- List

  Dynamic collection of elements.

  ```usl
  List<string> names = ["Alice", "Bob", "Charlie"];
  ```

- Dictionary (Map)

  Collection of key-value pairs.

  ```usl
  Map<string, int> ageMap = {
      "Alice": 30,
      "Bob": 25
  };
  ```

---

 3. Variables and Constants

 3.1 Variables

- Declaration and Initialization

  Use `var` to declare a variable.

  ```usl
  var x = 10;
  var message = "Hello, World!";
  ```

- Type Inference

  USL can infer the type based on the assigned value.

  ```usl
  var count = 5;          // Inferred as int
  var price = 19.99;      // Inferred as float
  var isAvailable = true; // Inferred as bool
  ```

 3.2 Constants

- Declaration

  Use `const` to declare a constant that cannot be reassigned.

  ```usl
  const PI = 3.14159;
  const APP_NAME = "My Application";
  ```

---

 4. Operators

 4.1 Arithmetic Operators

- Addition (`+`)

  ```usl
  var sum = a + b;
  ```

- Subtraction (`-`)

  ```usl
  var difference = a - b;
  ```

- Multiplication (`*`)

  ```usl
  var product = a * b;
  ```

- Division (`/`)

  ```usl
  var quotient = a / b;
  ```

- Modulus (`%`)

  Returns the remainder of division.

  ```usl
  var remainder = a % b;
  ```

 4.2 Comparison Operators

- Equal to (`==`)

  ```usl
  if (a == b) { /* ... */ }
  ```

- Not equal to (`!=`)

  ```usl
  if (a != b) { /* ... */ }
  ```

- Greater than (`>`)

  ```usl
  if (a > b) { /* ... */ }
  ```

- Less than (`<`)

  ```usl
  if (a < b) { /* ... */ }
  ```

- Greater than or equal to (`>=`)

  ```usl
  if (a >= b) { /* ... */ }
  ```

- Less than or equal to (`<=`)

  ```usl
  if (a <= b) { /* ... */ }
  ```

 4.3 Logical Operators

- Logical AND (`&&`)

  ```usl
  if (a > 0 && b > 0) { /* ... */ }
  ```

- Logical OR (`||`)

  ```usl
  if (a > 0 || b > 0) { /* ... */ }
  ```

- Logical NOT (`!`)

  ```usl
  if (!isActive) { /* ... */ }
  ```

 4.4 Assignment Operators

- Simple Assignment (`=`)

  ```usl
  var x = 5;
  ```

- Compound Assignment

  - Addition Assignment (`+=`)

    ```usl
    x += 5; // Equivalent to x = x + 5;
    ```

  - Subtraction Assignment (`-=`)

    ```usl
    x -= 3; // Equivalent to x = x - 3;
    ```

  - Multiplication Assignment (`*=`)

    ```usl
    x *= 2; // Equivalent to x = x * 2;
    ```

  - Division Assignment (`/=`)

    ```usl
    x /= 4; // Equivalent to x = x / 4;
    ```

  - Modulus Assignment (`%=`)

    ```usl
    x %= 2; // Equivalent to x = x % 2;
    ```

---

 5. Control Flow

 5.1 Conditional Statements

- If Statement

  ```usl
  if (condition) {
      // Code to execute if condition is true
  }
  ```

  Example:

  ```usl
  if (score >= 60) {
      print("You passed!");
  }
  ```

- If-Else Statement

  ```usl
  if (condition) {
      // Code if true
  } else {
      // Code if false
  }
  ```

  Example:

  ```usl
  if (age >= 18) {
      print("You are an adult.");
  } else {
      print("You are a minor.");
  }
  ```

- Else If Ladder

  ```usl
  if (condition1) {
      // Code
  } else if (condition2) {
      // Code
  } else {
      // Code
  }
  ```

  Example:

  ```usl
  if (grade == 'A') {
      print("Excellent!");
  } else if (grade == 'B') {
      print("Good job!");
  } else {
      print("Keep trying!");
  }
  ```

 5.2 Switch Statement

Used for multi-way branching based on the value of an expression.

```usl
switch (expression) {
    case value1:
        // Code
        break;
    case value2:
        // Code
        break;
    default:
        // Code
}
```

Example:

```usl
var day = "Monday";

switch (day) {
    case "Monday":
        print("Start of the work week.");
        break;
    case "Friday":
        print("End of the work week.");
        break;
    default:
        print("Midweek days.");
}
```

 5.3 Loops

- For Loop

  Used for iterating over a range.

  ```usl
  for (var i = 0; i < n; i++) {
      // Code
  }
  ```

  Example:

  ```usl
  for (var i = 1; i <= 5; i++) {
      print("Number: " + i);
  }
  ```

- While Loop

  Repeats as long as the condition is true.

  ```usl
  while (condition) {
      // Code
  }
  ```

  Example:

  ```usl
  var count = 0;
  while (count < 5) {
      print("Count: " + count);
      count++;
  }
  ```

- Do-While Loop

  Executes the code block at least once before checking the condition.

  ```usl
  do {
      // Code
  } while (condition);
  ```

  Example:

  ```usl
  var count = 0;
  do {
      print("Count: " + count);
      count++;
  } while (count < 5);
  ```

- For-Each Loop

  Iterates over each element in a collection.

  ```usl
  for (var item in collection) {
      // Code
  }
  ```

  Example:

  ```usl
  var fruits = ["Apple", "Banana", "Cherry"];
  for (var fruit in fruits) {
      print(fruit);
  }
  ```

---

 6. Functions

 6.1 Function Declaration

Functions are blocks of reusable code.

```usl
function functionName(parameter1, parameter2) {
    // Function body
    return value;
}
```

Example:

```usl
function greet(name) {
    return "Hello, " + name + "!";
}

var message = greet("Alice");
print(message); // Outputs: Hello, Alice!
```

 6.2 Function Overloading

Defining multiple functions with the same name but different parameters.

```usl
function add(int a, int b) {
    return a + b;
}

function add(float a, float b) {
    return a + b;
}
```

 6.3 Anonymous Functions (Lambdas)

Functions without a name, often used as arguments.

```usl
var multiply = (a, b) => a * b;
print(multiply(4, 5)); // Outputs: 20
```

---

 7. Classes and Objects

 7.1 Class Definition

Classes are blueprints for creating objects.

```usl
class ClassName {
    // Fields
    var field1;
    var field2;

    // Constructor
    function constructor(parameter1, parameter2) {
        this.field1 = parameter1;
        this.field2 = parameter2;
    }

    // Methods
    function methodName() {
        // Method body
    }
}
```

Example:

```usl
class Person {
    var name;
    var age;

    function constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    function greet() {
        print("Hi, I'm " + this.name);
    }
}

var person = new Person("Bob", 25);
person.greet(); // Outputs: Hi, I'm Bob
```

 7.2 Inheritance

Classes can inherit properties and methods from other classes.

```usl
class SubClass extends BaseClass {
    // Additional fields and methods
}
```

Example:

```usl
class Employee extends Person {
    var position;

    function constructor(name, age, position) {
        super(name, age);
        this.position = position;
    }

    function work() {
        print(this.name + " is working as a " + this.position);
    }
}

var employee = new Employee("Carol", 28, "Engineer");
employee.greet(); // Outputs: Hi, I'm Carol
employee.work();  // Outputs: Carol is working as a Engineer
```

 7.3 Interfaces

Interfaces define methods that implementing classes must provide.

```usl
interface Drivable {
    function drive();
}

class Car implements Drivable {
    function drive() {
        print("The car is driving.");
    }
}
```

---

 8. Modules and Packages

 8.1 Importing Modules

Use `import` to include external modules.

```usl
import math;
import utils.stringUtils;
```

 8.2 Exporting Modules

Use `export` to make functions or variables available to other modules.

```usl
export function calculateArea(radius) {
    return PI * radius * radius;
}
```

---

 9. Error Handling

 9.1 Try-Catch-Finally

Used to handle exceptions gracefully.

```usl
try {
    // Code that may throw an exception
} catch (ExceptionType e) {
    // Error handling code
} finally {
    // Code that runs regardless of exception
}
```

Example:

```usl
try {
    var result = divide(a, b);
} catch (DivideByZeroError e) {
    print("Cannot divide by zero.");
} finally {
    print("Operation completed.");
}
```

 9.2 Throwing Exceptions

Raise an exception using `throw`.

```usl
function divide(a, b) {
    if (b == 0) {
        throw new DivideByZeroError("Divider cannot be zero.");
    }
    return a / b;
}
```

---

 10. Generics and Templates

 10.1 Generic Functions

Generic functions work with any data type.

```usl
function identity<T>(value: T): T {
    return value;
}

var num = identity<int>(5);
var text = identity<string>("Hello");
```

 10.2 Generic Classes

Classes that operate on types specified by the programmer.

```usl
class Box<T> {
    var content: T;

    function constructor(content: T) {
        this.content = content;
    }

    function getContent(): T {
        return this.content;
    }
}

var intBox = new Box<int>(123);
print(intBox.getContent()); // Outputs: 123
```

---

 11. Concurrency

 11.1 Threads

Create and manage threads for concurrent execution.

```usl
var thread = new Thread(function() {
    // Code to run in a new thread
});
thread.start();
```

Example:

```usl
function task() {
    for (var i = 0; i < 5; i++) {
        print("Task iteration: " + i);
    }
}

var worker = new Thread(task);
worker.start();
```

 11.2 Async/Await

Handle asynchronous operations.

```usl
async function fetchData(url) {
    var response = await http.get(url);
    return response.data;
}

async function main() {
    var data = await fetchData("http://example.com/api");
    print(data);
}

main();
```

---

 12. File I/O

 12.1 Reading Files

```usl
var fileContent = readFile("path/to/file.txt");
print(fileContent);
```

 12.2 Writing Files

```usl
writeFile("path/to/file.txt", "Hello, World!");
```

---

 13. Networking

 13.1 HTTP Requests

```usl
import net.http;

function main() {
    var response = http.get("http://example.com/api");
    print("Status Code: " + response.statusCode);
    print("Response Body: " + response.body);
}

main();
```

 13.2 WebSocket

```usl
import net.websocket;

function main() {
    var socket = new WebSocket("ws://example.com/socket");

    socket.onOpen = function() {
        print("Connection opened.");
        socket.send("Hello, Server!");
    };

    socket.onMessage = function(message) {
        print("Received message: " + message);
    };

    socket.onClose = function() {
        print("Connection closed.");
    };
}

main();
```

---

 14. Advanced Topics

 14.1 Reflection

Examine and modify the structure of your code at runtime.

```usl
var obj = new MyClass();
var objType = typeof(obj);

print("Class Name: " + objType.name);
var methods = objType.getMethods();

for (var method in methods) {
    print("Method: " + method.name);
}
```

 14.2 Meta-programming

Generate and manipulate code dynamically.

- Code Generation

  ```usl
  function generateAdder(n) {
      return eval("function(x) { return x + " + n + "; }");
  }

  var addFive = generateAdder(5);
  print(addFive(10)); // Outputs: 15
  ```

- Annotations

  Use annotations to add metadata.

  ```usl
  @Deprecated("Use newFunction instead.")
  function oldFunction() {
      // ...
  }
  ```

---

 15. Best Practices

- Code Formatting

  - Use consistent indentation (e.g., 4 spaces).
  - Keep line lengths reasonable (e.g., 80-120 characters).
  - Use meaningful variable and function names.

- Naming Conventions

  - Variables and functions: `camelCase`
  - Classes and interfaces: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`

- Error Handling Strategies

  - Use exceptions for error conditions.
  - Validate user input and handle invalid data gracefully.
  - Clean up resources (e.g., files, network connections) in `finally` blocks.

- Performance Optimization

  - Avoid unnecessary computations and memory allocations.
  - Use efficient algorithms and data structures.
  - Profile and benchmark critical sections of code.

---

 16. Appendix A: Standard Library Reference

Refer to the [Standard Library Documentation](STANDARD_LIBRARY.md) for detailed information on built-in modules and functions.

---

 17. Appendix B: Glossary

- Variable: A storage location identified by a name that holds a value.
- Function: A reusable block of code that performs a specific task.
- Class: A blueprint for creating objects, defining properties and methods.
- Object: An instance of a class containing data and behavior.
- Exception: An error event that can be handled using error handling constructs.
- Module: A file containing definitions of functions, classes, or variables that can be imported.
- Thread: A sequence of executable instructions that can run concurrently with other threads.

---

End of SYNTAX.md

---

