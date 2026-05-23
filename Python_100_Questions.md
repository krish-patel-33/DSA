# 🐍 100 Python Questions for Placement Preparation

> **Topics Covered**: Data Types, Operators, Control Flow, Loops, Lists (Arrays), Strings  
> **Difficulty**: Beginner → Intermediate → Placement Level  
> **Author**: Practice Notes | May 2026

---

## Section 1: Data Types & Variables (Q1 – Q15)

---

### Q1. What will be the output?

```python
x = 10
y = 3
print(x / y)
print(x // y)
print(x % y)
```

<details>
<summary>Answer</summary>

```
3.3333333333333335
3
1
```

**Explanation**: `/` gives float division, `//` gives floor division (integer part), `%` gives remainder.

</details>

---

### Q2. What will be the output?

```python
a = 5
b = 2
print(type(a / b))
print(type(a // b))
```

<details>
<summary>Answer</summary>

```
<class 'float'>
<class 'int'>
```

**Explanation**: `/` always returns `float`, `//` returns `int` when both operands are `int`.

</details>

---

### Q3. What will be the output?

```python
x = "Hello"
y = 3
print(x * y)
```

<details>
<summary>Answer</summary>

```
HelloHelloHello
```

**Explanation**: Multiplying a string by an integer repeats the string that many times.

</details>

---

### Q4. What will be the output?

```python
print(type(True))
print(True + True + False)
print(True * 10)
```

<details>
<summary>Answer</summary>

```
<class 'bool'>
2
10
```

**Explanation**: `bool` is a subclass of `int`. `True = 1`, `False = 0`. So `True + True + False = 1 + 1 + 0 = 2`.

</details>

---

### Q5. What will be the output?

```python
a = 10
b = 10
c = a

print(a == b)
print(a is b)
print(a is c)
```

<details>
<summary>Answer</summary>

```
True
True
True
```

**Explanation**: Python caches small integers (-5 to 256). So `a` and `b` point to the same object. `c = a` also points to the same object.

</details>

---

### Q6. What will be the output?

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
```

<details>
<summary>Answer</summary>

```
True
False
```

**Explanation**: `==` compares values (equal), but `is` checks if they are the **same object in memory** (they are not — two different lists).

</details>

---

### Q7. Predict the output.

```python
x = None
print(type(x))
print(x == 0)
print(x == False)
print(x is None)
```

<details>
<summary>Answer</summary>

```
<class 'NoneType'>
False
False
True
```

**Explanation**: `None` is not `0` and not `False`. It is its own type. Always use `is None` to check for `None`.

</details>

---

### Q8. What will be the output?

```python
print(int(3.9))
print(int(-3.9))
print(int("100"))
print(float("3.14"))
```

<details>
<summary>Answer</summary>

```
3
-3
100
3.14
```

**Explanation**: `int()` truncates towards zero (does NOT round). `int("100")` converts string to integer.

</details>

---

### Q9. What will be the output?

```python
a = "5"
b = 3
print(a * b)
# print(a + b)  # What would this do?
```

<details>
<summary>Answer</summary>

```
555
```

`a * b` repeats the string `"5"` three times = `"555"`.  
`a + b` would raise a **TypeError** because you can't add a string and an integer directly. You would need `int(a) + b` or `a + str(b)`.

</details>

---

### Q10. What will be the output?

```python
x = 0
y = ""
z = []
w = None

print(bool(x))
print(bool(y))
print(bool(z))
print(bool(w))
print(bool("0"))
print(bool([0]))
```

<details>
<summary>Answer</summary>

```
False
False
False
False
True
True
```

**Explanation**: `0`, `""`, `[]`, `None` are all **falsy**. But `"0"` is a non-empty string (truthy) and `[0]` is a non-empty list (truthy).

</details>

---

### Q11. What will be the output?

```python
a, b, c = 10, 20, 30
print(a, b, c)

x = y = z = 100
print(x, y, z)
```

<details>
<summary>Answer</summary>

```
10 20 30
100 100 100
```

**Explanation**: Python supports multiple assignment in a single line and assigning the same value to multiple variables.

</details>

---

### Q12. What will be the output?

```python
a = 5
b = 10
a, b = b, a
print(a, b)
```

<details>
<summary>Answer</summary>

```
10 5
```

**Explanation**: Python can swap variables without a temp variable using tuple unpacking. This is a very common placement question.

</details>

---

### Q13. What will be the output?

```python
print(2 ** 3 ** 2)
```

<details>
<summary>Answer</summary>

```
512
```

**Explanation**: `**` (exponentiation) is **right-associative**. So `3 ** 2 = 9` first, then `2 ** 9 = 512`.

</details>

---

### Q14. What will be the output?

```python
x = 10
print(type(x).__name__)

x = 10.5
print(type(x).__name__)

x = "hello"
print(type(x).__name__)

