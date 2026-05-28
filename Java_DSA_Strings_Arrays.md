# ☕ 100 Java DSA Questions — Strings & Arrays

> **Topics Covered**: String Manipulation, Character Arrays, 1D Arrays, 2D Arrays, Searching, Sorting, Sliding Window, Two Pointers  
> **Difficulty**: Beginner → Intermediate → Advanced (Placement Level)  
> **Language**: Java  
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
| [6. Array Basics](#section-6-array-basics-q51--q60) | Q51 – Q60 | ⭐ Beginner |
| [7. Array Searching & Sorting](#section-7-array-searching--sorting-q61--q70) | Q61 – Q70 | ⭐⭐ Intermediate |
| [8. Array Two Pointers & Sliding Window](#section-8-array-two-pointers--sliding-window-q71--q80) | Q71 – Q80 | ⭐⭐⭐ Advanced |
| [9. Array Matrix / 2D Array](#section-9-array-matrix--2d-array-q81--q90) | Q81 – Q90 | ⭐⭐⭐ Advanced |
| [10. Array Placement Level](#section-10-array-placement-level-q91--q100) | Q91 – Q100 | 🔥 Placement |

---

# 🔤 PART A — STRINGS

---

## Section 1: String Basics (Q1 – Q10)

---

### Q1. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = new String("Hello");

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s1.equals(s3));
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
true
```

**Explanation**: `s1` and `s2` point to the same object in the **String Pool** (interning). `s3` is created using `new`, so it's a different object on the **heap**. `==` compares references, `.equals()` compares actual content.

> 💡 **Key Concept**: Always use `.equals()` to compare String values in Java, never `==`.

</details>

---

### Q2. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s = "Java";
        System.out.println(s.length());
        System.out.println(s.charAt(0));
        System.out.println(s.charAt(s.length() - 1));
    }
}
```

<details>
<summary>Answer</summary>

```
4
J
a
```

**Explanation**: `.length()` returns the number of characters. `.charAt(index)` returns the character at the given index (0-based). Last character is at index `length - 1`.

</details>

---

### Q3. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s = "Hello World";
        System.out.println(s.substring(0, 5));
        System.out.println(s.substring(6));
        System.out.println(s.indexOf("World"));
        System.out.println(s.indexOf("xyz"));
    }
}
```

<details>
<summary>Answer</summary>

```
Hello
World
6
-1
```

**Explanation**: `substring(start, end)` extracts from `start` to `end-1`. `substring(start)` extracts from `start` to end. `indexOf()` returns the first index of the substring, or `-1` if not found.

</details>

---

### Q4. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s = "Java Programming";
        System.out.println(s.toUpperCase());
        System.out.println(s.toLowerCase());
        System.out.println(s.contains("Pro"));
        System.out.println(s.contains("pro"));
    }
}
```

<details>
<summary>Answer</summary>

```
JAVA PROGRAMMING
java programming
true
false
```

**Explanation**: `toUpperCase()` and `toLowerCase()` convert case. `contains()` is **case-sensitive** — `"Pro"` is found but `"pro"` is not.

</details>

---

### Q5. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s = "  Hello Java  ";
        System.out.println("[" + s.trim() + "]");
        System.out.println(s.replace("Java", "World"));
        System.out.println(s.startsWith("  He"));
        System.out.println(s.endsWith("va  "));
    }
}
```

<details>
<summary>Answer</summary>

```
[Hello Java]
  Hello World  
true
true
```

**Explanation**: `trim()` removes leading and trailing whitespace. `replace()` replaces all occurrences of a substring. `startsWith()` and `endsWith()` check prefixes/suffixes.

</details>

---

### Q6. Are Strings mutable or immutable in Java? Prove with code.

<details>
<summary>Answer</summary>

```java
public class Main {
    public static void main(String[] args) {
        String s = "Hello";
        s.concat(" World");   // Returns a new string, does NOT modify s
        System.out.println(s); // Still "Hello"

        s = s.concat(" World"); // Reassigning to s
        System.out.println(s);  // Now "Hello World"
    }
}
```

```
Hello
Hello World
```

**Explanation**: Strings are **immutable** in Java. Methods like `concat()`, `replace()`, `toUpperCase()` etc. return a **new String** object — the original is never modified. The variable `s` just points to a new object after reassignment.

> 💡 **Why immutable?** Security, thread-safety, and String Pool caching.

</details>

---

### Q7. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = new String("Hello");
        String s4 = s3.intern();

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s1 == s4);
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
true
```

**Explanation**: `intern()` returns the reference from the **String Pool**. Since `"Hello"` is already in the pool (used by `s1`), `s4` now points to the same object as `s1`. So `s1 == s4` is `true`.

</details>

---

### Q8. What will be the output?

```java
public class Main {
    public static void main(String[] args) {
        String s = "";
        System.out.println(s.isEmpty());
        System.out.println(s.length());

        String s2 = "   ";
        System.out.println(s2.isEmpty());
        System.out.println(s2.isBlank()); // Java 11+
    }
}
```

<details>
<summary>Answer</summary>

```
true
0
false
true
```

**Explanation**: `isEmpty()` returns `true` if length is 0. A string with only spaces is NOT empty but IS blank. `isBlank()` (Java 11+) returns `true` if the string is empty or contains only whitespace.

</details>

---

### Q9. Convert between String and char array.

```java
public class Main {
    public static void main(String[] args) {
        // String → char array
        String s = "Hello";
        char[] chars = s.toCharArray();
        for (char c : chars) {
            System.out.print(c + " ");
        }
        System.out.println();

        // char array → String
        char[] arr = {'J', 'a', 'v', 'a'};
        String str = new String(arr);
        System.out.println(str);

        // Also works:
        String str2 = String.valueOf(arr);
        System.out.println(str2);
    }
}
```

<details>
<summary>Answer</summary>

```
H e l l o 
Java
Java
```

**Explanation**: `toCharArray()` converts a String to a character array. `new String(charArray)` or `String.valueOf(charArray)` converts back. These conversions are **essential** for many DSA problems.

</details>

---

### Q10. What is the difference between `String`, `StringBuilder`, and `StringBuffer`?

<details>
<summary>Answer</summary>

```java
public class Main {
    public static void main(String[] args) {
        // String - Immutable
        String s = "Hello";
        s = s + " World"; // Creates a new object each time

        // StringBuilder - Mutable, NOT thread-safe, FASTER
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World");
        System.out.println(sb); // Hello World

        // StringBuffer - Mutable, Thread-safe, SLOWER
        StringBuffer sbf = new StringBuffer("Hello");
        sbf.append(" World");
        System.out.println(sbf); // Hello World
    }
}
```

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| Mutability | Immutable | Mutable | Mutable |
| Thread Safe | Yes (immutable) | ❌ No | ✅ Yes |
| Performance | Slow (new object) | ⚡ Fast | Medium |
| Use When | Few modifications | Single thread, many modifications | Multi-thread |

> 💡 **Interview Tip**: Use `StringBuilder` in DSA problems when building strings in loops. Never concatenate strings with `+` inside loops — it creates O(n²) complexity.

</details>

---

## Section 2: String Methods & Operations (Q11 – Q20)

---

### Q11. Reverse a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "Hello World";

        // Method 1: Using StringBuilder
        String rev1 = new StringBuilder(s).reverse().toString();
        System.out.println(rev1);

        // Method 2: Using char array (manual)
        char[] chars = s.toCharArray();
        int left = 0, right = chars.length - 1;
        while (left < right) {
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }
        System.out.println(new String(chars));
    }
}
```

<details>
<summary>Answer</summary>

```
dlroW olleH
dlroW olleH
```

**Explanation**: Method 1 uses `StringBuilder.reverse()` — simplest approach. Method 2 uses the **two-pointer technique** on a char array — preferred in interviews to show understanding.

</details>

---

### Q12. Check if a String is a palindrome.

```java
public class Main {
    public static void main(String[] args) {
        String s = "madam";
        String reversed = new StringBuilder(s).reverse().toString();

        if (s.equals(reversed)) {
            System.out.println(s + " is a Palindrome");
        } else {
            System.out.println(s + " is NOT a Palindrome");
        }
    }
}
```

<details>
<summary>Answer</summary>

```
madam is a Palindrome
```

**Explanation**: A palindrome reads the same forwards and backwards. Reverse the string and compare. You can also use two pointers for O(1) space.

```java
// Two-pointer approach (no extra space)
boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) return false;
        left++;
        right--;
    }
    return true;
}
```

</details>

---

### Q13. Count the frequency of each character in a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "programming";
        int[] freq = new int[26]; // assuming lowercase a-z

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                System.out.println((char)(i + 'a') + " → " + freq[i]);
            }
        }
    }
}
```

<details>
<summary>Answer</summary>

```
a → 1
g → 2
i → 1
m → 2
n → 1
o → 1
p → 1
r → 2
```

**Explanation**: We use an integer array of size 26 as a **frequency map**. `c - 'a'` converts a character to its index (0–25). This is O(n) time and O(1) space (fixed 26 slots).

