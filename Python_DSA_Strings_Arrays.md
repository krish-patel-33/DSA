# 🐍 100 Python DSA Questions — Strings & Arrays (Lists)

> **Topics Covered**: String Manipulation, Slicing, List Operations, Searching, Sorting, Sliding Window, Two Pointers, Matrix  
> **Difficulty**: Beginner → Intermediate → Advanced (Placement Level)  
> **Language**: Python 3  
> **Author**: Practice Notes | May 2026

---

## 📚 Table of Contents

| Section | Questions | Difficulty |
|---------|-----------|------------|
| [1. String Basics](#section-1-string-basics-q1--q10) | Q1 – Q10 | ⭐ Beginner |
| [2. String Methods & Operations](#section-2-string-methods--operations-q11--q20) | Q11 – Q20 | ⭐ Beginner |
| [3. String Pattern Problems](#section-3-string-pattern-problems-q21--q30) | Q21 – Q30 | ⭐⭐ Intermediate |
| [4. String Advanced Problems](#section-4-string-advanced-problems-q31--q40) | Q31 – Q40 | ⭐⭐⭐ Advanced |
| [5. String Placement Level](#section-5-string-placement-level-q41--q50) | Q41 – Q50 | 🔥 Placement |
| [6. Array (List) Basics](#section-6-array-list-basics-q51--q60) | Q51 – Q60 | ⭐ Beginner |
| [7. Array Searching & Sorting](#section-7-array-searching--sorting-q61--q70) | Q61 – Q70 | ⭐⭐ Intermediate |
| [8. Array Two Pointers & Sliding Window](#section-8-array-two-pointers--sliding-window-q71--q80) | Q71 – Q80 | ⭐⭐⭐ Advanced |
| [9. Array Matrix / 2D List](#section-9-array-matrix--2d-list-q81--q90) | Q81 – Q90 | ⭐⭐⭐ Advanced |
| [10. Array Placement Level](#section-10-array-placement-level-q91--q100) | Q91 – Q100 | 🔥 Placement |

---

# 🔤 PART A — STRINGS

---

## Section 1: String Basics (Q1 – Q10)

---

### Q1. What will be the output?

```python
s1 = "Hello"
s2 = "Hello"
s3 = "".join(['H', 'e', 'l', 'l', 'o'])

print(s1 == s2)
print(s1 is s2)
print(s1 == s3)
print(s1 is s3)
```

<details>
<summary>Answer</summary>

```
True
True
True
True
```

**Explanation**: `==` compares values, `is` compares identity (same object). Python **interns** short strings and string literals, so `s1` and `s2` point to the same object. `s3` may also be interned depending on implementation.

> 💡 **Key Rule**: Always use `==` to compare string values, never rely on `is` for string comparison.

</details>

---

### Q2. What will be the output?

```python
s = "Python"
print(len(s))
print(s[0])
print(s[-1])
print(s[1:4])
print(s[::-1])
```

<details>
<summary>Answer</summary>

```
6
P
n
yth
nohtyP
```

**Explanation**: `len()` returns the length. Indexing is 0-based; negative indices count from the end (`-1` = last). Slicing `[start:stop]` extracts from `start` to `stop-1`. `[::-1]` reverses the string.

> 💡 **Python Power**: `s[::-1]` is the most Pythonic way to reverse a string.

</details>

---

### Q3. What will be the output?

```python
s = "Hello World"
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.capitalize())
```

<details>
<summary>Answer</summary>

```
HELLO WORLD
hello world
Hello World
hELLO wORLD
Hello world
```

**Explanation**: `upper()` → all uppercase. `lower()` → all lowercase. `title()` → capitalize first letter of each word. `swapcase()` → swap cases. `capitalize()` → capitalize only the first character, lowercase the rest.

</details>

---

### Q4. What will be the output?

```python
s = "  Hello Python  "
print(f"[{s.strip()}]")
print(f"[{s.lstrip()}]")
print(f"[{s.rstrip()}]")
print(s.replace("Python", "World"))
```

<details>
<summary>Answer</summary>

```
[Hello Python]
[Hello Python  ]
[  Hello Python]
  Hello World  
```

**Explanation**: `strip()` removes leading & trailing whitespace. `lstrip()` removes only left, `rstrip()` only right. `replace()` replaces all occurrences of a substring.

</details>

---

### Q5. What will be the output?

```python
s = "Hello World Python"
print(s.find("World"))
print(s.find("xyz"))
print(s.index("World"))
print(s.count("o"))
print(s.startswith("Hello"))
print(s.endswith("Python"))
```

<details>
<summary>Answer</summary>

```
6
-1
6
2
True
True
```

**Explanation**: `find()` returns index or `-1` if not found. `index()` returns index but raises `ValueError` if not found. `count()` counts occurrences. `startswith()` and `endswith()` check prefixes/suffixes.

> 💡 **Tip**: Use `find()` when you want to avoid exceptions. Use `index()` when absence means a bug.

</details>

---

### Q6. Are Strings mutable or immutable in Python? Prove it.

```python
s = "Hello"
print(id(s))

s = s + " World"
print(id(s))

# Try to modify in-place
try:
    s[0] = "h"
except TypeError as e:
    print(f"Error: {e}")
```

<details>
<summary>Answer</summary>

```
140234567890 (some id)
140234567891 (different id)
Error: 'str' object does not support item assignment
```

**Explanation**: Strings in Python are **immutable**. You cannot change individual characters. When you concatenate with `+`, a **new string object** is created (different `id`). This is why string concatenation in loops is slow — use `"".join()` instead.

</details>

---

### Q7. What will be the output?

```python
s = "Python Programming"
print(s.split())
print(s.split("o"))
print("-".join(["Hello", "World", "Python"]))
print(" ".join("Hello"))
```

<details>
<summary>Answer</summary>

```
['Python', 'Programming']
['Pyth', 'n Pr', 'gramming']
Hello-World-Python
H e l l o
```

**Explanation**: `split()` splits by whitespace (default). `split("o")` splits at every `"o"`. `join()` joins an iterable with the separator. `" ".join("Hello")` treats the string as an iterable of characters.

</details>

---

### Q8. What will be the output?

```python
s = ""
print(len(s) == 0)
print(not s)       # Falsy check
print(bool(s))

s2 = "   "
print(len(s2) == 0)
print(not s2)
print(s2.isspace())
```

<details>
<summary>Answer</summary>

```
True
True
False
False
False
True
```

**Explanation**: Empty string `""` is **falsy** in Python. `not ""` is `True`. A string with only spaces is **not empty** but `isspace()` returns `True`. Use `not s.strip()` to check if a string is empty or has only whitespace.

</details>

---

### Q9. String formatting methods in Python.

```python
name = "Python"
version = 3.12

# f-string (Python 3.6+) — PREFERRED
print(f"Language: {name}, Version: {version}")

# .format()
print("Language: {}, Version: {}".format(name, version))

# % formatting (old style)
print("Language: %s, Version: %.1f" % (name, version))

# f-string with expressions
print(f"2 + 3 = {2 + 3}")
print(f"{'hello':>15}")  # Right-aligned, width 15
print(f"{3.14159:.2f}")   # 2 decimal places
```

<details>
<summary>Answer</summary>

```
Language: Python, Version: 3.12
Language: Python, Version: 3.12
Language: Python, Version: 3.1
2 + 3 = 5
          hello
3.14
```

**Explanation**: f-strings are the most readable and fastest. `.format()` is versatile. `%` formatting is legacy. Format specs: `>` right-align, `.2f` two decimal places.

</details>

---

### Q10. String type-checking methods.

```python
print("hello".isalpha())    # Only letters?
print("12345".isdigit())    # Only digits?
print("hello123".isalnum()) # Letters or digits?
print("HELLO".isupper())    # All uppercase?
print("hello".islower())    # All lowercase?
print("   ".isspace())      # Only whitespace?
print("Hello World".istitle())  # Title case?
```

<details>
<summary>Answer</summary>

```
True
True
True
True
True
True
True
```

**Explanation**: Python provides many `is*()` methods for checking string properties. These are commonly used for input validation. All return `False` for empty strings.

</details>

---

## Section 2: String Methods & Operations (Q11 – Q20)

---

### Q11. Reverse a String.

```python
s = "Hello World"

# Method 1: Slicing (Pythonic)
rev1 = s[::-1]
print(rev1)

# Method 2: reversed() + join
rev2 = "".join(reversed(s))
print(rev2)

# Method 3: Two pointers (manual — interview style)
chars = list(s)
left, right = 0, len(chars) - 1
while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1
print("".join(chars))
```

<details>
<summary>Answer</summary>

```
dlroW olleH
dlroW olleH
dlroW olleH
```

**Explanation**: Method 1 (`[::-1]`) is the most Pythonic. Method 2 uses built-in `reversed()`. Method 3 uses the **two-pointer technique** — preferred in interviews to demonstrate understanding.

</details>

---

### Q12. Check if a String is a palindrome.

```python
s = "madam"

# Method 1: Slicing
if s == s[::-1]:
    print(f"'{s}' is a Palindrome")
else:
    print(f"'{s}' is NOT a Palindrome")

# Method 2: Two pointers (interview approach)
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

<details>
<summary>Answer</summary>

```
'madam' is a Palindrome
True
False
```

**Explanation**: A palindrome reads the same forwards and backwards. Slicing is clean for Python. Two-pointer is O(1) space and interview-friendly.

</details>

---

### Q13. Count the frequency of each character.

```python
s = "programming"

# Method 1: Dictionary
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1

for char, count in freq.items():
    print(f"{char} → {count}")

print()

# Method 2: collections.Counter (Pythonic)
from collections import Counter
counter = Counter(s)
print(counter)
print(counter.most_common(3))  # Top 3 most frequent
```

<details>
<summary>Answer</summary>

```
p → 1
r → 2
o → 1
g → 2
a → 1
m → 2
i → 1
n → 1

Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
[('r', 2), ('g', 2), ('m', 2)]
```

**Explanation**: `dict.get(key, default)` avoids `KeyError`. `Counter` from `collections` is the Pythonic way — gives frequency counts and has `most_common()` built-in.

> 💡 **Interview Tip**: Mention `Counter` but also know the manual approach.

</details>

---

### Q14. Find the first non-repeating character.

```python
from collections import Counter

def first_non_repeating(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

s = "aabbcdd"
result = first_non_repeating(s)
print(f"First non-repeating: {result}")

# Without Counter
def first_non_repeating_manual(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in s:
        if freq[c] == 1:
            return c
    return None

print(first_non_repeating_manual("swiss"))  # 'w'
```

<details>
<summary>Answer</summary>

```
First non-repeating: c
w
```

**Explanation**: Two-pass approach: first count frequencies, then find the first character with count 1. Order is preserved because we iterate the original string in the second pass. Time: O(n), Space: O(1) (at most 26 characters).

</details>

---

### Q15. Check if two Strings are anagrams.

```python
# Method 1: Sort and compare
def is_anagram_sort(s1, s2):
    return sorted(s1) == sorted(s2)

# Method 2: Counter (optimal Pythonic)
from collections import Counter
def is_anagram_counter(s1, s2):
    return Counter(s1) == Counter(s2)

# Method 3: Frequency array (manual)
def is_anagram_manual(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = [0] * 26
    for c in s1:
        freq[ord(c) - ord('a')] += 1
    for c in s2:
        freq[ord(c) - ord('a')] -= 1
    return all(f == 0 for f in freq)

print(is_anagram_sort("listen", "silent"))       # True
print(is_anagram_counter("listen", "silent"))     # True
print(is_anagram_manual("listen", "silent"))      # True
print(is_anagram_counter("hello", "world"))       # False
```

<details>
<summary>Answer</summary>

```
True
True
True
False
```

**Explanation**: Anagrams have the same character frequencies. 
- **Sort**: O(n log n) — simplest.
- **Counter**: O(n) — most Pythonic.
- **Frequency array**: O(n) — shows understanding for interviews.

</details>

---

### Q16. Count words in a String.

```python
s = "  Python is  a great  language  "

# Method 1: split() — handles multiple spaces
words = s.split()
print(f"Word count: {len(words)}")
print(f"Words: {words}")

# Method 2: Manual count
def count_words(s):
    count = 0
    in_word = False
    for c in s:
        if c != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count

print(f"Manual count: {count_words(s)}")
```

<details>
<summary>Answer</summary>

```
Word count: 5
Words: ['Python', 'is', 'a', 'great', 'language']
Manual count: 5
```

**Explanation**: `split()` without arguments splits by any whitespace and removes empty strings. The manual method uses a flag to track word boundaries.

</details>

---

### Q17. Reverse each word in a String.

```python
s = "Hello World Python"

# Method 1: Pythonic one-liner
result = " ".join(word[::-1] for word in s.split())
print(result)

# Method 2: Manual
words = s.split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
print(" ".join(reversed_words))
```

<details>
<summary>Answer</summary>

```
olleH dlroW nohtyP
olleH dlroW nohtyP
```

**Explanation**: Split into words, reverse each word individually using slicing, and join back. The one-liner uses a generator expression.

</details>

---

### Q18. Reverse the order of words in a String.

```python
s = "Hello World Python"

# Method 1: Pythonic
result = " ".join(s.split()[::-1])
print(result)

# Method 2: Using reversed()
result2 = " ".join(reversed(s.split()))
print(result2)

# Method 3: Manual with extra spaces handling
s2 = "  Hello   World  Python  "
result3 = " ".join(s2.split()[::-1])
print(result3)
```

<details>
<summary>Answer</summary>

```
Python World Hello
Python World Hello
Python World Hello
```

**Explanation**: `split()` → list of words, `[::-1]` → reverse the list, `" ".join()` → join back. Handles extra spaces automatically. This is a very common interview question.

</details>

---

### Q19. Remove all duplicate characters from a String.

```python
s = "programming"

# Method 1: dict.fromkeys() — preserves order
result1 = "".join(dict.fromkeys(s))
print(result1)

# Method 2: Seen set — preserves order
seen = set()
result2 = []
for c in s:
    if c not in seen:
        seen.add(c)
        result2.append(c)
print("".join(result2))

# Method 3: List comprehension (compact)
seen3 = set()
result3 = "".join(c for c in s if not (c in seen3 or seen3.add(c)))
print(result3)
```

<details>
<summary>Answer</summary>

```
progamin
progamin
progamin
```

**Explanation**: `dict.fromkeys()` preserves insertion order and removes duplicates (since dict keys are unique). The set-based approach is explicit and interview-friendly. All are O(n).

</details>

---

### Q20. Convert a String to an integer without using `int()`.

```python
def str_to_int(s):
    num = 0
    negative = False
    i = 0

    if s[0] == '-':
        negative = True
        i = 1
    elif s[0] == '+':
        i = 1

    while i < len(s):
        digit = ord(s[i]) - ord('0')
        num = num * 10 + digit
        i += 1

    return -num if negative else num

print(str_to_int("12345"))    # 12345
print(str_to_int("-42"))      # -42
print(str_to_int("12345") + 10)  # 12355 (proves it's an int)
```

<details>
<summary>Answer</summary>

```
12345
-42
12355
```

**Explanation**: `ord(c) - ord('0')` converts a digit character to its integer value. Build the number by multiplying by 10 and adding each digit. Handle sign separately.

> 💡 **Key Concept**: `ord('5') - ord('0') = 53 - 48 = 5`

</details>

---

## Section 3: String Pattern Problems (Q21 – Q30)

---

### Q21. Check if a String contains only digits.

```python
def is_numeric(s):
    if not s:
        return False
    for c in s:
        if not ('0' <= c <= '9'):
            return False
    return True

print(is_numeric("12345"))   # True
print(is_numeric("123a5"))   # False

# Pythonic ways
print("12345".isdigit())     # True
print("12345".isnumeric())   # True (also handles unicode numbers)
```

<details>
<summary>Answer</summary>

```
True
False
True
True
```

**Explanation**: Check each character against `'0'`–`'9'`. Python's `isdigit()` and `isnumeric()` do this natively. `isnumeric()` also recognizes Unicode numerals like ² and ½.

</details>

---

### Q22. Count vowels and consonants.

```python
def count_vowels_consonants(s):
    vowels = consonants = 0
    for c in s.lower():
        if c.isalpha():
            if c in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

s = "Hello World"
v, c = count_vowels_consonants(s)
print(f"Vowels: {v}")
print(f"Consonants: {c}")
```

<details>
<summary>Answer</summary>

```
Vowels: 3
Consonants: 7
```

**Explanation**: Convert to lowercase, check if alphabetic, then check against vowel set. Using `in "aeiou"` is a clean Python idiom.

</details>

---

### Q23. Find all permutations of a String.

```python
def permute(s, left, right, result):
    if left == right:
        result.append(s)
        return
    
    for i in range(left, right + 1):
        # Swap
        s_list = list(s)
        s_list[left], s_list[i] = s_list[i], s_list[left]
        s = "".join(s_list)
        
        permute(s, left + 1, right, result)
        
        # Backtrack
        s_list = list(s)
        s_list[left], s_list[i] = s_list[i], s_list[left]
        s = "".join(s_list)

result = []
permute("ABC", 0, 2, result)
for p in result:
    print(p)

print()

# Pythonic way using itertools
from itertools import permutations
for p in permutations("ABC"):
    print("".join(p))
```

<details>
<summary>Answer</summary>

```
ABC
ACB
BAC
BCA
CBA
CAB

ABC
ACB
BAC
BCA
CAB
CBA
```

**Explanation**: **Backtracking** approach — fix each character at the current position, recursively permute the rest, then swap back. `itertools.permutations` is the Pythonic shortcut. Total: n! permutations.

> 💡 **Time Complexity**: O(n × n!) — n! permutations, each takes O(n).

</details>

---

### Q24. Check if a String is a rotation of another.

```python
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

print(is_rotation("abcde", "cdeab"))   # True
print(is_rotation("abcde", "abced"))   # False
```

<details>
<summary>Answer</summary>

```
True
False
```

**Explanation**: If `s2` is a rotation of `s1`, then `s2` must be a substring of `s1 + s1`. Example: `"abcde" + "abcde" = "abcdeabcde"` contains `"cdeab"`. Brilliant one-liner trick!

</details>

---

### Q25. Find the longest common prefix.

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))

# Pythonic using zip
def lcp_zip(strs):
    if not strs:
        return ""
    prefix = []
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            prefix.append(chars[0])
        else:
            break
    return "".join(prefix)

print(lcp_zip(["flower", "flow", "flight"]))
```

<details>
<summary>Answer</summary>

```
fl
fl
```

**Explanation**: Method 1: Start with the first string as prefix, shrink until it matches all. Method 2: `zip(*strs)` groups characters by position; stop when characters differ. **LeetCode #14**.

</details>

---

### Q26. Compress a String using counts of repeated characters.

```python
def compress(s):
    result = []
    count = 1
    
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

print(compress("aabcccccaaa"))
print(compress("abc"))
```

<details>
<summary>Answer</summary>

```
a2b1c5a3
abc
```

**Explanation**: Count consecutive characters. If the compressed version is longer, return the original. **Cracking the Coding Interview 1.6**.

</details>

---

### Q27. Check if two Strings are one edit apart.

```python
def is_one_edit(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    shorter = s1 if len(s1) < len(s2) else s2
    longer = s1 if len(s1) >= len(s2) else s2
    
    i = j = 0
    found_diff = False
    
    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            if found_diff:
                return False
            found_diff = True
            if len(shorter) == len(longer):
                i += 1  # Replace: advance both
        else:
            i += 1
        j += 1
    
    return True

print(is_one_edit("pale", "ple"))     # True (remove)
print(is_one_edit("pales", "pale"))   # True (remove)
print(is_one_edit("pale", "bale"))    # True (replace)
print(is_one_edit("pale", "bake"))    # False
```

<details>
<summary>Answer</summary>

```
True
True
True
False
```

**Explanation**: Three operations: insert, delete, replace. If lengths differ by >1, impossible. Walk through with two pointers, allow at most one difference. **Cracking the Coding Interview 1.5**.

</details>

---

### Q28. Find the longest substring without repeating characters.

```python
def length_of_longest_substring(s):
    char_set = set()
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))      # 1 ("b")
print(length_of_longest_substring("pwwkew"))     # 3 ("wke")
```

<details>
<summary>Answer</summary>

```
3
1
3
```

**Explanation**: **Sliding Window** technique. Expand right pointer; when a duplicate is found, shrink from the left. Track the maximum window. **LeetCode #3**. Time: O(n).

</details>

---

### Q29. Generate all substrings of a String.

```python
s = "abc"
print(f"All substrings of '{s}':")

substrings = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])

for sub in substrings:
    print(sub)

print(f"\nTotal substrings: {len(substrings)}")

# One-liner using list comprehension
subs = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
print(f"Total: {len(subs)}")
```

<details>
<summary>Answer</summary>

```
All substrings of 'abc':
a
ab
abc
b
bc
c

Total substrings: 6
Total: 6
```

**Explanation**: Two nested loops — outer for start, inner for end. Total substrings = n(n+1)/2. The list comprehension is the Pythonic approach.

</details>

---

### Q30. Naive pattern matching — find first occurrence of pattern in text.

```python
def find_pattern(text, pattern):
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1

text = "hello world hello"
pattern = "world"
idx = find_pattern(text, pattern)
print(f"Pattern found at index: {idx}")

# Python built-in
print(f"Using find(): {text.find(pattern)}")
print(f"Using index(): {text.index(pattern)}")
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 6
Using find(): 6
Using index(): 6
```

**Explanation**: Slide the pattern over the text one character at a time. For each position, check all characters. Time: O(n×m) worst case. Python's `find()` and `index()` use optimized algorithms internally.

</details>

---

## Section 4: String Advanced Problems (Q31 – Q40)

---

### Q31. Find the longest palindromic substring.

```python
def longest_palindrome(s):
    if len(s) < 2:
        return s
    
    start, max_len = 0, 1
    
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1  # start, length
    
    for i in range(len(s)):
        # Odd length
        s1, l1 = expand_from_center(i, i)
        # Even length
        s2, l2 = expand_from_center(i, i + 1)
        
        if l1 > max_len:
            start, max_len = s1, l1
        if l2 > max_len:
            start, max_len = s2, l2
    
    return s[start:start + max_len]

print(longest_palindrome("babad"))    # "bab" or "aba"
print(longest_palindrome("cbbd"))     # "bb"
print(longest_palindrome("racecar"))  # "racecar"
```

<details>
<summary>Answer</summary>

```
bab
bb
racecar
```

**Explanation**: **Expand Around Center** technique. For each position, try expanding outward for both odd-length and even-length palindromes. **LeetCode #5**. Time: O(n²), Space: O(1).

</details>

---

### Q32. Implement `atoi` — String to Integer with edge cases.

```python
def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    i = 0
    result = 0
    INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
    
    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1
    
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    result *= sign
    return max(INT_MIN, min(INT_MAX, result))

print(my_atoi("   -42"))           # -42
print(my_atoi("4193 with words"))  # 4193
print(my_atoi("words and 987"))    # 0
print(my_atoi("91283472332"))      # 2147483647 (clamped)
```

<details>
<summary>Answer</summary>

```
-42
4193
0
2147483647
```

**Explanation**: Handle: leading whitespace, optional sign, digits, non-digit stop, overflow clamping. **LeetCode #8**.

</details>

---

### Q33. Count and Say sequence.

```python
def count_and_say(n):
    result = "1"
    
    for _ in range(2, n + 1):
        new_result = []
        count = 1
        
        for j in range(1, len(result)):
            if result[j] == result[j - 1]:
                count += 1
            else:
                new_result.append(str(count) + result[j - 1])
                count = 1
        new_result.append(str(count) + result[-1])
        result = "".join(new_result)
    
    return result

for i in range(1, 7):
    print(f"n={i}: {count_and_say(i)}")
```

<details>
<summary>Answer</summary>

```
n=1: 1
n=2: 11
n=3: 21
n=4: 1211
n=5: 111221
n=6: 312211
```

**Explanation**: Each term describes the previous. `1` → "one 1" → `11` → "two 1s" → `21` → "one 2, one 1" → `1211`. **LeetCode #38**.

</details>

---

### Q34. Group anagrams together.

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
for group in result:
    print(group)
```

<details>
<summary>Answer</summary>

```
['eat', 'tea', 'ate']
['tan', 'nat']
['bat']
```

**Explanation**: Sort each string to get a canonical key — all anagrams share the same sorted form. Use `defaultdict(list)` to group them. **LeetCode #49**. Time: O(n × k log k), where k is the max string length.

> 💡 **Alternative key**: Use `tuple(Counter(s).items())` — but sorted is simpler.

</details>

---

### Q35. Longest Common Subsequence (LCS).

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

print(f"LCS Length: {lcs('abcde', 'ace')}")
print(f"LCS Length: {lcs('abc', 'abc')}")
print(f"LCS Length: {lcs('abc', 'def')}")
```

<details>
<summary>Answer</summary>

```
LCS Length: 3
LCS Length: 3
LCS Length: 0
```

**Explanation**: Classic **Dynamic Programming**. `dp[i][j]` = LCS length of `s1[:i]` and `s2[:j]`. If characters match, add 1 to diagonal. Otherwise, take max of left or top. **LeetCode #1143**. Time: O(m×n).

</details>

---

### Q36. KMP Pattern Matching Algorithm.

```python
def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j  # Match found
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

text = "ababcababababcababd"
pattern = "ababd"
print(f"Pattern found at index: {kmp_search(text, pattern)}")
print(f"LPS array for '{pattern}': {build_lps(pattern)}")
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 13
LPS array for 'ababd': [0, 0, 1, 2, 0]
```

**Explanation**: KMP precomputes the **LPS (Longest Proper Prefix which is also Suffix)** array. On mismatch, it uses LPS to skip characters instead of restarting. Time: O(n + m).

> 💡 **Must-Know**: KMP is a top interview topic for string pattern matching.

</details>

---

### Q37. Minimum deletions to make a String a palindrome.

```python
def longest_palindromic_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

s = "aebcbda"
lps = longest_palindromic_subseq(s)
print(f"Longest Palindromic Subsequence: {lps}")
print(f"Min deletions: {len(s) - lps}")
```

<details>
<summary>Answer</summary>

```
Longest Palindromic Subsequence: 5
Min deletions: 2
```

**Explanation**: Min deletions = `len(s) - LPS length`. The LPS of `"aebcbda"` is `"abcba"` (length 5), so deletions = 7 - 5 = 2. Uses **DP** on intervals.

</details>

---

### Q38. Check if a String has all unique characters (without extra data structures).

```python
# Method 1: Bit manipulation — works for lowercase a-z
def is_unique_bits(s):
    checker = 0
    for c in s:
        bit = ord(c) - ord('a')
        if (checker & (1 << bit)) > 0:
            return False
        checker |= (1 << bit)
    return True

# Method 2: Set (Pythonic but uses extra space)
def is_unique_set(s):
    return len(set(s)) == len(s)

print(is_unique_bits("abcdef"))   # True
print(is_unique_bits("abcaef"))   # False
print(is_unique_set("abcdef"))    # True
print(is_unique_set("abcaef"))    # False
```

<details>
<summary>Answer</summary>

```
True
False
True
False
```

**Explanation**: Bit manipulation uses an integer as a **bit vector** — each bit represents a character. If the bit is already set, it's a duplicate. **Cracking the Coding Interview 1.1**. O(n) time, O(1) space.

</details>

---

### Q39. Decode a run-length encoded String.

```python
def decode(encoded):
    result = []
    i = 0
    
    while i < len(encoded):
        char = encoded[i]
        count = int(encoded[i + 1])
        result.append(char * count)
        i += 2
    
    return "".join(result)

encoded = "a2b1c5a3"
print(decode(encoded))

# General version (handles multi-digit counts)
def decode_general(encoded):
    result = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        num = ""
        while i < len(encoded) and encoded[i].isdigit():
            num += encoded[i]
            i += 1
        result.append(char * int(num))
    return "".join(result)

print(decode_general("a12b3c1"))
```

<details>
<summary>Answer</summary>

```
aabcccccaaa
aaaaaaaaaaaabbbc
```

**Explanation**: Read character then its count, repeat the character that many times. The general version handles multi-digit counts. This is the reverse of string compression (Q26).

</details>

---

### Q40. Minimum window substring.

```python
from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    need = Counter(t)
    window = {}
    have, required = 0, len(need)
    result = ""
    min_len = float('inf')
    left = 0
    
    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        
        if c in need and window[c] == need[c]:
            have += 1
        
        while have == required:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            # Shrink window
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            left += 1
    
    return result

print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("a", "a"))
print(min_window("a", "aa"))
```

<details>
<summary>Answer</summary>

```
BANC
a

```

**Explanation**: Classic **Sliding Window**. Expand right to include all chars of `t`, then shrink left to minimize. Track when all required characters are satisfied. **LeetCode #76**. Time: O(n).

</details>

---

## Section 5: String Placement Level (Q41 – Q50)

---

### Q41. Rabin-Karp pattern matching using hashing.

```python
def rabin_karp(text, pattern):
    d = 256       # alphabet size
    q = 101       # prime number
    m, n = len(pattern), len(text)
    p_hash = t_hash = 0
    h = pow(d, m - 1, q)
    results = []
    
    # Calculate initial hashes
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:  # Confirm match
                results.append(i)
        
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
    
    return results

text = "aaabcxyzaaabc"
pattern = "aaabc"
matches = rabin_karp(text, pattern)
for idx in matches:
    print(f"Pattern found at index: {idx}")
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 0
Pattern found at index: 8
```

**Explanation**: Rabin-Karp uses a **rolling hash** to quickly filter positions. Only does character-by-character check on hash matches. Average: O(n+m), Worst: O(nm).

</details>

---

### Q42. Valid parentheses.

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

print(is_valid("()[]{}"))   # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True
```

<details>
<summary>Answer</summary>

```
True
False
False
True
```

**Explanation**: Use a **Stack**. Push opening brackets. On closing brackets, pop and check if they match. The mapping dict makes it clean. **LeetCode #20**. Time: O(n).

</details>

---

### Q43. Longest repeating character replacement.

```python
def character_replacement(s, k):
    count = {}
    max_count = max_len = left = 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(character_replacement("AABABBA", 1))  # 4
print(character_replacement("ABAB", 2))     # 4
```

<details>
<summary>Answer</summary>

```
4
4
```

**Explanation**: Sliding window. Key insight: a valid window has `window_size - max_frequency <= k`. If invalid, shrink from the left. **LeetCode #424**. Time: O(n).

</details>

---

### Q44. Generate all valid combinations of n pairs of parentheses.

```python
def generate_parentheses(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

for p in generate_parentheses(3):
    print(p)
```

<details>
<summary>Answer</summary>

```
((()))
(()())
(())()
()(())
()()()
```

**Explanation**: **Backtracking**. At each step, add `(` if open_count < n, or `)` if close_count < open_count (ensures validity). **LeetCode #22**.

</details>

---

### Q45. Multiply two numbers represented as Strings.

```python
def multiply(num1, num2):
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            
            result[p2] = total % 10
            result[p1] += total // 10
    
    # Remove leading zeros
    result_str = "".join(str(d) for d in result).lstrip("0")
    return result_str or "0"

print(multiply("123", "456"))
print(multiply("0", "0"))
```

<details>
<summary>Answer</summary>

```
56088
0
```

**Explanation**: Simulates grade-school multiplication. Each pair of digits contributes to position `i + j` and `i + j + 1`. **LeetCode #43**. Time: O(m×n).

</details>

---

### Q46. Wildcard pattern matching.

```python
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # Handle leading *
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][n]

print(is_match("adceb", "*a*b"))    # True
print(is_match("acdcb", "a*c?b"))   # False
```

<details>
<summary>Answer</summary>

```
True
False
```

**Explanation**: `?` matches any single char, `*` matches any sequence (including empty). Uses **DP**. **LeetCode #44**. Time: O(m×n).

</details>

---

### Q47. Longest palindrome that can be built from a String's characters.

```python
from collections import Counter

def longest_palindrome(s):
    count = Counter(s)
    length = 0
    has_odd = False
    
    for freq in count.values():
        length += (freq // 2) * 2
        if freq % 2 != 0:
            has_odd = True
    
    return length + 1 if has_odd else length

print(longest_palindrome("abccccdd"))  # 7
print(longest_palindrome("a"))         # 1
print(longest_palindrome("aabb"))      # 4
```

<details>
<summary>Answer</summary>

```
7
1
4
```

**Explanation**: Use all character pairs + at most one odd character in the center. `"dccaccd"` is one valid palindrome of length 7. **LeetCode #409**.

</details>

---

### Q48. Edit Distance (Levenshtein Distance).

```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
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
                    dp[i - 1][j - 1],  # Replace
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1]       # Insert
                )
    
    return dp[m][n]

print(edit_distance("horse", "ros"))      # 3
print(edit_distance("intention", "execution"))  # 5
```

<details>
<summary>Answer</summary>

```
3
5
```

**Explanation**: Classic **DP**. Min operations (insert, delete, replace) to convert one string to another. `horse → ros`: replace h→r, remove r, remove e = 3 edits. **LeetCode #72**. Time: O(m×n).

</details>

---

### Q49. Regular expression matching (`.` and `*`).

```python
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc.
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Zero occurrences
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # One or more
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][n]

print(is_match("aa", "a"))       # False
print(is_match("aa", "a*"))      # True
print(is_match("ab", ".*"))      # True
print(is_match("aab", "c*a*b"))  # True
```

<details>
<summary>Answer</summary>

```
False
True
True
True
```

**Explanation**: `.` matches any single char, `*` means zero or more of the preceding char. **LeetCode #10** (Hard). Time: O(m×n).

</details>

---

### Q50. Z-Algorithm for pattern matching.

```python
def z_search(text, pattern):
    combined = pattern + "$" + text
    z = build_z_array(combined)
    results = []
    
    for i in range(len(z)):
        if z[i] == len(pattern):
            results.append(i - len(pattern) - 1)
    
    return results

def build_z_array(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    
    return z

text = "aaabcxyzaaabc"
pattern = "aaabc"
matches = z_search(text, pattern)
for idx in matches:
    print(f"Pattern found at index: {idx}")
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 0
Pattern found at index: 8
```

**Explanation**: Z-array at position `i` stores the length of the longest substring starting at `i` that matches a prefix. Concatenate `pattern + "$" + text` and find where Z-value equals pattern length. Time: O(n + m).

</details>

---

# 📦 PART B — ARRAYS (Lists)

---

## Section 6: Array (List) Basics (Q51 – Q60)

---

### Q51. Create, access, and print a list.

```python
# Create lists
arr1 = [10, 20, 30, 40, 50]
arr2 = list(range(1, 6))
arr3 = [0] * 5  # [0, 0, 0, 0, 0]

# Access
print(arr1[0])      # First element
print(arr1[-1])     # Last element
print(arr1[1:4])    # Slicing

# Print
print(arr1)
print(*arr1)  # Unpacked — prints without brackets

# Useful properties
print(f"Length: {len(arr1)}")
print(f"Sum: {sum(arr1)}")
print(f"Max: {max(arr1)}")
print(f"Min: {min(arr1)}")
```

<details>
<summary>Answer</summary>

```
10
50
[20, 30, 40]
[10, 20, 30, 40, 50]
10 20 30 40 50
Length: 5
Sum: 150
Max: 50
Min: 10
```

**Explanation**: Python lists are dynamic arrays. Negative indexing, slicing, and built-in functions like `len()`, `sum()`, `max()`, `min()` are extremely powerful. `*arr` unpacks the list.

</details>

---

### Q52. Find the largest and smallest element.

```python
arr = [12, 35, 1, 10, 34, 1]

# Method 1: Built-in
print(f"Max: {max(arr)}, Min: {min(arr)}")

# Method 2: Manual (interview approach)
maximum = minimum = arr[0]

for num in arr[1:]:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"Max: {maximum}, Min: {minimum}")
```

<details>
<summary>Answer</summary>

```
Max: 35, Min: 1
Max: 35, Min: 1
```

**Explanation**: Built-in `max()` and `min()` are clean. Manual approach iterates once — O(n) time, O(1) space. Interview expects the manual approach.

</details>

---

### Q53. Find the sum and average.

```python
arr = [10, 20, 30, 40, 50]

total = sum(arr)
average = total / len(arr)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")

# Manual
total_manual = 0
for val in arr:
    total_manual += val
print(f"Manual Sum: {total_manual}")
```

<details>
<summary>Answer</summary>

```
Sum: 150
Average: 30.00
Manual Sum: 150
```

**Explanation**: `sum()` is built-in. `.2f` format spec gives 2 decimal places. Division in Python 3 always returns float.

</details>

---

### Q54. Reverse a list in-place.

```python
arr = [1, 2, 3, 4, 5]

# Method 1: Slicing (creates new list)
rev1 = arr[::-1]
print(rev1)

# Method 2: reverse() method (in-place)
arr2 = [1, 2, 3, 4, 5]
arr2.reverse()
print(arr2)

# Method 3: Two pointers (in-place, interview)
arr3 = [1, 2, 3, 4, 5]
left, right = 0, len(arr3) - 1
while left < right:
    arr3[left], arr3[right] = arr3[right], arr3[left]
    left += 1
    right -= 1
print(arr3)
```

<details>
<summary>Answer</summary>

```
[5, 4, 3, 2, 1]
[5, 4, 3, 2, 1]
[5, 4, 3, 2, 1]
```

**Explanation**: `[::-1]` creates a new list. `.reverse()` modifies in-place. Two-pointer swap is the interview-preferred approach — O(n) time, O(1) space.

</details>

---

### Q55. Check if a list is sorted.

```python
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Pythonic one-liner
def is_sorted_pythonic(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

print(is_sorted([1, 2, 3, 4, 5]))   # True
print(is_sorted([1, 3, 2, 4, 5]))   # False
print(is_sorted_pythonic([1, 2, 3])) # True
```

<details>
<summary>Answer</summary>

```
True
False
True
```

**Explanation**: Compare each element with its predecessor. `all()` with a generator is the Pythonic one-liner. Time: O(n).

</details>

---

### Q56. Remove duplicates from a sorted list (in-place).

```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return j + 1

arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_len = remove_duplicates(arr)
print(f"New length: {new_len}")
print(f"Result: {arr[:new_len]}")

# Pythonic (creates new list)
arr2 = [1, 1, 2, 2, 3, 4, 4, 5]
print(f"Using set: {sorted(set(arr2))}")
print(f"Using dict: {list(dict.fromkeys(arr2))}")
```

<details>
<summary>Answer</summary>

```
New length: 5
Result: [1, 2, 3, 4, 5]
Using set: [1, 2, 3, 4, 5]
Using dict: [1, 2, 3, 4, 5]
```

**Explanation**: Slow pointer `j` tracks unique positions. When a new unique is found, place it at `j+1`. **LeetCode #26**. `set()` is Pythonic but doesn't preserve order (though sorted fixes that). `dict.fromkeys()` preserves order.

</details>

---

### Q57. Left rotate a list by one position.

```python
arr = [1, 2, 3, 4, 5]

# Method 1: Slicing (Pythonic)
rotated = arr[1:] + arr[:1]
print(rotated)

# Method 2: pop and append
arr2 = [1, 2, 3, 4, 5]
first = arr2.pop(0)
arr2.append(first)
print(arr2)

# Method 3: Manual shift
arr3 = [1, 2, 3, 4, 5]
first = arr3[0]
for i in range(len(arr3) - 1):
    arr3[i] = arr3[i + 1]
arr3[-1] = first
print(arr3)
```

<details>
<summary>Answer</summary>

```
[2, 3, 4, 5, 1]
[2, 3, 4, 5, 1]
[2, 3, 4, 5, 1]
```

**Explanation**: Slicing is the cleanest. `pop(0)` is O(n) since it shifts all elements. Manual shift makes the operation explicit.

</details>

---

### Q58. Left rotate a list by K positions.

```python
def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Method 1: Slicing (Pythonic)
    return arr[k:] + arr[:k]

# Method 2: Reversal algorithm (in-place, O(1) space)
def rotate_left_inplace(arr, k):
    n = len(arr)
    k = k % n
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

arr = [1, 2, 3, 4, 5, 6, 7]
print(rotate_left(arr, 3))

arr2 = [1, 2, 3, 4, 5, 6, 7]
rotate_left_inplace(arr2, 3)
print(arr2)
```

<details>
<summary>Answer</summary>

```
[4, 5, 6, 7, 1, 2, 3]
[4, 5, 6, 7, 1, 2, 3]
```

**Explanation**: Slicing is O(n) time and space. **Reversal algorithm** is O(n) time, O(1) space — reverse first k, reverse rest, reverse all. This is the optimal interview approach.

</details>

---

### Q59. Move all zeros to the end.

```python
def move_zeros(arr):
    j = 0  # Position for next non-zero
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

arr = [0, 1, 0, 3, 12]
move_zeros(arr)
print(arr)

# Pythonic (creates new list)
arr2 = [0, 1, 0, 3, 12]
result = [x for x in arr2 if x != 0] + [0] * arr2.count(0)
print(result)
```

<details>
<summary>Answer</summary>

```
[1, 3, 12, 0, 0]
[1, 3, 12, 0, 0]
```

**Explanation**: Use pointer `j` to track the position for the next non-zero. Swap non-zeros to the front. **LeetCode #283**. Time: O(n), Space: O(1). The Pythonic way is clean but uses extra space.

</details>

---

### Q60. Find the second largest element.

```python
def second_largest(arr):
    first = second = float('-inf')
    
    for val in arr:
        if val > first:
            second = first
            first = val
        elif val > second and val != first:
            second = val
    
    return second if second != float('-inf') else None

arr = [12, 35, 1, 10, 34, 1]
print(f"Second largest: {second_largest(arr)}")

# Pythonic (but O(n log n) due to sorting)
unique = sorted(set(arr), reverse=True)
print(f"Second largest: {unique[1] if len(unique) > 1 else None}")
```

<details>
<summary>Answer</summary>

```
Second largest: 34
Second largest: 34
```

**Explanation**: Track both largest and second largest in a single pass. Update `second` when `first` changes or when current is between them. Time: O(n), Space: O(1).

</details>

---

## Section 7: Array Searching & Sorting (Q61 – Q70)

---

### Q61. Linear Search.

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
idx = linear_search(arr, 30)
print(f"Found at index: {idx}" if idx != -1 else "Not found")

# Pythonic
print(f"Using index(): {arr.index(30)}")
print(f"Using 'in': {30 in arr}")
```

<details>
<summary>Answer</summary>

```
Found at index: 2
Using index(): 2
Using 'in': True
```

**Explanation**: Check each element sequentially. Time: O(n). Python's `in` operator and `.index()` use linear search under the hood. `.index()` raises `ValueError` if not found.

</details>

---

### Q62. Binary Search (iterative and recursive).

```python
# Iterative
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Recursive
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"Iterative: {binary_search(arr, 23)}")
print(f"Recursive: {binary_search_recursive(arr, 23, 0, len(arr) - 1)}")

# Python built-in
import bisect
print(f"bisect: {bisect.bisect_left(arr, 23)}")
```

<details>
<summary>Answer</summary>

```
Iterative: 5
Recursive: 5
bisect: 5
```

**Explanation**: Halves the search space each time. **Requires sorted data**. Time: O(log n). `bisect` module provides efficient binary search in Python.

</details>

---

### Q63. Bubble Sort.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Already sorted

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
```

<details>
<summary>Answer</summary>

```
[11, 12, 22, 25, 34, 64, 90]
```

**Explanation**: Repeatedly swap adjacent elements if in wrong order. `swapped` flag optimizes for nearly sorted arrays. Time: O(n²) worst, O(n) best. Space: O(1). **Stable sort**.

</details>

---

### Q64. Selection Sort.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)
```

<details>
<summary>Answer</summary>

```
[11, 12, 22, 25, 64]
```

**Explanation**: Find the minimum in the unsorted portion and place it at the correct position. Time: O(n²) always. Space: O(1). Makes minimum swaps: O(n). **Not stable**.

</details>

---

### Q65. Insertion Sort.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
```

<details>
<summary>Answer</summary>

```
[5, 6, 11, 12, 13]
```

**Explanation**: Build sorted array one element at a time by inserting each into its correct position. Time: O(n²) worst, O(n) best (nearly sorted). **Stable sort**. Best for small/nearly sorted data.

</details>

---

### Q66. Merge Sort.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
```

<details>
<summary>Answer</summary>

```
[3, 9, 10, 27, 38, 43, 82]
```

**Explanation**: **Divide and Conquer** — split in half, sort each, merge sorted halves. Time: O(n log n) always. Space: O(n). **Stable sort**. Python's `sorted()` uses **Timsort** which is hybrid merge+insertion sort.

</details>

---

### Q67. Quick Sort.

```python
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

# Pythonic one-liner (for fun, not in-place)
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    return qsort([x for x in arr[1:] if x < pivot]) + [pivot] + qsort([x for x in arr[1:] if x >= pivot])

print(qsort([10, 7, 8, 9, 1, 5]))
```

<details>
<summary>Answer</summary>

```
[1, 5, 7, 8, 9, 10]
[1, 5, 7, 8, 9, 10]
```

**Explanation**: Pick pivot, partition (smaller left, larger right), recurse. Time: O(n log n) average, O(n²) worst. Space: O(log n). **Not stable**. The one-liner is elegant but uses O(n) extra space.

</details>

---

### Q68. Count occurrences using Binary Search.

```python
def find_first(arr, target):
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_last(arr, target):
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

arr = [1, 2, 2, 2, 2, 3, 4, 5]
first = find_first(arr, 2)
last = find_last(arr, 2)
print(f"Count of 2: {last - first + 1}" if first != -1 else "Not found")

# Pythonic using bisect
import bisect
count = bisect.bisect_right(arr, 2) - bisect.bisect_left(arr, 2)
print(f"Using bisect: {count}")
```

<details>
<summary>Answer</summary>

```
Count of 2: 4
Using bisect: 4
```

**Explanation**: Find first and last occurrence using modified binary search. Count = `last - first + 1`. **LeetCode #34**. `bisect` module makes this trivial. Time: O(log n).

</details>

---

### Q69. Find the peak element.

```python
def find_peak(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]

arr = [1, 3, 20, 4, 1, 0]
print(f"Peak element: {find_peak(arr)}")
```

<details>
<summary>Answer</summary>

```
Peak element: 20
```

**Explanation**: A peak is greater than its neighbors. Binary search: if `arr[mid] < arr[mid+1]`, peak is right; otherwise left or at mid. **LeetCode #162**. Time: O(log n).

</details>

---

### Q70. Search in a rotated sorted array.

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
print(f"Found at index: {search_rotated(arr, 0)}")
print(f"Found at index: {search_rotated(arr, 3)}")
```

<details>
<summary>Answer</summary>

```
Found at index: 4
Found at index: -1
```

**Explanation**: One half is always sorted. Check which half is sorted, then check if target lies in that range. **LeetCode #33**. Time: O(log n).

</details>

---

## Section 8: Array Two Pointers & Sliding Window (Q71 – Q80)

---

### Q71. Two Sum.

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2, 7, 11, 15]
result = two_sum(nums, 9)
print(f"Indices: {result}")
```

<details>
<summary>Answer</summary>

```
Indices: [0, 1]
```

**Explanation**: Use a dictionary to store `{value: index}`. For each number, check if its complement exists. **LeetCode #1**. Time: O(n), Space: O(n).

> 💡 **Most asked interview question** across all companies!

</details>

---

### Q72. Container With Most Water.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Max area: {max_area(height)}")
```

<details>
<summary>Answer</summary>

```
Max area: 49
```

**Explanation**: **Two Pointers** — start from both ends. Move the shorter pointer inward to potentially find a taller line. **LeetCode #11**. Time: O(n).

</details>

---

### Q73. Three Sum.

```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
```

<details>
<summary>Answer</summary>

```
[[-1, -1, 2], [-1, 0, 1]]
```

**Explanation**: Sort, fix one element, use two pointers for the rest. Skip duplicates at all levels. **LeetCode #15**. Time: O(n²).

</details>

---

### Q74. Maximum subarray sum (Kadane's Algorithm).

```python
def max_subarray(arr):
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Max subarray sum: {max_subarray(arr)}")

# Also find the subarray itself
def max_subarray_with_indices(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i
    
    return max_sum, arr[start:end + 1]

max_val, subarray = max_subarray_with_indices(arr)
print(f"Max sum: {max_val}, Subarray: {subarray}")
```

<details>
<summary>Answer</summary>

```
Max subarray sum: 6
Max sum: 6, Subarray: [4, -1, 2, 1]
```

**Explanation**: **Kadane's Algorithm** — at each position, either start new or extend previous subarray. Track global max. **LeetCode #53**. Time: O(n), Space: O(1).

> 💡 **Most asked DSA question** in interviews. Know this by heart!

</details>

---

### Q75. Maximum sum subarray of size K (Sliding Window).

```python
def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide window
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Max sum of subarray of size {k}: {max_sum_subarray_k(arr, k)}")
```

<details>
<summary>Answer</summary>

```
Max sum of subarray of size 3: 9
```

**Explanation**: **Fixed-size Sliding Window**. Initialize with first k elements. Then slide by adding the next and removing the first of the window. Time: O(n), much better than O(n×k) brute force.

</details>

---

### Q76. Longest subarray with sum K.

```python
def longest_subarray_sum_k(arr, k):
    prefix_map = {}  # {prefix_sum: first_index}
    total = 0
    max_len = 0
    
    for i in range(len(arr)):
        total += arr[i]
        
        if total == k:
            max_len = i + 1
        
        if (total - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[total - k])
        
        if total not in prefix_map:
            prefix_map[total] = i
    
    return max_len

arr = [10, 5, 2, 7, 1, 9]
print(f"Longest subarray length: {longest_subarray_sum_k(arr, 15)}")
```

<details>
<summary>Answer</summary>

```
Longest subarray length: 4
```

**Explanation**: **Prefix Sum + HashMap**. Store `{prefix_sum: first_index}`. If `prefix_sum - k` exists, a subarray with sum k ends here. Time: O(n), Space: O(n).

</details>

---

### Q77. Sort an array of 0s, 1s, and 2s (Dutch National Flag).

```python
def sort_012(arr):
    low = mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [2, 0, 2, 1, 1, 0]
sort_012(arr)
print(arr)
```

<details>
<summary>Answer</summary>

```
[0, 0, 1, 1, 2, 2]
```

**Explanation**: **Dutch National Flag Algorithm** by Dijkstra. Three pointers: `low` (0s boundary), `mid` (current), `high` (2s boundary). Single pass! **LeetCode #75**. Time: O(n), Space: O(1).

</details>

---

### Q78. Find the majority element (Moore's Voting Algorithm).

```python
def majority_element(arr):
    candidate = arr[0]
    count = 1
    
    for num in arr[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate

arr = [2, 2, 1, 1, 1, 2, 2]
print(f"Majority element: {majority_element(arr)}")

# Pythonic
from collections import Counter
c = Counter(arr)
print(f"Using Counter: {c.most_common(1)[0][0]}")
```

<details>
<summary>Answer</summary>

```
Majority element: 2
Using Counter: 2
```

**Explanation**: **Boyer-Moore Voting Algorithm**. Cancel out different elements; the majority survives. **LeetCode #169**. Time: O(n), Space: O(1). `Counter.most_common(1)` is the Pythonic shortcut.

</details>

---

### Q79. Trapping Rain Water.

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    
    return water

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Water trapped: {trap(height)}")
```

<details>
<summary>Answer</summary>

```
Water trapped: 6
```

**Explanation**: **Two Pointers**. Water at each position = `min(left_max, right_max) - height[i]`. Move the pointer with the smaller max. **LeetCode #42** (Hard). Time: O(n), Space: O(1).

</details>

---

### Q80. Longest consecutive sequence.

```python
def longest_consecutive(nums):
    num_set = set(nums)
    max_len = 0
    
    for num in num_set:
        # Only start from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            max_len = max(max_len, length)
    
    return max_len

nums = [100, 4, 200, 1, 3, 2]
print(f"Longest consecutive: {longest_consecutive(nums)}")
```

<details>
<summary>Answer</summary>

```
Longest consecutive: 4
```

**Explanation**: Use a set for O(1) lookups. Only start counting from numbers with no predecessor (no `num-1`). Sequence `1,2,3,4` → length 4. **LeetCode #128**. Time: O(n).

</details>

---

## Section 9: Array Matrix / 2D List (Q81 – Q90)

---

### Q81. Create and print a 2D list (matrix).

```python
# Create
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print formatted
for row in matrix:
    for val in row:
        print(f"{val:4d}", end="")
    print()

print(f"Rows: {len(matrix)}")
print(f"Cols: {len(matrix[0])}")

# Access
print(f"Element [1][2]: {matrix[1][2]}")

# Create using list comprehension
m, n = 3, 4
grid = [[0] * n for _ in range(m)]
print(grid)
```

<details>
<summary>Answer</summary>

```
   1   2   3
   4   5   6
   7   8   9
Rows: 3
Cols: 3
Element [1][2]: 6
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

**Explanation**: 2D lists are lists of lists. `len(matrix)` = rows, `len(matrix[0])` = cols. **Warning**: Never use `[[0]*n]*m` — it creates references to the same inner list!

> 💡 **Common Bug**: `[[0]*4]*3` → modifying one row modifies all rows. Use `[[0]*4 for _ in range(3)]` instead.

</details>

---

### Q82. Transpose a matrix.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Method 1: List comprehension
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in transpose:
    print(row)

print()

# Method 2: zip (Pythonic one-liner)
transpose2 = [list(row) for row in zip(*matrix)]
for row in transpose2:
    print(row)
```

<details>
<summary>Answer</summary>

```
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```

**Explanation**: Swap rows and columns: `transpose[i][j] = matrix[j][i]`. The `zip(*matrix)` trick is beautifully Pythonic — `*` unpacks the rows, `zip` groups by column.

</details>

---

### Q83. Rotate a matrix 90 degrees clockwise.

```python
def rotate_90(matrix):
    n = len(matrix)
    
    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_90(matrix)

for row in matrix:
    print(row)

# Pythonic one-liner (creates new matrix)
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
rotated = [list(row) for row in zip(*matrix2[::-1])]
print("\nOne-liner:")
for row in rotated:
    print(row)
```

<details>
<summary>Answer</summary>

```
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]

One-liner:
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

**Explanation**: Transpose + reverse each row = 90° clockwise. **LeetCode #48**. Time: O(n²), Space: O(1) in-place. The one-liner `zip(*matrix[::-1])` is a Python classic.

</details>

---

### Q84. Spiral order traversal.

```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(spiral_order(matrix))
```

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

**Explanation**: Maintain four boundaries. Traverse right → down → left → up, shrinking boundaries each time. **LeetCode #54**. Time: O(m×n).

</details>

---

### Q85. Search in a row-wise and column-wise sorted matrix.

```python
def search_matrix(matrix, target):
    row, col = 0, len(matrix[0]) - 1  # Start top-right
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return (-1, -1)

matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]

result = search_matrix(matrix, 29)
print(f"Found at: {result}")
```

<details>
<summary>Answer</summary>

```
Found at: (2, 1)
```

**Explanation**: Start top-right. If current > target, go left. If current < target, go down. **LeetCode #240**. Time: O(m + n).

</details>

---

### Q86. Set matrix zeroes.

```python
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row = first_col = False
    
    # Check first row/col
    for j in range(n):
        if matrix[0][j] == 0:
            first_row = True
    for i in range(m):
        if matrix[i][0] == 0:
            first_col = True
    
    # Use first row/col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Zero out based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Handle first row/col
    if first_row:
        for j in range(n):
            matrix[0][j] = 0
    if first_col:
        for i in range(m):
            matrix[i][0] = 0

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
set_zeroes(matrix)
for row in matrix:
    print(row)
```

<details>
<summary>Answer</summary>

```
[1, 0, 1]
[0, 0, 0]
[1, 0, 1]
```

**Explanation**: Use the first row/column as markers. **LeetCode #73**. Time: O(m×n), Space: O(1).

</details>

---

### Q87. Matrix multiplication.

```python
def matrix_multiply(A, B):
    m, k, n = len(A), len(A[0]), len(B[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += A[i][p] * B[p][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = matrix_multiply(A, B)
for row in result:
    print(row)
```

<details>
<summary>Answer</summary>

```
[19, 22]
[43, 50]
```

**Explanation**: `result[i][j] = sum(A[i][p] * B[p][j])` for all p. Time: O(m × n × k). A(m×k) × B(k×n) = result(m×n).

</details>

---

### Q88. Print matrix in diagonal order.

```python
from collections import defaultdict

def diagonal_order(matrix):
    if not matrix:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    
    for d in range(m + n - 1):
        diagonal = []
        row = 0 if d < n else d - n + 1
        col = d if d < n else n - 1
        
        while row < m and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        
        if d % 2 == 0:
            diagonal.reverse()
        result.extend(diagonal)
    
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_order(matrix))
```

<details>
<summary>Answer</summary>

```
[1, 2, 4, 7, 5, 3, 6, 8, 9]
```

**Explanation**: Traverse diagonals alternating direction. **LeetCode #498**. Time: O(m×n).

</details>

---

### Q89. Find the row with the maximum number of 1s (rows sorted).

```python
def row_with_max_1s(matrix):
    max_row = -1
    j = len(matrix[0]) - 1
    
    for i in range(len(matrix)):
        while j >= 0 and matrix[i][j] == 1:
            max_row = i
            j -= 1
    
    return max_row

matrix = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
]
print(f"Row with max 1s: {row_with_max_1s(matrix)}")
```

<details>
<summary>Answer</summary>

```
Row with max 1s: 2
```

**Explanation**: Start top-right. If cell is 1, move left (this row has more 1s). If 0, move down. Time: O(m + n) — optimal!

</details>

---

### Q90. Find all paths from top-left to bottom-right.

```python
def find_paths(grid, r, c, path, all_paths):
    m, n = len(grid), len(grid[0])
    path.append(grid[r][c])
    
    if r == m - 1 and c == n - 1:
        all_paths.append(path[:])  # Copy the path
    else:
        if r + 1 < m:
            find_paths(grid, r + 1, c, path, all_paths)
        if c + 1 < n:
            find_paths(grid, r, c + 1, path, all_paths)
    
    path.pop()  # Backtrack

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

all_paths = []
find_paths(grid, 0, 0, [], all_paths)
for p in all_paths:
    print(p)
```

<details>
<summary>Answer</summary>

```
[1, 4, 7, 8, 9]
[1, 4, 5, 8, 9]
[1, 4, 5, 6, 9]
[1, 2, 5, 8, 9]
[1, 2, 5, 6, 9]
[1, 2, 3, 6, 9]
```

**Explanation**: **Backtracking** — from each cell, go right or down. At bottom-right, save the path. `path[:]` creates a copy to avoid mutation. Time: O(2^(m+n)).

</details>

---

## Section 10: Array Placement Level (Q91 – Q100)

---

### Q91. Merge two sorted arrays without extra space.

```python
def merge_without_space(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = (n + m + 1) // 2
    
    def get_val(i):
        return arr1[i] if i < n else arr2[i - n]
    
    def set_val(i, val):
        if i < n:
            arr1[i] = val
        else:
            arr2[i - n] = val
    
    while gap > 0:
        i, j = 0, gap
        while j < n + m:
            vi, vj = get_val(i), get_val(j)
            if vi > vj:
                set_val(i, vj)
                set_val(j, vi)
            i += 1
            j += 1
        gap = 1 if gap == 1 and gap != (n + m + 1) // 2 else (gap + 1) // 2
        if gap == 1 and gap == (n + m + 1) // 2:
            break

# Simpler approach using pointer comparison
def merge_simple(arr1, arr2):
    i = len(arr1) - 1
    j = 0
    
    while i >= 0 and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
    
    arr1.sort()
    arr2.sort()

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge_simple(arr1, arr2)
print(arr1)
print(arr2)
```

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4]
[5, 6, 7, 8]
```

**Explanation**: Compare largest of arr1 with smallest of arr2 and swap if needed. Then sort both arrays. Overall effective time: O((n+m) log(n+m)).

</details>

---

### Q92. Find the missing and repeating number.

```python
def find_missing_repeating(arr):
    n = len(arr)
    
    sum_arr = sum(arr)
    sum_sq_arr = sum(x * x for x in arr)
    
    sum_expected = n * (n + 1) // 2
    sum_sq_expected = n * (n + 1) * (2 * n + 1) // 6
    
    # x - y = diff, x² - y² = sq_diff
    diff = sum_arr - sum_expected      # repeating - missing
    sq_diff = sum_sq_arr - sum_sq_expected
    
    sum_xy = sq_diff // diff           # repeating + missing
    
    repeating = (diff + sum_xy) // 2
    missing = (sum_xy - diff) // 2
    
    return repeating, missing

arr = [3, 1, 2, 5, 3]
rep, mis = find_missing_repeating(arr)
print(f"Repeating: {rep}")
print(f"Missing: {mis}")
```

<details>
<summary>Answer</summary>

```
Repeating: 3
Missing: 4
```

**Explanation**: Using math: `x - y` from sum difference, `x² - y²` from sum-of-squares difference. Solve the system of equations. Time: O(n), Space: O(1).

</details>

---

### Q93. Count inversions (Merge Sort based).

```python
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    
    merged = []
    inversions = left_inv + right_inv
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i  # All remaining in left are inversions
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

arr = [2, 4, 1, 3, 5]
_, inv_count = count_inversions(arr)
print(f"Inversion count: {inv_count}")
```

<details>
<summary>Answer</summary>

```
Inversion count: 3
```

**Explanation**: An inversion is `(i, j)` where `i < j` but `arr[i] > arr[j]`. Inversions: (2,1), (4,1), (4,3). **Merge Sort** counts split inversions during merge. Time: O(n log n).

</details>

---

### Q94. Next permutation.

```python
def next_permutation(nums):
    n = len(nums)
    
    # Step 1: Find breakpoint (first decreasing from right)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find smallest element > nums[i] from right
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse from i+1 to end
    nums[i + 1:] = reversed(nums[i + 1:])

nums1 = [1, 2, 3]
next_permutation(nums1)
print(nums1)

nums2 = [3, 2, 1]
next_permutation(nums2)
print(nums2)
```

<details>
<summary>Answer</summary>

```
[1, 3, 2]
[1, 2, 3]
```

**Explanation**: Find rightmost ascending pair, swap with next larger, reverse suffix. Fully descending → reverse all. **LeetCode #31**. Time: O(n).

</details>

---

### Q95. Merge overlapping intervals.

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print(result)
```

<details>
<summary>Answer</summary>

```
[[1, 6], [8, 10], [15, 18]]
```

**Explanation**: Sort by start time. If current overlaps with last merged, extend it. Otherwise add as new. **LeetCode #56**. Time: O(n log n).

</details>

---

### Q96. Product of array except self.

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Left pass
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right pass
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

nums = [1, 2, 3, 4]
print(product_except_self(nums))
```

<details>
<summary>Answer</summary>

```
[24, 12, 8, 6]
```

**Explanation**: Two-pass: first pass stores left products, second pass multiplies by right products. No division used. **LeetCode #238**. Time: O(n), Space: O(1) (output doesn't count).

</details>

---

### Q97. Subarray with given XOR.

```python
def count_subarrays_xor(arr, target):
    prefix_xor_count = {}
    xor = 0
    count = 0
    
    for num in arr:
        xor ^= num
        
        if xor == target:
            count += 1
        
        if (xor ^ target) in prefix_xor_count:
            count += prefix_xor_count[xor ^ target]
        
        prefix_xor_count[xor] = prefix_xor_count.get(xor, 0) + 1
    
    return count

arr = [4, 2, 2, 6, 4]
print(f"Subarrays with XOR 6: {count_subarrays_xor(arr, 6)}")
```

<details>
<summary>Answer</summary>

```
Subarrays with XOR 6: 4
```

**Explanation**: Like prefix sum but with XOR. If `prefix_xor ^ target` exists in the map, a valid subarray ends here. Uses property: `a ^ b = c ⟹ a ^ c = b`. Time: O(n).

</details>

---

### Q98. Longest subarray with sum 0.

```python
def longest_zero_sum(arr):
    prefix_map = {}  # {prefix_sum: first_index}
    total = 0
    max_len = 0
    
    for i in range(len(arr)):
        total += arr[i]
        
        if total == 0:
            max_len = i + 1
        elif total in prefix_map:
            max_len = max(max_len, i - prefix_map[total])
        else:
            prefix_map[total] = i
    
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(f"Longest zero-sum subarray: {longest_zero_sum(arr)}")
```

<details>
<summary>Answer</summary>

```
Longest zero-sum subarray: 5
```

**Explanation**: If `prefix_sum[i] == prefix_sum[j]`, then `sum(arr[i+1..j]) = 0`. Store first occurrence of each prefix sum. Subarray: `[-2, 2, -8, 1, 7]`. Time: O(n).

</details>

---

### Q99. Maximum product subarray.

```python
def max_product(nums):
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    
    return result

nums = [2, 3, -2, 4]
print(f"Max product: {max_product(nums)}")

nums2 = [-2, 0, -1]
print(f"Max product: {max_product(nums2)}")
```

<details>
<summary>Answer</summary>

```
Max product: 6
Max product: 0
```

**Explanation**: Track both max and min products (negative × negative = positive). Swap when current is negative. **LeetCode #152**. Time: O(n), Space: O(1).

</details>

---

### Q100. 4Sum — find all unique quadruplets summing to target.

```python
def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result

nums = [1, 0, -1, 0, -2, 2]
print(four_sum(nums, 0))
```

<details>
<summary>Answer</summary>

```
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

**Explanation**: Extension of 3Sum. Fix two elements, use two pointers for the remaining two. Skip duplicates at all levels. **LeetCode #18**. Time: O(n³).

</details>

---

# 📊 Quick Reference — Complexity Cheat Sheet

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space |
|-----------|-------------|------------|--------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Kadane's | O(n) | O(n) | O(n) | O(1) |
| KMP | O(n+m) | O(n+m) | O(n+m) | O(m) |
| Two Pointers | O(n) | O(n) | O(n) | O(1) |
| Sliding Window | O(n) | O(n) | O(n) | O(1) |

---

# 💡 Key Patterns to Remember

| Pattern | When to Use | Examples |
|---------|-------------|---------|
| **Two Pointers** | Sorted arrays, pairs, palindromes | Q54, Q72, Q73, Q79 |
| **Sliding Window** | Subarray/substring problems | Q28, Q40, Q43, Q75 |
| **Prefix Sum/XOR** | Subarray sum queries | Q76, Q97, Q98 |
| **Binary Search** | Sorted data, search problems | Q62, Q68, Q69, Q70 |
| **Backtracking** | Generate all combinations/permutations | Q23, Q44, Q90 |
| **Dynamic Programming** | Optimal substructure, overlapping subproblems | Q35, Q37, Q46, Q48, Q49 |
| **HashMap/Dict** | Frequency, pairs, complement problems | Q71, Q76, Q80 |
| **Bit Manipulation** | Unique chars, XOR tricks | Q38, Q97 |
| **Counter** | Frequency counting (Pythonic) | Q13, Q15, Q34, Q78 |

---

# 🐍 Python-Specific Tips for DSA

| Task | Pythonic Way | Time |
|------|-------------|------|
| Reverse string/list | `s[::-1]` | O(n) |
| Sort | `sorted()` or `.sort()` | O(n log n) |
| Frequency count | `Counter(iterable)` | O(n) |
| Remove duplicates | `list(dict.fromkeys(arr))` | O(n) |
| Check membership | `x in set_obj` | O(1) |
| Flatten 2D list | `[x for row in matrix for x in row]` | O(m×n) |
| Transpose matrix | `list(zip(*matrix))` | O(m×n) |
| Min/Max with index | `min(range(len(a)), key=a.__getitem__)` | O(n) |
| Swap variables | `a, b = b, a` | O(1) |
| Unpack list | `first, *rest = arr` | O(n) |

---

> 🎯 **Pro Tip**: Practice each question without looking at the answer first. Then compare your solution. In Python interviews, knowing both the **Pythonic way** and the **algorithmic approach** makes you stand out.

---

*Happy Coding! 🐍 Keep Practicing! 🚀*
