# Periodic Table Spelling — Code Explained

> Given a word, spell it using chemical element symbols from the periodic table. Uses recursive backtracking to find a valid combination.

---

## Table of Contents
1. [The Problem](#1-the-problem)
2. [Why This Is Harder Than It Looks](#2-why-this-is-harder-than-it-looks)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [How Backtracking Works](#4-how-backtracking-works)
5. [Methods Used](#5-methods-used)
6. [Full Annotated Code](#6-full-annotated-code)

---

## 1. The Problem

Given a word like `"rational"`, return an array of element symbols whose combined letters spell it:

```
"rational" → ["Ra", "Ti", "O", "N", "Al"]
```

If no valid combination exists (e.g. `"value"` — `"l"` has no matching element), return `[]`.

---

## 2. Why This Is Harder Than It Looks

Elements can be one **or** two letters long. At every position in the word you face a fork:

```
"neon"
├── "N" (1 letter) + "eon"  → eventually fails
└── "Ne" (2 letters) + "on" → "O" + "N" ✅
```

A simple greedy approach ("always try 2 letters first") fails for words like `"rational"`:

```
r-a → "Ra" ✅
t-i → "Ti" ✅
o-n → tries "On" (not an element), falls back to "O" ✅
n-a → tries "Na" ✅ ... but then "l" has no match ❌
```

The greedy path chose `"Na"` but should have chosen `"N"` + `"Al"`. **Backtracking** solves this by reversing a bad choice and trying the alternative.

---

## 3. Step-by-Step Code Breakdown

### Step 1 — The elements list

```js
const elements = ["H","He","Li","Be","B","C","N","O", ... ,"Og"];
```

A flat array of all 118 element symbols in periodic table order. Used as the lookup source for every match attempt.

---

### Step 2 — The outer function and entry point

```js
function getPeriodicSpelling(word) {
  ...
  return solve(word.toLowerCase(), []) ?? [];
}
```

The outer function sets up the elements list and calls `solve()` with:
- `word.toLowerCase()` — normalised to lowercase so comparisons are case-insensitive
- `[]` — an empty accumulator that builds up the result

The `?? []` (nullish coalescing) converts a `null` result (no solution found) to an empty array `[]`.

---

### Step 3 — Base case: word fully consumed

```js
function solve(remaining, current) {
  if (remaining === '') return current;
  ...
}
```

When `remaining` becomes an empty string, every character has been matched. The `current` array holds the full solution — return it immediately.

---

### Step 4 — Extract candidates

```js
const two = remaining.slice(0, 2);
const one = remaining.slice(0, 1);
```

At each recursive call, look at the next 1 and 2 characters of the remaining string. These are the two candidates to try matching against the elements list.

---

### Step 5 — Try the two-letter match first

```js
const twoMatch = elements.find(el => el.toLowerCase() === two.toLowerCase());
if (twoMatch) {
  const result = solve(remaining.slice(2), [...current, twoMatch]);
  if (result !== null) return result;
}
```

`.find()` returns the first element whose lowercase name matches the two-character candidate, or `undefined` if none exists.

If a two-letter element is found, recurse with:
- `remaining.slice(2)` — the word minus the two matched characters
- `[...current, twoMatch]` — the current result with the new element appended

If the recursive call returns `null` (that path hit a dead end), **don't return** — fall through and try the one-letter match instead. This is the backtracking step.

---

### Step 6 — Fall back to one-letter match

```js
const oneMatch = elements.find(el => el.toLowerCase() === one.toLowerCase());
if (oneMatch) {
  const result = solve(remaining.slice(1), [...current, oneMatch]);
  if (result !== null) return result;
}
```

Same logic but consuming only one character. If this path also leads to a dead end further down the word, return `null` to signal failure to the caller.

---

### Step 7 — Dead end: backtrack

```js
return null;
```

Neither a one-letter nor a two-letter match led to a complete solution from this position. Return `null` to tell the parent call to try its alternative path.

---

## 4. How Backtracking Works

Think of it as a decision tree. Each node is a position in the word, each branch is a choice (1-letter or 2-letter element). The algorithm explores branches depth-first and backtracks when a branch hits a dead end:

```
"rational"
└── "Ra" (2) → "tional"
    └── "Ti" (2) → "onal"
        └── "On" ✗ → try "O" (1) → "nal"
            └── "Na" (2) → "l"
                └── "L" ✗ → "l" ✗ → NULL ← dead end!
            backtrack → try "N" (1) → "al"
                └── "Al" (2) → "" ← base case! ✅
result: ["Ra","Ti","O","N","Al"]
```

---

## 5. Methods Used

| Method | Where Used | What It Does |
|---|---|---|
| `.toLowerCase()` | Comparison normalisation | Converts string to all lowercase for case-insensitive matching |
| `.slice(start, end)` | Extracting candidates and advancing | Returns a portion of the string without modifying the original |
| `.find(callback)` | Element lookup | Returns the first array element satisfying the condition, or `undefined` |
| `[...array, item]` | Building result | Spread creates a new array with the item appended — avoids mutating the accumulator |
| `?? []` | Nullish coalescing | Returns the right-hand value only if the left is `null` or `undefined` |
| Recursion | Core algorithm | `solve()` calls itself with a smaller `remaining` string each time |

---

## 6. Full Annotated Code

```js
function getPeriodicSpelling(word) {
  const elements = ["H","He","Li", ... ,"Og"]; // all 118 symbols

  function solve(remaining, current) {
    // Base case: entire word matched successfully
    if (remaining === '') return current;

    const two = remaining.slice(0, 2); // next 2 chars
    const one = remaining.slice(0, 1); // next 1 char

    // Try 2-letter element first
    const twoMatch = elements.find(el => el.toLowerCase() === two.toLowerCase());
    if (twoMatch) {
      const result = solve(remaining.slice(2), [...current, twoMatch]);
      if (result !== null) return result; // path succeeded — bubble up
      // else: fall through and try 1-letter (backtrack)
    }

    // Try 1-letter element
    const oneMatch = elements.find(el => el.toLowerCase() === one.toLowerCase());
    if (oneMatch) {
      const result = solve(remaining.slice(1), [...current, oneMatch]);
      if (result !== null) return result;
    }

    // Both options exhausted — signal dead end to parent
    return null;
  }

  // Convert null (no solution) to [] for clean output
  return solve(word.toLowerCase(), []) ?? [];
}
```