> 💡 **Key Concept**: `c - 'a'` gives the alphabet position (a=0, b=1, ..., z=25). This trick is used in many string problems.

</details>

---

### Q14. Find the first non-repeating character in a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "aabbcdd";
        int[] freq = new int[26];

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        for (char c : s.toCharArray()) {
            if (freq[c - 'a'] == 1) {
                System.out.println("First non-repeating: " + c);
                return;
            }
        }
        System.out.println("No non-repeating character found");
    }
}
```

<details>
<summary>Answer</summary>

```
First non-repeating: c
```

**Explanation**: Two-pass approach — first pass counts frequencies, second pass finds the first character with frequency 1. Time: O(n), Space: O(1).

</details>

---

### Q15. Check if two Strings are anagrams.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String s1 = "listen";
        String s2 = "silent";

        // Method 1: Sort and compare
        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        System.out.println(Arrays.equals(a, b)); // true

        // Method 2: Frequency count (optimal)
        int[] freq = new int[26];
        for (char c : s1.toCharArray()) freq[c - 'a']++;
        for (char c : s2.toCharArray()) freq[c - 'a']--;

        boolean isAnagram = true;
        for (int f : freq) {
            if (f != 0) {
                isAnagram = false;
                break;
            }
        }
        System.out.println(isAnagram); // true
    }
}
```

<details>
<summary>Answer</summary>

```
true
true
```

**Explanation**: Anagrams have the same characters with the same frequencies. 
- **Method 1**: Sort both → O(n log n).
- **Method 2**: Frequency count → O(n), preferred in interviews.

</details>

---

### Q16. Count words in a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "  Java is  a great  language  ";

        // Method 1: Using split with regex
        String[] words = s.trim().split("\\s+");
        System.out.println("Word count: " + words.length);

        // Print each word
        for (String word : words) {
            System.out.println("'" + word + "'");
        }
    }
}
```

<details>
<summary>Answer</summary>

```
Word count: 5
'Java'
'is'
'a'
'great'
'language'
```

**Explanation**: `trim()` removes leading/trailing spaces. `split("\\s+")` splits by one or more whitespace characters. This handles multiple spaces between words correctly.

</details>

---

### Q17. Reverse each word in a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "Hello World Java";
        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            result.append(new StringBuilder(word).reverse());
            result.append(" ");
        }

        System.out.println(result.toString().trim());
    }
}
```

<details>
<summary>Answer</summary>

```
olleH dlroW avaJ
```

**Explanation**: Split by space, reverse each word individually using `StringBuilder`, and join them back.

</details>

---

### Q18. Reverse the order of words in a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "Hello World Java";
        String[] words = s.trim().split("\\s+");
        StringBuilder result = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {
            result.append(words[i]);
            if (i > 0) result.append(" ");
        }

        System.out.println(result.toString());
    }
}
```

<details>
<summary>Answer</summary>

```
Java World Hello
```

**Explanation**: Split the string into words, then iterate in reverse order and build the result. This is a very common interview question.

</details>

---

### Q19. Remove all duplicate characters from a String.

```java
import java.util.LinkedHashSet;

public class Main {
    public static void main(String[] args) {
        String s = "programming";
        
        // Method 1: Using LinkedHashSet (preserves order)
        LinkedHashSet<Character> set = new LinkedHashSet<>();
        for (char c : s.toCharArray()) {
            set.add(c);
        }
        StringBuilder sb = new StringBuilder();
        for (char c : set) {
            sb.append(c);
        }
        System.out.println(sb); // proamin (removed duplicate r, g, m)

        // Method 2: Using boolean array
        boolean[] seen = new boolean[26];
        StringBuilder sb2 = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (!seen[c - 'a']) {
                seen[c - 'a'] = true;
                sb2.append(c);
            }
        }
        System.out.println(sb2);
    }
}
```

<details>
<summary>Answer</summary>

```
proaming
proaming
```

**Explanation**: Use a `LinkedHashSet` to maintain insertion order while removing duplicates. Or use a boolean array for O(1) lookup. Both are O(n) time.

</details>

---

### Q20. Convert a String to an integer without using `Integer.parseInt()`.

```java
public class Main {
    public static void main(String[] args) {
        String s = "12345";
        int num = 0;

        for (char c : s.toCharArray()) {
            num = num * 10 + (c - '0');
        }

        System.out.println(num);        // 12345
        System.out.println(num + 10);   // 12355 (proves it's an int)
    }
}
```

<details>
<summary>Answer</summary>

```
12345
12355
```

**Explanation**: `c - '0'` converts a digit character to its integer value (e.g., `'5' - '0' = 5`). We build the number by multiplying the current result by 10 and adding the next digit.

> 💡 **Interview Enhancement**: Handle negative numbers by checking if the first char is `'-'`, and handle overflow for production code.

</details>

---

## Section 3: String Pattern Problems (Q21 – Q30)

---

### Q21. Check if a String contains only digits.

```java
public class Main {
    public static void main(String[] args) {
        String s1 = "12345";
        String s2 = "123a5";

        System.out.println(isNumeric(s1)); // true
        System.out.println(isNumeric(s2)); // false
    }

    static boolean isNumeric(String s) {
        for (char c : s.toCharArray()) {
            if (c < '0' || c > '9') return false;
        }
        return !s.isEmpty();
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
```

**Explanation**: Check each character to see if it's between `'0'` and `'9'`. You can also use `Character.isDigit(c)` or regex `s.matches("\\d+")`.

</details>

---

### Q22. Count vowels and consonants in a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "Hello World";
        int vowels = 0, consonants = 0;

        for (char c : s.toLowerCase().toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                if ("aeiou".indexOf(c) != -1) {
                    vowels++;
                } else {
                    consonants++;
                }
            }
        }

        System.out.println("Vowels: " + vowels);
        System.out.println("Consonants: " + consonants);
    }
}
```

<details>
<summary>Answer</summary>

```
Vowels: 3
Consonants: 7
```

**Explanation**: Convert to lowercase, check if each character is a letter, then check if it's a vowel using `indexOf()` on the vowel string.

</details>

---

### Q23. Find all permutations of a String.

```java
public class Main {
    public static void main(String[] args) {
        permute("ABC", 0, 2);
    }

    static void permute(String s, int left, int right) {
        if (left == right) {
            System.out.println(s);
            return;
        }

        for (int i = left; i <= right; i++) {
            s = swap(s, left, i);
            permute(s, left + 1, right);
            s = swap(s, left, i); // backtrack
        }
    }

    static String swap(String s, int i, int j) {
        char[] chars = s.toCharArray();
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
        return new String(chars);
    }
}
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
```

**Explanation**: This uses **backtracking**. Fix each character at the current position, recursively permute the rest, then backtrack (swap back). Total permutations = n! (3! = 6 for "ABC").

> 💡 **Time Complexity**: O(n × n!) — n! permutations, each takes O(n) to print.

</details>

---

### Q24. Check if a String is a rotation of another String.

```java
public class Main {
    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "cdeab";

        if (s1.length() == s2.length() && (s1 + s1).contains(s2)) {
            System.out.println(s2 + " is a rotation of " + s1);
        } else {
            System.out.println("Not a rotation");
        }
    }
}
```

<details>
<summary>Answer</summary>

```
cdeab is a rotation of abcde
```

**Explanation**: If `s2` is a rotation of `s1`, then `s2` must be a substring of `s1 + s1`. For example: `"abcde" + "abcde" = "abcdeabcde"` contains `"cdeab"`. Brilliant trick!

</details>

---

### Q25. Find the longest common prefix among an array of Strings.

```java
public class Main {
    public static void main(String[] args) {
        String[] strs = {"flower", "flow", "flight"};
        System.out.println(longestCommonPrefix(strs));
    }

    static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }
        return prefix;
    }
}
```

<details>
<summary>Answer</summary>

```
fl
```

**Explanation**: Start with the first string as the prefix. For each subsequent string, shrink the prefix until it matches the start. **LeetCode #14**.

</details>

---

### Q26. Compress a String using counts of repeated characters.

```java
public class Main {
    public static void main(String[] args) {
        String s = "aabcccccaaa";
        System.out.println(compress(s));
    }

    static String compress(String s) {
        StringBuilder sb = new StringBuilder();
        int count = 1;

        for (int i = 1; i <= s.length(); i++) {
            if (i < s.length() && s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                sb.append(s.charAt(i - 1));
                sb.append(count);
                count = 1;
            }
        }

        String compressed = sb.toString();
        return compressed.length() < s.length() ? compressed : s;
    }
}
```

<details>
<summary>Answer</summary>

```
a2b1c5a3
```

**Explanation**: Count consecutive occurrences of each character. If the compressed string is longer than the original, return the original. This is **Cracking the Coding Interview 1.6**.

</details>

---

### Q27. Check if two Strings are one edit apart (Insert, Delete, Replace).

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(isOneEditAway("pale", "ple"));    // true (remove)
        System.out.println(isOneEditAway("pales", "pale"));  // true (remove)
        System.out.println(isOneEditAway("pale", "bale"));   // true (replace)
        System.out.println(isOneEditAway("pale", "bake"));   // false
    }