x = [1, 2]
print(type(x).__name__)
```

<details>
<summary>Answer</summary>

```
int
float
str
list
```

**Explanation**: Python is dynamically typed — the same variable `x` can hold values of different types. `type().__name__` gives the type name as a string.

</details>

---

### Q15. What will be the output?

```python
a = 10
b = -10
print(abs(b))
print(pow(a, 3))
print(max(a, b))
print(min(a, b))
```

<details>
<summary>Answer</summary>

```
10
1000
10
-10
```

**Explanation**: `abs()` returns absolute value, `pow(a, 3)` = `a ** 3`, `max()` and `min()` return largest and smallest values.

</details>

---

## Section 2: Control Flow & Conditions (Q16 – Q25)

---

### Q16. What will be the output?

```python
x = 15

if x > 20:
    print("Big")
elif x > 10:
    print("Medium")
elif x > 5:
    print("Small")
else:
    print("Tiny")
```

<details>
<summary>Answer</summary>

```
Medium
```

**Explanation**: Python checks conditions top-to-bottom and executes the **first** matching block only. `x > 10` is `True`, so it prints "Medium" and skips the rest.

</details>

---

### Q17. What will be the output?

```python
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```

<details>
<summary>Answer</summary>

```
Odd
```

**Explanation**: This is the ternary operator. `x % 2 == 0` is `False`, so the `else` value `"Odd"` is assigned.

</details>

---

### Q18. What will be the output?

```python
print(True and "Hello")
print(False and "Hello")
print(True or "Hello")
print(False or "Hello")
```

<details>
<summary>Answer</summary>

```
Hello
False
True
Hello
```

**Explanation**: `and` returns the first falsy value or the last value. `or` returns the first truthy value or the last value. This is called **short-circuit evaluation**.

</details>

---

### Q19. Write a program to check if a number is positive, negative, or zero.

<details>
<summary>Answer</summary>

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

</details>

---

### Q20. Write a program to find the largest of three numbers.

<details>
<summary>Answer</summary>

```python
a, b, c = 10, 25, 15

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Largest is: {largest}")

# Shortcut using max()
print(f"Largest is: {max(a, b, c)}")
```

**Output:**
```
Largest is: 25
Largest is: 25
```

</details>

---

### Q21. What will be the output?

```python
x = 0
if x:
    print("Truthy")
else:
    print("Falsy")
```

<details>
<summary>Answer</summary>

```
Falsy
```

**Explanation**: `0` is falsy in Python. `if x:` is equivalent to `if bool(x):` which is `if False:`.

</details>

---

### Q22. Write a program to check if a year is a leap year.

<details>
<summary>Answer</summary>

```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")
```

**Output:**
```
2024 is a Leap Year
```

**Rule**: A year is a leap year if:
- Divisible by 4 AND not divisible by 100, OR
- Divisible by 400

</details>

---

### Q23. Write a program to check if a character is a vowel or consonant.

<details>
<summary>Answer</summary>

```python
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print(f"'{ch}' is a Vowel")
elif ch.isalpha():
    print(f"'{ch}' is a Consonant")
else:
    print("Not a letter")
```

</details>

---

### Q24. What will be the output?

```python
x = 5
y = 10
print("Yes" if x > 3 and y > 5 else "No")
print("Yes" if x > 3 or y > 20 else "No")
print("Yes" if not (x > 10) else "No")
```

<details>
<summary>Answer</summary>

```
Yes
Yes
Yes
```

**Explanation**: Both conditions true for `and`. First condition true for `or`. `x > 10` is `False`, `not False` is `True`.

</details>

---

### Q25. Write a simple calculator using if-elif-else.

<details>
<summary>Answer</summary>

```python
a = 20
b = 5
op = "+"

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator")
```

**Output:**
```
20 + 5 = 25
```

</details>

---

## Section 3: Loops (Q26 – Q45)

---

### Q26. Print numbers from 1 to 10 using a for loop.

<details>
<summary>Answer</summary>

```python
for i in range(1, 11):
    print(i, end=" ")
```

**Output:**
```
1 2 3 4 5 6 7 8 9 10
```

</details>

---

### Q27. Print the sum of numbers from 1 to 100.

<details>
<summary>Answer</summary>

```python
total = 0
for i in range(1, 101):
    total += i
print(f"Sum = {total}")

# One-liner using sum()
print(f"Sum = {sum(range(1, 101))}")
```

**Output:**
```
Sum = 5050
Sum = 5050
```

</details>

---

### Q28. Print multiplication table of 7.

<details>
<summary>Answer</summary>

```python
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

**Output:**
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

</details>

---

### Q29. What will be the output?

```python
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
print("\nDone")
```

<details>
<summary>Answer</summary>

```
0 1 2 
Done
```

**Explanation**: `break` exits the loop when `i == 3`. So 3 and 4 are never printed.

</details>

---

### Q30. What will be the output?

```python
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
```

<details>
<summary>Answer</summary>

```
0 1 2 4
```

**Explanation**: `continue` skips the current iteration. So `3` is skipped but the loop continues.

</details>

---

### Q31. Print all even numbers from 1 to 20.

<details>
<summary>Answer</summary>

```python
# Method 1: Using if condition
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print()

# Method 2: Using range step
for i in range(2, 21, 2):
    print(i, end=" ")
```

**Output:**
```
2 4 6 8 10 12 14 16 18 20
2 4 6 8 10 12 14 16 18 20
```

