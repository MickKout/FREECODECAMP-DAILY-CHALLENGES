# Kaprekar's Routine — Code Explained

> Given a 4-digit number, count how many steps of Kaprekar's routine it takes to reach the "black hole" number 6174.

---

## Table of Contents
1. [The Problem](#1-the-problem)
2. [What Is Kaprekar's Routine](#2-what-is-kaprekers-routine)
3. [Why 6174 Is Special](#3-why-6174-is-special)
4. [Step-by-Step Code Breakdown](#4-step-by-step-code-breakdown)
5. [Worked Examples](#5-worked-examples)
6. [Methods Used](#6-methods-used)
7. [Full Annotated Code](#7-full-annotated-code)

---

## 1. The Problem

Given any 4-digit number, repeatedly apply Kaprekar's routine until you reach `6174`. Return the number of steps it took.

```js
kaprekar(1234) // → 3
kaprekar(8082) // → 2
```

---

## 2. What Is Kaprekar's Routine

Each step of the routine does the same three things:

1. Sort the digits in **descending** order → the **largest** possible number
2. Sort the digits in **ascending** order → the **smallest** possible number (pad with leading zeros if needed)
3. **Subtract** smallest from largest → the new number

Then repeat with the result until you hit `6174`.

```
1234 → largest: 4321, smallest: 1234, diff: 3087
3087 → largest: 8730, smallest: 0378, diff: 8352
8352 → largest: 8532, smallest: 2358, diff: 6174 ✅  (3 steps)
```

---

## 3. Why 6174 Is Special

`6174` is called **Kaprekar's constant**. It is the only 4-digit fixed point of the routine — applying the routine to `6174` itself produces `6174` again:

```
largest:  7641
smallest: 1467
diff:     7641 - 1467 = 6174  ← same number!
```

Every 4-digit number (with at least two distinct digits) is guaranteed to reach `6174` within 7 steps. This is why the function can use a `while` loop with `6174` as the stop condition without risk of an infinite loop.

---

## 4. Step-by-Step Code Breakdown

### Step 1 — Initialise the counter and run the first iteration

```js
let count = 0;
let largest  = n.toString().split("").sort().reverse().join("");
let smallest = n.toString().split("").sort().join("");
let difference = largest - smallest;
```

Before the loop begins, the first step of the routine is run on the original input `n`. This produces the first `difference`.

- `n.toString()` — converts the number to a string so it can be split into characters
- `.split("")` — breaks `"1234"` into `["1","2","3","4"]`
- `.sort()` — sorts the characters alphabetically, which for single digits is numerically ascending: `["1","2","3","4"]`
- `.reverse()` — flips to descending order: `["4","3","2","1"]`
- `.join("")` — rejoins into a string: `"4321"`
- `largest - smallest` — JavaScript coerces both strings to numbers and subtracts them: `4321 - 1234 = 3087`

At this point `count` is still `0` and `difference` is the result of the first step.

---

### Step 2 — Loop until 6174 is reached

```js
while (difference !== 6174) {
  largest    = difference.toString().split("").sort().reverse().join("");
  smallest   = difference.toString().split("").sort().join("");
  difference = largest - smallest;
  count++;
}
```

The `while` loop repeats the routine on the new `difference` — applying the same sort/reverse/join/subtract pattern. Each iteration increments `count` by 1.

The loop runs as long as `difference` is not `6174`. Once the result equals `6174`, the loop stops.

> **Important:** `count` tracks iterations of the *loop*, not total steps. The first step (before the loop) is not counted here — that's corrected in the return statement.

---

### Step 3 — Return the total step count

```js
return count + 1;
```

Because the first step of the routine was run **before** the loop started, `count` is always one short of the true total. Adding `1` corrects this:

```
kaprekar(1234):
  Before loop: diff = 3087          ← step 1 (not counted yet)
  Loop iter 1: diff = 8352, count=1 ← step 2
  Loop iter 2: diff = 6174, count=2 ← step 3, loop exits
  return 2 + 1 = 3 ✅
```

---

## 5. Worked Examples

### Example 1 — `kaprekar(1234)` → `3`

```
Step 1: 4321 - 1234 = 3087
Step 2: 8730 - 0378 = 8352
Step 3: 8532 - 2358 = 6174 ✅
```

Note step 2: `0378` has a leading zero because `3087` sorted ascending is `0378`. JavaScript treats `"0378"` as a string, but `largest - smallest` coerces it to `378`, giving the correct subtraction: `8730 - 378 = 8352`.

---

### Example 2 — `kaprekar(8082)` → `2`

```
Step 1: 8820 - 0288 = 8532
Step 2: 8532 - 2358 = 6174 ✅
```

`8082` starts close to `6174` — only 2 steps needed.

---

### Example 3 — `kaprekar(2025)` → `6`

```
Step 1: 5220 - 0225 = 4995
Step 2: 9954 - 4599 = 5355
Step 3: 5553 - 3555 = 1998
Step 4: 9981 - 1899 = 8082
Step 5: 8820 - 0288 = 8532
Step 6: 8532 - 2358 = 6174 ✅
```

Notice steps 5 and 6 are identical to `kaprekar(8082)` — once the routine converges to the same intermediate number, it always follows the same path to `6174`.

---

## 6. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `.toString()` | Every step | Converts a number to a string so it can be split into characters |
| `.split("")` | Every step | Breaks a string into an array of individual characters |
| `.sort()` | Ascending sort | Sorts array elements as strings — works correctly for single digits |
| `.reverse()` | Descending sort | Reverses an array in place after sorting ascending |
| `.join("")` | Every step | Joins an array of characters back into a single string |
| `string - string` | Subtraction | JavaScript coerces both strings to numbers before subtracting |
| `while` loop | Main routine | Repeats until the stop condition (`=== 6174`) is met |
| `!==` | Loop condition | Strict inequality — loop continues as long as result is not 6174 |
| `count + 1` | Return value | Compensates for the first step being run before the loop |

---

## 7. Full Annotated Code

```js
function kaprekar(n) {

  let count = 0;

  // Run the first step of the routine on the original number
  let largest    = n.toString().split("").sort().reverse().join(""); // descending
  let smallest   = n.toString().split("").sort().join("");           // ascending
  let difference = largest - smallest;                               // step 1 result

  // Keep applying the routine until we reach Kaprekar's constant
  while (difference !== 6174) {
    largest    = difference.toString().split("").sort().reverse().join("");
    smallest   = difference.toString().split("").sort().join("");
    difference = largest - smallest;
    count++;  // count loop iterations (steps 2 onwards)
  }

  // +1 because step 1 was run before the loop and not counted
  return count + 1;
}
```