    static boolean isOneEditAway(String s1, String s2) {
        if (Math.abs(s1.length() - s2.length()) > 1) return false;

        String shorter = s1.length() < s2.length() ? s1 : s2;
        String longer = s1.length() < s2.length() ? s2 : s1;

        int i = 0, j = 0;
        boolean foundDifference = false;

        while (i < shorter.length() && j < longer.length()) {
            if (shorter.charAt(i) != longer.charAt(j)) {
                if (foundDifference) return false;
                foundDifference = true;

                if (shorter.length() == longer.length()) {
                    i++; // replace: move both
                }
            } else {
                i++;
            }
            j++;
        }

        return true;
    }
}
```

<details>
<summary>Answer</summary>

```
true
true
true
false
```

**Explanation**: Three possible edits: insert, delete, replace. If lengths differ by more than 1, impossible. Otherwise, walk through both strings tracking differences. **Cracking the Coding Interview 1.5**.

</details>

---

### Q28. Find the longest substring without repeating characters.

```java
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        String s = "abcabcbb";
        System.out.println(lengthOfLongestSubstring(s));
    }

    static int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLen = 0, left = 0;

        for (int right = 0; right < s.length(); right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
```

<details>
<summary>Answer</summary>

```
3
```

**Explanation**: Uses the **Sliding Window** technique. Expand the right pointer; when a duplicate is found, shrink from the left. Track the maximum window size. **LeetCode #3**. Time: O(n).

</details>

---

### Q29. Generate all substrings of a String.

```java
public class Main {
    public static void main(String[] args) {
        String s = "abc";
        System.out.println("All substrings of '" + s + "':");

        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                System.out.println(s.substring(i, j));
            }
        }
    }
}
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
```

**Explanation**: Use two nested loops — outer for start index, inner for end index. Total substrings = n(n+1)/2. Time: O(n²).

</details>

---

### Q30. Implement `indexOf()` — find first occurrence of a pattern in a text (Naive approach).

```java
public class Main {
    public static void main(String[] args) {
        String text = "hello world hello";
        String pattern = "world";

        int index = findPattern(text, pattern);
        System.out.println("Pattern found at index: " + index);
    }

    static int findPattern(String text, String pattern) {
        int n = text.length(), m = pattern.length();

        for (int i = 0; i <= n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) break;
            }
            if (j == m) return i; // all characters matched
        }
        return -1;
    }
}
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 6
```

**Explanation**: Slide the pattern over the text one character at a time. For each position, check if all characters match. Time: O(n×m) worst case. Better algorithms: **KMP** (O(n+m)), **Rabin-Karp**.

</details>

---

## Section 4: String Advanced Problems (Q31 – Q40)

---

### Q31. Find the longest palindromic substring.

```java
public class Main {
    public static void main(String[] args) {
        String s = "babad";
        System.out.println(longestPalindrome(s));
    }

    static String longestPalindrome(String s) {
        if (s.length() < 2) return s;
        int start = 0, maxLen = 1;

        for (int i = 0; i < s.length(); i++) {
            // Odd length palindromes
            int len1 = expandFromCenter(s, i, i);
            // Even length palindromes
            int len2 = expandFromCenter(s, i, i + 1);
            int len = Math.max(len1, len2);

            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }
        return s.substring(start, start + maxLen);
    }

    static int expandFromCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

<details>
<summary>Answer</summary>

```
bab
```

(or `"aba"` — both are valid)

**Explanation**: **Expand Around Center** technique. For each index, try expanding outward treating it as the center of both odd-length and even-length palindromes. **LeetCode #5**. Time: O(n²), Space: O(1).

</details>

---

### Q32. Implement `atoi` — String to Integer (handle edge cases).

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(myAtoi("   -42"));
        System.out.println(myAtoi("4193 with words"));
        System.out.println(myAtoi("words and 987"));
        System.out.println(myAtoi("91283472332"));
    }

    static int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty()) return 0;

        int sign = 1, i = 0;
        long result = 0;

        if (s.charAt(0) == '-') { sign = -1; i++; }
        else if (s.charAt(0) == '+') { i++; }

        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');
            if (result * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (result * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;
            i++;
        }

        return (int)(result * sign);
    }
}
```

<details>
<summary>Answer</summary>

```
-42
4193
0
2147483647
```

**Explanation**: Handle: leading whitespace, optional sign, overflow, and stop at non-digit characters. **LeetCode #8**.

</details>

---

### Q33. Count and say sequence.

```java
public class Main {
    public static void main(String[] args) {
        int n = 5;
        System.out.println(countAndSay(n));
    }

    static String countAndSay(int n) {
        String result = "1";

        for (int i = 2; i <= n; i++) {
            StringBuilder sb = new StringBuilder();
            int count = 1;

            for (int j = 1; j < result.length(); j++) {
                if (result.charAt(j) == result.charAt(j - 1)) {
                    count++;
                } else {
                    sb.append(count).append(result.charAt(j - 1));
                    count = 1;
                }
            }
            sb.append(count).append(result.charAt(result.length() - 1));
            result = sb.toString();
        }

        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
111221
```

**Explanation**: 
- 1 → `"1"` 
- 2 → `"11"` (one 1) 
- 3 → `"21"` (two 1s) 
- 4 → `"1211"` (one 2, one 1) 
- 5 → `"111221"` (one 1, one 2, two 1s)

**LeetCode #38**.

</details>

---

### Q34. Group anagrams together.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};

        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        for (List<String> group : map.values()) {
            System.out.println(group);
        }
    }
}
```

<details>
<summary>Answer</summary>

```
[eat, tea, ate]
[tan, nat]
[bat]
```

**Explanation**: Sort each string to get a canonical form as the key. All anagrams will have the same sorted key. Use a `HashMap` to group them. **LeetCode #49**. Time: O(n × k log k) where k is max string length.

</details>

---

### Q35. Longest common subsequence (LCS) of two Strings.

```java
public class Main {
    public static void main(String[] args) {
        String s1 = "abcde";
        String s2 = "ace";
        System.out.println("LCS Length: " + lcs(s1, s2));
    }

    static int lcs(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[m][n];
    }
}
```

<details>
<summary>Answer</summary>

```
LCS Length: 3
```

**Explanation**: Classic **Dynamic Programming** problem. `dp[i][j]` = LCS length of `s1[0..i-1]` and `s2[0..j-1]`. If characters match, add 1 to diagonal. Otherwise, take max of left or top. **LeetCode #1143**. Time: O(m×n).

</details>

---

### Q36. Implement KMP (Knuth-Morris-Pratt) pattern matching.

```java
public class Main {
    public static void main(String[] args) {
        String text = "ababcababababcababd";
        String pattern = "ababd";

        int index = kmpSearch(text, pattern);
        System.out.println("Pattern found at index: " + index);
    }

    static int kmpSearch(String text, String pattern) {
        int[] lps = buildLPS(pattern);
        int i = 0, j = 0;

        while (i < text.length()) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i++; j++;
                if (j == pattern.length()) return i - j;
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return -1;
    }

    static int[] buildLPS(String pattern) {
        int[] lps = new int[pattern.length()];
        int len = 0, i = 1;

        while (i < pattern.length()) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
}
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 13
```

**Explanation**: KMP avoids redundant comparisons by precomputing the **LPS (Longest Proper Prefix which is also Suffix)** array. When a mismatch occurs, it uses the LPS to skip characters. Time: O(n + m), where n = text length, m = pattern length.

> 💡 **Interview Must-Know**: KMP is a top pattern matching algorithm. Understand the LPS array construction.

</details>

---

### Q37. Minimum number of deletions to make a String a palindrome.

```java
public class Main {
    public static void main(String[] args) {
        String s = "aebcbda";
        int lpsLength = longestPalindromicSubseq(s);
        System.out.println("Min deletions: " + (s.length() - lpsLength));
    }

    static int longestPalindromicSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) dp[i][i] = 1;

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

<details>
<summary>Answer</summary>

```
Min deletions: 2
```

**Explanation**: Find the **Longest Palindromic Subsequence (LPS)** length. Minimum deletions = `string length - LPS length`. The LPS of `"aebcbda"` is `"abcba"` (length 5), so deletions = 7 - 5 = 2.

</details>

---

### Q38. Check if a String has all unique characters (without extra data structures).

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(isUnique("abcdef"));  // true
        System.out.println(isUnique("abcaef"));  // false
    }

    static boolean isUnique(String s) {
        // Using bit manipulation — works for lowercase a-z
        int checker = 0;

        for (char c : s.toCharArray()) {
            int bit = c - 'a';
            if ((checker & (1 << bit)) > 0) return false;
            checker |= (1 << bit);
        }
        return true;
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
```

**Explanation**: Uses a 32-bit integer as a **bit vector**. Each bit represents a character (a=bit 0, b=bit 1, ...). If a bit is already set, the character is a duplicate. **Cracking the Coding Interview 1.1**. O(n) time, O(1) space.

</details>

---

### Q39. Decode a run-length encoded String.

```java
public class Main {
    public static void main(String[] args) {
        String encoded = "a2b1c5a3";
        System.out.println(decode(encoded));
    }

    static String decode(String s) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s.length(); i += 2) {
            char ch = s.charAt(i);
            int count = s.charAt(i + 1) - '0';
            for (int j = 0; j < count; j++) {
                result.append(ch);
            }
        }

        return result.toString();
    }
}
```

<details>
<summary>Answer</summary>

```
aabcccccaaa
```

**Explanation**: The encoded format is `char + count`. Read character and its count, then append the character that many times. This is the reverse of Q26 (String Compression).

</details>

---

### Q40. Find the smallest window in a String containing all characters of another String.

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minWindow(s, t));
    }

    static String minWindow(String s, String t) {
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();

        for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);

        int left = 0, matched = 0;
        int minLen = Integer.MAX_VALUE, minStart = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            window.merge(c, 1, Integer::sum);

            if (need.containsKey(c) && window.get(c).intValue() == need.get(c).intValue()) {
                matched++;
            }

            while (matched == need.size()) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }
                char leftChar = s.charAt(left);
                window.merge(leftChar, -1, Integer::sum);
                if (need.containsKey(leftChar) && window.get(leftChar) < need.get(leftChar)) {
                    matched--;
                }
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }
}
```

<details>
<summary>Answer</summary>

```
BANC
```

**Explanation**: Classic **Sliding Window** problem. Expand right to include all characters of `t`, then shrink left to minimize the window. **LeetCode #76**. Time: O(n).

</details>

---

## Section 5: String Placement Level (Q41 – Q50)

---

### Q41. Rabin-Karp pattern matching using hashing.

```java
public class Main {
    public static void main(String[] args) {
        String text = "hello world hello java";
        String pattern = "hello";
        rabinKarp(text, pattern);
    }