</details>

---

### Q32. Print the factorial of a number using a while loop.

<details>
<summary>Answer</summary>

```python
n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"Factorial of {n} = {factorial}")
```

**Output:**
```
Factorial of 5 = 120
```

</details>

---

### Q33. Check if a number is prime.

<details>
<summary>Answer</summary>

```python
num = 29
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"{num} is {'Prime' if is_prime else 'Not Prime'}")
```

**Output:**
```
29 is Prime
```

**Explanation**: We only check divisors up to the square root of the number. This is an optimization commonly asked in placements.

</details>

---

### Q34. Print the Fibonacci sequence up to n terms.

<details>
<summary>Answer</summary>

```python
n = 10
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

**Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Explanation**: Each number is the sum of the previous two. `a, b = b, a + b` is the Pythonic way to do it using tuple unpacking.

</details>

---

### Q35. Print this pattern:

```
*
**
***
****
*****
```

<details>
<summary>Answer</summary>

```python
for i in range(1, 6):
    print("*" * i)
```

</details>

---

### Q36. Print this pattern:

```
*****
****
***
**
*
```

<details>
<summary>Answer</summary>

```python
for i in range(5, 0, -1):
    print("*" * i)
```

</details>

---

### Q37. Print this number triangle:

```
1
12
123
1234
12345
```

<details>
<summary>Answer</summary>

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

</details>

---

### Q38. What will be the output? (else with for loop)

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")
```

<details>
<summary>Answer</summary>

```
Loop completed without break
```

**Explanation**: The `else` block in a loop runs only if the loop completes **without** hitting a `break`. Since `i` never equals 10, the loop finishes normally and `else` executes.

</details>

---

### Q39. Print all prime numbers between 1 and 50.

<details>
<summary>Answer</summary>

```python
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
```

**Output:**
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

</details>

---

### Q40. Reverse a number using a while loop.

<details>
<summary>Answer</summary>

```python
num = 12345
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"Reversed: {reversed_num}")
```

**Output:**
```
Reversed: 54321
```

**Explanation**: Extract last digit using `% 10`, build reversed number, remove last digit using `// 10`. Very common placement question.

</details>

---

### Q41. Check if a number is a palindrome.

<details>
<summary>Answer</summary>

```python
num = 12321
original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original == reversed_num:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is NOT a Palindrome")
```

**Output:**
```
12321 is a Palindrome
```

</details>

---

### Q42. Check if a number is an Armstrong number.

An Armstrong number of n digits: sum of each digit raised to the power n equals the number itself.  
Example: `153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`

<details>
<summary>Answer</summary>

```python
num = 153
original = num
n = len(str(num))  # number of digits
total = 0

while num > 0:
    digit = num % 10
    total += digit ** n
    num //= 10

if total == original:
    print(f"{original} is an Armstrong Number")
else:
    print(f"{original} is NOT an Armstrong Number")
```

**Output:**
```
153 is an Armstrong Number
```

</details>

---

### Q43. Print the sum of digits of a number.

<details>
<summary>Answer</summary>

```python
num = 9876
total = 0
temp = num

while temp > 0:
    total += temp % 10
    temp //= 10

print(f"Sum of digits of {num} = {total}")

# One-liner Pythonic way
print(f"Sum of digits of {num} = {sum(int(d) for d in str(num))}")
```

**Output:**
```
Sum of digits of 9876 = 30
Sum of digits of 9876 = 30
```

</details>

---

### Q44. Count the number of digits in a number.

<details>
<summary>Answer</summary>

```python
num = 123456
count = 0
temp = num

while temp > 0:
    count += 1
    temp //= 10

print(f"Number of digits in {num} = {count}")

# One-liner
print(f"Number of digits in {num} = {len(str(num))}")
```

**Output:**
```
Number of digits in 123456 = 6
Number of digits in 123456 = 6
```

</details>

---

### Q45. Print the GCD (Greatest Common Divisor) of two numbers.

<details>
<summary>Answer</summary>

```python
a, b = 48, 18

# Method 1: Using Euclidean algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y
print(f"GCD of {a} and {b} = {x}")

# Method 2: Using math module
import math
print(f"GCD of {a} and {b} = {math.gcd(a, b)}")
```

**Output:**
```
GCD of 48 and 18 = 6
GCD of 48 and 18 = 6
```

**Explanation**: The Euclidean algorithm repeatedly divides and takes the remainder. Very commonly asked in placements.

</details>

---

## Section 4: Lists / Arrays (Q46 – Q75)

---

### Q46. What will be the output?

```python
arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[::-1])
```

<details>
<summary>Answer</summary>

```
10
50
[20, 30, 40]
[50, 40, 30, 20, 10]
```

**Explanation**: `arr[0]` = first element, `arr[-1]` = last, `arr[1:4]` = elements at index 1,2,3, `arr[::-1]` = reversed list.

</details>

---

### Q47. Find the largest element in a list without using max().

<details>
<summary>Answer</summary>

```python
arr = [12, 45, 7, 89, 23, 56]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(f"Largest element: {largest}")
```

**Output:**
```
Largest element: 89
```

