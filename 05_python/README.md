# python_for_cloud

## day_01

### Finished the codewithmosh tutorial on python for beginners from youtube

* variables
* receiving user input
* type conversion
* strings: methods(replace, find, upper)
* arithmetic operators(/, //, %, **, *, +, -, )
* operator precedence
* comparison operators(=, ==, >, <, =>, <=)
* logical operators(or, and, not)
* if statements
* while loops
* Lists
* list methods(append, insert, remove, clear, in, len)
* for loop
* range()function
* tuples

## day_02

### Python Basics

#### Dynamic Typing

Python stores the type of an object with the object. When the operation is performed, it checks whether that operation makes sense for that object. This technique is called dynamic typing.

## Data Types

### Common Data Types

* `int`: Integer numbers
* `float`: Floating-point numbers
* `boolean`: Boolean values (`True` or `False`)
* `str`: Strings (text)

### Mutable vs Immutable Data Types

* **Mutable**:
  
  * `list`
  * `set`
  * `dictionary`
  * `byte array`

* **Immutable**:
  * `tuple`
  * `strings`
  * `int`
  * `float`
  * `complex`
  * `frozen sets`

## Loops

### While Loop

`while` loops can run indefinitely, so you must include a condition for the loop to stop. Otherwise, the code creates an infinite loop. It is common to use an iterative counter with loops. As the loop completes, the counter increases (or decreases). When the counter reaches a specific number, the loop stops.

```python
counter = 0
while counter < 10:
    print(counter)
    counter += 1
```

#### Loops(for, while)

#### WHILE LOOP

* Whileloops can run indefinitely, so you must include the condition for the loop to stop. Otherwise, the code creates an infinite loop.
* It is common to use an iterative counter with loops. As the loop completes, the counter increases (or decreases). When the counter reaches a specific number, the loop stops.

#### For loops

* A forloop reads: for each element in (thing),do a certain task.•Some real-life examplesare:
For every egg in a recipe, add 2 cups of flour.

### Dictionaries

* Dictionaries contain immutable keys, which are associated to their values.
* Keys must be immutable data types.
* Dictionaries can be nested inside each other.
* To create an empty dictionary, use a pair of braces with nothing inside: {}
* Keys are separated from their values with a colon: {"Key":"Value"}
* Retrieve a value in the dictionary by its key:   myDict.get("key") or myDict["key"]
  
### dictionary_methods

* get(), update(), pop(), popitem(), clear(), keys(), values(), items()
  