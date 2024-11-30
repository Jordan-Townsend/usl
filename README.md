---

# Universal Scripting Language (USL) Interpreter

The Universal Scripting Language (USL) is an innovative programming language designed to unify the syntax and features of (at this moment) 466 programming languages. 
This repository contains a USL interpreter implemented in Python, allowing you to run USL scripts on your system.

---

 Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running USL Scripts](#running-usl-scripts)
  - [Examples](#examples)
- [USL Language Overview](#usl-language-overview)
  - [Syntax](#syntax)
  - [Data Types](#data-types)
  - [Variables and Constants](#variables-and-constants)
  - [Operators](#operators)
  - [Control Flow](#control-flow)
  - [Functions](#functions)
  - [Classes and Objects](#classes-and-objects)
  - [Inheritance](#inheritance)
  - [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- [Additional Resources](#additional-resources)

---

 Features

- Multi-language Integration: USL abstracts common features from hundreds of programming languages.
- Object-Oriented Programming: Supports classes, inheritance, and polymorphism.
- Functional Programming: Includes first-class functions and higher-order functions.
- Extensible Interpreter: Implemented in Python for easy extension and modification.
- Error Handling: Supports try-catch-finally blocks for robust error management.
- Standard Library: Includes built-in functions for math, I/O, and more.

---

 Getting Started

 Prerequisites

- Python 3.6 or higher: Ensure Python is installed on your system.
  - Download from [python.org](https://www.python.org/downloads/).
- Git: For cloning the repository.
  - Download from [git-scm.com](https://git-scm.com/downloads).

 Installation

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/usl_interpreter.git
   ```

2. Navigate to the Project Directory

   ```bash
   cd usl_interpreter
   ```

3. Install Dependencies

   Install any required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not provided, all dependencies are included in the standard Python library.*

---

 Usage

 Running USL Scripts

To run a USL script, use the `main.py` file followed by the path to your `.usl` script:

```bash
python main.py path/to/your_script.usl
```

Example:

```bash
python main.py examples/hello_world.usl
```

 Examples

The `examples/` directory contains sample USL scripts demonstrating various features:

- `hello_world.usl`: Basic "Hello, World!" program.
- `calculator.usl`: Simple calculator using functions.
- `classes.usl`: Demonstrates classes and inheritance.
- `fibonacci.usl`: Calculates Fibonacci numbers using recursion.

To run an example:

```bash
python main.py examples/hello_world.usl
```

---

 USL Language Overview

 Syntax

USL's syntax is designed to be familiar to users of popular programming languages like Python, JavaScript, Java, and C++.

Hello World Example:

```usl
function main() {
    print("Hello, World!");
}

main();
```

 Data Types

- Numbers: Integer and floating-point numbers.
- Strings: Enclosed in double (`"`) or single (`'`) quotes.
- Booleans: `true` or `false`.
- None: Represents the absence of a value, similar to `null` or `None`.

 Variables and Constants

Variables:

```usl
var age = 30;
var name = "Alice";
```

Constants:

```usl
const PI = 3.14159;
```

 Operators

Arithmetic Operators:

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Modulus: `%`

Comparison Operators:

- Equal to: `==`
- Not equal to: `!=`
- Greater than: `>`
- Less than: `<`
- Greater than or equal to: `>=`
- Less than or equal to: `<=`

Logical Operators:

- Logical AND: `&&`
- Logical OR: `||`
- Logical NOT: `!`

 Control Flow

If-Else Statements:

```usl
if (age >= 18) {
    print("You are an adult.");
} else {
    print("You are a minor.");
}
```

Else If Ladder:

```usl
if (score >= 90) {
    print("Grade: A");
} else if (score >= 80) {
    print("Grade: B");
} else if (score >= 70) {
    print("Grade: C");
} else {
    print("Grade: D");
}
```

Switch Statements:

```usl
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

Loops:

- For Loop:

  ```usl
  for (var i = 0; i < 5; i++) {
      print("Iteration: " + i);
  }
  ```

- While Loop:

  ```usl
  var count = 0;
  while (count < 5) {
      print("Count: " + count);
      count++;
  }
  ```

- Do-While Loop:

  ```usl
  var count = 0;
  do {
      print("Count: " + count);
      count++;
  } while (count < 5);
  ```

 Functions

Function Definition and Calling:

```usl
function add(a, b) {
    return a + b;
}

var result = add(5, 3);
print("Result: " + result);
```

Recursive Functions:

```usl
function factorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

print("Factorial of 5 is " + factorial(5));
```

Anonymous Functions (Lambdas):

```usl
var square = (x) => x * x;
print("Square of 4 is " + square(4)); // Outputs: 16
```

 Classes and Objects

Class Definition:

```usl
class Person {
    var name;
    var age;

    def __init__(self, name, age) {
        self.name = name;
        self.age = age;
    }

    def greet(self) {
        print("Hello, my name is " + self.name);
    }
}
```

Object Instantiation:

```usl
var person = new Person("Alice", 30);
person.greet(); // Outputs: Hello, my name is Alice
```

 Inheritance

Subclass Definition:

```usl
class Employee extends Person {
    var position;

    def __init__(self, name, age, position) {
        super.__init__(name, age);
        self.position = position;
    }

    def work(self) {
        print(self.name + " is working as a " + self.position);
    }
}
```

Using the Subclass:

```usl
var employee = new Employee("Bob", 28, "Engineer");
employee.greet(); // Outputs: Hello, my name is Bob
employee.work();  // Outputs: Bob is working as a Engineer
```

 Error Handling

Try-Catch-Finally Blocks:

```usl
try {
    var result = divide(a, b);
    print("Result: " + result);
} catch (DivideByZeroError e) {
    print("Error: Cannot divide by zero.");
} finally {
    print("Operation completed.");
}
```

Throwing Exceptions:

```usl
function divide(a, b) {
    if (b == 0) {
        throw new DivideByZeroError("Divider cannot be zero.");
    }
    return a / b;
}
```

---

 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

Ways to Contribute:

- Report Bugs: Use the issue tracker to report bugs or suggest enhancements.
- Submit Pull Requests: Fork the repository and submit pull requests for improvements.
- Improve Documentation: Help us improve and expand the documentation.
- Write Tests: Enhance test coverage to ensure code reliability.

---

 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

 Acknowledgements

- OpenAI's GPT-4: For providing assistance in refining the interpreter.
- Community Contributors: Thanks to everyone who has contributed to the development and testing of USL.

---

 Contact

- Author: [Jordan Townsend](https://github.com/Jordan-Townsend)
- Email: jordan@townsendsdesigns.com
- GitHub Repository: [github.com/Jordan-Townsend/usl]([(https://github.com/Jordan-Townsend/usl))

---

Happy Coding with USL!

---

 Sample Code Snippets

Factorial Function Example:

```usl
function factorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

var number = 5;
print("Factorial of " + number + " is " + factorial(number));
```

Output:

```
Factorial of 5 is 120
```

Fibonacci Sequence Example:

```usl
function fibonacci(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

for (var i = 0; i < 10; i++) {
    print("Fibonacci(" + i + ") = " + fibonacci(i));
}
```

---

 Project Structure

```
usl_interpreter/
├── main.py
├── interpreter.py
├── parser.py
├── lexer.py
├── ast_nodes.py
├── environment.py
├── usl_builtins.py
├── examples/
│   ├── hello_world.usl
│   ├── calculator.usl
│   ├── classes.usl
│   ├── fibonacci.usl
│   └── inheritance.usl
├── docs/
│   ├── SYNTAX.md
│   ├── LANGUAGES.md
│   ├── EXAMPLES.md
│   └── CONTRIBUTING.md
├── tests/
│   └── test_interpreter.py
├── README.md
├── LICENSE
└── .gitignore
```

---

 Setting Up a Development Environment

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/usl_interpreter.git
   ```

2. Create a Virtual Environment

   ```bash
   python -m venv venv
   ```

3. Activate the Virtual Environment

   - Windows:

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install Development Dependencies

   ```bash
   pip install -r dev-requirements.txt
   ```

5. Run Tests

   ```bash
   python -m unittest discover tests
   ```

---

 Testing

Unit tests are located in the `tests/` directory. To run the tests:

```bash
python -m unittest discover tests
```

---

 Extending the Interpreter

The interpreter is designed with extensibility in mind. You can add new features or modify existing ones by:

- Adding New AST Nodes: Define new nodes in `ast_nodes.py`.
- Extending the Lexer/Parser: Modify `lexer.py` and `parser.py` to recognize new syntax.
- Implementing Built-in Functions: Add functions to `usl_builtins.py`.
- Enhancing the Interpreter: Update `interpreter.py` to handle new nodes or behaviors.

Example: Adding a New Built-in Function

To add a new built-in function `sqrt`, which calculates the square root of a number:

1. Update `usl_builtins.py`:

   ```python
   def sqrt(x):
       return x  0.5

   built_in_functions = {
       'print': print_function,
       'sqrt': sqrt,
       # ... other built-in functions
   }
   ```

2. Use in a USL Script:

   ```usl
   var number = 16;
   var result = sqrt(number);
   print("Square root of " + number + " is " + result);
   ```

---

 Known Issues

- Limited Standard Library: Currently, the standard library is minimal. Contributions to expand it are welcome.
- Error Handling: Error messages can be improved for clarity and helpfulness.
- Performance: The interpreter may not be optimized for performance-critical applications.

---

 Development Roadmap

- Upcoming Features:
  - Implement standard library functions.
  - Add support for asynchronous programming.
  - Enhance error reporting and debugging tools.
- Long-Term Goals:
  - Create a USL package manager.
  - Develop an Integrated Development Environment (IDE) with syntax highlighting and code completion.
  - Expand compatibility with additional programming languages.

---

 Feedback

Your feedback is valuable to us! Please take a moment to share your thoughts on:

- Features you'd like to see
- Bugs you've encountered
- General suggestions to improve USL

You can open an issue or contact the maintainer directly.

---

*This README provides comprehensive information about the USL interpreter project. If you find any inaccuracies or omissions, please feel free to submit a pull request or open an issue.*

---

# Thank You for Using USL!