    static void rabinKarp(String text, String pattern) {
        int d = 256; // number of characters in alphabet
        int q = 101; // a prime number
        int m = pattern.length(), n = text.length();

        int pHash = 0, tHash = 0, h = 1;

        for (int i = 0; i < m - 1; i++) h = (h * d) % q;

        for (int i = 0; i < m; i++) {
            pHash = (d * pHash + pattern.charAt(i)) % q;
            tHash = (d * tHash + text.charAt(i)) % q;
        }

        for (int i = 0; i <= n - m; i++) {
            if (pHash == tHash) {
                boolean match = true;
                for (int j = 0; j < m; j++) {
                    if (text.charAt(i + j) != pattern.charAt(j)) {
                        match = false;
                        break;
                    }
                }
                if (match) System.out.println("Pattern found at index: " + i);
            }

            if (i < n - m) {
                tHash = (d * (tHash - text.charAt(i) * h) + text.charAt(i + m)) % q;
                if (tHash < 0) tHash += q;
            }
        }
    }
}
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 0
Pattern found at index: 12
```

**Explanation**: Rabin-Karp uses a **rolling hash** to quickly compare pattern hash with text window hash. Only does character-by-character comparison on hash matches. Average: O(n+m), Worst: O(nm).

</details>

---

### Q42. Valid parentheses String.

```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        System.out.println(isValid("()[]{}")); // true
        System.out.println(isValid("(]"));     // false
        System.out.println(isValid("([)]"));   // false
        System.out.println(isValid("{[]}"));   // true
    }

    static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == ']' && top != '[') return false;
                if (c == '}' && top != '{') return false;
            }
        }

        return stack.isEmpty();
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
false
true
```

**Explanation**: Use a **Stack**. Push opening brackets, pop on closing brackets and verify they match. **LeetCode #20**. Time: O(n), Space: O(n).

</details>

---

### Q43. Longest repeating character replacement (with at most k replacements).

```java
public class Main {
    public static void main(String[] args) {
        String s = "AABABBA";
        int k = 1;
        System.out.println(characterReplacement(s, k));
    }

    static int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int maxCount = 0, maxLen = 0, left = 0;

        for (int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'A']++;
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);

            // If window size - maxCount > k, shrink window
            if (right - left + 1 - maxCount > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
```

<details>
<summary>Answer</summary>

```
4
```

**Explanation**: Sliding window. The key insight: a valid window has `windowSize - maxFrequency <= k`. If not, shrink from the left. **LeetCode #424**. Time: O(n).

</details>

---

### Q44. Generate all valid combinations of n pairs of parentheses.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> result = new ArrayList<>();
        generateParenthesis(3, 0, 0, "", result);

        for (String s : result) {
            System.out.println(s);
        }
    }

    static void generateParenthesis(int n, int open, int close, String current, List<String> result) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }

        if (open < n) {
            generateParenthesis(n, open + 1, close, current + "(", result);
        }
        if (close < open) {
            generateParenthesis(n, open, close + 1, current + ")", result);
        }
    }
}
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

**Explanation**: **Backtracking** approach. At each step, we can add `(` if we haven't used all, or `)` if it doesn't exceed open count. **LeetCode #22**.

</details>

---

### Q45. Multiply two numbers represented as Strings.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(multiply("123", "456"));
    }

    static String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] result = new int[m + n];

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int p1 = i + j, p2 = i + j + 1;
                int sum = mul + result[p2];

                result[p2] = sum % 10;
                result[p1] += sum / 10;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int digit : result) {
            if (!(sb.length() == 0 && digit == 0)) {
                sb.append(digit);
            }
        }

        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

<details>
<summary>Answer</summary>

```
56088
```

**Explanation**: Simulates grade-school multiplication. Multiply each digit pair and place results at the correct position. **LeetCode #43**. Time: O(m×n).

</details>

---

### Q46. Wildcard pattern matching.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(isMatch("adceb", "*a*b"));   // true
        System.out.println(isMatch("acdcb", "a*c?b"));  // false
    }

    static boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        // Handle patterns starting with *
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == '*') dp[0][j] = dp[0][j - 1];
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
                } else if (p.charAt(j - 1) == '?' || s.charAt(i - 1) == p.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }

        return dp[m][n];
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
```

**Explanation**: `?` matches any single character, `*` matches any sequence (including empty). Uses **Dynamic Programming**. **LeetCode #44**. Time: O(m×n).

</details>

---

### Q47. Longest palindrome that can be formed from a String's characters.

```java
public class Main {
    public static void main(String[] args) {
        String s = "abccccdd";
        System.out.println(longestPalindrome(s));
    }

    static int longestPalindrome(String s) {
        int[] freq = new int[128]; // ASCII
        for (char c : s.toCharArray()) freq[c]++;

        int length = 0;
        boolean hasOdd = false;

        for (int f : freq) {
            length += (f / 2) * 2; // Take pairs
            if (f % 2 != 0) hasOdd = true;
        }

        return hasOdd ? length + 1 : length;
    }
}
```

<details>
<summary>Answer</summary>

```
7
```

**Explanation**: Use all character pairs + at most one odd character in the center. `"dccaccd"` is one valid palindrome of length 7. **LeetCode #409**.

</details>

---

### Q48. Edit Distance (Levenshtein Distance) between two Strings.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(editDistance("horse", "ros"));
    }

    static int editDistance(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], // replace
                                   Math.min(dp[i - 1][j],      // delete
                                            dp[i][j - 1]));    // insert
                }
            }
        }

        return dp[m][n];
    }
}
```

<details>
<summary>Answer</summary>

```
3
```

**Explanation**: Classic **DP** problem. Minimum operations (insert, delete, replace) to convert one string to another. `horse → ros`: replace h→r, remove r, remove e. **LeetCode #72**. Time: O(m×n).

</details>

---

### Q49. Implement a basic regular expression matcher (`.` and `*` only).

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(isMatch("aa", "a"));     // false
        System.out.println(isMatch("aa", "a*"));    // true
        System.out.println(isMatch("ab", ".*"));    // true
        System.out.println(isMatch("aab", "c*a*b")); // true
    }

    static boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*') dp[0][j] = dp[0][j - 2];
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    dp[i][j] = dp[i][j - 2]; // zero occurrences
                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j]; // one or more
                    }
                } else if (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }

        return dp[m][n];
    }
}
```

<details>
<summary>Answer</summary>

```
false
true
true
true
```

**Explanation**: `.` matches any character, `*` means zero or more of the preceding character. Uses **DP**. **LeetCode #10** (Hard). Time: O(m×n).

</details>

---

### Q50. Z-Algorithm for pattern matching.

```java
public class Main {
    public static void main(String[] args) {
        String text = "aaabcxyzaaabc";
        String pattern = "aaabc";
        zSearch(text, pattern);
    }

    static void zSearch(String text, String pattern) {
        String combined = pattern + "$" + text;
        int[] z = buildZArray(combined);

        for (int i = 0; i < z.length; i++) {
            if (z[i] == pattern.length()) {
                System.out.println("Pattern found at index: " + (i - pattern.length() - 1));
            }
        }
    }

    static int[] buildZArray(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;

        for (int i = 1; i < n; i++) {
            if (i < r) {
                z[i] = Math.min(r - i, z[i - l]);
            }
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }
        return z;
    }
}
```