</details>

---

### Q48. Find the second largest element in a list.

<details>
<summary>Answer</summary>

```python
arr = [12, 45, 7, 89, 23, 56]
first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(f"Second Largest: {second}")
```

**Output:**
```
Second Largest: 56
```

**Explanation**: Track both first and second largest in a single pass. Time: O(n). Very commonly asked!

</details>

---

### Q49. Reverse a list without using reverse() or slicing.

<details>
<summary>Answer</summary>

```python
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
```

**Output:**
```
[5, 4, 3, 2, 1]
```

**Explanation**: Two-pointer technique. Swap elements from both ends moving inward. Time: O(n), Space: O(1).

</details>

---

### Q50. Remove duplicates from a list while preserving order.

<details>
<summary>Answer</summary>

```python
arr = [1, 3, 5, 3, 7, 1, 9, 5]
seen = set()
result = []

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)

# One-liner using dict (preserves order in Python 3.7+)
print(list(dict.fromkeys(arr)))
```

**Output:**
```
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9]
```

</details>

---

### Q51. Find the frequency/count of each element in a list.

<details>
<summary>Answer</summary>

```python
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    print(f"{key} appears {value} times")
```

**Output:**
```
1 appears 1 times
2 appears 2 times
3 appears 3 times
4 appears 4 times
```

</details>

---

### Q52. Rotate an array to the left by k positions.

<details>
<summary>Answer</summary>

```python
arr = [1, 2, 3, 4, 5]
k = 2

# Method 1: Using slicing
rotated = arr[k:] + arr[:k]
print(rotated)

# Method 2: Without extra space (in-place)
def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    arr[:] = arr[k:] + arr[:k]

rotate_left(arr, 2)
print(arr)
```

**Output:**
```
[3, 4, 5, 1, 2]
[3, 4, 5, 1, 2]
```

**Explanation**: Left rotation by 2 means moving first 2 elements to the end. Very common placement question.

</details>

---

### Q53. Rotate an array to the right by k positions.

<details>
<summary>Answer</summary>

```python
arr = [1, 2, 3, 4, 5]
k = 2

rotated = arr[-k:] + arr[:-k]
print(rotated)
```

**Output:**
```
[4, 5, 1, 2, 3]
```

</details>

---

### Q54. Find the missing number in a list from 1 to n.

```
Given: [1, 2, 4, 5, 6] — find the missing number (answer: 3)
```

<details>
<summary>Answer</summary>

```python
arr = [1, 2, 4, 5, 6]
n = len(arr) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum

print(f"Missing number: {missing}")
```

**Output:**
```
Missing number: 3
```

**Explanation**: Sum of 1 to n = `n*(n+1)/2`. Subtract actual sum to find missing. Time: O(n), Space: O(1). Extremely common placement question!

</details>

---

### Q55. Move all zeros to the end of the list.

```
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

<details>
<summary>Answer</summary>

```python
arr = [0, 1, 0, 3, 12]
pos = 0  # position to place non-zero element

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print(arr)
```

**Output:**
```
[1, 3, 12, 0, 0]
```

**Explanation**: Two-pointer approach. `pos` tracks where the next non-zero element should go. Time: O(n), Space: O(1).

</details>

---

### Q56. Find the intersection of two lists.

<details>
<summary>Answer</summary>

```python
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

# Method 1: Using set
intersection = list(set(a) & set(b))
print(intersection)

# Method 2: Using list comprehension
intersection = [x for x in a if x in b]
print(intersection)
```

**Output:**
```
[3, 4, 5]
[3, 4, 5]
```

</details>

---

### Q57. Find the union of two lists (no duplicates).

<details>
<summary>Answer</summary>

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

union = list(set(a) | set(b))
print(sorted(union))
```

**Output:**
```
[1, 2, 3, 4, 5, 6]
```

</details>

---

### Q58. Merge two sorted lists into a single sorted list.

<details>
<summary>Answer</summary>

```python
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

# Method 1: Simple (using sorted)
merged = sorted(a + b)
print(merged)

# Method 2: Efficient merge (like merge sort)
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

print(merge_sorted(a, b))
```

**Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
```

**Explanation**: Method 2 is the merge step of Merge Sort. Time: O(n + m). Commonly asked!

</details>

---

### Q59. Find pair of elements whose sum equals a target.

```
Input:  arr = [2, 7, 11, 15], target = 9
Output: (2, 7)
```

<details>
<summary>Answer</summary>

```python
arr = [2, 7, 11, 15]
target = 9
seen = {}

for num in arr:
    complement = target - num
    if complement in seen:
        print(f"Pair found: ({complement}, {num})")
        break
    seen[num] = True
```

**Output:**
```
Pair found: (2, 7)
```

**Explanation**: Use a dictionary/set to check if `target - current_number` exists. Time: O(n). This is LeetCode's famous "Two Sum" problem!

</details>

---

### Q60. Find the element that appears more than n/2 times (Majority Element).

<details>
<summary>Answer</summary>

```python
arr = [3, 3, 4, 2, 3, 3, 3]

# Boyer-Moore Voting Algorithm
candidate = arr[0]
count = 1

