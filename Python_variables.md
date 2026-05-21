# 🐍 Python Fundamentals — Complete Beginner Guide

> **Author**: Learning Notes  
> **Python Version**: 3.x  
> **Last Updated**: May 2026

---

## Table of Contents

1. [Data Types & Properties](#1-data-types--properties)
2. [Operators](#2-operators)
3. [Control Flow Statements](#3-control-flow-statements)
4. [Loops](#4-loops)
5. [Strings](#5-strings)
6. [Lists](#6-lists)
7. [Tuples](#7-tuples)
8. [Sets](#8-sets)
9. [Dictionaries](#9-dictionaries)
10. [Functions](#10-functions)

---

## 1. Data Types & Properties

Python is **dynamically typed** — you don't need to declare the type of a variable; it is inferred at runtime.

### 1.1 Numeric Types

| Type | Description | Example | Mutable? |
|------|-------------|---------|----------|
| `int` | Whole numbers (unlimited precision) | `x = 10` | ❌ Immutable |
| `float` | Decimal numbers (64-bit double) | `y = 3.14` | ❌ Immutable |
| `complex` | Complex numbers (real + imaginary) | `z = 2 + 3j` | ❌ Immutable |

```python
# Integer
age = 25
print(type(age))       # <class 'int'>

# Float
pi = 3.14159
print(type(pi))        # <class 'float'>

# Complex
c = 4 + 5j
print(c.real)          # 4.0
print(c.imag)          # 5.0
print(type(c))         # <class 'complex'>
```

**Key Properties of Numeric Types:**
- `int` has **unlimited precision** (no overflow like in Java/C).
- `float` follows **IEEE 754** double-precision (64-bit).
- You can convert between types: `int()`, `float()`, `complex()`.

```python
# Type Conversion
print(int(3.9))        # 3  (truncates, does NOT round)
print(float(5))        # 5.0
print(complex(2, 3))   # (2+3j)
```

---

### 1.2 Boolean Type

| Type | Description | Values | Mutable? |
|------|-------------|--------|----------|
| `bool` | Boolean (subclass of `int`) | `True` / `False` | ❌ Immutable |

```python
is_active = True
print(type(is_active))   # <class 'bool'>

# bool is a subclass of int
print(True + True)       # 2
print(False + 10)        # 10
print(isinstance(True, int))  # True
```

**Falsy Values in Python** (evaluate to `False`):
- `False`, `None`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}`, `set()` (empty collections)

Everything else is **Truthy**.

```python
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool("hello"))  # True
print(bool(42))       # True
```

---

### 1.3 String Type

| Type | Description | Example | Mutable? |
|------|-------------|---------|----------|
| `str` | Sequence of Unicode characters | `s = "hello"` | ❌ Immutable |

```python
name = "Python"
print(type(name))     # <class 'str'>
print(len(name))      # 6

# Strings are immutable
# name[0] = 'J'  ❌ TypeError!
```

> 📝 Detailed string methods are covered in [Section 5](#5-strings).

---

### 1.4 Sequence Types

| Type | Description | Ordered? | Mutable? | Duplicates? |
|------|-------------|----------|----------|-------------|
| `list` | Dynamic array | ✅ Yes | ✅ Mutable | ✅ Allowed |
| `tuple` | Fixed-size sequence | ✅ Yes | ❌ Immutable | ✅ Allowed |
| `range` | Sequence of numbers | ✅ Yes | ❌ Immutable | ❌ No |

```python
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.5, 20.3)

# Range
numbers = range(1, 11)     # 1 to 10
print(list(numbers))       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### 1.5 Set Types

| Type | Description | Ordered? | Mutable? | Duplicates? |
|------|-------------|----------|----------|-------------|
| `set` | Unordered collection of unique items | ❌ No | ✅ Mutable | ❌ No |
| `frozenset` | Immutable version of set | ❌ No | ❌ Immutable | ❌ No |

```python
unique = {1, 2, 3, 3, 4}
print(unique)              # {1, 2, 3, 4}

frozen = frozenset([1, 2, 3])
# frozen.add(4)  ❌ Error! frozenset is immutable
```

---

### 1.6 Mapping Type

| Type | Description | Ordered? | Mutable? | Duplicates? |
|------|-------------|----------|----------|-------------|
| `dict` | Key-value pairs | ✅ Yes (insertion order from 3.7+) | ✅ Mutable | Keys: ❌ / Values: ✅ |

```python
student = {"name": "Krish", "age": 22, "grade": "A"}
print(student["name"])     # Krish
```

---

### 1.7 None Type

| Type | Description | Value |
|------|-------------|-------|
| `NoneType` | Represents absence of a value | `None` |

```python
result = None
print(type(result))        # <class 'NoneType'>
print(result is None)      # True
```

---

### 1.8 Binary Types

| Type | Description | Mutable? |
|------|-------------|----------|
| `bytes` | Immutable sequence of bytes | ❌ Immutable |
| `bytearray` | Mutable sequence of bytes | ✅ Mutable |
| `memoryview` | Memory view of binary data | — |

```python
b = b"hello"
print(type(b))              # <class 'bytes'>

ba = bytearray(b"hello")
ba[0] = 72                  # ASCII for 'H'
print(ba)                   # bytearray(b'Hello')
```

---

### 1.9 Checking & Converting Types

```python
# type() — returns the type
print(type(42))             # <class 'int'>
print(type("hi"))           # <class 'str'>

# isinstance() — checks if object is of a given type
print(isinstance(42, int))          # True
print(isinstance("hi", (int, str))) # True (checks multiple types)

# Common Type Conversions
int("123")       # 123
str(456)         # "456"
float("3.14")    # 3.14
list("abc")      # ['a', 'b', 'c']
tuple([1, 2])    # (1, 2)
set([1, 1, 2])   # {1, 2}
bool(0)          # False
```

---

## 2. Operators

### 2.1 Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (float) | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus (remainder) | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

```python
print(10 / 3)      # 3.3333...  (always returns float)
print(10 // 3)     # 3          (truncates toward negative infinity)
print(-10 // 3)    # -4         (floor, not truncate!)
print(10 % 3)      # 1
print(2 ** 10)     # 1024
```

---

### 2.2 Comparison (Relational) Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

```python
print(10 == 10.0)    # True  (compares values, not types)
print("abc" < "abd") # True  (lexicographic comparison)
print([1,2] == [1,2])# True  (element-wise comparison)

# Chained comparisons (Python special!)
x = 5
print(1 < x < 10)       # True  (equivalent to: 1 < x and x < 10)
print(1 < x < 3)        # False
```

---

### 2.3 Assignment Operators

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `x = 5` | Assign 5 to x |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `\|=` | `x \|= 3` | `x = x \| 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 2` | `x = x >> 2` |
| `<<=` | `x <<= 2` | `x = x << 2` |
| `:=` | `y := 10` | Walrus operator (assign + use in expression) |

```python
x = 10
x += 5       # x = 15
x **= 2      # x = 225

# Walrus Operator (:=) — Python 3.8+
# Assigns a value AND returns it in one step
if (n := len("hello")) > 3:
    print(f"Length is {n}")   # Length is 5
```

---

### 2.4 Logical Operators

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns `True` if BOTH are true | `True and False` | `False` |
| `or` | Returns `True` if AT LEAST ONE is true | `True or False` | `True` |
| `not` | Reverses the boolean value | `not True` | `False` |

```python
# Short-circuit evaluation
print(True and "hello")    # "hello"  (returns last evaluated value)
print(False and "hello")   # False    (short-circuits, doesn't evaluate "hello")
print(True or "hello")     # True     (short-circuits)
print(False or "hello")    # "hello"

# Practical use
name = input_name or "Anonymous"   # Default value pattern
```

---

### 2.5 Identity Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Returns `True` if both refer to the **same object in memory** | `x is y` |
| `is not` | Returns `True` if they are **different objects** | `x is not y` |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True   (same values)
print(a is b)       # False  (different objects in memory)
print(a is c)       # True   (same object)

# Always use 'is' to compare with None
x = None
print(x is None)    # True ✅
print(x == None)    # True, but not recommended ⚠️
```

---

### 2.6 Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Returns `True` if value is found in sequence | `"a" in "apple"` → `True` |
| `not in` | Returns `True` if value is NOT found | `"z" not in "apple"` → `True` |

```python
# Works with strings, lists, tuples, sets, dicts
print("py" in "python")         # True
print(3 in [1, 2, 3, 4])       # True
print("name" in {"name": "K"}) # True (checks keys in dict)
print(5 not in (1, 2, 3))      # True
```

---

### 2.7 Bitwise Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT (complement) | `~5` | `-6` |
| `<<` | Left Shift | `5 << 1` | `10` |
| `>>` | Right Shift | `5 >> 1` | `2` |

```python
# Binary representations:
# 5 = 0101
# 3 = 0011

print(5 & 3)     # 1   (0001)  — bits that are 1 in BOTH
print(5 | 3)     # 7   (0111)  — bits that are 1 in EITHER
print(5 ^ 3)     # 6   (0110)  — bits that are 1 in ONE but not both
print(~5)        # -6  (inverts all bits, -(n+1))
print(5 << 1)    # 10  (0101 → 1010)  — multiply by 2
print(5 >> 1)    # 2   (0101 → 0010)  — divide by 2
```

---

### 2.8 Ternary (Conditional) Operator

```python
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)    # Adult

# Nested ternary
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C"
```

---

### 2.9 Operator Precedence (Highest → Lowest)

| Priority | Operator | Description |
|----------|----------|-------------|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `~`, `+x`, `-x` | Unary NOT, positive, negative |
| 4 | `*`, `/`, `//`, `%` | Multiplication, Division, Floor, Modulus |
| 5 | `+`, `-` | Addition, Subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |
| 14 | `:=` | Walrus operator |

```python
# Example showing precedence
result = 2 + 3 * 4 ** 2
# Step 1: 4 ** 2 = 16
# Step 2: 3 * 16 = 48
# Step 3: 2 + 48 = 50
print(result)   # 50
```

---

## 3. Control Flow Statements

### 3.1 `if` Statement

```python
age = 18

if age >= 18:
    print("You can vote!")
```

### 3.2 `if-else` Statement

```python
age = 15

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
```

### 3.3 `if-elif-else` Statement

```python
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")   # Your grade is: A
```

### 3.4 Nested `if`

```python
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Non-positive number")
```

### 3.5 `match-case` Statement (Python 3.10+)

Similar to `switch-case` in Java/C.

```python
command = "start"

match command:
    case "start":
        print("Starting the process...")
    case "stop":
        print("Stopping the process...")
    case "pause":
        print("Pausing the process...")
    case _:                              # Default case (like 'default' in Java)
        print("Unknown command!")
```

**Advanced pattern matching:**

```python
# Matching with conditions (guards)
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, y) if x == y:
        print(f"On diagonal at ({x}, {y})")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Output: On Y-axis at y=5
```

### 3.6 `pass` Statement

A placeholder that does nothing. Used when a statement is syntactically required.

```python
if True:
    pass       # TODO: implement later

def my_function():
    pass       # Empty function placeholder
```

---

## 4. Loops

### 4.1 `for` Loop

Iterates over a **sequence** (list, tuple, string, range, etc.).

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char, end=" ")   # P y t h o n

# Using range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Reverse iteration
for i in range(10, 0, -1):  # 10, 9, 8, ... 1
    print(i)
```

### 4.2 `for` Loop with `enumerate()`

Get both **index** and **value** while iterating.

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Output:
# 0: red
# 1: green
# 2: blue

# Start from a custom index
for index, color in enumerate(colors, start=1):
    print(f"{index}: {color}")
```

### 4.3 `for` Loop with `zip()`

Iterate over **multiple sequences** simultaneously.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
```

### 4.4 `while` Loop

Executes as long as the condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Output: 0 1 2 3 4
```

### 4.5 `break` Statement

Exits the loop immediately.

```python
for num in range(1, 100):
    if num == 5:
        break
    print(num)

# Output: 1 2 3 4
```

### 4.6 `continue` Statement

Skips the current iteration and moves to the next.

```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Output: 1 2 4 5
```

### 4.7 `else` Clause in Loops

The `else` block runs **only if the loop completes without `break`**.

```python
# With for loop
for num in range(2, 10):
    if num == 15:
        print("Found!")
        break
else:
    print("Not found in range")    # This runs because break was never hit

# With while loop
n = 0
while n < 5:
    n += 1
else:
    print("Loop completed normally")   # Runs when condition becomes False
```

### 4.8 Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

# Output:
# 1 x 1 = 1    1 x 2 = 2    1 x 3 = 3
# 2 x 1 = 2    2 x 2 = 4    2 x 3 = 6
# 3 x 1 = 3    3 x 2 = 6    3 x 3 = 9
```

### 4.9 List Comprehension (Concise Loop)

```python
# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension way
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)     # [2, 4, 6, 8, 10]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print(labels)    # ['odd', 'even', 'odd', 'even', 'odd']
```

---

## 5. Strings

Strings in Python are **immutable sequences** of Unicode characters.

### 5.1 Creating Strings

```python
# Single quotes
s1 = 'Hello'

# Double quotes
s2 = "World"

# Triple quotes (multi-line)
s3 = """This is
a multi-line
string"""

# Raw strings (ignores escape characters)
s4 = r"C:\new\folder"      # C:\new\folder (no escaping)

# f-strings (formatted strings) — Python 3.6+
name = "Krish"
s5 = f"Hello, {name}!"     # Hello, Krish!
```

### 5.2 String Indexing & Slicing

```python
text = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5    (positive index)
#      -6 -5 -4 -3 -2 -1   (negative index)

# Indexing
print(text[0])       # P
print(text[-1])      # n

# Slicing — text[start:stop:step]
print(text[0:3])     # Pyt   (index 0, 1, 2)
print(text[2:])      # thon  (from index 2 to end)
print(text[:3])      # Pyt   (from start to index 2)
print(text[::2])     # Pto   (every 2nd character)
print(text[::-1])    # nohtyP (reverse the string)
```

### 5.3 String Methods — Complete Reference

#### Case Methods

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `upper()` | All uppercase | `"hello".upper()` | `"HELLO"` |
| `lower()` | All lowercase | `"HELLO".lower()` | `"hello"` |
| `title()` | First letter of each word uppercase | `"hello world".title()` | `"Hello World"` |
| `capitalize()` | First letter uppercase, rest lowercase | `"hello WORLD".capitalize()` | `"Hello world"` |
| `swapcase()` | Swap case of each character | `"Hello".swapcase()` | `"hELLO"` |
| `casefold()` | Aggressive lowercase (for comparison) | `"Straße".casefold()` | `"strasse"` |

#### Search & Find Methods

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `find(sub)` | First index of `sub`, or `-1` | `"hello".find("ll")` | `2` |
| `rfind(sub)` | Last index of `sub`, or `-1` | `"hello".rfind("l")` | `3` |
| `index(sub)` | Like `find()`, but raises `ValueError` if not found | `"hello".index("ll")` | `2` |
| `rindex(sub)` | Like `rfind()`, but raises `ValueError` | `"hello".rindex("l")` | `3` |
| `count(sub)` | Count occurrences of `sub` | `"hello".count("l")` | `2` |
| `startswith(prefix)` | Check if starts with prefix | `"hello".startswith("he")` | `True` |
| `endswith(suffix)` | Check if ends with suffix | `"hello".endswith("lo")` | `True` |

#### Modify & Replace Methods

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `replace(old, new)` | Replace all occurrences | `"hello".replace("l", "r")` | `"herro"` |
| `strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` | `"hi"` |
| `lstrip()` | Remove leading whitespace | `"  hi  ".lstrip()` | `"hi  "` |
| `rstrip()` | Remove trailing whitespace | `"  hi  ".rstrip()` | `"  hi"` |
| `center(width, char)` | Center-align string | `"hi".center(10, "-")` | `"----hi----"` |
| `ljust(width, char)` | Left-align string | `"hi".ljust(10, "-")` | `"hi--------"` |
| `rjust(width, char)` | Right-align string | `"hi".rjust(10, "-")` | `"--------hi"` |
| `zfill(width)` | Pad with zeros on left | `"42".zfill(5)` | `"00042"` |
| `expandtabs(size)` | Set tab size | `"a\tb".expandtabs(4)` | `"a   b"` |

#### Split & Join Methods

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `split(sep)` | Split into list | `"a,b,c".split(",")` | `["a","b","c"]` |
| `rsplit(sep)` | Split from right | `"a.b.c".rsplit(".", 1)` | `["a.b","c"]` |
| `splitlines()` | Split by newlines | `"a\nb\nc".splitlines()` | `["a","b","c"]` |
| `join(iterable)` | Join list into string | `",".join(["a","b"])` | `"a,b"` |
| `partition(sep)` | Split into 3 parts at first sep | `"a-b-c".partition("-")` | `("a","-","b-c")` |
| `rpartition(sep)` | Split into 3 parts at last sep | `"a-b-c".rpartition("-")` | `("a-b","-","c")` |

#### Validation Methods (return `True`/`False`)

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `isalpha()` | All alphabetic? | `"hello".isalpha()` | `True` |
| `isdigit()` | All digits? | `"123".isdigit()` | `True` |
| `isalnum()` | All alphanumeric? | `"abc123".isalnum()` | `True` |
| `isspace()` | All whitespace? | `"  ".isspace()` | `True` |
| `isupper()` | All uppercase? | `"HELLO".isupper()` | `True` |
| `islower()` | All lowercase? | `"hello".islower()` | `True` |
| `istitle()` | Title case? | `"Hello World".istitle()` | `True` |
| `isnumeric()` | All numeric characters? | `"½".isnumeric()` | `True` |
| `isdecimal()` | All decimal characters? | `"123".isdecimal()` | `True` |
| `isidentifier()` | Valid Python identifier? | `"my_var".isidentifier()` | `True` |
| `isprintable()` | All printable characters? | `"hello".isprintable()` | `True` |
| `isascii()` | All ASCII characters? | `"hello".isascii()` | `True` |

### 5.4 String Formatting

```python
name = "Krish"
age = 22

# f-string (recommended — Python 3.6+)
print(f"Name: {name}, Age: {age}")

# format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# % formatting (old style)
print("Name: %s, Age: %d" % (name, age))

# Formatting numbers
pi = 3.14159
print(f"{pi:.2f}")              # 3.14
print(f"{1000000:,}")           # 1,000,000
print(f"{255:08b}")             # 11111111 (binary with padding)
print(f"{42:05d}")              # 00042
```

### 5.5 Escape Characters

| Escape | Description |
|--------|-------------|
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\n` | Newline |
| `\t` | Tab |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\0` | Null character |
| `\uXXXX` | Unicode character |

---

## 6. Lists

Lists are **ordered, mutable** collections that can hold **mixed data types**.

### 6.1 Creating Lists

```python
# Empty list
empty = []
empty2 = list()

# List with values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]

# From other iterables
from_string = list("hello")        # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(1, 6))     # [1, 2, 3, 4, 5]

# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 6.2 Indexing & Slicing

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing
print(fruits[0])      # apple
print(fruits[-1])     # elderberry

# Slicing
print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'date', 'elderberry']
print(fruits[::-1])   # reversed list

# Nested list access
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])   # 3
```

### 6.3 List Methods — Complete Reference

#### Adding Elements

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Add `x` to the end | `[1,2].append(3)` → `[1,2,3]` |
| `insert(i, x)` | Insert `x` at index `i` | `[1,3].insert(1, 2)` → `[1,2,3]` |
| `extend(iterable)` | Add all items from iterable | `[1,2].extend([3,4])` → `[1,2,3,4]` |

```python
fruits = ["apple", "banana"]

fruits.append("cherry")          # ['apple', 'banana', 'cherry']
fruits.insert(1, "blueberry")    # ['apple', 'blueberry', 'banana', 'cherry']
fruits.extend(["date", "fig"])   # [..., 'date', 'fig']

# Difference: append vs extend
a = [1, 2]
a.append([3, 4])     # [1, 2, [3, 4]]  — adds as single element

b = [1, 2]
b.extend([3, 4])     # [1, 2, 3, 4]    — unpacks and adds each
```

#### Removing Elements

| Method | Description | Example |
|--------|-------------|---------|
| `remove(x)` | Remove first occurrence of `x` | `[1,2,3,2].remove(2)` → `[1,3,2]` |
| `pop(i)` | Remove & return element at index `i` (default: last) | `[1,2,3].pop()` → returns `3` |
| `clear()` | Remove all elements | `[1,2,3].clear()` → `[]` |
| `del` | Delete by index or slice (keyword, not method) | `del lst[0]` |

```python
nums = [10, 20, 30, 40, 50]

nums.remove(30)          # [10, 20, 40, 50]
popped = nums.pop()      # popped = 50, nums = [10, 20, 40]
popped = nums.pop(0)     # popped = 10, nums = [20, 40]
nums.clear()             # []

# Using del
nums = [1, 2, 3, 4, 5]
del nums[0]              # [2, 3, 4, 5]
del nums[1:3]            # [2, 5]
```

#### Searching & Counting

| Method | Description | Example |
|--------|-------------|---------|
| `index(x)` | Return index of first `x` (raises `ValueError` if not found) | `[1,2,3].index(2)` → `1` |
| `count(x)` | Count occurrences of `x` | `[1,2,2,3].count(2)` → `2` |

#### Sorting & Reversing

| Method | Description | Example |
|--------|-------------|---------|
| `sort()` | Sort in-place (ascending by default) | `[3,1,2].sort()` → `[1,2,3]` |
| `sort(reverse=True)` | Sort in-place (descending) | `[3,1,2].sort(reverse=True)` → `[3,2,1]` |
| `sort(key=func)` | Sort using a key function | `words.sort(key=len)` |
| `reverse()` | Reverse in-place | `[1,2,3].reverse()` → `[3,2,1]` |
| `sorted(list)` | Return new sorted list (built-in function) | `sorted([3,1,2])` → `[1,2,3]` |

```python
nums = [5, 2, 8, 1, 9]

# sort() modifies the original list — returns None
nums.sort()
print(nums)              # [1, 2, 5, 8, 9]

# sorted() returns a NEW list — original unchanged
original = [5, 2, 8, 1, 9]
new_sorted = sorted(original)
print(original)          # [5, 2, 8, 1, 9]  (unchanged)
print(new_sorted)        # [1, 2, 5, 8, 9]

# Sort by custom key
words = ["banana", "pie", "apple", "fig"]
words.sort(key=len)
print(words)             # ['pie', 'fig', 'apple', 'banana']
```

#### Copying

| Method | Description |
|--------|-------------|
| `copy()` | Shallow copy |
| `list(original)` | Shallow copy |
| `original[:]` | Shallow copy using slicing |
| `copy.deepcopy(original)` | Deep copy (for nested lists) |

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy — inner lists are still shared
shallow = original.copy()
shallow[0][0] = 99
print(original)          # [[99, 2], [3, 4]] — affected!

# Deep copy — completely independent
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)          # [[1, 2], [3, 4]] — not affected!
```

### 6.4 Useful Built-in Functions with Lists

```python
nums = [10, 20, 5, 30, 15]

print(len(nums))         # 5
print(min(nums))         # 5
print(max(nums))         # 30
print(sum(nums))         # 80
print(any(nums))         # True  (at least one truthy)
print(all(nums))         # True  (all truthy)
```

---

## 7. Tuples

Tuples are **ordered, immutable** collections. They are faster than lists and can be used as dictionary keys.

### 7.1 Creating Tuples

```python
# Empty tuple
empty = ()
empty2 = tuple()

# Tuple with values
colors = ("red", "green", "blue")

# Single element tuple — MUST have trailing comma!
single = (5,)       # ✅ This is a tuple
not_tuple = (5)     # ❌ This is just int 5

# Without parentheses (tuple packing)
coords = 10, 20, 30
print(type(coords))   # <class 'tuple'>

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")   # ('h', 'e', 'l', 'l', 'o')
```

### 7.2 Accessing Elements

```python
colors = ("red", "green", "blue", "yellow", "purple")

# Indexing
print(colors[0])       # red
print(colors[-1])      # purple

# Slicing
print(colors[1:3])     # ('green', 'blue')
print(colors[::-1])    # ('purple', 'yellow', 'blue', 'green', 'red')

# Unpacking
a, b, c = (1, 2, 3)
print(a, b, c)         # 1 2 3

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)            # 1
print(rest)             # [2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)
print(middle)           # [2, 3, 4]
```

### 7.3 Tuple Methods

Tuples have only **2 methods** (because they're immutable):

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `count(x)` | Count occurrences of `x` | `(1,2,2,3).count(2)` | `2` |
| `index(x)` | Return index of first `x` | `(1,2,3).index(2)` | `1` |

```python
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))      # 3
print(t.index(2))      # 1 (first occurrence)
```

### 7.4 Why Use Tuples?

| Feature | Tuple | List |
|---------|-------|------|
| Mutability | ❌ Immutable | ✅ Mutable |
| Speed | ✅ Faster | ❌ Slower |
| Memory | ✅ Less | ❌ More |
| Dict Key? | ✅ Yes (hashable) | ❌ No |
| Use Case | Fixed data | Dynamic data |

```python
# Tuples as dictionary keys
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai"
}
print(locations[(28.6, 77.2)])   # Delhi
```

---

## 8. Sets

Sets are **unordered, mutable** collections of **unique** elements.

### 8.1 Creating Sets

```python
# Empty set — MUST use set(), NOT {}
empty = set()       # ✅ Empty set
empty_dict = {}     # ❌ This creates an empty DICT, not a set!

# Set with values
fruits = {"apple", "banana", "cherry"}

# Duplicates are automatically removed
nums = {1, 2, 3, 3, 4, 4, 5}
print(nums)         # {1, 2, 3, 4, 5}

# From other iterables
from_list = set([1, 2, 2, 3])   # {1, 2, 3}
from_string = set("hello")      # {'h', 'e', 'l', 'o'}
```

### 8.2 Set Methods — Complete Reference

#### Adding & Removing Elements

| Method | Description | Example |
|--------|-------------|---------|
| `add(x)` | Add element `x` | `{1,2}.add(3)` → `{1,2,3}` |
| `update(iterable)` | Add all elements from iterable | `{1}.update([2,3])` → `{1,2,3}` |
| `remove(x)` | Remove `x` (raises `KeyError` if not found) | `{1,2,3}.remove(2)` → `{1,3}` |
| `discard(x)` | Remove `x` (does nothing if not found) | `{1,2,3}.discard(5)` → `{1,2,3}` |
| `pop()` | Remove and return an arbitrary element | `{1,2,3}.pop()` → removes random |
| `clear()` | Remove all elements | `{1,2,3}.clear()` → `set()` |

```python
s = {1, 2, 3}

s.add(4)                # {1, 2, 3, 4}
s.update([5, 6])        # {1, 2, 3, 4, 5, 6}
s.remove(3)             # {1, 2, 4, 5, 6}
s.discard(99)           # No error — {1, 2, 4, 5, 6}
removed = s.pop()       # Removes arbitrary element
```

#### Set Operations (Mathematical)

| Method | Operator | Description | Example |
|--------|----------|-------------|---------|
| `union(B)` | `A \| B` | All elements from both | `{1,2} \| {2,3}` → `{1,2,3}` |
| `intersection(B)` | `A & B` | Elements common to both | `{1,2,3} & {2,3,4}` → `{2,3}` |
| `difference(B)` | `A - B` | Elements in A but not B | `{1,2,3} - {2,3,4}` → `{1}` |
| `symmetric_difference(B)` | `A ^ B` | Elements in A or B, but not both | `{1,2,3} ^ {2,3,4}` → `{1,4}` |

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)     # {1, 2, 3, 4, 5, 6, 7, 8}  — Union
print(A & B)     # {4, 5}                      — Intersection
print(A - B)     # {1, 2, 3}                   — Difference
print(A ^ B)     # {1, 2, 3, 6, 7, 8}          — Symmetric Difference
```

#### In-Place Set Operations

| Method | Operator | Description |
|--------|----------|-------------|
| `update(B)` | `A \|= B` | Add all elements from B to A |
| `intersection_update(B)` | `A &= B` | Keep only elements found in both |
| `difference_update(B)` | `A -= B` | Remove elements found in B from A |
| `symmetric_difference_update(B)` | `A ^= B` | Keep elements in either but not both |

#### Comparison Methods

| Method | Operator | Description | Example |
|--------|----------|-------------|---------|
| `issubset(B)` | `A <= B` | Is A a subset of B? | `{1,2} <= {1,2,3}` → `True` |
| `issuperset(B)` | `A >= B` | Is A a superset of B? | `{1,2,3} >= {1,2}` → `True` |
| `isdisjoint(B)` | — | Do A and B have no common elements? | `{1,2}.isdisjoint({3,4})` → `True` |

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))      # True   (all of A is in B)
print(B.issuperset(A))    # True   (B contains all of A)
print(A.isdisjoint({5}))  # True   (no common elements)
```

### 8.3 Frozen Sets

Immutable version of sets. Can be used as dictionary keys.

```python
fs = frozenset([1, 2, 3, 4])
# fs.add(5)    ❌ Error! frozenset is immutable

# Can be used as dictionary key
d = {frozenset([1, 2]): "pair"}
```

### 8.4 Set Comprehension

```python
squares = {x**2 for x in range(1, 6)}
print(squares)   # {1, 4, 9, 16, 25}

even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)   # {4, 16, 36, 64, 100}
```

---

## 9. Dictionaries

Dictionaries are **ordered (3.7+), mutable** collections of **key-value pairs**. Keys must be unique and hashable.

### 9.1 Creating Dictionaries

```python
# Empty dictionary
empty = {}
empty2 = dict()

# With values
student = {
    "name": "Krish",
    "age": 22,
    "grade": "A",
    "courses": ["Python", "DSA", "DBMS"]
}

# Using dict() constructor
person = dict(name="Alice", age=30)

# From list of tuples
pairs = dict([("a", 1), ("b", 2), ("c", 3)])

# Using dict.fromkeys()
keys = ["x", "y", "z"]
d = dict.fromkeys(keys, 0)    # {'x': 0, 'y': 0, 'z': 0}
```

### 9.2 Accessing Values

```python
student = {"name": "Krish", "age": 22, "grade": "A"}

# Using [] — raises KeyError if key not found
print(student["name"])       # Krish
# print(student["email"])    # ❌ KeyError

# Using get() — returns None (or default) if key not found
print(student.get("name"))           # Krish
print(student.get("email"))          # None
print(student.get("email", "N/A"))   # N/A (custom default)
```

### 9.3 Adding & Modifying

```python
student = {"name": "Krish", "age": 22}

# Add new key-value pair
student["email"] = "krish@example.com"

# Modify existing value
student["age"] = 23

# update() — merge another dict
student.update({"grade": "A", "age": 24})
print(student)
# {'name': 'Krish', 'age': 24, 'email': 'krish@example.com', 'grade': 'A'}

# setdefault() — set value only if key doesn't exist
student.setdefault("name", "Unknown")    # Does nothing (key exists)
student.setdefault("phone", "N/A")       # Adds phone: N/A
```

### 9.4 Removing Elements

| Method | Description | Example |
|--------|-------------|---------|
| `pop(key)` | Remove by key & return value | `d.pop("name")` |
| `pop(key, default)` | Remove or return default | `d.pop("x", "N/A")` |
| `popitem()` | Remove & return last key-value pair | `d.popitem()` |
| `del d[key]` | Delete by key | `del d["name"]` |
| `clear()` | Remove all items | `d.clear()` |

```python
student = {"name": "Krish", "age": 22, "grade": "A"}

removed = student.pop("grade")      # removed = "A"
last = student.popitem()             # ('age', 22)
del student["name"]                  # {}
```

### 9.5 Dictionary Methods — Complete Reference

| Method | Description | Returns |
|--------|-------------|---------|
| `keys()` | All keys | `dict_keys` view |
| `values()` | All values | `dict_values` view |
| `items()` | All key-value pairs as tuples | `dict_items` view |
| `get(key, default)` | Get value by key (safe) | Value or default |
| `setdefault(key, default)` | Get or set default | Value |
| `update(dict2)` | Merge another dict into this | `None` |
| `pop(key, default)` | Remove and return value | Value or default |
| `popitem()` | Remove and return last pair | `(key, value)` tuple |
| `copy()` | Shallow copy | New dict |
| `clear()` | Remove all items | `None` |
| `fromkeys(keys, value)` | Create dict from keys with same value | New dict |

### 9.6 Iterating Over Dictionaries

```python
student = {"name": "Krish", "age": 22, "grade": "A"}

# Iterate over keys (default)
for key in student:
    print(key)

# Iterate over values
for value in student.values():
    print(value)

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

### 9.7 Dictionary Comprehension

```python
# Basic
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_sq = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_sq)   # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)   # {1: 'a', 2: 'b', 3: 'c'}
```

### 9.8 Nested Dictionaries

```python
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22},
    "student3": {"name": "Charlie", "age": 21}
}

