# Duplicate Character Count — Code Explained

> Count how many unique characters appear in both strings at the same time.

---

## Table of Contents
1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [What "Unique" Means Here](#2-what-unique-means-here)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [The Key Condition Explained](#4-the-key-condition-explained)
5. [Worked Example](#5-worked-example)
6. [Methods Used](#6-methods-used)
7. [Full Annotated Code](#7-full-annotated-code)

---

## 1. The Problem in Plain English

Given two strings, count how many characters they share in common — but count each shared character only **once**, even if it appears multiple times in either string.

```js
duplicateCharacterCount("hello", "hola")
// Shared characters: "h", "o", "l"
// → 3

duplicateCharacterCount("ola", "hej")
// No characters in common
// → 0
```

---

## 2. What "Unique" Means Here

The tricky part is the word "unique". Consider `"hello"` and `"hello to everyone around the world"`:

- `"l"` appears twice in `"hello"` — but it should only count as **1** shared character, not 2
- The function counts distinct shared characters, not total occurrences

This is what makes the condition inside the loop more complex than a simple equality check.

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Initialise the counter

```js
let count = 0;
```

A simple integer that starts at zero and is incremented once for each unique shared character found.

---

### Step 2 — Loop through every character of `str1`

```js
for (let i = 0; i < str1.length; i++) {
```

`i` is the index into `str1`. At each iteration, `str1[i]` is the current character being checked — for example, when `str1 = "hello"`:

```
i=0 → "h"
i=1 → "e"
i=2 → "l"
i=3 → "l"   ← duplicate
i=4 → "o"
```

---

### Step 3 — Loop through every character of `str2`

```js
for (let j = 0; j < str2.length; j++) {
```

For each character in `str1`, scan the entirety of `str2` looking for a match. `j` is the index into `str2`. This creates a nested loop that compares every possible pair of characters between the two strings.

For `str1 = "hello"` and `str2 = "hola"`, the pairs visited are:

```
[h,h] [h,o] [h,l] [h,a]
[e,h] [e,o] [e,l] [e,a]
[l,h] [l,o] [l,l] [l,a]
[l,h] [l,o] [l,l] [l,a]   ← i=3, same as i=2 (duplicate "l")
[o,h] [o,o] [o,l] [o,a]
```

---

### Step 4 — The matching condition

```js
if (str2[j] === str1[i] && str1.indexOf(str2[j]) === i) {
  count++;
}
```

This is the heart of the function. It has **two conditions** that must both be true:

**Condition 1:** `str2[j] === str1[i]`
The character at position `j` in `str2` must equal the character at position `i` in `str1`. This is a basic character match.

**Condition 2:** `str1.indexOf(str2[j]) === i`
The **first** occurrence of the matched character in `str1` must be at position `i`.

Condition 2 is what prevents counting duplicates. See the next section for a detailed explanation.

---

### Step 5 — Return the count

```js
return count;
```

After all pairs have been compared, return the total number of unique shared characters.

---

## 4. The Key Condition Explained

The second condition `str1.indexOf(str2[j]) === i` is the most important and least obvious line in the function. Here is exactly what it does and why it is needed.

### What `indexOf` does

`str1.indexOf(char)` returns the index of the **first** occurrence of `char` in `str1`. It always finds the first one, regardless of how many times the character appears.

```js
"hello".indexOf("l")  // → 2  (the first "l", not the second at index 3)
"hello".indexOf("h")  // → 0
"hello".indexOf("z")  // → -1 (not found)
```

### Why the condition is needed

Consider `str1 = "hello"` and `str2 = "hola"`. The character `"l"` appears at index `2` and index `3` in `str1`.

Without condition 2, the loop would count `"l"` **twice** — once when `i=2` and once when `i=3` — because both positions match `"l"` in `str2`.

With condition 2:
```
When i=2, str1[i]="l":
  str1.indexOf("l") → 2
  2 === 2 → TRUE  ✅ → count it (first occurrence)

When i=3, str1[i]="l":
  str1.indexOf("l") → 2   (always returns the FIRST occurrence)
  2 === 3 → FALSE ❌ → skip it (duplicate, don't count again)
```

In plain English: condition 2 asks *"is the current position the first time this character appears in str1?"* — if yes, count it; if no, it's a duplicate and skip it.

### Visual summary

```
str1 = "h  e  l  l  o"
idx  =  0  1  2  3  4

Character "l" at i=2:  indexOf("l") = 2, and i = 2  → 2 === 2 ✅ COUNT
Character "l" at i=3:  indexOf("l") = 2, and i = 3  → 2 === 3 ❌ SKIP
```

---

## 5. Worked Example

```js
duplicateCharacterCount("hello", "hola")
```

```
str1 = "hello"   (indices 0-4: h,e,l,l,o)
str2 = "hola"    (indices 0-3: h,o,l,a)

Scanning i=0, str1[0]="h":
  j=0: str2[0]="h" → "h"==="h" ✅, indexOf("h")=0 === i=0 ✅ → count=1
  j=1: str2[1]="o" → "o"==="h" ❌ → skip
  j=2: str2[2]="l" → "l"==="h" ❌ → skip
  j=3: str2[3]="a" → "a"==="h" ❌ → skip

Scanning i=1, str1[1]="e":
  j=0: "h"==="e" ❌  j=1: "o"==="e" ❌  j=2: "l"==="e" ❌  j=3: "a"==="e" ❌

Scanning i=2, str1[2]="l":
  j=0: "h"==="l" ❌
  j=1: "o"==="l" ❌
  j=2: "l"==="l" ✅, indexOf("l")=2 === i=2 ✅ → count=2
  j=3: "a"==="l" ❌

Scanning i=3, str1[3]="l":       ← duplicate "l"
  j=0: "h"==="l" ❌
  j=1: "o"==="l" ❌
  j=2: "l"==="l" ✅, indexOf("l")=2, but i=3 → 2 === 3 ❌ → SKIPPED ✅
  j=3: "a"==="l" ❌

Scanning i=4, str1[4]="o":
  j=0: "h"==="o" ❌
  j=1: "o"==="o" ✅, indexOf("o")=4 === i=4 ✅ → count=3
  j=2: "l"==="o" ❌
  j=3: "a"==="o" ❌

Final count: 3  →  shared characters are "h", "l", "o"
```

---

## 6. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `str.length` | Loop bounds | Returns the number of characters in a string |
| `str[i]` | Accessing characters | Returns the character at index `i` (strings work like arrays) |
| `===` | Strict equality | Checks that two values are identical with no type coercion |
| `str.indexOf(char)` | Duplicate prevention | Returns the index of the **first** occurrence of `char` in `str`, or `-1` if not found |
| `count++` | Incrementing | Adds 1 to the count variable (shorthand for `count = count + 1`) |
| Nested `for` loops | Pair comparison | Outer loop iterates `str1`, inner loop iterates `str2` — visits every character pair |

---

## 7. Full Annotated Code

```js
function duplicateCharacterCount(str1, str2) {
  let count = 0; // tracks number of unique shared characters

  // Visit every character in str1
  for (let i = 0; i < str1.length; i++) {

    // For each str1 character, scan all of str2
    for (let j = 0; j < str2.length; j++) {

      if (
        str2[j] === str1[i]           // Condition 1: characters match
        &&
        str1.indexOf(str2[j]) === i   // Condition 2: this is the FIRST occurrence
                                      //              of this character in str1
                                      //              (prevents counting duplicates)
      ) {
        count++;
      }
    }
  }

  return count;
}
```

### All test outputs

```js
duplicateCharacterCount("aloha", "hei")          // → 1   (shared: "h")
duplicateCharacterCount("jambo", "bonjour")       // → 3   (shared: "j", "b", "o")
duplicateCharacterCount("hello", "hola")          // → 3   (shared: "h", "l", "o")
duplicateCharacterCount("ola", "hej")             // → 0   (no shared characters)
duplicateCharacterCount("ciao", "konnichiwa")     // → 4   (shared: "c", "i", "a", "o")
duplicateCharacterCount("merhaba", "xin chao")    // → 2   (shared: "h", "a")
duplicateCharacterCount("hello world", "hello to everyone around the world") // → 26
```
