# Max Stock Profit — Code Explained

> Given an array of daily stock prices and a budget, calculate the maximum profit from a single buy/sell transaction using only whole shares.

---

## Table of Contents
1. [The Problem](#1-the-problem)
2. [The Formula](#2-the-formula)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [Why Per-Pair Share Calculation Matters](#4-why-per-pair-share-calculation-matters)
5. [Why Floor to Cents Correctly](#5-why-floor-to-cents-correctly)
6. [Methods Used](#6-methods-used)
7. [Full Annotated Code](#7-full-annotated-code)

---

## 1. The Problem

Given a list of daily prices and a budget:
- Buy on day `i`, sell on a later day `j` (`j > i`)
- You can only buy **whole shares**
- At most **one** buy and one sell
- Return the **maximum possible profit**, floored to the nearest cent, as a two-decimal string

```js
getMaxProfit([8, 2, 5, 10], 20)  // → "80.00"
// Buy 10 shares at $2, sell at $10 → profit = 10 × $8 = $80.00
```

---

## 2. The Formula

For every valid buy day `i` and sell day `j`:

```
shares = floor(budget / prices[i])
profit = shares × (prices[j] - prices[i])
```

Track the highest `profit` across all pairs. At the end, floor it to the nearest cent.

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Edge case: fewer than 2 prices

```js
if (prices.length < 2) return "0.00";
```

You need at least a buy day and a sell day. If the array has only one price (or is empty), no transaction is possible.

---

### Step 2 — Try every valid buy/sell pair

```js
for (let i = 0; i < prices.length; i++) {
  for (let j = i + 1; j < prices.length; j++) {
```

The outer loop is the **buy day**, the inner loop is the **sell day**. `j` always starts at `i + 1` so the sell is always after the buy — you can never sell before you buy.

---

### Step 3 — Skip unprofitable pairs

```js
if (prices[j] > prices[i]) {
```

If the sell price isn't higher than the buy price, there's no profit. Skip it and move on.

---

### Step 4 — Calculate shares and profit for this pair

```js
const shares = Math.floor(budget / prices[i]);
const profit = shares * (prices[j] - prices[i]);
```

`Math.floor(budget / prices[i])` — divides the budget by today's buy price and rounds **down**, since you can only buy whole shares.

`shares × (prices[j] - prices[i])` — multiplies the number of shares by the gain per share. This is the real profit for this specific pair.

---

### Step 5 — Track the maximum profit

```js
if (profit > maxProfit) {
  maxProfit = profit;
}
```

If this pair's profit beats the current best, update `maxProfit`. After all pairs are checked, `maxProfit` holds the best possible outcome.

---

### Step 6 — Return the result floored to the nearest cent

```js
return (Math.floor(maxProfit * 100) / 100).toFixed(2);
```

- `× 100` — shifts two decimal places left (e.g. `8.319` → `831.9`)
- `Math.floor(...)` — drops everything below a whole cent (`831.9` → `831`)
- `/ 100` — shifts back (`831` → `8.31`)
- `.toFixed(2)` — formats as a string with exactly two decimal places (`"8.31"`)

This three-step approach is the standard way to floor to a specific decimal place in JavaScript.

---

## 4. Why Per-Pair Share Calculation Matters

The key insight is that the **best price difference** is not always the **best profit**. The number of shares you can buy changes depending on the buy price, so each pair must be evaluated independently.

Consider `[4, 5, 3, 6]` with a budget of `$20`:

| Buy | Sell | Diff | Shares | Profit |
|-----|------|------|--------|--------|
| $4  | $5   | $1   | 5      | $5.00  |
| $4  | $6   | $2   | 5      | $10.00 |
| $3  | $6   | $3   | 6      | $18.00 ✅ |
| $5  | $6   | $1   | 4      | $4.00  |

The largest price difference (`$4 → $6 = $2`) is not the winner. Buying at `$3` allows 6 shares, and `6 × $3 = $18` is the best profit. Your original code found the best difference first and then calculated shares — which would have wrongly picked the `$4/$6` pair.

---

## 5. Why Floor to Cents Correctly

`Math.floor(profit)` floors to the nearest **whole dollar** — wrong for prices like `$8.31`.

`.toFixed(2)` alone **rounds**, not floors — `8.319` becomes `"8.32"` instead of `"8.31"`.

The correct pattern:

```js
Math.floor(maxProfit * 100) / 100).toFixed(2)
// 8.319 → 831.9 → 831 → 8.31 → "8.31" ✅
```

---

## 6. Methods Used

| Method | Where Used | What It Does |
|---|---|---|
| `Math.floor(n)` | Shares + cent flooring | Rounds a number **down** to the nearest integer |
| `Math.floor(n * 100) / 100` | Cent flooring | Floors to exactly 2 decimal places |
| `.toFixed(2)` | Return value | Formats a number as a string with exactly 2 decimal places |
| Nested `for` loops | Pair scanning | Tries every valid buy/sell combination where `j > i` |

---

## 7. Full Annotated Code

```js
function getMaxProfit(prices, budget) {

  // Need at least a buy day and a sell day
  if (prices.length < 2) return "0.00";

  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {       // buy day
    for (let j = i + 1; j < prices.length; j++) { // sell day (always after buy)

      if (prices[j] > prices[i]) {                // only consider profitable pairs
        const shares = Math.floor(budget / prices[i]);       // whole shares affordable
        const profit = shares * (prices[j] - prices[i]);     // profit for this pair
        if (profit > maxProfit) maxProfit = profit;          // keep the best
      }
    }
  }

  // Floor to nearest cent and return as a 2-decimal string
  return (Math.floor(maxProfit * 100) / 100).toFixed(2);
}
```