# Access nested values
print(students["student1"]["name"])   # Alice

# Iterate nested
for student_id, info in students.items():
    print(f"{student_id}: {info['name']} (Age: {info['age']})")
```

### 9.9 Merge Dictionaries (Python 3.9+)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Using | operator (Python 3.9+)
merged = dict1 | dict2
print(merged)        # {'a': 1, 'b': 3, 'c': 4}  (dict2 values override)

# In-place merge using |=
dict1 |= dict2
print(dict1)         # {'a': 1, 'b': 3, 'c': 4}

# Using ** unpacking (works in all Python 3.x)
merged = {**dict1, **dict2}
```

---

## 10. Functions

### 10.1 Defining Functions

```python
# Basic function
def greet():
    print("Hello, World!")

greet()              # Hello, World!

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Krish")       # Hello, Krish!

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)        # 8
```

### 10.2 Parameters & Arguments

```python
# Positional arguments
def power(base, exp):
    return base ** exp

print(power(2, 3))       # 8

# Keyword arguments
print(power(exp=3, base=2))   # 8

# Default parameter values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Krish"))                 # Hello, Krish!
print(greet("Krish", "Welcome"))      # Welcome, Krish!
```

### 10.3 `*args` — Variable Positional Arguments

Collects **extra positional arguments** into a **tuple**.

