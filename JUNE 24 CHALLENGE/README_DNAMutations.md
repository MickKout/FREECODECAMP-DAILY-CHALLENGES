# DNA Mutation Detector — Code Explained

> Compare two DNA strands of equal length and return the indices where they differ. Returns an empty array if the strands have different lengths or no mutations are found.

---

## Table of Contents
1. [The Problem](#1-the-problem)
2. [What Is a DNA Mutation](#2-what-is-a-dna-mutation)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [The Original Bug](#4-the-original-bug)
5. [Methods Used](#5-methods-used)
6. [Full Annotated Code](#6-full-annotated-code)

---

## 1. The Problem

Given two DNA strand strings of the same length, return an array of **indices** where the characters differ:

```js
detectMutations("ATCG", "ATGG")
// index:          0123    0123
// mismatch at index 2: C vs G
// → [2]

detectMutations("ATGCGTACGTTAGC", "ATGCATACGATTGC")
// mismatches at indices 4, 9, 11
// → [4, 9, 11]
```

If the two strands have different lengths — meaning they can't be meaningfully compared position by position — return `[]`.

---

## 2. What Is a DNA Mutation

DNA is made of four bases: **A** (adenine), **T** (thymine), **G** (guanine), **C** (cytosine). A mutation is a position where one strand has a different base than the other at the same index. These point mutations are a simplified model of real SNPs (Single Nucleotide Polymorphisms) used in genetics research.

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Guard against different-length strands

```js
if (strand1.length !== strand2.length) {
  return [];
}
```

If the strands are different lengths, a position-by-position comparison is meaningless — the strands may simply be shifted or truncated. Return early with `[]` before the loop even starts.

This check must come **before** the loop. In the original buggy version, the check was buried inside the loop's mutation branch, which caused it to wipe the results at the wrong moment.

---

### Step 2 — Initialise the result array

```js
const mutations = [];
```

An empty array that will collect the indices of every mismatch found. If no mutations exist, it stays empty and `[]` is returned.

---

### Step 3 — Loop through every position

```js
for (let i = 0; i < strand1.length; i++) {
  ...
}
```

Iterates from index `0` to the last character of the strand. Since both strands are guaranteed the same length at this point (we checked above), `strand1.length` safely bounds the loop for both.

---

### Step 4 — Compare characters at each position

```js
if (strand1[i] !== strand2[i]) {
  mutations.push(i);
}
```

`strand1[i]` and `strand2[i]` access the character at position `i` in each string — JavaScript strings support bracket notation just like arrays.

`!==` is the strict inequality operator — it checks both value and type with no type coercion. If the characters differ, the current index `i` is pushed into `mutations`.

---

### Step 5 — Return the result

```js
return mutations;
```

After all positions have been compared, return the collected array of mismatch indices. If no mismatches were found, this is `[]`. If all positions differ, it contains every index from `0` to `length - 1`.

---

## 4. The Original Bug

The original code had the length check in completely the wrong place:

```js
// BUGGY version
for (let i = 0; i < strand1.length; i++) {
  if (strand1[i] !== strand2[i]) {
    mutations.push(i);
    if (i === strand1.length - 1) {  // ← inside the mutation check!
      return [];                      // ← wipes all collected results
    }
  }
}
```

This caused two problems:

**Problem 1 — Wrong condition:** It checked `i === strand1.length - 1` (whether we're at the last index) inside the mutation branch. This triggered only when the **last character was also a mutation**, not when strands were different lengths.

**Problem 2 — Wipes valid results:** When it did trigger, it returned `[]` after already collecting valid mutation indices — throwing away all the work done so far.

**Test 5 failure explained:**
```
strand1: "ACGTCAGTACGCACATGACCATTGACATA"  (29 chars)
strand2: "AACGTCAGTACGCACATGACCATTGACAT"  (29 chars)
```
The last characters are `"A"` vs `"T"` — a mutation at the final index. The buggy code hit `i === strand1.length - 1` inside the mutation branch and returned `[]` instead of the 26-element array.

**The fix** — move the length check before the loop entirely:

```js
// FIXED version
if (strand1.length !== strand2.length) {
  return [];
}
// Now loop cleanly with no extra conditions inside
for (let i = 0; i < strand1.length; i++) {
  if (strand1[i] !== strand2[i]) {
    mutations.push(i);  // just collect, nothing else
  }
}
return mutations;
```

---

## 5. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `.length` | Length guard and loop bound | Returns the number of characters in a string |
| `!==` | Character comparison | Strict inequality — no type coercion, checks value and type |
| `string[i]` | Character access | Accesses the character at index `i` (strings behave like arrays) |
| `.push(value)` | Collecting results | Appends a value to the end of an array |
| `return []` | Early exit | Exits the function immediately, returning an empty array |
| `for` loop | Iteration | Iterates with a counter variable from `0` to `length - 1` |

---

## 6. Full Annotated Code

```js
function detectMutations(strand1, strand2) {

  // Strands must be same length to compare position by position
  if (strand1.length !== strand2.length) {
    return [];
  }

  const mutations = []; // will hold indices of mismatches

  for (let i = 0; i < strand1.length; i++) {
    if (strand1[i] !== strand2[i]) {
      mutations.push(i); // record the index where strands differ
    }
  }

  return mutations; // [] if identical, [indices...] if mutations found
}
```

### Example Trace

```
detectMutations("ATGCGTACGTTAGC", "ATGCATACGATTGC")

i=0:  A vs A  → match
i=1:  T vs T  → match
i=2:  G vs G  → match
i=3:  C vs C  → match
i=4:  G vs A  → MISMATCH → push(4)
i=5:  T vs T  → match
i=6:  A vs A  → match
i=7:  C vs C  → match
i=8:  G vs G  → match
i=9:  T vs A  → MISMATCH → push(9)
i=10: T vs T  → match
i=11: A vs G  → MISMATCH → push(11)
i=12: G vs C  → match  ← wait, G vs C?
      actually: G vs G → match
i=13: C vs C  → match

result: [4, 9, 11] ✅
```