<details>
<summary>Answer</summary>

```
Pattern found at index: 0
Pattern found at index: 8
```

**Explanation**: Z-array at position `i` stores the length of the longest substring starting at `i` that matches a prefix of the string. Concatenate `pattern + "$" + text` and find positions where Z-value equals pattern length. Time: O(n + m).

</details>

---

# 📦 PART B — ARRAYS

---

## Section 6: Array Basics (Q51 – Q60)

---

### Q51. Declare, initialize, and print an array.

```java
public class Main {
    public static void main(String[] args) {
        // Method 1: Declare and initialize
        int[] arr1 = {10, 20, 30, 40, 50};

        // Method 2: Declare with size, then fill
        int[] arr2 = new int[5];
        arr2[0] = 100;
        arr2[1] = 200;

        // Print using for loop
        for (int i = 0; i < arr1.length; i++) {
            System.out.print(arr1[i] + " ");
        }
        System.out.println();

        // Print using for-each
        for (int val : arr1) {
            System.out.print(val + " ");
        }
        System.out.println();

        // Print using Arrays.toString()
        System.out.println(java.util.Arrays.toString(arr1));
    }
}
```

<details>
<summary>Answer</summary>

```
10 20 30 40 50 
10 20 30 40 50 
[10, 20, 30, 40, 50]
```

**Explanation**: Arrays in Java have fixed size. Default value for `int[]` is `0`. `Arrays.toString()` is the easiest way to print arrays.

</details>

---

### Q52. Find the largest and smallest element in an array.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {12, 35, 1, 10, 34, 1};

        int max = arr[0], min = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) max = arr[i];
            if (arr[i] < min) min = arr[i];
        }

        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
    }
}
```

<details>
<summary>Answer</summary>

```
Maximum: 35
Minimum: 1
```

**Explanation**: Initialize max and min with the first element, then iterate through the rest comparing each. Time: O(n), Space: O(1).

</details>

---

### Q53. Find the sum and average of array elements.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};

        int sum = 0;
        for (int val : arr) {
            sum += val;
        }

        double average = (double) sum / arr.length;

        System.out.println("Sum: " + sum);
        System.out.printf("Average: %.2f%n", average);
    }
}
```

<details>
<summary>Answer</summary>

```
Sum: 150
Average: 30.00
```

**Explanation**: Iterate and accumulate the sum. Cast to `double` before dividing for accurate average. `printf` with `%.2f` formats to 2 decimal places.

</details>

---

### Q54. Reverse an array in-place.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }

        System.out.println(Arrays.toString(arr));
    }
}
```

<details>
<summary>Answer</summary>

```
[5, 4, 3, 2, 1]
```

**Explanation**: **Two-pointer technique** — swap elements from both ends moving inward. Time: O(n/2) = O(n), Space: O(1). This is in-place.

</details>

---

### Q55. Check if an array is sorted.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {1, 3, 2, 4, 5};

        System.out.println(isSorted(arr1)); // true
        System.out.println(isSorted(arr2)); // false
    }

    static boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) return false;
        }
        return true;
    }
}
```

<details>
<summary>Answer</summary>

```
true
false
```

**Explanation**: Compare each element with the previous one. If any element is smaller than its predecessor, the array is not sorted. Time: O(n).

</details>

---

### Q56. Remove duplicates from a sorted array (in-place).

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 1, 2, 2, 3, 4, 4, 5};

        int j = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[j]) {
                j++;
                arr[j] = arr[i];
            }
        }

        int newLength = j + 1;
        System.out.println("New length: " + newLength);
        System.out.println(Arrays.toString(Arrays.copyOf(arr, newLength)));
    }
}
```

<details>
<summary>Answer</summary>

```
New length: 5
[1, 2, 3, 4, 5]
```

**Explanation**: Use a slow pointer `j` to track the position of unique elements. When a new unique element is found, place it at `j+1`. **LeetCode #26**. Time: O(n), Space: O(1).

</details>

---

### Q57. Left rotate an array by one position.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        int first = arr[0];
        for (int i = 0; i < arr.length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr[arr.length - 1] = first;

        System.out.println(Arrays.toString(arr));
    }
}
```

<details>
<summary>Answer</summary>

```
[2, 3, 4, 5, 1]
```

**Explanation**: Save the first element, shift all elements left by one, place the saved element at the end. Time: O(n).

</details>

---

### Q58. Left rotate an array by K positions.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;

        k = k % arr.length; // Handle k > length

        // Reversal algorithm
        reverse(arr, 0, k - 1);
        reverse(arr, k, arr.length - 1);
        reverse(arr, 0, arr.length - 1);

        System.out.println(Arrays.toString(arr));
    }

    static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
```

<details>
<summary>Answer</summary>

```
[4, 5, 6, 7, 1, 2, 3]
```

**Explanation**: **Reversal Algorithm** — reverse first k elements, reverse remaining elements, reverse the whole array. Time: O(n), Space: O(1). This is the optimal approach.

</details>

---

### Q59. Move all zeros to the end of an array.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {0, 1, 0, 3, 12};

        int j = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                j++;
            }
        }

        System.out.println(Arrays.toString(arr));
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 3, 12, 0, 0]
```

**Explanation**: Use a pointer `j` to track the position for the next non-zero element. Swap non-zero elements to the front. **LeetCode #283**. Time: O(n), Space: O(1).

</details>

---

### Q60. Find the second largest element in an array.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {12, 35, 1, 10, 34, 1};

        int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;

        for (int val : arr) {
            if (val > first) {
                second = first;
                first = val;
            } else if (val > second && val != first) {
                second = val;
            }
        }

        if (second == Integer.MIN_VALUE) {
            System.out.println("No second largest element");
        } else {
            System.out.println("Second largest: " + second);
        }
    }
}
```

<details>
<summary>Answer</summary>

```
Second largest: 34
```

**Explanation**: Track both the largest and second largest in a single pass. Update `second` when we update `first`, or when current element is between them. Time: O(n), Space: O(1).

</details>

---

## Section 7: Array Searching & Sorting (Q61 – Q70)

---

### Q61. Linear Search.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int target = 30;

        int index = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                index = i;
                break;
            }
        }

        System.out.println(index != -1 ? "Found at index: " + index : "Not found");
    }
}
```

<details>
<summary>Answer</summary>

```
Found at index: 2
```

**Explanation**: Check each element sequentially. Time: O(n). Works on both sorted and unsorted arrays.

</details>

---

### Q62. Binary Search (iterative and recursive).

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;

        System.out.println("Iterative: " + binarySearchIterative(arr, target));
        System.out.println("Recursive: " + binarySearchRecursive(arr, target, 0, arr.length - 1));
    }

    static int binarySearchIterative(int[] arr, int target) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Avoid overflow
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    static int binarySearchRecursive(int[] arr, int target, int left, int right) {
        if (left > right) return -1;

        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) return binarySearchRecursive(arr, target, mid + 1, right);
        else return binarySearchRecursive(arr, target, left, mid - 1);
    }
}
```

<details>
<summary>Answer</summary>

```
Iterative: 5
Recursive: 5
```

**Explanation**: Binary search halves the search space each time. **Requires sorted array**. Time: O(log n). Use `left + (right - left) / 2` instead of `(left + right) / 2` to avoid integer overflow.

</details>

---

### Q63. Bubble Sort.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};

        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break; // Optimization: already sorted
        }

        System.out.println(Arrays.toString(arr));
    }
}
```

<details>
<summary>Answer</summary>

```
[11, 12, 22, 25, 34, 64, 90]
```

**Explanation**: Repeatedly swap adjacent elements if they're in the wrong order. The `swapped` flag optimizes for nearly sorted arrays. Time: O(n²) worst/average, O(n) best. Space: O(1). **Stable sort**.

</details>

---

### Q64. Selection Sort.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};

        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }

        System.out.println(Arrays.toString(arr));
    }
}
```

<details>
<summary>Answer</summary>

```
[11, 12, 22, 25, 64]
```

**Explanation**: Find the minimum element and place it at the correct position. Time: O(n²) always. Space: O(1). **Not stable** (can be made stable). Makes minimum swaps: O(n).

</details>

---

### Q65. Insertion Sort.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};

        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }

        System.out.println(Arrays.toString(arr));
    }
}
```

<details>
<summary>Answer</summary>

```
[5, 6, 11, 12, 13]
```

**Explanation**: Build the sorted array one element at a time by inserting each element into its correct position. Time: O(n²) worst, O(n) best (nearly sorted). **Stable sort**. Best for small or nearly sorted arrays.

</details>

---

### Q66. Merge Sort.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        mergeSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }

    static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1, n2 = right - mid;
        int[] L = new int[n1], R = new int[n2];

        System.arraycopy(arr, left, L, 0, n1);
        System.arraycopy(arr, mid + 1, R, 0, n2);

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
}
```

<details>
<summary>Answer</summary>

```
[3, 9, 10, 27, 38, 43, 82]
```

**Explanation**: **Divide and Conquer** — split array in half, sort each half recursively, merge the sorted halves. Time: O(n log n) always. Space: O(n). **Stable sort**.

</details>

---

### Q67. Quick Sort.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        quickSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivot = partition(arr, low, high);
            quickSort(arr, low, pivot - 1);
            quickSort(arr, pivot + 1, high);
        }
    }

    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 5, 7, 8, 9, 10]
```

