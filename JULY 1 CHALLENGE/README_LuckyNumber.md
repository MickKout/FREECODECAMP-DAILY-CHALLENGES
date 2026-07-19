# Lucky Number — Code Explained

> Calculate a "lucky number" from a person's full name by comparing vowel counts, consonant counts, and name lengths between first and last name.

---

## Table of Contents
1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [The Formula](#2-the-formula)
3. [Why Regex Instead of `.count()`](#3-why-regex-instead-of-count)
4. [Step-by-Step Code Breakdown](#4-step-by-step-code-breakdown)
5. [Worked Examples](#5-worked-examples)
6. [The Special Case — Lucky 13](#6-the-special-case--lucky-13)
7. [Methods Used](#7-methods-used)
8. [Full Annotated Code](#8-full-annotated-code)

---

## 1. The Problem in Plain English

Given a full name as a string (e.g. `"John Doe"`), the function:

1. Splits it into first and last name
2. Counts the vowels and consonants in each name (case-insensitively)
3. Compares the two names using a formula involving `min` and `max` of those counts
4. Returns the absolute difference between two calculated scores as the lucky number
5. If the lucky number would be `0`, returns `13` instead

```python
get_lucky_number("John Doe")    # → 21
get_lucky_number("Chloe Perez") # → 13  (would be 0, so returns 13)
```

---

## 2. The Formula

The algorithm computes two intermediate scores and subtracts them:

```
first_result  = smaller_vowel_count  × smaller_consonant_count  × smaller_name_length
second_result = larger_vowel_count   × larger_consonant_count   × larger_name_length

lucky_number = |first_result - second_result|
```

Where `smaller` and `larger` refer to the **minimum** and **maximum** of each property **across** the two names — not within a single name.

If `lucky_number` is `0`, return `13`.

---

## 3. Why Regex Instead of `.count()`

An earlier version of this function used Python's `.count("a")` five times to count vowels. This approach has a critical flaw — it is **case-sensitive**:

```python
"Elizabeth".count("e")   # → 2  (misses the capital "E" at the start!)
"Elizabeth".count("E")   # → 1
# Total found: 3 — but requires calling count() twice per vowel, ten times total
```

The correct approach uses `re.findall()` with the `re.IGNORECASE` flag, which matches both `"e"` and `"E"` in a single call:

```python
re.findall(r'[aeiou]', "Elizabeth", re.IGNORECASE)
# → ['E', 'i', 'a', 'e']  — 4 vowels, all found ✅
```

This matters for the test outputs. `"Elizabeth Hernandez"` should return `81`, but the case-sensitive version returned `13` because it missed the capital `"E"`, making both names appear to have `3` vowels instead of `4` and `3`.

| Name | `.count()` vowels | `re.IGNORECASE` vowels | Correct? |
|---|---|---|---|
| `"Elizabeth"` | 3 (misses `"E"`) | 4 | `re` ✅ |
| `"Olivia"` | 4 | 4 | both ✅ |
| `"John"` | 1 | 1 | both ✅ |

---

## 4. Step-by-Step Code Breakdown

### Step 1 — Import `re` and validate the input

```python
import re

def get_lucky_number(name):
    if not name:
        return "Please enter a valid name."
```

`import re` loads Python's built-in regular expressions module. `not name` is falsy for `None`, empty string `""`, or any other empty value — this guard prevents the function from crashing on bad input.

---

### Step 2 — Split the name into first and last

```python
name_parts = name.split(" ")
first_name = name_parts[0]
last_name  = name_parts[1]
```

`.split(" ")` cuts the string at every space, returning a list of words. For `"John Doe"`:

```python
"John Doe".split(" ")  →  ["John", "Doe"]
                               [0]     [1]
```

`name_parts[0]` is the first name, `name_parts[1]` is the last name.

---

### Step 3 — Count vowels and consonants with regex

```python
first_vowel_count     = len(re.findall(r'[aeiou]', first_name, re.IGNORECASE))
first_consonant_count = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', first_name, re.IGNORECASE))
last_vowel_count      = len(re.findall(r'[aeiou]', last_name, re.IGNORECASE))
last_consonant_count  = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', last_name, re.IGNORECASE))
```

`re.findall(pattern, string, flags)` scans the entire string and returns a **list** of every character that matches the pattern. `len()` of that list is the count.

- `r'[aeiou]'` — a character class matching any single vowel
- `r'[bcdfghjklmnpqrstvwxyz]'` — a character class matching any single consonant
- `re.IGNORECASE` — makes the match case-insensitive, so `"E"` matches `[aeiou]`

Unlike the previous `.count()` approach, consonants are now counted **directly** by their own regex rather than derived by subtraction. This is more accurate because it explicitly excludes non-letter characters (spaces, hyphens, apostrophes) if they were ever present.

```python
re.findall(r'[aeiou]', "Elizabeth", re.IGNORECASE)
# → ['E', 'i', 'a', 'e']  →  len = 4

re.findall(r'[bcdfghjklmnpqrstvwxyz]', "Elizabeth", re.IGNORECASE)
# → ['l', 'z', 'b', 't', 'h']  →  len = 5
```

---

### Step 4 — Find the smaller and larger values across both names

```python
smaller_vowel_count     = min(first_vowel_count,     last_vowel_count)
smaller_consonant_count = min(first_consonant_count, last_consonant_count)
larger_vowel_count      = max(first_vowel_count,     last_vowel_count)
larger_consonant_count  = max(first_consonant_count, last_consonant_count)
smaller_name_length     = min(len(first_name),       len(last_name))
larger_name_length      = max(len(first_name),       len(last_name))
```

`min()` and `max()` compare two values and return the smaller or larger one respectively. These six variables capture the full picture of how the two names compare across three dimensions: vowels, consonants, and total length.

For `"Elizabeth Hernandez"`:

```
             First(Elizabeth)  Last(Hernandez)   min    max
Vowels:             4                3            3      4
Consonants:         5                6            5      6
Length:             9                9            9      9
```

---

### Step 5 — Calculate the two scores

```python
first_result  = smaller_vowel_count * smaller_consonant_count * smaller_name_length
second_result = larger_vowel_count  * larger_consonant_count  * larger_name_length
```

Multiply the three "smaller" properties together for one score and the three "larger" properties for the other. This creates a contrast between the structurally "weaker" and "stronger" name across all three dimensions at once.

For `"Elizabeth Hernandez"`:
```
first_result  = 3 × 5 × 9 = 135
second_result = 4 × 6 × 9 = 216
```

---

### Step 6 — Calculate the lucky number

```python
lucky_number = abs(first_result - second_result)
return 13 if lucky_number == 0 else lucky_number
```

`abs()` ensures the result is always positive regardless of which score was larger. The ternary on the return line is Python shorthand for returning `13` when the result is `0`, and the actual lucky number otherwise.

---

## 5. Worked Examples

### Example 1 — `"John Doe"` → `21`

```
First name: "John"  → vowels=1 ("o"),     consonants=3 ("J","h","n"), length=4
Last name:  "Doe"   → vowels=2 ("o","e"), consonants=1 ("D"),         length=3

Comparing across names:
  smaller vowels      = min(1, 2) = 1
  smaller consonants  = min(3, 1) = 1
  smaller length      = min(4, 3) = 3
  larger vowels       = max(1, 2) = 2
  larger consonants   = max(3, 1) = 3
  larger length       = max(4, 3) = 4

first_result  = 1 × 1 × 3 =  3
second_result = 2 × 3 × 4 = 24

lucky_number = |3 - 24| = 21 ✅
```

---

### Example 2 — `"Olivia Lewis"` → `52`

```
First name: "Olivia" → vowels=4 ("O","i","i","a"), consonants=2 ("l","v"), length=6
Last name:  "Lewis"  → vowels=2 ("e","i"),          consonants=3 ("L","w","s"), length=5

Note: "O" in "Olivia" is caught by re.IGNORECASE ✅

Comparing across names:
  smaller vowels      = min(4, 2) = 2
  smaller consonants  = min(2, 3) = 2
  smaller length      = min(6, 5) = 5
  larger vowels       = max(4, 2) = 4
  larger consonants   = max(2, 3) = 3
  larger length       = max(6, 5) = 6

first_result  = 2 × 2 × 5 = 20
second_result = 4 × 3 × 6 = 72

lucky_number = |20 - 72| = 52 ✅
```

---

### Example 3 — `"Elizabeth Hernandez"` → `81`

```
First name: "Elizabeth" → vowels=4 ("E","i","a","e"), consonants=5 ("l","z","b","t","h"), length=9
Last name:  "Hernandez" → vowels=3 ("e","a","e"),     consonants=6 ("H","r","n","d","z"), length=9

Note: "E" in "Elizabeth" is caught by re.IGNORECASE — this was MISSED by the old .count() version ✅

Comparing across names:
  smaller vowels      = min(4, 3) = 3
  smaller consonants  = min(5, 6) = 5
  smaller length      = min(9, 9) = 9
  larger vowels       = max(4, 3) = 4
  larger consonants   = max(5, 6) = 6
  larger length       = max(9, 9) = 9

first_result  = 3 × 5 × 9 = 135
second_result = 4 × 6 × 9 = 216

lucky_number = |135 - 216| = 81 ✅
```

---

### Example 4 — `"Chloe Perez"` → `13`

```
First name: "Chloe" → vowels=2 ("o","e"), consonants=3 ("C","h","l"), length=5
Last name:  "Perez" → vowels=2 ("e","e"), consonants=3 ("P","r","z"), length=5

Both names are perfectly balanced — same vowels, consonants, and length.

first_result  = 2 × 3 × 5 = 30
second_result = 2 × 3 × 5 = 30

lucky_number = |30 - 30| = 0 → fallback to 13 ✅
```

> Any two names with identical vowel count, consonant count, and length will always produce `0` and return `13`.

---

## 6. The Special Case — Lucky 13

When both names are structurally identical in all three dimensions, the formula produces `0`. Rather than returning `0`, the function substitutes `13`.

```python
return 13 if lucky_number == 0 else lucky_number
#      ↑ fallback   ↑ condition   ↑ normal result
```

It reads like plain English: "return 13 *if* lucky_number is zero, *else* return lucky_number."

---

## 7. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `import re` | Top of file | Loads Python's built-in regular expressions module |
| `not name` | Input validation | Falsy check — true for `None`, `""`, and other empty values |
| `str.split(" ")` | Splitting the name | Splits a string at every space, returns a list of substrings |
| `re.findall(pattern, string, flags)` | Counting vowels/consonants | Returns a list of all matches of `pattern` in `string` |
| `r'[aeiou]'` | Vowel pattern | Raw string regex — character class matching any one vowel |
| `r'[bcdfghjklmnpqrstvwxyz]'` | Consonant pattern | Character class matching any one consonant |
| `re.IGNORECASE` | Regex flag | Makes matching case-insensitive — catches `"E"` as a vowel |
| `len(list)` | Getting the count | Returns the number of items in the list returned by `findall` |
| `min(a, b)` | Comparing names | Returns the smaller of two values |
| `max(a, b)` | Comparing names | Returns the larger of two values |
| `abs(n)` | Lucky number | Returns the absolute (always positive) value of a number |
| `x if condition else y` | Fallback to 13 | Python ternary — returns `x` if condition is true, otherwise `y` |

---

## 8. Full Annotated Code

```python
import re

def get_lucky_number(name):

    # Guard: return message for empty/None input
    if not name:
        return "Please enter a valid name."

    # Split "First Last" into two parts
    name_parts = name.split(" ")
    first_name = name_parts[0]
    last_name  = name_parts[1]

    # Count vowels and consonants using case-insensitive regex
    # re.IGNORECASE ensures capital letters (e.g. "E" in "Elizabeth") are matched
    first_vowel_count     = len(re.findall(r'[aeiou]', first_name, re.IGNORECASE))
    first_consonant_count = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', first_name, re.IGNORECASE))
    last_vowel_count      = len(re.findall(r'[aeiou]', last_name, re.IGNORECASE))
    last_consonant_count  = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', last_name, re.IGNORECASE))

    # Compare the two names: find smaller and larger for each property
    smaller_vowel_count     = min(first_vowel_count,     last_vowel_count)
    smaller_consonant_count = min(first_consonant_count, last_consonant_count)
    larger_vowel_count      = max(first_vowel_count,     last_vowel_count)
    larger_consonant_count  = max(first_consonant_count, last_consonant_count)
    smaller_name_length     = min(len(first_name),       len(last_name))
    larger_name_length      = max(len(first_name),       len(last_name))

    # Multiply the three "smaller" values, and separately the three "larger" values
    first_result  = smaller_vowel_count * smaller_consonant_count * smaller_name_length
    second_result = larger_vowel_count  * larger_consonant_count  * larger_name_length

    # Absolute difference; return 13 if the result is 0
    lucky_number = abs(first_result - second_result)
    return 13 if lucky_number == 0 else lucky_number

print(get_lucky_number("John Doe"))            # → 21
print(get_lucky_number("Olivia Lewis"))        # → 52
print(get_lucky_number("James Wilson"))        # → 18
print(get_lucky_number("Elizabeth Hernandez")) # → 81
print(get_lucky_number("Mike Walker"))         # → 32
print(get_lucky_number("Chloe Perez"))         # → 13
```
