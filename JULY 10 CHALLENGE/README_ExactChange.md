# Exact Change — Code Explained

> Count the number of distinct ways to make a given amount in cents using pennies (1¢), nickels (5¢), dimes (10¢), and quarters (25¢).

---

## Table of Contents
1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [The Algorithm — Dynamic Programming](#2-the-algorithm--dynamic-programming)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [Tracing the Array for `amount=10`](#4-tracing-the-array-for-amount10)
5. [Why the Outer Loop Is Coins, Not Amounts](#5-why-the-outer-loop-is-coins-not-amounts)
6. [Worked Examples](#6-worked-examples)
7. [A Simpler Alternative — Recursion](#7-a-simpler-alternative--recursion)
8. [Methods Used](#8-methods-used)
9. [Full Annotated Code](#9-full-annotated-code)

---

## 1. The Problem in Plain English

Given an amount in cents, count how many **different combinations** of coins add up to exactly that amount.

```
exactChange(10) → 4

The 4 ways to make 10¢:
  10 × 1¢
   5 × 1¢  +  1 × 5¢
         2 × 5¢
              1 × 10¢
```

Order doesn't matter — `1¢ + 5¢` and `5¢ + 1¢` are the same combination.

---

## 2. The Algorithm — Dynamic Programming

The solution uses a technique called **Dynamic Programming (DP)**. Instead of trying every possible combination directly, it builds up the answer incrementally — solving small subproblems first and using those results to solve larger ones.

The key idea: the number of ways to make `10¢` using pennies and nickels equals the number of ways to make `10¢` using **only pennies**, plus the number of ways to make `5¢` using pennies and nickels (because adding one nickel to each of those gives another way to make 10¢).

This is tracked in a `ways` array where `ways[i]` means "how many ways can I make exactly `i` cents using the coins considered so far."

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Define the coins

```js
const coins = [1, 5, 10, 25];
```

The four coin denominations in ascending order. The order matters — see Section 5.

---

### Step 2 — Create and initialise the `ways` array

```js
const ways = new Array(amount + 1).fill(0);
ways[0] = 1;
```

`new Array(amount + 1).fill(0)` creates an array of zeros with one slot for every amount from `0` to `amount` inclusive. For `amount = 10`:

```
Index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Value: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0]
```

`ways[0] = 1` sets the base case: there is exactly **1 way** to make 0 cents — use no coins at all. This single seed value is what allows the rest of the array to be built correctly.

---

### Step 3 — Outer loop: iterate over each coin

```js
for (const coin of coins) {
```

Each pass of the outer loop considers one coin denomination. After the penny pass, `ways` reflects how many ways each amount can be made using only pennies. After the nickel pass, it reflects pennies and nickels. And so on.

---

### Step 4 — Inner loop: update every reachable amount

```js
for (let i = coin; i <= amount; i++) {
  ways[i] += ways[i - coin];
}
```

`i` starts at `coin` (not `0`) because you can't use a 5¢ coin to make 3¢ — there's nothing to update below the coin's value.

`ways[i] += ways[i - coin]` is the core formula. It says:

> "The number of ways to make `i` cents, now that we're considering this coin, equals the old number of ways to make `i` cents, **plus** the number of ways to make `i - coin` cents."

Why `i - coin`? Because if you can make `i - coin` cents some number of ways, you can make `i` cents by adding one of the current coin to each of those combinations.

---

### Step 5 — Return the answer

```js
return ways[amount];
```

After all coins have been processed, `ways[amount]` holds the total number of distinct combinations.

---

## 4. Tracing the Array for `amount=10`

Here is the full `ways` array after each coin pass:

```
Index:          0  1  2  3  4  5  6  7  8  9  10
                ─────────────────────────────────
Initial:        1  0  0  0  0  0  0  0  0  0   0
After coin=1:   1  1  1  1  1  1  1  1  1  1   1   ← 1 way each (all pennies)
After coin=5:   1  1  1  1  1  2  2  2  2  2   3   ← 5¢ and 10¢ gain new ways
After coin=10:  1  1  1  1  1  2  2  2  2  2   4   ← 10¢ gains one more way
After coin=25:  1  1  1  1  1  2  2  2  2  2   4   ← 25¢ > 10, no change
```

Focus on index `10` (the answer):

- After pennies: `1` (ten pennies)
- After nickels: `3` (ten pennies / five pennies + one nickel / two nickels)
- After dimes: `4` (the above three + one dime)
- After quarters: `4` (25 > 10, nothing added)

Focus on index `5` after the nickel pass:
```
ways[5] += ways[5 - 5]
ways[5] += ways[0]
ways[5] += 1   →  ways[5] = 2
```
Two ways to make 5¢: five pennies, or one nickel. ✅

---

## 5. Why the Outer Loop Is Coins, Not Amounts

This is the subtlest part of the algorithm. What if we swapped the loops — iterating amounts on the outside and coins on the inside?

```js
// WRONG order
for (let i = 1; i <= amount; i++) {
  for (const coin of coins) {
    if (i >= coin) ways[i] += ways[i - coin];
  }
}
```

This would count `1¢ + 5¢` and `5¢ + 1¢` as **two different combinations**, turning it into a permutation counter instead of a combination counter. For `amount=6` it would give `2` instead of the correct `2` — coincidentally right sometimes, but wrong in general.

By iterating coins on the outside, each coin is fully "committed" before moving to the next. This ensures combinations are counted only once, regardless of order.

---

## 6. Worked Examples

### `exactChange(3)` → `1`

```
Only one way to make 3¢: three pennies.
No coin ≥ 3¢ other than pennies exists (5¢ > 3¢).
ways[3] = 1
```

### `exactChange(10)` → `4`

```
10 × 1¢
 5 × 1¢  +  1 × 5¢
       2 × 5¢
            1 × 10¢
```

### `exactChange(99)` → `213`

213 distinct combinations of pennies, nickels, dimes, and quarters that sum to 99¢. The DP approach calculates this in a single pass — a brute-force triple nested loop would be far slower.

---

## 7. A Simpler Alternative — Recursion

The DP solution is efficient but hard to read at first glance. Here is a simpler recursive version that is easier to understand:

```js
function exactChange(amount, coins = [1, 5, 10, 25], index = 0) {
  // Base case: exact change made
  if (amount === 0) return 1;
  // Base case: overshot or ran out of coins
  if (amount < 0 || index >= coins.length) return 0;

  // Two choices at every step:
  // 1. Use the current coin again (stay at same index)
  // 2. Move on to the next coin (skip current)
  return exactChange(amount - coins[index], coins, index) +
         exactChange(amount, coins, index + 1);
}
```

### How it works

At every call, you face exactly two choices:

- **Use** the current coin — subtract it from `amount`, stay on the same coin (you can use it again)
- **Skip** the current coin — move to the next denomination

The recursion branches into both choices and sums their results. The three base cases stop the recursion:

| Condition | Meaning | Return |
|---|---|---|
| `amount === 0` | Found a valid combination | `1` |
| `amount < 0` | Overshot — invalid path | `0` |
| `index >= coins.length` | No coins left, still have amount | `0` |

### Trace for `amount=6`

```
exactChange(6, index=0, coin=1¢)
  ├── use 1¢: exactChange(5, index=0)
  │     ├── use 1¢: exactChange(4, index=0) ...
  │     └── skip: exactChange(5, index=1, coin=5¢)
  │           ├── use 5¢: exactChange(0) → 1 ✅  (1 nickel + 5 pennies... wait)
  │           └── skip: exactChange(5, index=2, coin=10¢) → 0 (10 > 5)
  └── skip: exactChange(6, index=1, coin=5¢)
        ├── use 5¢: exactChange(1, index=1) → 0 (can't make 1¢ with 5¢+)
        └── skip: exactChange(6, index=2) → 0

Result: 2 (six pennies / one nickel + one penny)
```

### Trade-off

| | DP version | Recursive version |
|---|---|---|
| Readability | Harder | Easier |
| Speed | Fast (O(n × coins)) | Slow for large amounts (exponential without memoisation) |
| Memory | O(n) array | O(n) call stack |

For small amounts the recursive version is perfectly fine and much easier to reason about. For large amounts, the DP version is far more efficient.

---

## 8. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `new Array(n).fill(0)` | Creating `ways` | Creates an array of length `n` with every slot set to `0` |
| `for...of` | Iterating coins | Loops over each element of an iterable (cleaner than index-based loop) |
| `ways[i] += ways[i - coin]` | Core DP formula | Adds the number of ways to make `i - coin` to the ways to make `i` |
| `ways[0] = 1` | Base case | Seeds the DP — 1 way to make 0 cents (use no coins) |

---

## 9. Full Annotated Code

```js
function exactChange(amount) {

  const coins = [1, 5, 10, 25]; // penny, nickel, dime, quarter

  // ways[i] = number of ways to make exactly i cents
  // initialised to 0; ways[0] = 1 is the base case (0 coins = 1 way)
  const ways = new Array(amount + 1).fill(0);
  ways[0] = 1;

  // For each coin denomination...
  for (const coin of coins) {
    // ...update every amount >= coin
    for (let i = coin; i <= amount; i++) {
      // Adding this coin to every way of making (i - coin) cents
      // gives us new ways to make i cents
      ways[i] += ways[i - coin];
    }
  }

  // After all coins processed, ways[amount] has the final answer
  return ways[amount];
}
```
## 10. Alternative Solution

```js
function exactChange(amount, coins = [1, 5, 10, 25], index = 0) {
  if (amount === 0) return 1;
  if (amount < 0 || index >= coins.length) return 0;
  return exactChange(amount - coins[index], coins, index) +
         exactChange(amount, coins, index + 1);
}
```