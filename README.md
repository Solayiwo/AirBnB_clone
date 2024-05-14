![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240514%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240514T215205Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=768ca85b93fc51665760d375366b26ca9f7456f01a6c824e321aaa35eac51cf9)

  

# AirBnB clone project!

  

## Project Description

This project is an implementation of a simplified clone of AirBnB. It serves as a foundational step towards building a full-stack web application, mimicking the basic functionalities of the AirBnB platform. The project is structured to develop a command interpreter in Python that manages AirBnB objects such as Users, Places, States, and Cities.

  

## Command Interpreter

  

The command interpreter is designed to manage the lifecycle of the application's data entities. This component allows for creating, retrieving, updating, and destroying objects within the application, facilitating a controlled environment for data management.

  

### How to Start the Interpreter

To start the command interpreter, navigate to the project directory in your terminal and execute:

  

```
./console.py
```

This will enter you into the interactive mode where you can begin issuing commands.

  

### Usage

  

The interpreter can operate in both interactive and non-interactive modes.

  

##### Interactive Mode:
In interactive mode, you can directly interact with the command prompt by typing commands. To get started, you can type help to see the available commands.

Example:

```
$  ./console.py
(hbnb) help

Documented  commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

##### Non-Interactive Mode:
In non-interactive mode, you can pipe commands into the interpreter from a shell command or script.

 
Example:
```
$  echo  "help" | ./console.py
(hbnb)

Documented  commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
Commands

-  `help` - Displays all available commands.

-  `quit` - Exits the command interpreter.

- More commands will be added as development progresses.

  
##### Examples

Below are examples of using the command interpreter to manage objects:

Creating a new user:

```
(hbnb) create User
```
Retrieving an object:
```
(hbnb) show User 1234-1234-1234
```
Updating an object:
```
(hbnb) update User 1234-1234-1234 email example@example.com
```
Destroying an object:
```
(hbnb) destroy User 1234-1234-1234
```

Requirements
------------

### Python Scripts

*   Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   The code uses pycodestyle (version `2.8.*`)
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All  classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### Python Unit Tests

*   All tests should be executed by using this command: `python3 -m unittest discover tests`
*   You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`