
---

# docs/COMMANDS.md

# USL Command Reference

This document provides a comprehensive list of all commands available in the Universal Scripting Language (USL). Each command includes its syntax, description, and practical examples to help you effectively utilize USL in your projects.

---

 Table of Contents

1. [Basic Commands](#1-basic-commands)
   - [`print`](#11-print)
   - [`read`](#12-read)
   - [`exit`](#13-exit)
2. [Variable Commands](#2-variable-commands)
   - [`var`](#21-var)
   - [`const`](#22-const)
3. [Control Flow Commands](#3-control-flow-commands)
   - [`if`, `else if`, `else`](#31-if-else-if-else)
   - [`switch`, `case`, `default`](#32-switch-case-default)
   - [`for`](#33-for)
   - [`while`](#34-while)
   - [`do...while`](#35-do-while)
   - [`break`](#36-break)
   - [`continue`](#37-continue)
4. [Function Commands](#4-function-commands)
   - [`function`](#41-function)
   - [`return`](#42-return)
5. [Class and Object Commands](#5-class-and-object-commands)
   - [`class`](#51-class)
   - [`new`](#52-new)
   - [`this`](#53-this)
   - [`extends`](#54-extends)
   - [`implements`](#55-implements)
6. [Error Handling Commands](#6-error-handling-commands)
   - [`try`, `catch`, `finally`](#61-try-catch-finally)
   - [`throw`](#62-throw)
7. [Module Commands](#7-module-commands)
   - [`import`](#71-import)
   - [`export`](#72-export)
8. [Asynchronous Programming Commands](#8-asynchronous-programming-commands)
   - [`async`](#81-async)
   - [`await`](#82-await)
9. [Miscellaneous Commands](#9-miscellaneous-commands)
   - [`typeof`](#91-typeof)
   - [`instanceof`](#92-instanceof)
   - [`super`](#93-super)
10. [Reflection Commands](#10-reflection-commands)
    - [`typeof`](#101-typeof)
    - [`instanceof`](#102-instanceof)
11. [Meta-programming Commands](#11-meta-programming-commands)
    - [`eval`](#111-eval)
    - [`generateCode`](#112-generatecode)
    - [`@Annotations`](#113-annotations)

---

 1. Basic Commands

 1.1 `print`

Syntax:

```usl
print(expression);
```

Description:

Outputs the result of the expression to the console.

Example:

```usl
// Printing a simple string
print("Hello, World!");

// Printing the result of an arithmetic operation
var sum = 5 + 3;
print("Sum: " + sum);
```

---

 1.2 `read`

Syntax:

```usl
var input = read();
```

Description:

Reads input from the user and returns it as a string.

Example:

```usl
// Prompting the user for their name and greeting them
print("Enter your name:");
var name = read();
print("Hello, " + name + "!");
```

---

 1.3 `exit`

Syntax:

```usl
exit(code);
```

Description:

Terminates the program with the given exit code. If no code is provided, the default is `0`, indicating successful termination.

Example:

```usl
// Exiting the program when an error occurs
if (errorOccurred) {
    print("An error has occurred.");
    exit(1);
}

// Exiting successfully
print("Program completed successfully.");
exit();
```

---

 2. Variable Commands

 2.1 `var`

Syntax:

```usl
var variableName = value;
```

Description:

Declares a mutable variable that can be reassigned later.

Example:

```usl
var counter = 10;
print("Initial counter: " + counter);

counter = 20;
print("Updated counter: " + counter);
```

---

 2.2 `const`

Syntax:

```usl
const CONSTANT_NAME = value;
```

Description:

Declares an immutable constant that cannot be reassigned after its initial declaration.

Example:

```usl
const PI = 3.14159;
print("Value of PI: " + PI);

// Attempting to reassign a constant will result in an error
// PI = 3.14; // This will cause an error
```

---

 3. Control Flow Commands

 3.1 `if`, `else if`, `else`

Syntax:

```usl
if (condition) {
    // Code to execute if condition is true
} else if (anotherCondition) {
    // Code to execute if anotherCondition is true
} else {
    // Code to execute if all conditions are false
}
```

Description:

Conditional statements that execute different blocks of code based on evaluated conditions.

Example:

```usl
var score = 85;

if (score >= 90) {
    print("Grade: A");
} else if (score >= 80) {
    print("Grade: B");
} else {
    print("Grade: C");
}
```

---

 3.2 `switch`, `case`, `default`

Syntax:

```usl
switch (expression) {
    case value1:
        // Code to execute for value1
        break;
    case value2:
        // Code to execute for value2
        break;
    default:
        // Code to execute if no case matches
}
```

Description:

Multi-way branching based on the value of an expression.

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

---

 3.3 `for`

Syntax:

```usl
for (initialization; condition; increment) {
    // Code to execute in each iteration
}
```

Description:

Loop that runs a block of code a specified number of times.

Example:

```usl
// Printing numbers from 1 to 5
for (var i = 1; i <= 5; i++) {
    print("Number: " + i);
}
```

---

 3.4 `while`

Syntax:

```usl
while (condition) {
    // Code to execute as long as condition is true
}
```

Description:

Loop that continues to execute a block of code as long as the specified condition remains true.

Example:

```usl
var count = 0;

while (count < 5) {
    print("Count: " + count);
    count++;
}
```

---

 3.5 `do...while`

Syntax:

```usl
do {
    // Code to execute at least once and repeatedly as long as condition is true
} while (condition);
```

Description:

Loop that executes a block of code once before checking the condition and continues to execute as long as the condition is true.

Example:

```usl
var count = 0;

do {
    print("Count: " + count);
    count++;
} while (count < 5);
```

---

 3.6 `break`

Syntax:

```usl
break;
```

Description:

Terminates the nearest enclosing loop (`for`, `while`, `do...while`) or `switch` statement immediately.

Example:

```usl
// Searching for a specific number in a list
var numbers = [1, 2, 3, 4, 5];
var target = 3;

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] == target) {
        print("Found target at index: " + i);
        break; // Exit the loop once the target is found
    }
}
```

---

 3.7 `continue`

Syntax:

```usl
continue;
```

Description:

Skips the rest of the current loop iteration and continues with the next iteration.

Example:

```usl
// Printing only odd numbers from 1 to 5
for (var i = 1; i <= 5; i++) {
    if (i % 2 == 0) {
        continue; // Skip even numbers
    }
    print("Odd Number: " + i);
}
```

---

 4. Function Commands

 4.1 `function`

Syntax:

```usl
function functionName(parameter1, parameter2) {
    // Function body
    return value;
}
```

Description:

Defines a reusable block of code that can perform a specific task. Functions can accept parameters and return values.

Example:

```usl
// Function to greet a user
function greet(name) {
    return "Hello, " + name + "!";
}

// Calling the function
var message = greet("Alice");
print(message); // Outputs: Hello, Alice!
```

---

 4.2 `return`

Syntax:

```usl
return expression;
```

Description:

Exits a function and optionally returns a value to the caller.

Example:

```usl
// Function to add two numbers
function add(a, b) {
    return a + b;
}

var sum = add(5, 7);
print("Sum: " + sum); // Outputs: Sum: 12
```

---

 5. Class and Object Commands

 5.1 `class`

Syntax:

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

Description:

Defines a blueprint for creating objects, encapsulating data (fields) and behavior (methods).

Example:

```usl
// Defining a Person class
class Person {
    var name;
    var age;

    // Constructor to initialize name and age
    function constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    // Method to display person's information
    function displayInfo() {
        print("Name: " + this.name);
        print("Age: " + this.age);
    }
}

// Creating an instance of Person
var person = new Person("Bob", 25);
person.displayInfo();
// Outputs:
// Name: Bob
// Age: 25
```

---

 5.2 `new`

Syntax:

```usl
var object = new ClassName(arguments);
```

Description:

Creates a new instance (object) of the specified class by calling its constructor with the provided arguments.

Example:

```usl
// Defining a Car class
class Car {
    var make;
    var model;

    function constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    function displayCar() {
        print("Car: " + this.make + " " + this.model);
    }
}

// Creating a new Car object
var myCar = new Car("Toyota", "Corolla");
myCar.displayCar(); // Outputs: Car: Toyota Corolla
```

---

 5.3 `this`

Description:

Refers to the current instance of the class within its methods. It is used to access the object's fields and other methods.

Example:

```usl
class Rectangle {
    var width;
    var height;

    function constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    function area() {
        return this.width * this.height;
    }

    function displayArea() {
        print("Area: " + this.area());
    }
}

var rect = new Rectangle(5, 10);
rect.displayArea(); // Outputs: Area: 50
```

---

 5.4 `extends`

Syntax:

```usl
class SubClass extends SuperClass {
    // Additional fields and methods
}
```

Description:

Enables a class to inherit properties and methods from another class (superclass), promoting code reuse and hierarchical class structures.

Example:

```usl
// Base class: Animal
class Animal {
    var name;

    function constructor(name) {
        this.name = name;
    }

    function speak() {
        print(this.name + " makes a sound.");
    }
}

// Subclass: Dog extends Animal
class Dog extends Animal {
    function constructor(name) {
        // Call the superclass constructor
        super(name);
    }

    // Override the speak method
    function speak() {
        print(this.name + " barks.");
    }
}

var dog = new Dog("Rex");
dog.speak(); // Outputs: Rex barks.
```

---

 5.5 `implements`

Syntax:

```usl
class ClassName implements InterfaceName {
    // Implementation of interface methods
}
```

Description:

Allows a class to promise to implement the methods defined by an interface, ensuring a certain contract of behavior.

Example:

```usl
// Defining an interface: Drivable
interface Drivable {
    function drive();
    function stop();
}

// Implementing the Drivable interface in Car class
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

---

 6. Error Handling Commands

 6.1 `try`, `catch`, `finally`

Syntax:

```usl
try {
    // Code that may throw an exception
} catch (ExceptionType error) {
    // Error handling code
} finally {
    // Code that runs regardless of whether an exception occurred
}
```

Description:

Handles exceptions gracefully by allowing you to attempt to execute code that may fail (`try`), catch and handle specific errors (`catch`), and execute cleanup code regardless of success or failure (`finally`).

Example:

```usl
function divide(a, b) {
    if (b == 0) {
        throw new DivideByZeroError("Divider cannot be zero.");
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
Error: Divider cannot be zero.
Division operation completed.
*/
```

---

 6.2 `throw`

Syntax:

```usl
throw new ExceptionType("Error message");
```

Description:

Raises an exception, interrupting the normal flow of the program and transferring control to the nearest `catch` block that can handle the exception.

Example:

```usl
// Defining a custom exception: InvalidAgeError
class InvalidAgeError extends Error {
    function constructor(message) {
        super(message);
    }
}

function checkAge(age) {
    if (age < 0 || age > 150) {
        throw new InvalidAgeError("Age must be between 0 and 150.");
    }
    print("Valid age: " + age);
}

function main() {
    var age = -5;

    try {
        checkAge(age);
    } catch (InvalidAgeError e) {
        print("Caught an error: " + e.message);
    }
}

main();
/*
Outputs:
Caught an error: Age must be between 0 and 150.
*/
```

---

 7. Module Commands

 7.1 `import`

Syntax:

```usl
import moduleName;
import moduleName.subModule;
```

Description:

Includes external modules or specific submodules into your current script, allowing you to use their functions, classes, and variables.

Example:

```usl
// Importing the math module
import math;

// Using the sqrt function from the math module
var number = 16;
var root = math.sqrt(number);
print("Square root of " + number + " is " + root);

// Importing a submodule from utils
import utils.stringUtils;

// Using a function from the stringUtils submodule
var original = "hello world";
var capitalized = stringUtils.capitalize(original);
print(capitalized); // Outputs: Hello world
```

---

 7.2 `export`

Syntax:

```usl
export function functionName;
export var variableName;
export class ClassName;
```

Description:

Makes functions, variables, or classes available to other modules that import them. This is essential for modular programming and code reuse.

Example:

```usl
// math_utils.usl
export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export const PI = 3.14159;
```

```usl
// main.usl
import math_utils;

var sum = math_utils.add(5, 3);
var difference = math_utils.subtract(10, 4);
print("Sum: " + sum);          // Outputs: Sum: 8
print("Difference: " + difference); // Outputs: Difference: 6
print("Value of PI: " + math_utils.PI); // Outputs: Value of PI: 3.14159
```

---

 8. Asynchronous Programming Commands

 8.1 `async`

Syntax:

```usl
async function functionName(parameters) {
    // Asynchronous function body
}
```

Description:

Declares a function as asynchronous, allowing it to perform non-blocking operations. Asynchronous functions can use the `await` keyword to wait for asynchronous operations to complete without blocking the main thread.

Example:

```usl
// Asynchronous function to fetch data from an API
async function fetchData(url) {
    var response = await http.get(url);
    return response.data;
}

function main() {
    var url = "http://example.com/api/data";
    
    // Calling the asynchronous function
    var data = await fetchData(url);
    print("Fetched Data: " + data);
}

main();
```

---

 8.2 `await`

Syntax:

```usl
var result = await asyncOperation();
```

Description:

Pauses the execution of an asynchronous function until the awaited asynchronous operation completes, then resumes execution with the result of the operation.

Example:

```usl
// Asynchronous function that returns a promise
async function delayedMessage(message, delay) {
    await sleep(delay); // Assume sleep is a built-in function that returns a promise
    return message;
}

async function main() {
    print("Waiting for the message...");
    var msg = await delayedMessage("Hello after delay!", 2000); // 2-second delay
    print(msg); // Outputs after 2 seconds: Hello after delay!
}

main();
```

---

 9. Miscellaneous Commands

 9.1 `typeof`

Syntax:

```usl
var dataType = typeof(variable);
```

Description:

Returns the data type of a given variable as a string.

Example:

```usl
var number = 42;
var text = "Hello, USL!";
var isActive = true;

print(typeof(number)); // Outputs: int
print(typeof(text));   // Outputs: string
print(typeof(isActive)); // Outputs: bool
```

---

 9.2 `instanceof`

Syntax:

```usl
if (object instanceof ClassName) {
    // Code to execute if object is an instance of ClassName
}
```

Description:

Checks if an object is an instance of a specified class or interface, returning `true` if it is, and `false` otherwise.

Example:

```usl
class Animal {
    function speak() {
        print("Animal sound.");
    }
}

class Dog extends Animal {
    function speak() {
        print("Bark!");
    }
}

var animal = new Animal();
var dog = new Dog();

if (animal instanceof Animal) {
    print("animal is an Animal.");
}

if (dog instanceof Animal) {
    print("dog is an Animal.");
}

if (dog instanceof Dog) {
    print("dog is a Dog.");
}
```

Outputs:

```
animal is an Animal.
dog is an Animal.
dog is a Dog.
```

---

 9.3 `super`

Description:

Used within a subclass to refer to its superclass. It allows access to the superclass's methods and constructors, enabling method overriding and extension.

Example:

```usl
class Vehicle {
    var make;
    var model;

    function constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    function displayInfo() {
        print("Vehicle: " + this.make + " " + this.model);
    }
}

class Car extends Vehicle {
    var doors;

    function constructor(make, model, doors) {
        // Call the superclass constructor
        super(make, model);
        this.doors = doors;
    }

    // Override the displayInfo method
    function displayInfo() {
        // Call the superclass method
        super.displayInfo();
        print("Doors: " + this.doors);
    }
}

var myCar = new Car("Tesla", "Model S", 4);
myCar.displayInfo();
/*
Outputs:
Vehicle: Tesla Model S
Doors: 4
*/
```

---

 10. Reflection Commands

 10.1 `typeof`

Note: The `typeof` command was previously described in [Miscellaneous Commands](#91-typeof). It can also be used in reflection contexts to inspect the type of objects at runtime.

Example:

```usl
class Person {
    var name;
    var age;

    function constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

var person = new Person("Alice", 30);
var typeInfo = typeof(person);
print("Type: " + typeInfo.name); // Outputs: Type: Person

var methods = typeInfo.getMethods();
print("Methods:");
for (var method in methods) {
    print("- " + method.name);
}
/*
Outputs:
Type: Person
Methods:
- constructor
- displayInfo
*/
```

 10.2 `instanceof`

Note: The `instanceof` command was previously described in [Miscellaneous Commands](#92-instanceof). It is also utilized in reflection to determine the inheritance hierarchy or interface implementation of objects at runtime.

Example:

```usl
interface Movable {
    function move();
}

class Robot implements Movable {
    function move() {
        print("Robot is moving.");
    }
}

var robot = new Robot();

if (robot instanceof Movable) {
    print("robot can move.");
}
```

Outputs:

```
robot can move.
```

---

 11. Meta-programming Commands

 11.1 `eval`

Syntax:

```usl
var result = eval("codeString");
```

Description:

Executes a string of USL code at runtime. This allows for dynamic code generation and execution but should be used cautiously to avoid security risks.

Example:

```usl
var code = "print('Executing dynamically generated code!');";
eval(code); // Outputs: Executing dynamically generated code!
```

---

 11.2 `generateCode`

Description:

Generates and returns a block of USL code as a string, which can then be executed using `eval`. This is useful for scenarios where code needs to be constructed based on runtime conditions.

Example:

```usl
// Function to generate a greeting function dynamically
function generateGreetingFunction(greeting) {
    return "function greet(name) { print('" + greeting + ", ' + name + '!'); }";
}

// Generate the greet function with a custom greeting
var code = generateGreetingFunction("Hi");
eval(code);

// Call the dynamically generated function
greet("Bob"); // Outputs: Hi, Bob!
```

---

 11.3 `@Annotations`

Description:

Annotations allow you to add metadata to classes, methods, or functions. This metadata can be used for various purposes, such as marking deprecated methods or adding documentation.

Example:

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

// Reflection to access annotations
var funcType = typeof(oldFunction);
var annotations = funcType.getAnnotations();

for (var annotation in annotations) {
    if (annotation instanceof Deprecated) {
        print("Deprecated: " + annotation.message);
    }
}
```

Outputs:

```
Deprecated: Use newFunction instead.
```

---

End of COMMANDS.md

---