**Explanation**: Pick a pivot, partition the array (smaller elements left, larger right), recursively sort partitions. Time: O(n log n) average, O(n²) worst. Space: O(log n). **Not stable**. Generally fastest in practice.

</details>

---

### Q68. Count occurrences of an element using Binary Search.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 2, 2, 3, 4, 5};
        int target = 2;

        int first = findFirst(arr, target);
        int last = findLast(arr, target);

        if (first == -1) {
            System.out.println("Element not found");
        } else {
            System.out.println("Count: " + (last - first + 1));
        }
    }

    static int findFirst(int[] arr, int target) {
        int left = 0, right = arr.length - 1, result = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) { result = mid; right = mid - 1; }
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return result;
    }

    static int findLast(int[] arr, int target) {
        int left = 0, right = arr.length - 1, result = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) { result = mid; left = mid + 1; }
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
Count: 4
```

**Explanation**: Find the first and last occurrence using modified Binary Search. Count = `last - first + 1`. **LeetCode #34**. Time: O(log n).

</details>

---

### Q69. Find the peak element in an array.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 3, 20, 4, 1, 0};
        System.out.println("Peak element: " + findPeak(arr));
    }

    static int findPeak(int[] arr) {
        int left = 0, right = arr.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < arr[mid + 1]) {
                left = mid + 1; // Peak is on the right
            } else {
                right = mid; // Peak is on the left (or at mid)
            }
        }

        return arr[left];
    }
}
```

<details>
<summary>Answer</summary>

```
Peak element: 20
```

**Explanation**: A peak element is greater than its neighbors. Use Binary Search — if `arr[mid] < arr[mid+1]`, the peak is to the right; otherwise, it's to the left. **LeetCode #162**. Time: O(log n).

</details>

---

### Q70. Search in a rotated sorted array.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        System.out.println("Found at index: " + search(arr, target));
    }

    static int search(int[] arr, int target) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;

            // Left half is sorted
            if (arr[left] <= arr[mid]) {
                if (target >= arr[left] && target < arr[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Right half is sorted
            else {
                if (target > arr[mid] && target <= arr[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

<details>
<summary>Answer</summary>

```
Found at index: 4
```

**Explanation**: One half of a rotated sorted array is always sorted. Determine which half is sorted, then check if target lies in that half. **LeetCode #33**. Time: O(log n).

</details>

---

## Section 8: Array Two Pointers & Sliding Window (Q71 – Q80)

---

### Q71. Two Sum — find two numbers that add up to a target.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                System.out.println("Indices: [" + map.get(complement) + ", " + i + "]");
                return;
            }
            map.put(nums[i], i);
        }
    }
}
```

<details>
<summary>Answer</summary>

```
Indices: [0, 1]
```

**Explanation**: Use a HashMap to store each number and its index. For each number, check if its complement exists. **LeetCode #1**. Time: O(n), Space: O(n).

</details>

---

### Q72. Container With Most Water.

```java
public class Main {
    public static void main(String[] args) {
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println("Max area: " + maxArea(height));
    }

    static int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, area);

            if (height[left] < height[right]) left++;
            else right--;
        }

        return maxArea;
    }
}
```

<details>
<summary>Answer</summary>

```
Max area: 49
```

**Explanation**: **Two Pointers** — start from both ends. Move the pointer with the shorter line inward (to potentially find a taller line). **LeetCode #11**. Time: O(n).

</details>

---

### Q73. Three Sum — find all unique triplets that sum to zero.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = threeSum(nums);
        System.out.println(result);
    }

    static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicates

            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
[[-1, -1, 2], [-1, 0, 1]]
```

**Explanation**: Sort the array, fix one element, then use two pointers to find the other two. Skip duplicates to avoid duplicate triplets. **LeetCode #15**. Time: O(n²).

</details>

---

### Q74. Maximum subarray sum (Kadane's Algorithm).

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Max subarray sum: " + maxSubarraySum(arr));
    }

    static int maxSubarraySum(int[] arr) {
        int maxSum = arr[0], currentSum = arr[0];

        for (int i = 1; i < arr.length; i++) {
            currentSum = Math.max(arr[i], currentSum + arr[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
```

<details>
<summary>Answer</summary>

```
Max subarray sum: 6
```

**Explanation**: **Kadane's Algorithm** — at each position, either start a new subarray or extend the previous one. Track the global maximum. Subarray `[4, -1, 2, 1]` gives sum 6. **LeetCode #53**. Time: O(n), Space: O(1).

> 💡 **Most asked DSA question** in interviews. Know this by heart!

</details>

---

### Q75. Maximum sum subarray of size K (Sliding Window).

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};
        int k = 3;
        System.out.println("Max sum of subarray of size " + k + ": " + maxSumSubarray(arr, k));
    }

    static int maxSumSubarray(int[] arr, int k) {
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }

        int maxSum = windowSum;
        for (int i = k; i < arr.length; i++) {
            windowSum += arr[i] - arr[i - k]; // Slide the window
            maxSum = Math.max(maxSum, windowSum);
        }

        return maxSum;
    }
}
```

<details>
<summary>Answer</summary>

```
Max sum of subarray of size 3: 9
```

**Explanation**: **Fixed-size Sliding Window**. Initialize with the first k elements. Then slide by adding the next element and removing the first element of the window. Time: O(n).

</details>

---

### Q76. Longest subarray with sum K.

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        int[] arr = {10, 5, 2, 7, 1, 9};
        int k = 15;
        System.out.println("Longest subarray length: " + longestSubarray(arr, k));
    }

    static int longestSubarray(int[] arr, int k) {
        HashMap<Integer, Integer> prefixSumMap = new HashMap<>();
        int sum = 0, maxLen = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];

            if (sum == k) {
                maxLen = i + 1;
            }

            if (prefixSumMap.containsKey(sum - k)) {
                maxLen = Math.max(maxLen, i - prefixSumMap.get(sum - k));
            }

            if (!prefixSumMap.containsKey(sum)) {
                prefixSumMap.put(sum, i);
            }
        }

        return maxLen;
    }
}
```

<details>
<summary>Answer</summary>

```
Longest subarray length: 4
```

**Explanation**: Use **Prefix Sum + HashMap**. Store `(prefixSum, firstIndex)`. If `prefixSum - k` exists in the map, a subarray with sum k ends at the current index. Time: O(n), Space: O(n).

</details>

---

### Q77. Sort an array of 0s, 1s, and 2s (Dutch National Flag).

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 0, 2, 1, 1, 0};

        int low = 0, mid = 0, high = arr.length - 1;

        while (mid <= high) {
            if (arr[mid] == 0) {
                swap(arr, low, mid);
                low++;
                mid++;
            } else if (arr[mid] == 1) {
                mid++;
            } else {
                swap(arr, mid, high);
                high--;
            }
        }

        System.out.println(Arrays.toString(arr));
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
```

<details>
<summary>Answer</summary>

```
[0, 0, 1, 1, 2, 2]
```

**Explanation**: **Dutch National Flag Algorithm** by Dijkstra. Three pointers: `low` (boundary for 0s), `mid` (current), `high` (boundary for 2s). **LeetCode #75**. Time: O(n), Space: O(1), single pass.

</details>

---

### Q78. Find the majority element (appears more than n/2 times).

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("Majority element: " + majorityElement(arr));
    }

    static int majorityElement(int[] arr) {
        // Boyer-Moore Voting Algorithm
        int candidate = arr[0], count = 1;

        for (int i = 1; i < arr.length; i++) {
            if (count == 0) {
                candidate = arr[i];
                count = 1;
            } else if (arr[i] == candidate) {
                count++;
            } else {
                count--;
            }
        }

        return candidate;
    }
}
```

<details>
<summary>Answer</summary>

```
Majority element: 2
```

**Explanation**: **Boyer-Moore Voting Algorithm**. Maintain a candidate and count. If count drops to 0, pick a new candidate. The majority element will survive. **LeetCode #169**. Time: O(n), Space: O(1).

</details>

---

### Q79. Trapping Rain Water.

```java
public class Main {
    public static void main(String[] args) {
        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println("Water trapped: " + trap(height));
    }