for i in range(1, len(arr)):
    if count == 0:
        candidate = arr[i]
        count = 1
    elif arr[i] == candidate:
        count += 1
    else:
        count -= 1

print(f"Majority Element: {candidate}")
```

**Output:**
```
Majority Element: 3
```

**Explanation**: Boyer-Moore algorithm finds the majority element in O(n) time and O(1) space. Very popular in placements!

</details>

---

### Q61. What will be the output? (List comprehension)

```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
```

<details>
<summary>Answer</summary>

```
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

**Explanation**: List comprehensions create lists in a single line. The nested one creates a 2D matrix (list of lists).

</details>

---

### Q62. Flatten a 2D list into a 1D list.

<details>
<summary>Answer</summary>

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Method 1: Using nested loop
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print(flat)

# Method 2: Using list comprehension
flat = [num for row in matrix for num in row]
print(flat)
```

**Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</details>

---

### Q63. Sort a list without using sort() — Implement Bubble Sort.

<details>
<summary>Answer</summary>

```python
arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
```

**Output:**
```
[11, 12, 22, 25, 34, 64, 90]
```

**Explanation**: Bubble Sort compares adjacent elements and swaps them if out of order. Time: O(n^2). Know this for placements!

</details>

---

### Q64. Find the subarray with the maximum sum (Kadane's Algorithm).

```
Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6 (subarray: [4, -1, 2, 1])
```

<details>
<summary>Answer</summary>

```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(f"Maximum Subarray Sum: {max_sum}")
```

**Output:**
```
Maximum Subarray Sum: 6
```

**Explanation**: Kadane's Algorithm — at each step, decide whether to add current element to existing subarray or start fresh. Time: O(n). One of the most asked placement questions!

</details>

---

### Q65. Find leaders in an array.

A leader is an element that is greater than all elements to its right.

```
Input:  [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
```

<details>
<summary>Answer</summary>

```python
arr = [16, 17, 4, 3, 5, 2]
leaders = []

max_from_right = arr[-1]
leaders.append(max_from_right)

for i in range(len(arr) - 2, -1, -1):
    if arr[i] > max_from_right:
        leaders.append(arr[i])
        max_from_right = arr[i]

leaders.reverse()
print(leaders)
```

**Output:**
```
[17, 5, 2]
```

**Explanation**: Traverse from right, track the maximum. If current element is greater than max, it's a leader.

</details>

---

### Q66. Check if a list is sorted (ascending).

<details>
<summary>Answer</summary>

```python
arr = [1, 2, 3, 4, 5]

is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
print(f"Is sorted: {is_sorted}")

# Manual approach
def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(f"Is sorted: {check_sorted(arr)}")
```

**Output:**
```
Is sorted: True
Is sorted: True
```

</details>

---

### Q67. Find the equilibrium index of an array.

Equilibrium index = index where sum of left elements = sum of right elements.

```
Input:  [-7, 1, 5, 2, -4, 3, 0]
Output: 3 (left sum = -1, right sum = -1)
```

<details>
<summary>Answer</summary>

```python
arr = [-7, 1, 5, 2, -4, 3, 0]
total = sum(arr)
left_sum = 0

for i in range(len(arr)):
    right_sum = total - left_sum - arr[i]
    if left_sum == right_sum:
        print(f"Equilibrium index: {i}")
        break
    left_sum += arr[i]
```

**Output:**
```
Equilibrium index: 3
```

</details>

---

### Q68. Find duplicate elements in a list.

<details>
<summary>Answer</summary>

```python
arr = [1, 3, 4, 2, 3, 1, 5, 4]
seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    seen.add(num)

print(f"Duplicates: {list(duplicates)}")
```

**Output:**
```
Duplicates: [1, 3, 4]
```

</details>

---

### Q69. Find the first non-repeating element in a list.

<details>
<summary>Answer</summary>

```python
arr = [5, 3, 4, 3, 5, 4, 6, 7, 6]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print(f"First non-repeating: {num}")
        break
```

**Output:**
```
First non-repeating: 7
```

</details>

---

### Q70. Implement Selection Sort.

<details>
<summary>Answer</summary>

```python
arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
```

**Output:**
```
[11, 12, 22, 25, 64]
```

**Explanation**: Find the minimum element from the unsorted portion and place it at the beginning. Time: O(n^2).

</details>

---

### Q71. What will be the output? (List methods)

```python
arr = [3, 1, 4, 1, 5, 9]
arr.append(2)
print(arr)

arr.insert(0, 99)
print(arr)

arr.remove(1)   # removes first occurrence of 1
print(arr)

popped = arr.pop()  # removes and returns last element
print(f"Popped: {popped}, List: {arr}")

print(f"Count of 1: {arr.count(1)}")
print(f"Index of 5: {arr.index(5)}")
```

<details>
<summary>Answer</summary>

```
[3, 1, 4, 1, 5, 9, 2]
[99, 3, 1, 4, 1, 5, 9, 2]
[99, 3, 4, 1, 5, 9, 2]
Popped: 2, List: [99, 3, 4, 1, 5, 9]
Count of 1: 1
Index of 5: 4
```

</details>

---

### Q72. What is the difference between shallow copy and deep copy?

<details>
<summary>Answer</summary>

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy — inner lists are still shared
shallow = original.copy()
shallow[0][0] = 99
print(f"Original: {original}")  # [[99, 2], [3, 4]] — CHANGED!

# Reset
original = [[1, 2], [3, 4]]

# Deep copy — completely independent
deep = copy.deepcopy(original)
deep[0][0] = 99
print(f"Original: {original}")  # [[1, 2], [3, 4]] — NOT changed
```

**Output:**
```
Original: [[99, 2], [3, 4]]
Original: [[1, 2], [3, 4]]
```

**Explanation**: Shallow copy copies the outer list but shares inner objects. Deep copy creates completely independent copies at all levels.

</details>

---

### Q73. Find the Kth largest element in a list.

<details>
<summary>Answer</summary>

```python
arr = [3, 2, 1, 5, 6, 4]
k = 2

# Method 1: Sort and index
sorted_arr = sorted(arr, reverse=True)
print(f"{k}th largest: {sorted_arr[k - 1]}")

# Method 2: Using set to remove duplicates first
unique_sorted = sorted(set(arr), reverse=True)
print(f"{k}th largest (unique): {unique_sorted[k - 1]}")
```

**Output:**
```
2th largest: 5
2th largest (unique): 5
```

</details>

---

### Q74. Dutch National Flag Problem — Sort an array of 0s, 1s, and 2s.

```
Input:  [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

<details>
<summary>Answer</summary>

```python
arr = [2, 0, 2, 1, 1, 0]
low, mid, high = 0, 0, len(arr) - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:  # arr[mid] == 2
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)
```

**Output:**
```
[0, 0, 1, 1, 2, 2]
```

**Explanation**: Three pointers — `low` (0s boundary), `mid` (current), `high` (2s boundary). Time: O(n), Space: O(1). Very popular placement question!

</details>

---

### Q75. Trapping Rain Water Problem.

```
Input:  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
```

<details>
<summary>Answer</summary>

```python
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(height)