```python
def add_all(*args):
    print(type(args))     # <class 'tuple'>
    return sum(args)

print(add_all(1, 2, 3))          # 6
print(add_all(10, 20, 30, 40))   # 100

# Mixing regular and *args
def introduce(name, *hobbies):
    print(f"I'm {name}")
    for hobby in hobbies:
        print(f"  - {hobby}")

introduce("Krish", "coding", "reading", "gaming")
```

### 10.4 `**kwargs` — Variable Keyword Arguments

Collects **extra keyword arguments** into a **dictionary**.

```python
def print_info(**kwargs):
    print(type(kwargs))     # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Krish", age=22, city="Ahmedabad")

# Mixing all types of parameters
def func(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, x=10, y=20)
# a=1, b=2
# args=(3, 4)
# kwargs={'x': 10, 'y': 20}
```

### 10.5 Parameter Order Rule

```
def func(positional, /, positional_or_keyword, *, keyword_only, **kwargs):
```

**Order**: Regular → `*args` → Keyword-only → `**kwargs`

```python
def func(a, b, *args, key1="default", **kwargs):
    print(a, b, args, key1, kwargs)

func(1, 2, 3, 4, key1="custom", extra=True)
# 1 2 (3, 4) custom {'extra': True}
```

### 10.6 Return Values