    static int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
                left++;
            } else {
                rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
                right--;
            }
        }

        return water;
    }
}
```

<details>
<summary>Answer</summary>

```
Water trapped: 6
```

**Explanation**: **Two Pointers** approach. Water at each position = `min(leftMax, rightMax) - height[i]`. Move the pointer with the smaller max. **LeetCode #42** (Hard). Time: O(n), Space: O(1).

</details>

---

### Q80. Find the longest consecutive sequence.

```java
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        int[] nums = {100, 4, 200, 1, 3, 2};
        System.out.println("Longest consecutive sequence: " + longestConsecutive(nums));
    }

    static int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int maxLen = 0;

        for (int num : set) {
            // Only start counting from the beginning of a sequence
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int currentLen = 1;

                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    currentLen++;
                }

                maxLen = Math.max(maxLen, currentLen);
            }
        }

        return maxLen;
    }
}
```

<details>
<summary>Answer</summary>

```
Longest consecutive sequence: 4
```

**Explanation**: Use a HashSet for O(1) lookups. Only start counting from numbers that are the **start of a sequence** (no `num-1` in set). Sequence: `1, 2, 3, 4` → length 4. **LeetCode #128**. Time: O(n).

</details>

---

## Section 9: Array Matrix / 2D Array (Q81 – Q90)

---

### Q81. Declare, initialize, and print a 2D array.

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Print using nested loops
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf("%4d", matrix[i][j]);
            }
            System.out.println();
        }

        System.out.println("Rows: " + matrix.length);
        System.out.println("Cols: " + matrix[0].length);
    }
}
```

<details>
<summary>Answer</summary>

```
   1   2   3
   4   5   6
   7   8   9
Rows: 3
Cols: 3
```

**Explanation**: 2D arrays in Java are arrays of arrays. `matrix.length` = rows, `matrix[0].length` = columns.

</details>

---

### Q82. Transpose a matrix.

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int rows = matrix.length, cols = matrix[0].length;
        int[][] transpose = new int[cols][rows];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transpose[j][i] = matrix[i][j];
            }
        }

        // Print
        for (int[] row : transpose) {
            for (int val : row) {
                System.out.printf("%4d", val);
            }
            System.out.println();
        }
    }
}
```

<details>
<summary>Answer</summary>

```
   1   4   7
   2   5   8
   3   6   9
```

**Explanation**: Swap rows and columns: `transpose[j][i] = matrix[i][j]`. For square matrices, you can do this in-place by swapping `matrix[i][j]` with `matrix[j][i]` for `j > i`.

</details>

---

### Q83. Rotate a matrix by 90 degrees clockwise.

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int n = matrix.length;

        // Step 1: Transpose
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }

        // Print
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.printf("%4d", val);
            }
            System.out.println();
        }
    }
}
```

<details>
<summary>Answer</summary>

```
   7   4   1
   8   5   2
   9   6   3
```

**Explanation**: Two-step approach: (1) Transpose the matrix, (2) Reverse each row. **LeetCode #48**. Time: O(n²), Space: O(1) — in-place!

</details>

---

### Q84. Spiral order traversal of a matrix.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        };

        List<Integer> result = spiralOrder(matrix);
        System.out.println(result);
    }

    static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Right
            for (int i = left; i <= right; i++) result.add(matrix[top][i]);
            top++;
            // Down
            for (int i = top; i <= bottom; i++) result.add(matrix[i][right]);
            right--;
            // Left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) result.add(matrix[bottom][i]);
                bottom--;
            }
            // Up
            if (left <= right) {
                for (int i = bottom; i >= top; i--) result.add(matrix[i][left]);
                left++;
            }
        }

        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

**Explanation**: Maintain four boundaries (top, bottom, left, right). Traverse right → down → left → up, shrinking boundaries each time. **LeetCode #54**. Time: O(m×n).

</details>

---

### Q85. Search in a row-wise and column-wise sorted matrix.

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {10, 20, 30, 40},
            {15, 25, 35, 45},
            {27, 29, 37, 48},
            {32, 33, 39, 50}
        };

        int target = 29;
        int[] result = search(matrix, target);
        System.out.println("Found at: (" + result[0] + ", " + result[1] + ")");
    }

    static int[] search(int[][] matrix, int target) {
        int row = 0, col = matrix[0].length - 1;

        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) return new int[]{row, col};
            else if (matrix[row][col] > target) col--;
            else row++;
        }

        return new int[]{-1, -1};
    }
}
```

<details>
<summary>Answer</summary>

```
Found at: (2, 1)
```

**Explanation**: Start from the **top-right corner**. If current > target, go left. If current < target, go down. **LeetCode #240**. Time: O(m + n).

</details>

---

### Q86. Set matrix zeroes.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 1, 1},
            {1, 0, 1},
            {1, 1, 1}
        };

        setZeroes(matrix);

        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    static void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRow = false, firstCol = false;

        // Check if first row/col have zeros
        for (int j = 0; j < n; j++) if (matrix[0][j] == 0) firstRow = true;
        for (int i = 0; i < m; i++) if (matrix[i][0] == 0) firstCol = true;

        // Use first row/col as markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Zero out cells based on markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Handle first row and column
        if (firstRow) Arrays.fill(matrix[0], 0);
        if (firstCol) for (int i = 0; i < m; i++) matrix[i][0] = 0;
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 0, 1]
[0, 0, 0]
[1, 0, 1]
```

**Explanation**: If an element is 0, set its entire row and column to 0. Use the first row/column as markers to achieve O(1) extra space. **LeetCode #73**. Time: O(m×n).

</details>

---

### Q87. Matrix multiplication.

```java
public class Main {
    public static void main(String[] args) {
        int[][] A = {{1, 2}, {3, 4}};
        int[][] B = {{5, 6}, {7, 8}};

        int[][] result = multiply(A, B);

        for (int[] row : result) {
            for (int val : row) {
                System.out.printf("%4d", val);
            }
            System.out.println();
        }
    }

    static int[][] multiply(int[][] A, int[][] B) {
        int m = A.length, n = B[0].length, k = A[0].length;
        int[][] result = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int p = 0; p < k; p++) {
                    result[i][j] += A[i][p] * B[p][j];
                }
            }
        }
        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
  19  22
  43  50
```

**Explanation**: `result[i][j] = sum of A[i][p] * B[p][j]` for all p. Matrix multiplication is O(m × n × k). Result dimensions: A(m×k) × B(k×n) = (m×n).

</details>

---

### Q88. Print matrix in diagonal order.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        List<Integer> result = diagonalOrder(matrix);
        System.out.println(result);
    }

    static List<Integer> diagonalOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int m = matrix.length, n = matrix[0].length;

        for (int d = 0; d < m + n - 1; d++) {
            List<Integer> diagonal = new ArrayList<>();
            int row = d < n ? 0 : d - n + 1;
            int col = d < n ? d : n - 1;

            while (row < m && col >= 0) {
                diagonal.add(matrix[row][col]);
                row++;
                col--;
            }

            if (d % 2 == 0) Collections.reverse(diagonal);
            result.addAll(diagonal);
        }

        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 2, 4, 7, 5, 3, 6, 8, 9]
```

**Explanation**: Traverse diagonals alternating direction (up-right, then down-left). **LeetCode #498**. Time: O(m×n).

</details>

---

### Q89. Find the row with the maximum number of 1s in a binary matrix (rows sorted).

```java
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {0, 0, 0, 1},
            {0, 0, 1, 1},
            {0, 1, 1, 1},
            {0, 0, 0, 0}
        };

        System.out.println("Row with max 1s: " + rowWithMax1s(matrix));
    }

    static int rowWithMax1s(int[][] matrix) {
        int maxRow = -1;
        int j = matrix[0].length - 1;

        for (int i = 0; i < matrix.length; i++) {
            while (j >= 0 && matrix[i][j] == 1) {
                maxRow = i;
                j--;
            }
        }

        return maxRow;
    }
}
```

<details>
<summary>Answer</summary>

```
Row with max 1s: 2
```

**Explanation**: Start from the top-right corner. If cell is 1, move left (this row has more 1s). If cell is 0, move down. Time: O(m + n) — much better than O(m × n).

</details>

---

### Q90. Find all paths from top-left to bottom-right in a matrix.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] grid = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        List<List<Integer>> paths = new ArrayList<>();
        findPaths(grid, 0, 0, new ArrayList<>(), paths);

        for (List<Integer> path : paths) {
            System.out.println(path);
        }
    }

    static void findPaths(int[][] grid, int r, int c, List<Integer> current, List<List<Integer>> paths) {
        int m = grid.length, n = grid[0].length;

        current.add(grid[r][c]);

        if (r == m - 1 && c == n - 1) {
            paths.add(new ArrayList<>(current));
        } else {
            if (r + 1 < m) findPaths(grid, r + 1, c, current, paths);
            if (c + 1 < n) findPaths(grid, r, c + 1, current, paths);
        }

        current.remove(current.size() - 1); // backtrack
    }
}
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

**Explanation**: **Backtracking** — from each cell, move right or down. When reaching the bottom-right, save the path. Time: O(2^(m+n)).

</details>

---

## Section 10: Array Placement Level (Q91 – Q100)

---

### Q91. Merge two sorted arrays without extra space.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 5, 7};
        int[] arr2 = {2, 4, 6, 8};

        int n = arr1.length, m = arr2.length;

        // Gap method (Shell sort inspired)
        int gap = (n + m + 1) / 2;

        while (gap > 0) {
            int i = 0, j = gap;

            while (j < n + m) {
                int val1 = (i < n) ? arr1[i] : arr2[i - n];
                int val2 = (j < n) ? arr1[j] : arr2[j - n];

                if (val1 > val2) {
                    if (i < n && j < n) {
                        int temp = arr1[i]; arr1[i] = arr1[j]; arr1[j] = temp;
                    } else if (i < n) {
                        int temp = arr1[i]; arr1[i] = arr2[j - n]; arr2[j - n] = temp;
                    } else {
                        int temp = arr2[i - n]; arr2[i - n] = arr2[j - n]; arr2[j - n] = temp;
                    }
                }
                i++;
                j++;
            }
            if (gap == 1) break;
            gap = (gap + 1) / 2;
        }

        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 2, 3, 4]
[5, 6, 7, 8]
```