left_max = [0] * n
right_max = [0] * n

left_max[0] = height[0]
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], height[i])

right_max[n - 1] = height[n - 1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], height[i])

water = 0
for i in range(n):
    water += min(left_max[i], right_max[i]) - height[i]

print(f"Trapped water: {water}")
```

**Output:**
```
Trapped water: 6
```

**Explanation**: For each bar, water = `min(left_max, right_max) - height`. Very popular LeetCode and placement question!

</details>

---

## Section 5: Strings (Q76 – Q100)

---

### Q76. What will be the output?

```python
s = "Hello, World!"
print(s[0])
print(s[-1])
print(s[7:12])
print(s[:5])
print(s[::-1])
print(len(s))
```

<details>
<summary>Answer</summary>

```
H
!
World
Hello
!dlroW ,olleH
13
```

</details>

---

### Q77. Reverse a string.

<details>
<summary>Answer</summary>

```python
s = "Python"

# Method 1: Slicing
print(s[::-1])

# Method 2: Using reversed()
print("".join(reversed(s)))

# Method 3: Manual loop
result = ""
for char in s:
    result = char + result
print(result)
```

**Output:**
```
nohtyP
nohtyP
nohtyP
```

</details>

---

### Q78. Check if a string is a palindrome.

<details>
<summary>Answer</summary>

```python
s = "madam"

# Method 1: Slicing
if s == s[::-1]:
    print(f"'{s}' is a Palindrome")
else:
    print(f"'{s}' is NOT a Palindrome")

# Method 2: Two-pointer approach
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome(s))
```

**Output:**
```
'madam' is a Palindrome
True
```

</details>

---

### Q79. Count vowels and consonants in a string.

<details>
<summary>Answer</summary>

```python
s = "Hello World"
vowels = consonants = 0

for ch in s.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print(f"Vowels: {vowels}, Consonants: {consonants}")
```

**Output:**
```
Vowels: 3, Consonants: 7
```

</details>

---

### Q80. Count the frequency of each character in a string.

<details>
<summary>Answer</summary>

```python
s = "programming"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for char, count in freq.items():
    print(f"'{char}' : {count}")
```

**Output:**
```
'p' : 1
'r' : 2
'o' : 1
'g' : 2
'a' : 1
'm' : 2
'i' : 1
'n' : 1
```

</details>

---

### Q81. Find the first non-repeating character in a string.

<details>
<summary>Answer</summary>

```python
s = "aabbccdde"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(f"First non-repeating: '{ch}'")
        break
else:
    print("No non-repeating character")
```

**Output:**
```
First non-repeating: 'e'
```

**Explanation**: Build frequency map, then find the first character with count 1. Very common in placements!

</details>

---

### Q82. Check if two strings are anagrams.

Two strings are anagrams if they have the same characters with the same frequency.

```
"listen" and "silent" -> True
```

<details>
<summary>Answer</summary>

```python
s1 = "listen"
s2 = "silent"

# Method 1: Sorting
print(sorted(s1) == sorted(s2))

