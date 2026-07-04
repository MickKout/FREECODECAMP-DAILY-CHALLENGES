# Blood Triage — Code Explained

> Match blood bank donors to patients following real compatibility rules, maximising the number of patients served.

---

## Table of Contents
1. [The Problem](#1-the-problem)
2. [Compatibility Rules](#2-compatibility-rules)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [Methods Used](#4-methods-used)
5. [Why Donor Order Matters](#5-why-donor-order-matters)
6. [Full Annotated Code](#6-full-annotated-code)

---

## 1. The Problem

Given two arrays:
- `bank` — available blood units (donor types)
- `patients` — patients who each need one unit

Return a string saying how many patients were successfully served, e.g. `"13 of 14 patients served"`.

Each blood unit can only be used once, and each patient can only receive one unit.

---

## 2. Compatibility Rules

Blood type compatibility is not symmetric. A donor can only give to certain recipients:

| Donor | Can Give To |
|---|---|
| `O`  | `O`, `A`, `B`, `AB` (universal donor) |
| `A`  | `A`, `AB` |
| `B`  | `B`, `AB` |
| `AB` | `AB` only |

This is encoded as a lookup object so the logic stays clean and readable:

```js
const compatible = {
  "O":  ["O", "A", "B", "AB"],
  "A":  ["A", "AB"],
  "B":  ["B", "AB"],
  "AB": ["AB"]
};
```

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Build the compatibility map

```js
const compatible = {
  "O":  ["O", "A", "B", "AB"],
  "A":  ["A", "AB"],
  "B":  ["B", "AB"],
  "AB": ["AB"]
};
```

A plain object used as a lookup table. Given any donor type, it tells you the full list of patient types that can safely receive that blood. This replaces a messy chain of `if/else` conditions with a single `.includes()` check later.

---

### Step 2 — Sort the bank: specific donors first, `O` last

```js
const order = { "AB": 0, "A": 1, "B": 2, "O": 3 };
const sortedBank = [...bank].sort((a, b) => order[a] - order[b]);
```

`O` is the universal donor — it can give to anyone. If we used `O` units first, they would be "wasted" on patients who could have been served by a more specific donor, leaving patients at the end with no match. By processing `AB → A → B → O` in that order, we always try the most restrictive donors first and keep `O` as a last resort.

`[...bank]` creates a shallow copy so the original array is not mutated by `.sort()`.

---

### Step 3 — Copy the patients array

```js
const remainingPatients = [...patients];
```

We need to remove patients as they get served (to prevent the same patient being matched twice). Using a copy means the original `patients` array stays intact so we can use `patients.length` for the final count at the end.

---

### Step 4 — Loop through each donor unit

```js
for (let i = 0; i < sortedBank.length; i++) {
  const donor = sortedBank[i];
  const canDonateTo = compatible[donor];
  ...
}
```

For each blood unit in the (sorted) bank, look up which patient types it can serve using the compatibility map. `canDonateTo` is an array like `["A", "AB"]` for a donor of type `"A"`.

---

### Step 5 — Find the first matching patient

```js
for (let j = 0; j < remainingPatients.length; j++) {
  if (canDonateTo.includes(remainingPatients[j])) {
    count++;
    remainingPatients.splice(j, 1);
    break;
  }
}
```

The inner loop scans `remainingPatients` for the first patient this donor can serve. When found:
- `count++` increments the served counter
- `.splice(j, 1)` removes that patient from the list so they can't be matched again
- `break` stops the inner loop immediately — one donor unit serves exactly one patient

If no compatible patient is found, the donor unit goes unused and the outer loop moves to the next one.

---

### Step 6 — Return the result

```js
return `${count} of ${patients.length} patients served`;
```

`patients.length` is the **total number of patients** (not bank units), which is what the message is about. The template literal builds the required string format.

---

## 4. Methods Used

| Method | Where Used | What It Does |
|---|---|---|
| `[...array]` | Copying `bank` and `patients` | Spread operator — creates a shallow copy so the original is not mutated |
| `.sort((a, b) => ...)` | Sorting the bank | Sorts with a custom comparator; negative result means `a` comes first |
| `.includes(value)` | Checking compatibility | Returns `true` if the array contains the value |
| `.splice(j, 1)` | Removing a served patient | Removes 1 element at index `j` in place, shortening the array |
| Template literal `` `${...}` `` | Return string | Embeds expressions directly into a string |

---

## 5. Why Donor Order Matters

Consider this scenario:

```
Bank:     ["O", "A"]
Patients: ["A", "O"]
```

**Wrong order (O first):**
- `O` matches first patient `"A"` ✅ (O can give to A)
- `A` cannot match `"O"` ❌ (A cannot give to O)
- Result: 1 of 2 served ❌

**Correct order (specific first, O last):**
- `A` matches first patient `"A"` ✅
- `O` matches remaining patient `"O"` ✅
- Result: 2 of 2 served ✅

Greedy allocation of the most restricted donors first always produces the optimal outcome.

---

## 6. Full Annotated Code

```js
function triageBlood(bank, patients) {

  // Lookup: donor type → compatible patient types
  const compatible = {
    "O":  ["O", "A", "B", "AB"],
    "A":  ["A", "AB"],
    "B":  ["B", "AB"],
    "AB": ["AB"]
  };

  // Sort bank so specific donors are used before universal O
  const order = { "AB": 0, "A": 1, "B": 2, "O": 3 };
  const sortedBank = [...bank].sort((a, b) => order[a] - order[b]);

  // Work on a copy so we can splice without affecting the original
  const remainingPatients = [...patients];

  let count = 0;

  for (let i = 0; i < sortedBank.length; i++) {
    const donor = sortedBank[i];
    const canDonateTo = compatible[donor]; // e.g. ["A", "AB"] for donor "A"

    for (let j = 0; j < remainingPatients.length; j++) {
      if (canDonateTo.includes(remainingPatients[j])) {
        count++;                        // one more patient served
        remainingPatients.splice(j, 1); // remove matched patient
        break;                          // move to next donor unit
      }
    }
  }

  // Total patients (not bank size) goes in the message
  return `${count} of ${patients.length} patients served`;
}
```