```python
# Return single value
def square(n):
    return n ** 2

# Return multiple values (as tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)     # 1 9

# Return None (implicit)
def do_nothing():
    pass

result = do_nothing()
print(result)        # None
```

### 10.7 Lambda Functions (Anonymous Functions)

Single-line, anonymous functions.

```python
# Syntax: lambda parameters: expression

# Basic lambda
square = lambda x: x ** 2
print(square(5))     # 25

# Multiple parameters
add = lambda a, b: a + b
print(add(3, 4))     # 7

# Lambda with built-in functions
numbers = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(numbers)                         # [1, 1, 3, 4, 5, 9]
sorted_desc = sorted(numbers, reverse=True)            # [9, 5, 4, 3, 1, 1]

# Sort by custom key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda s: s[1])                      # Sort by score
print(students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
print(squared)       # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)         # [2, 4]

from functools import reduce
total = reduce(lambda a, b: a + b, numbers)
print(total)         # 15
```

### 10.8 Scope — `global` and `nonlocal`

```python
x = 10                  # Global variable

def outer():
    y = 20              # Enclosing variable

    def inner():
        z = 30          # Local variable
        print(x, y, z)  # Can read all

    inner()

outer()                 # 10 20 30

# Modifying global variable
count = 0

def increment():
    global count        # Must declare 'global' to modify
    count += 1

increment()
print(count)            # 1

# Modifying enclosing variable
def outer():
    value = 10

    def inner():
        nonlocal value  # Must declare 'nonlocal' to modify
        value += 5

    inner()
    print(value)        # 15

outer()
```