# Method 2: Using frequency count
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        freq[ch] = freq.get(ch, 0) - 1
    return all(v == 0 for v in freq.values())

print(are_anagrams(s1, s2))
```

**Output:**
```
True
True
```

</details>

---

### Q83. Reverse each word in a sentence.

```
Input:  "Hello World Python"
Output: "olleH dlroW nohtyP"
```

<details>
<summary>Answer</summary>

```python
s = "Hello World Python"

result = " ".join(word[::-1] for word in s.split())
print(result)
```

**Output:**
```
olleH dlroW nohtyP
```

**Explanation**: `split()` breaks into words, `[::-1]` reverses each word, `" ".join()` combines them back.

</details>

---

### Q84. Reverse the order of words in a sentence.

```
Input:  "Hello World Python"
Output: "Python World Hello"
```

<details>
<summary>Answer</summary>

```python
s = "Hello World Python"

result = " ".join(s.split()[::-1])
print(result)
```

**Output:**
```
Python World Hello
```

</details>

---

### Q85. Remove all duplicate characters from a string.

<details>
<summary>Answer</summary>

```python
s = "programming"
result = ""
seen = set()

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)

# One-liner
print("".join(dict.fromkeys(s)))
```

**Output:**
```
progamin
progamin
```

</details>

---

### Q86. Check if a string contains only digits.

<details>
<summary>Answer</summary>

```python
s1 = "12345"
s2 = "123a5"

print(f"'{s1}' is all digits: {s1.isdigit()}")
print(f"'{s2}' is all digits: {s2.isdigit()}")

# Other useful checks
print("hello".isalpha())     # True - only letters
print("hello123".isalnum())  # True - letters and digits
print("HELLO".isupper())     # True - all uppercase
print("hello".islower())     # True - all lowercase
print("  ".isspace())        # True - only whitespace
```

**Output:**
```
'12345' is all digits: True
'123a5' is all digits: False
True
True
True
True
True
```

</details>

---

### Q87. Convert a string to title case without using title().

<details>
<summary>Answer</summary>

```python
s = "hello world python programming"
words = s.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:].lower())

print(" ".join(result))
```

**Output:**
```
Hello World Python Programming
```

</details>

---

### Q88. Find the longest word in a sentence.

<details>
<summary>Answer</summary>

```python
s = "Python programming is really fun"
words = s.split()
longest = max(words, key=len)

print(f"Longest word: '{longest}' (length: {len(longest)})")
```

**Output:**
```
Longest word: 'programming' (length: 11)
```

</details>

---

### Q89. Count the number of words in a string.

<details>
<summary>Answer</summary>

```python
s = "  Hello   World   Python  "

# Method 1: Using split() — handles multiple spaces
word_count = len(s.split())
print(f"Word count: {word_count}")

# Method 2: Manual counting
count = 0
in_word = False
for ch in s:
    if ch != ' ' and not in_word:
        count += 1
        in_word = True
    elif ch == ' ':
        in_word = False

print(f"Word count: {count}")
```

**Output:**
```
Word count: 3
Word count: 3
```

</details>

---

### Q90. Replace all spaces with a specific character (URL encoding style).

```
Input:  "Hello World Python"
Output: "Hello%20World%20Python"
```

<details>
<summary>Answer</summary>

```python
s = "Hello World Python"

# Method 1: Using replace()
print(s.replace(" ", "%20"))

# Method 2: Manual
result = ""
for ch in s:
    if ch == " ":
        result += "%20"
    else:
        result += ch
print(result)
```

**Output:**
```
Hello%20World%20Python
Hello%20World%20Python
```

</details>

---

### Q91. Find all permutations of a string.

<details>
<summary>Answer</summary>

```python
def permutations(s, left, right):
    if left == right:
        print("".join(s), end=" ")
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]
            permutations(s, left + 1, right)
            s[left], s[i] = s[i], s[left]  # backtrack

s = "ABC"
permutations(list(s), 0, len(s) - 1)
```

**Output:**
```
ABC ACB BAC BCA CBA CAB
```

**Explanation**: Uses recursion and backtracking. Total permutations = n!. Common placement question!

</details>

---

### Q92. Find the longest common prefix among a list of strings.

```
Input:  ["flower", "flow", "flight"]
Output: "fl"
```

<details>
<summary>Answer</summary>

```python
strs = ["flower", "flow", "flight"]
prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break

print(f"Longest Common Prefix: '{prefix}'")
```

**Output:**
```
Longest Common Prefix: 'fl'
```

**Explanation**: Start with the first string as the prefix. Keep shrinking it until it matches the start of every string. LeetCode classic!

</details>

---

### Q93. Check if a string is a valid parentheses sequence.

```
Input:  "((()))"  -> True
Input:  "(()("    -> False
```

<details>
<summary>Answer</summary>

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0

print(is_valid("(())"))      # True
print(is_valid("({[]})"))    # True
print(is_valid("(()"))       # False
print(is_valid("([)]"))      # False
```

**Output:**
```
True
True
False
False
```

**Explanation**: Use a stack. Push opening brackets, pop on closing brackets and check if they match. Extremely common placement question!

</details>

---

### Q94. Find the longest palindromic substring.