**Explanation**: **Gap Method** — inspired by Shell Sort. Start with a large gap and reduce it. Swap elements that are `gap` apart if they're in the wrong order. Time: O((n+m) × log(n+m)), Space: O(1).

</details>

---

### Q92. Find the missing and repeating number.

```java
public class Main {
    public static void main(String[] args) {
        int[] arr = {3, 1, 2, 5, 3};
        int n = arr.length;

        int[] result = findMissingRepeating(arr, n);
        System.out.println("Repeating: " + result[0]);
        System.out.println("Missing: " + result[1]);
    }

    static int[] findMissingRepeating(int[] arr, int n) {
        long sumArr = 0, sumSqArr = 0;

        for (int val : arr) {
            sumArr += val;
            sumSqArr += (long) val * val;
        }

        long sumExpected = (long) n * (n + 1) / 2;
        long sumSqExpected = (long) n * (n + 1) * (2 * n + 1) / 6;

        long diff = sumArr - sumExpected;       // x - y
        long sqDiff = sumSqArr - sumSqExpected; // x² - y²

        long sumXY = sqDiff / diff;             // x + y

        int repeating = (int) ((diff + sumXY) / 2);
        int missing = (int) ((sumXY - diff) / 2);

        return new int[]{repeating, missing};
    }
}
```

<details>
<summary>Answer</summary>

```
Repeating: 3
Missing: 4
```

**Explanation**: Using math: `x - y = sumArr - sumExpected`, `x² - y² = sumSqArr - sumSqExpected`, so `x + y = (x² - y²) / (x - y)`. Solve the two equations. Time: O(n), Space: O(1).

</details>

---

### Q93. Count inversions in an array (Merge Sort based).

```java
public class Main {
    static int count = 0;

    public static void main(String[] args) {
        int[] arr = {2, 4, 1, 3, 5};
        count = 0;
        mergeSort(arr, 0, arr.length - 1);
        System.out.println("Inversion count: " + count);
    }

    static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int i = left, j = mid + 1, k = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                count += (mid - i + 1); // All remaining in left are inversions
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) temp[k++] = arr[i++];
        while (j <= right) temp[k++] = arr[j++];

        System.arraycopy(temp, 0, arr, left, temp.length);
    }
}
```

<details>
<summary>Answer</summary>

```
Inversion count: 3
```

**Explanation**: An inversion is a pair (i, j) where `i < j` but `arr[i] > arr[j]`. Inversions: (2,1), (4,1), (4,3). Using **Merge Sort** to count inversions efficiently. Time: O(n log n).

</details>

---

### Q94. Next permutation.

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        nextPermutation(nums);
        System.out.println(Arrays.toString(nums));

        int[] nums2 = {3, 2, 1};
        nextPermutation(nums2);
        System.out.println(Arrays.toString(nums2));
    }

    static void nextPermutation(int[] nums) {
        int n = nums.length;

        // Step 1: Find the break point (first decreasing from right)
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;

        if (i >= 0) {
            // Step 2: Find the smallest element > nums[i] from the right
            int j = n - 1;
            while (nums[j] <= nums[i]) j--;
            // Step 3: Swap
            int temp = nums[i]; nums[i] = nums[j]; nums[j] = temp;
        }

        // Step 4: Reverse from i+1 to end
        int left = i + 1, right = n - 1;
        while (left < right) {
            int temp = nums[left]; nums[left] = nums[right]; nums[right] = temp;
            left++; right--;
        }
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 3, 2]
[1, 2, 3]
```

**Explanation**: Find the rightmost ascending pair, swap with the next larger element, reverse the suffix. If no ascending pair exists (descending order), reverse the whole array. **LeetCode #31**. Time: O(n).

</details>

---

### Q95. Merge overlapping intervals.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] intervals = {{1,3},{2,6},{8,10},{15,18}};
        int[][] merged = mergeIntervals(intervals);

        for (int[] interval : merged) {
            System.out.println(Arrays.toString(interval));
        }
    }

    static int[][] mergeIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            int[] last = result.get(result.size() - 1);
            if (intervals[i][0] <= last[1]) {
                last[1] = Math.max(last[1], intervals[i][1]);
            } else {
                result.add(intervals[i]);
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}
```

<details>
<summary>Answer</summary>

```
[1, 6]
[8, 10]
[15, 18]
```

**Explanation**: Sort by start time. If the current interval overlaps with the last merged one, extend it. Otherwise, add as new. **LeetCode #56**. Time: O(n log n).

</details>

---

### Q96. Product of array except self (without using division).

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        System.out.println(Arrays.toString(productExceptSelf(nums)));
    }

    static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        // Left pass: result[i] = product of all elements to the left
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        // Right pass: multiply by product of all elements to the right
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
[24, 12, 8, 6]
```

**Explanation**: Two-pass approach. First pass computes left products. Second pass multiplies with right products. No division used. **LeetCode #238**. Time: O(n), Space: O(1) (result array doesn't count).

</details>

---

### Q97. Subarray with given XOR.

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        int[] arr = {4, 2, 2, 6, 4};
        int target = 6;
        System.out.println("Count of subarrays with XOR " + target + ": " + countSubarraysWithXOR(arr, target));
    }

    static int countSubarraysWithXOR(int[] arr, int target) {
        HashMap<Integer, Integer> prefixXorCount = new HashMap<>();
        int xor = 0, count = 0;

        for (int num : arr) {
            xor ^= num;

            if (xor == target) count++;

            if (prefixXorCount.containsKey(xor ^ target)) {
                count += prefixXorCount.get(xor ^ target);
            }

            prefixXorCount.merge(xor, 1, Integer::sum);
        }

        return count;
    }
}
```

<details>
<summary>Answer</summary>

```
Count of subarrays with XOR 6: 4
```

**Explanation**: Similar to prefix sum approach but with XOR. If `prefixXor[0..i] ^ prefixXor[0..j] = target`, then `subarray[j+1..i]` has XOR = target. Use HashMap to count. Time: O(n).

</details>

---

### Q98. Longest subarray with sum 0.

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        int[] arr = {15, -2, 2, -8, 1, 7, 10, 23};
        System.out.println("Longest subarray with sum 0: " + longestZeroSumSubarray(arr));
    }

    static int longestZeroSumSubarray(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int sum = 0, maxLen = 0;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];

            if (sum == 0) {
                maxLen = i + 1;
            } else if (map.containsKey(sum)) {
                maxLen = Math.max(maxLen, i - map.get(sum));
            } else {
                map.put(sum, i);
            }
        }

        return maxLen;
    }
}
```

<details>
<summary>Answer</summary>

```
Longest subarray with sum 0: 5
```

**Explanation**: If `prefixSum[i] == prefixSum[j]`, then `sum[i+1..j] = 0`. Store the first occurrence of each prefix sum. Subarray: `[-2, 2, -8, 1, 7]` has sum 0 and length 5. Time: O(n).

</details>

---

### Q99. Maximum product subarray.

```java
public class Main {
    public static void main(String[] args) {
        int[] nums = {2, 3, -2, 4};
        System.out.println("Max product: " + maxProduct(nums));
    }

    static int maxProduct(int[] nums) {
        int maxProd = nums[0], minProd = nums[0], result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
                int temp = maxProd;
                maxProd = minProd;
                minProd = temp;
            }

            maxProd = Math.max(nums[i], maxProd * nums[i]);
            minProd = Math.min(nums[i], minProd * nums[i]);

            result = Math.max(result, maxProd);
        }

        return result;
    }
}
```

<details>
<summary>Answer</summary>

```
Max product: 6
```

**Explanation**: Track both **max** and **min** products (because a negative × negative = positive). Swap max and min when current number is negative. **LeetCode #152**. Time: O(n), Space: O(1).

</details>

---

### Q100. 4Sum — find all unique quadruplets that sum to a target.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 0, -1, 0, -2, 2};
        int target = 0;
        System.out.println(fourSum(nums, target));
    }

    static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1, right = n - 1;
                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return result;
    }
}
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
| **HashMap** | Frequency, pairs, complement problems | Q71, Q76, Q80 |
| **Bit Manipulation** | Unique chars, XOR tricks | Q38, Q97 |

---

> 🎯 **Pro Tip**: Practice each question without looking at the answer first. Then compare your solution. Understanding the **why** behind each approach is more important than memorizing code.

---

*Happy Coding! ☕ Keep Practicing! 🚀*
