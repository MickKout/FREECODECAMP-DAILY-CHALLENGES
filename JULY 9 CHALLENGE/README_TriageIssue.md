# Issue Triage — Code Explained

> Automatically assign or update labels on a GitHub-style issue based on keywords in its title and what labels it already has.

---

## Table of Contents
1. [The Problem in Plain English](#1-the-problem-in-plain-english)
2. [The Decision Tree](#2-the-decision-tree)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [Why `splice` + `push` Instead of Just Replacing](#4-why-splice--push-instead-of-just-replacing)
5. [Why the Security Check Is Separate](#5-why-the-security-check-is-separate)
6. [Worked Examples](#6-worked-examples)
7. [Methods Used](#7-methods-used)
8. [Full Annotated Code](#8-full-annotated-code)

---

## 1. The Problem in Plain English

Imagine a GitHub issue tracker. When someone opens an issue, it gets labelled automatically based on its title. As the issue progresses, its labels get updated.

The function takes:
- `title` — the issue title string
- `labels` — the array of labels the issue currently has

And returns an updated labels array following a set of rules.

```js
triageIssue("bug in login form", [])
// → ["bug", "needs triage"]

triageIssue("simple error fix", ["needs triage"])
// → ["good first issue"]
```

---

## 2. The Decision Tree

The logic has three separate layers that run in order:

```
START
  │
  ├── Are labels EMPTY?
  │     ├── title has "error" or "bug"    → add "bug" + "needs triage"
  │     ├── title has "feature" or "add"  → add "enhancement" + "discussing"
  │     └── neither                       → do nothing
  │
  └── Labels NOT empty?
        ├── Has "needs triage"?
        │     ├── title has "simple" or "easy"  → swap → "good first issue"
        │     └── otherwise                     → swap → "help wanted"
        │
        └── Has "discussing"?
              ├── title has "planned" or "next"  → swap → "on the roadmap"
              └── otherwise                      → swap → "help wanted"

ALWAYS (regardless of the above):
  └── title has "security" → add "critical"
```

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Copy the labels array

```js
const updatedLabels = [...labels];
```

The spread operator `[...labels]` creates a **shallow copy** of the incoming array. All changes are made to `updatedLabels`, never to the original `labels`. This is good practice — it prevents the function from mutating data that was passed in from outside.

---

### Step 2 — Branch: no labels yet

```js
if (updatedLabels.length === 0) {
```

The first major branch handles issues that have **no labels at all** — a freshly opened issue. `length === 0` checks if the array is empty.

---

### Step 3 — New issue: bug or error

```js
if (title.includes("error") || title.includes("bug")) {
  updatedLabels.push("bug", "needs triage");
}
```

`.includes()` checks if the substring exists anywhere in the title string. If the title mentions `"error"` or `"bug"`, two labels are added at once with a single `.push()` call. `"needs triage"` signals the issue needs a human to review it.

---

### Step 4 — New issue: feature or enhancement

```js
else if (title.includes("feature") || title.includes("add")) {
  updatedLabels.push("enhancement", "discussing");
}
```

`else if` means this only runs if the bug check above was false. So a title like `"add bug fix"` would match the bug rule first — the enhancement rule would never run for it.

`"discussing"` signals the feature is being talked about but not yet committed to.

---

### Step 5 — Branch: labels already exist

```js
} else {
```

If the issue already has labels, the `else` block runs instead. Inside it, two independent checks run back to back — one for `"needs triage"` and one for `"discussing"`. Both can run in the same call if the issue has both labels.

---

### Step 6 — Upgrade "needs triage"

```js
if (updatedLabels.includes("needs triage")) {
  if (title.includes("simple") || title.includes("easy")) {
    updatedLabels.splice(updatedLabels.indexOf("needs triage"), 1);
    updatedLabels.push("good first issue");
  } else {
    updatedLabels.splice(updatedLabels.indexOf("needs triage"), 1);
    updatedLabels.push("help wanted");
  }
}
```

If `"needs triage"` is in the labels, it gets **replaced** — removed and swapped for something more specific:

- Title mentions `"simple"` or `"easy"` → replace with `"good first issue"` (suitable for new contributors)
- Anything else → replace with `"help wanted"` (needs someone to pick it up)

The replacement is a two-step operation — see Section 4 for why.

---

### Step 7 — Upgrade "discussing"

```js
if (updatedLabels.includes("discussing")) {
  if (title.includes("planned") || title.includes("next")) {
    updatedLabels.splice(updatedLabels.indexOf("discussing"), 1);
    updatedLabels.push("on the roadmap");
  } else {
    updatedLabels.splice(updatedLabels.indexOf("discussing"), 1);
    updatedLabels.push("help wanted");
  }
}
```

Same pattern as Step 6, applied to `"discussing"`:

- Title mentions `"planned"` or `"next"` → replace with `"on the roadmap"` (committed feature)
- Anything else → replace with `"help wanted"`

This check is **independent** from the `"needs triage"` check — both can fire in the same function call if both labels are present.

---

### Step 8 — Security check (always runs)

```js
if (title.includes("security")) {
  updatedLabels.push("critical");
}
```

This `if` is **outside** both the empty and non-empty branches. It runs regardless of what happened above — a security issue should always be marked critical, whether it's brand new or already labelled.

---

### Step 9 — Return the result

```js
return updatedLabels;
```

Return the updated copy of the labels array.

---

## 4. Why `splice` + `push` Instead of Just Replacing

You can't do `updatedLabels["needs triage"] = "good first issue"` — arrays use numeric indices, not string keys.

The swap is done in two steps:

```js
// Step 1: find the index of "needs triage" and remove it
updatedLabels.splice(updatedLabels.indexOf("needs triage"), 1);

// Step 2: add the new label at the end
updatedLabels.push("good first issue");
```

**`indexOf("needs triage")`** scans the array and returns the numeric index of the first match — e.g. `0` if it's the first element.

**`splice(index, 1)`** removes exactly `1` element at that index, shifting everything after it left.

**`push("good first issue")`** appends the new label at the end.

For example:

```
labels = ["needs triage", "bug"]

indexOf("needs triage") → 0
splice(0, 1) → removes "needs triage" → ["bug"]
push("good first issue") → ["bug", "good first issue"]
```

---

## 5. Why the Security Check Is Separate

The security `if` sits outside the main `if/else` block deliberately:

```js
if (updatedLabels.length === 0) { ... }   // block A
else { ... }                               // block B

if (title.includes("security")) { ... }   // always runs ← outside both blocks
```

This means `"critical"` can be added **on top of** whatever the main logic did. An issue can be both a new bug and security-critical at the same time:

```js
triageIssue("security vulnerability in auth", [])
// Main block adds nothing (no "error"/"bug"/"feature"/"add" in title)
// Security check adds "critical"
// → ["critical"]

triageIssue("security patch easy fix", ["needs triage"])
// Main block: "easy" → swap "needs triage" for "good first issue"
// Security check: adds "critical"
// → ["good first issue", "critical"]
```

If the security check were inside either branch, it would only run for new issues or only for labelled issues — not both.

---

## 6. Worked Examples

### No labels — bug title

```
title:  "bug in login form"
labels: []

→ length === 0 ✅
→ title includes "bug" ✅
→ push "bug", "needs triage"
→ no "security" in title
Result: ["bug", "needs triage"]
```

---

### No labels — feature title

```
title:  "add dark mode feature"
labels: []

→ length === 0 ✅
→ title includes "bug"? No. includes "error"? No.
→ title includes "add"? Yes ✅
→ push "enhancement", "discussing"
Result: ["enhancement", "discussing"]
```

---

### Has "needs triage" — simple fix

```
title:  "simple error fix"
labels: ["needs triage"]

→ length !== 0, go to else block
→ includes "needs triage"? Yes ✅
→ title includes "simple"? Yes ✅
→ splice out "needs triage", push "good first issue"
→ includes "discussing"? No
→ no "security" in title
Result: ["good first issue"]
```

---

### Has "needs triage" — no special keyword

```
title:  "fix button color"
labels: ["needs triage"]

→ length !== 0, go to else block
→ includes "needs triage"? Yes ✅
→ title includes "simple" or "easy"? No
→ splice out "needs triage", push "help wanted"
Result: ["help wanted"]
```

---

### Has "discussing" — planned feature

```
title:  "planned feature discussion"
labels: ["discussing"]

→ length !== 0, go to else block
→ includes "needs triage"? No
→ includes "discussing"? Yes ✅
→ title includes "planned"? Yes ✅
→ splice out "discussing", push "on the roadmap"
Result: ["on the roadmap"]
```

---

### Security always adds "critical"

```
title:  "security patch easy fix"
labels: ["needs triage"]

→ length !== 0, go to else block
→ includes "needs triage"? Yes ✅
→ title includes "easy"? Yes ✅
→ splice out "needs triage", push "good first issue"
→ title includes "security"? Yes ✅ → push "critical"
Result: ["good first issue", "critical"]
```

---

## 7. Methods Used

| Method / Syntax | Where Used | What It Does |
|---|---|---|
| `[...labels]` | Copying the array | Spread — creates a shallow copy so the original is never mutated |
| `.length === 0` | Empty check | Returns `true` if the array has no elements |
| `str.includes(substr)` | Keyword checks | Returns `true` if `substr` appears anywhere in `str` |
| `.push(a, b)` | Adding labels | Appends one or more items to the end of the array |
| `.indexOf(value)` | Finding label position | Returns the numeric index of the first match, or `-1` if not found |
| `.splice(index, 1)` | Removing a label | Removes exactly 1 element at the given index, in place |
| `if / else if / else` | Branching logic | Runs only the first matching branch — later ones are skipped |

---

## 8. Full Annotated Code

```js
function triageIssue(title, labels) {

  // Work on a copy — never mutate the original array
  const updatedLabels = [...labels];

  if (updatedLabels.length === 0) {
    // ── NEW ISSUE: no labels yet ──────────────────────────────────
    if (title.includes("error") || title.includes("bug")) {
      updatedLabels.push("bug", "needs triage");       // bug report
    } else if (title.includes("feature") || title.includes("add")) {
      updatedLabels.push("enhancement", "discussing"); // feature request
    }
    // else: unrecognised title → no labels added

  } else {
    // ── EXISTING ISSUE: upgrade labels based on progress ─────────

    // Handle "needs triage"
    if (updatedLabels.includes("needs triage")) {
      updatedLabels.splice(updatedLabels.indexOf("needs triage"), 1); // remove it
      if (title.includes("simple") || title.includes("easy")) {
        updatedLabels.push("good first issue"); // easy enough for new contributors
      } else {
        updatedLabels.push("help wanted");      // needs someone to pick it up
      }
    }

    // Handle "discussing" (independent — both checks can fire)
    if (updatedLabels.includes("discussing")) {
      updatedLabels.splice(updatedLabels.indexOf("discussing"), 1); // remove it
      if (title.includes("planned") || title.includes("next")) {
        updatedLabels.push("on the roadmap"); // committed to the plan
      } else {
        updatedLabels.push("help wanted");    // still needs attention
      }
    }
  }

  // ── SECURITY: always runs, regardless of the branches above ────
  if (title.includes("security")) {
    updatedLabels.push("critical");
  }

  return updatedLabels;
}
```