```
Input:  "babad"
Output: "bab" or "aba"
```

<details>
<summary>Answer</summary>

```python
def longest_palindrome(s):
    result = ""

    def expand(left, right):
        nonlocal result
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(result):
                result = s[left:right + 1]
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)      # Odd-length palindromes
        expand(i, i + 1)  # Even-length palindromes

    return result

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
```

**Output:**
```
bab
bb
```

**Explanation**: Expand around each character (and between characters) to find palindromes. Time: O(n^2). Very popular in placements!

</details>

---

### Q95. Compress a string using character counts.

```
Input:  "aaabbbccdd"
Output: "a3b3c2d2"
```

<details>
<summary>Answer</summary>

```python
s = "aaabbbccdd"
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)  # Don't forget the last group

print(result)
```

**Output:**
```
a3b3c2d2
```

**Explanation**: Run-Length Encoding — count consecutive occurrences and encode as character + count.

</details>

---

### Q96. Find all substrings of a string.

<details>
<summary>Answer</summary>

```python
s = "abc"

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j], end=" ")
```

**Output:**
```
a ab abc b bc c
```

**Explanation**: Total substrings of a string of length n = `n * (n + 1) / 2`.

</details>

---

### Q97. Check if one string is a rotation of another.

```
Input:  s1 = "abcde", s2 = "cdeab"
Output: True (rotate left by 2)
```

<details>
<summary>Answer</summary>

```python
s1 = "abcde"
s2 = "cdeab"

if len(s1) == len(s2) and s2 in (s1 + s1):
    print(f"'{s2}' is a rotation of '{s1}'")
else:
    print("Not a rotation")
```

**Output:**
```
'cdeab' is a rotation of 'abcde'
```

**Explanation**: If `s2` is a rotation of `s1`, then `s2` will always be a substring of `s1 + s1`. Brilliant trick! Very commonly asked!

</details>

---

### Q98. Convert a string to an integer without using int() (Implement atoi).

<details>
<summary>Answer</summary>

```python
def my_atoi(s):
    s = s.strip()
    if not s:
        return 0

    sign = 1
    i = 0

    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1

    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord('0'))
        i += 1

    return sign * result

print(my_atoi("   -42"))
print(my_atoi("4193 with words"))
print(my_atoi("+123"))
```

**Output:**
```
-42
4193
123
```

**Explanation**: Parse sign, then convert digit characters to integer using `ord(ch) - ord('0')`. Classic placement question!

</details>

---

### Q99. Find the minimum number of operations to convert one string to another (Edit Distance).

```
Input:  s1 = "horse", s2 = "ros"
Output: 3
```

<details>
<summary>Answer</summary>

```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )

    return dp[m][n]

print(f"Edit Distance: {edit_distance('horse', 'ros')}")
print(f"Edit Distance: {edit_distance('intention', 'execution')}")
```

**Output:**
```
Edit Distance: 3
Edit Distance: 5
```

**Explanation**: Dynamic Programming approach. Build a 2D table where `dp[i][j]` = min operations to convert `s1[0:i]` to `s2[0:j]`. Advanced placement question!

</details>

---

### Q100. Find the longest substring without repeating characters.

```
Input:  "abcabcbb"
Output: 3 ("abc")
```

<details>
<summary>Answer</summary>

```python
def longest_unique_substring(s):
    char_index = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len

print(f"Length: {longest_unique_substring('abcabcbb')}")
print(f"Length: {longest_unique_substring('bbbbb')}")
print(f"Length: {longest_unique_substring('pwwkew')}")
```

**Output:**
```
Length: 3
Length: 1
Length: 3
```

**Explanation**: Sliding Window technique. Maintain a window `[start, end]` that contains unique characters. Use a dictionary to track the last seen index of each character. Time: O(n). One of the most asked LeetCode + placement questions!

</details>

---

## Quick Reference: Topic Distribution

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| 1 | Data Types & Variables | Q1 – Q15 | Beginner |
| 2 | Control Flow & Conditions | Q16 – Q25 | Beginner |
| 3 | Loops | Q26 – Q45 | Beginner to Intermediate |
| 4 | Lists / Arrays | Q46 – Q75 | Intermediate to Advanced |
| 5 | Strings | Q76 – Q100 | Intermediate to Advanced |

## Top 10 Most Asked in Placements

| # | Question | Section |
|---|----------|---------|
| 1 | Two Sum (Find pair with target sum) | Q59 |
| 2 | Reverse a String / Palindrome Check | Q77, Q78 |
| 3 | Anagram Check | Q82 |
| 4 | Missing Number in Array | Q54 |
| 5 | Kadane's Algorithm (Max Subarray Sum) | Q64 |
| 6 | Valid Parentheses | Q93 |
| 7 | Fibonacci Series | Q34 |
| 8 | Longest Substring Without Repeating | Q100 |
| 9 | Dutch National Flag (Sort 0s, 1s, 2s) | Q74 |
| 10 | String Rotation Check | Q97 |

---

> **Tip**: Try solving each question yourself first before looking at the answer. Practice writing the code by hand (on paper) — many placement interviews require this!