### 10.9 Docstrings

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

### 10.10 Recursive Functions

A function that calls itself.

```python
# Factorial: n! = n * (n-1)!
def factorial(n):
    if n <= 1:       # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print(factorial(5))   # 120  (5 * 4 * 3 * 2 * 1)

# Fibonacci: fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))   # 13  (0, 1, 1, 2, 3, 5, 8, 13)
```

### 10.11 Higher-Order Functions

Functions that take other functions as arguments or return functions.

```python
# map() — apply function to each element
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)        # [2, 4, 6, 8, 10]

# filter() — keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)          # [2, 4]

# reduce() — accumulate values
from functools import reduce
product = reduce(lambda a, b: a * b, numbers)
print(product)        # 120

# zip() — combine iterables
names = ["Alice", "Bob"]
scores = [85, 92]
combined = list(zip(names, scores))
print(combined)       # [('Alice', 85), ('Bob', 92)]

# any() and all()
print(any([False, False, True]))   # True
print(all([True, True, True]))     # True
print(all([True, False, True]))    # False
```

### 10.12 Decorators (Preview)

A decorator is a function that takes another function and extends its behavior.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Krish")
# Output:
# Before function call
# Hello, Krish!
# After function call
```

---

## Quick Reference Cheat Sheet

| Type | Ordered | Mutable | Duplicates | Syntax |
|------|---------|---------|------------|--------|
| `list` | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| `tuple` | ✅ | ❌ | ✅ | `(1, 2, 3)` |
| `set` | ❌ | ✅ | ❌ | `{1, 2, 3}` |
| `frozenset` | ❌ | ❌ | ❌ | `frozenset([1,2])` |
| `dict` | ✅ | ✅ | Keys: ❌ | `{"a": 1}` |
| `str` | ✅ | ❌ | ✅ | `"hello"` |

---

> 🎯 **Next Steps**: Practice each section by writing code in your Python IDE. Start with simple examples, then try combining concepts (e.g., use loops with lists, functions with dictionaries).

---

*Happy Coding! 🐍*
