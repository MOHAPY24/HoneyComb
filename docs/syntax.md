
# HoneyComb Docs 🐝📔

## Part *2* of *20*

### This part will cover

1. Core Syntax
2. Tape Operations
3. Comb Operations
4. Input/Output
5. Utility Commands

---

## Core Syntax

HoneyComb syntax is made up of **single-character operators**. Each operator manipulates the multidimensional tapes (`xtape`, `ytape`) or controls the interpreter state. Programs are written as `.hc` files with only HoneyComb symbols (spaces, tabs, and newlines are ignored).

---

## Tape Operations 🧵

* `+` → Increment current cell by **1**
* `-` → Decrement current cell by **1**
* `.` → Print current cell as **number**
* `,` → Print current cell as **ASCII character**
* `:` → Input integer from user → add to current cell

---

## Pointer Movement 🎯

* `>` → Move **right** along `xtape` (switches to X-mode)
* `<` → Move **left** along `xtape` (switches to X-mode)
* `^` → Move **up** along `ytape` (switches to Y-mode)
* `V` → Move **down** along `ytape` (switches to Y-mode)

---

## Comb Movement 🍯

HoneyComb uses the idea of **combs** — groups of cells inside each dimension.

* `/` → Move to **next comb** (in X or Y depending on mode)
* `W` → Move to **previous comb** (in X or Y depending on mode) (Used to be \ but now replaced due to parsing errors)

---

## Clearing & Math 🧼✖️

* `!` → Clear **current cell** → `0`
* `~` → Clear **current comb** → all cells in that comb set to `0`
* `%` → Clear **entire tape** → reset all cells in tape to `0`
* `S` → Square current cell → `cell = cell * cell`

---

## Memory Save/Load 🍃

* `*` → Save current cell into a temporary buffer (pollen storage)
* `&` → Load saved value from buffer back into current cell

---

## Flow Control 🔀

* `#` → If current cell equals `0`, jump pointer to the given position in code
  *(Currently limited: reads the **next character as an integer** for jump index)*

---

## Comments ✍️

* `(` → Start comment mode → interpreter ignores tokens
* `)` → End comment mode

---

## Example 🐝

```hc
+++>+++.
```

Explanation:

1. `+++` → increment cell 0 three times (value = 3).
2. `>` → move pointer right (cell 1).
3. `+++` → increment cell 1 three times (value = 3).
4. `.` → print current cell (prints `3`).

---

## Notes

* HoneyComb syntax is **strict**: any character not part of the above set raises a `SyntaxError`.
* Integers (`0–9`) are tokenized but not yet functional in this version.
* Comments are fully ignored until the matching `)`.

---

## MORE DOCS COMING SOON!
