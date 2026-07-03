# Parse Frontmatter — Code Explained

> Parse YAML-style frontmatter strings into JavaScript objects, correctly converting values to their native types (string, number, boolean).

---

## Table of Contents
1. [The Problem](#1-the-problem)
2. [What Is Frontmatter](#2-what-is-frontmatter)
3. [Step-by-Step Code Breakdown](#3-step-by-step-code-breakdown)
4. [The Type Conversion Logic](#4-the-type-conversion-logic)
5. [Why `indexOf` Instead of `split`](#5-why-indexof-instead-of-split)
6. [Methods Used](#6-methods-used)
7. [Full Annotated Code](#7-full-annotated-code)

---

## 1. The Problem

Given a raw frontmatter string like:

```
---
title: My Post
draft: false
views: 100
---
```

Return a JavaScript object with correctly typed values:

```js
{ title: 'My Post', draft: false, views: 100 }
//         string    boolean       number
```

---

## 2. What Is Frontmatter

Frontmatter is metadata placed at the top of text files (like Markdown blog posts). It is surrounded by `---` delimiters and contains `key: value` pairs. Static site generators like Jekyll, Hugo, and Astro use it to read page metadata.

---

## 3. Step-by-Step Code Breakdown

### Step 1 — Initialise the result object and split into lines

```js
function parseFrontmatter(str) {
  const result = {};
  const lines = str.split("\n");
  ...
}
```

`str.split("\n")` breaks the input string at every newline, producing an array of individual lines:

```js
["---", "title: My Post", "draft: false", "views: 100", "---"]
```

`result` will accumulate the parsed key-value pairs.

---

### Step 2 — Skip delimiter and empty lines

```js
for (let i = 0; i < lines.length; i++) {
  if (lines[i] === '' || lines[i] === '---') continue;
  ...
}
```

The `---` delimiters and any blank lines are not data — `continue` skips them and moves straight to the next iteration. Without this, the parser would try to split `"---"` as a key-value pair and fail.

---

### Step 3 — Find the first colon only

```js
const colonIndex = lines[i].indexOf(':');
if (colonIndex === -1) continue;
```

`indexOf(':')` returns the position of the **first** colon in the line. This is critical for lines like:

```
url: https://example.com
```

A simple `split(':')` would produce `["url", " https", "//example.com"]` — three parts instead of two, breaking the value. `indexOf` finds only the first colon, so the split is always clean.

If no colon is found (`-1`), the line is malformed — `continue` skips it safely.

---

### Step 4 — Extract key and raw value

```js
const key = lines[i].slice(0, colonIndex).trim();
const raw = lines[i].slice(colonIndex + 1).trim();
```

`slice(0, colonIndex)` takes everything **before** the colon → the key.  
`slice(colonIndex + 1)` takes everything **after** the colon → the raw value string.  
`.trim()` removes any leading or trailing whitespace from both.

For `"title: My Post"` with `colonIndex = 5`:
```
key = "title"
raw = "My Post"
```

---

### Step 5 — Convert the raw value to its native type

```js
if (raw === 'true')             result[key] = true;
else if (raw === 'false')       result[key] = false;
else if (raw !== '' && !isNaN(Number(raw))) result[key] = Number(raw);
else                            result[key] = raw;
```

Three checks run in order:

1. Exact string `"true"` → boolean `true`
2. Exact string `"false"` → boolean `false`
3. Non-empty string that converts cleanly to a number → number
4. Everything else stays as a string

See the next section for why the order and the `raw !== ''` guard both matter.

---

## 4. The Type Conversion Logic

### Why check booleans before numbers?

`Number("true")` is `NaN`, so booleans would fall through correctly even without the ordering. But being explicit and checking booleans first makes the intent clearer and avoids any edge cases.

### Why `raw !== ''` before `isNaN`?

```js
Number('')   // → 0  (empty string converts to 0!)
isNaN(0)     // → false
```

Without the empty string guard, a line with no value (e.g. `"title:"`) would be stored as `0` instead of `""`. The `raw !== ''` check prevents this.

### Why `Number(raw)` instead of `parseFloat` or `parseInt`?

`Number()` is stricter — it only converts strings that are entirely numeric:

```js
Number("100")    // → 100   ✅
Number("1.0.0")  // → NaN  ✅ stays a string (version number)
Number("10abc")  // → NaN  ✅ stays a string
parseFloat("1.0.0")  // → 1  ❌ would wrongly convert this
```

This is why `"version: 1.0.0"` correctly stays a string.

---

## 5. Why `indexOf` Instead of `split`

| Approach | Input | Result |
|---|---|---|
| `split(':')` | `"url: https://example.com"` | `["url", " https", "//example.com"]` ❌ |
| `indexOf(':')` + `slice` | `"url: https://example.com"` | key=`"url"`, value=`"https://example.com"` ✅ |

`split(':')` splits at **every** colon. `indexOf` finds only the first, letting `slice` take everything after it as one unbroken value.

---

## 6. Methods Used

| Method | Where Used | What It Does |
|---|---|---|
| `.split("\n")` | Breaking string into lines | Splits a string at every newline, returns an array |
| `.indexOf(char)` | Finding the first colon | Returns the index of the first occurrence, or `-1` if not found |
| `.slice(start, end)` | Extracting key and value | Returns a substring from `start` up to (not including) `end` |
| `.trim()` | Cleaning whitespace | Removes leading and trailing spaces/tabs from a string |
| `Number(value)` | Type conversion | Converts a string to a number; returns `NaN` if not purely numeric |
| `isNaN(value)` | Checking numeric validity | Returns `true` if the value is `NaN` |
| `continue` | Skipping lines | Jumps immediately to the next loop iteration |

---

## 7. Full Annotated Code

```js
function parseFrontmatter(str) {
  const result = {};
  const lines = str.split("\n"); // ["---", "title: My Post", ...]

  for (let i = 0; i < lines.length; i++) {
    // Skip delimiters and blank lines
    if (lines[i] === '' || lines[i] === '---') continue;

    // Find the FIRST colon only (protects URLs like https://...)
    const colonIndex = lines[i].indexOf(':');
    if (colonIndex === -1) continue; // malformed line, skip

    // Split at the colon position
    const key = lines[i].slice(0, colonIndex).trim();
    const raw = lines[i].slice(colonIndex + 1).trim();

    // Convert to the correct JS type
    if (raw === 'true') {
      result[key] = true;                     // boolean true
    } else if (raw === 'false') {
      result[key] = false;                    // boolean false
    } else if (raw !== '' && !isNaN(Number(raw))) {
      result[key] = Number(raw);              // number (int or float)
    } else {
      result[key] = raw;                      // string (default)
    }
  }

  return result;
}
```
