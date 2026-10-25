# Day 1: Base Conversion (0x3D to Decimal)

- **Platform:** picoCTF / CTF General Skills
- **Category:** General Skills
- **Difficulty:** Easy / Beginner
- **Points:** 50
- **Date Solved:** 2026-10-25
- **Challenge Type:** Number Systems & Radix Conversion (Base 16 to Base 10)

---

## 📌 Description

We are asked to convert a hexadecimal (base 16) integer representation into its equivalent decimal (base 10) representation:

> **What is `0x3D` (base 16) to decimal (base 10)?**

### Attached Files & Artifacts
- [`values.txt`](values.txt) — Original challenge question.
- [`solve.py`](solve.py) — Standalone non-interactive automated solver and verification script.

---

## 💡 TL;DR

Hexadecimal uses base 16 positional notation with digits `0`–`9` and `A`–`F` (where `D` = 13). Each digit is multiplied by $16^i$ based on its zero-indexed position from the right and **added** together: $(3 \times 16^1) + (13 \times 16^0) = 48 + 13 = \mathbf{61}$.

---

## 🔍 Detailed Analysis & Methodology

### 1. Number System Theory: Positional Radix Notation

In any positional numeral system with base $b$, an $n$-digit integer string $d_{n-1}d_{n-2}\dots d_1 d_0$ corresponds to the value:

$$\text{Value}_{10} = \sum_{i=0}^{n-1} d_i \cdot b^i = (d_{n-1} \cdot b^{n-1}) + \dots + (d_1 \cdot b^1) + (d_0 \cdot b^0)$$

For **Hexadecimal (Base 16)**:
- $b = 16$
- Available digits:
  $$\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \text{A}(10), \text{B}(11), \text{C}(12), \text{D}(13), \text{E}(14), \text{F}(15)\}$$
- The prefix `0x` is a syntactic convention indicating hexadecimal representation.

---

### 2. Step-by-Step Manual Calculation

Given the number `0x3D`:

1. **Extract digits and map to base 10 values**:
   - Digit at position 1: `3` $\rightarrow 3$
   - Digit at position 0: `D` $\rightarrow 13$

2. **Apply powers of 16**:
   - Position 1: $3 \times 16^1 = 3 \times 16 = 48$
   - Position 0: $13 \times 16^0 = 13 \times 1 = 13$

3. **Sum the positional values**:
   $$\text{Result} = 48 + 13 = \mathbf{61}$$

> [!TIP]
> **Common Formula Pitfall:**
> Be careful when writing out the expansion. Positional values must be **added** together, not multiplied:
> - ❌ *Incorrect:* $(3 \times 16^1) \times (13 \times 16^0) = 48 \times 13 = 624$
> - ✅ *Correct:* $(3 \times 16^1) + (13 \times 16^0) = 48 + 13 = \mathbf{61}$

---

### 3. Quick Command-Line & Automation Methods

In a timed CTF competition, manual arithmetic can be validated quickly using terminal one-liners:

#### Python CLI
```bash
# Direct hex literal evaluation
python3 -c "print(0x3D)"
# 61

# Base conversion with int(string, base)
python3 -c "print(int('0x3D', 16))"
# 61
```

#### Linux Shell (Bash / Zsh)
```bash
# Using printf format specifier %d
printf "%d\n" 0x3D
# 61

# Using shell arithmetic expansion with base syntax $((base#number))
echo $((16#3D))
# 61
```

---

## 💻 Exploit / Solution Script

The complete standalone solver is available in [`solve.py`](solve.py):

```python
#!/usr/bin/env python3
"""
Solution script for Day 1: Hexadecimal to Decimal Conversion (0x3D)
Category: General Skills
"""

def hex_to_dec(hex_str: str) -> int:
    return int(hex_str, 16)

def solve():
    challenge_input = "0x3D"
    val = hex_to_dec(challenge_input)
    print(f"[*] Input: {challenge_input} (Base 16)")
    print(f"[*] Formula: (3 * 16^1) + (13 * 16^0) = 48 + 13 = {val}")
    print(f"[+] Flag recovered: {val}")

if __name__ == "__main__":
    solve()
```

---

## 🚩 Flag / Answer

```text
61
```

*(Or formatted as a flag if requested: `picoCTF{61}`)*

---

## 🧠 Key Takeaways & Lessons Learned

- **Positional Weighting:** Digits in base $b$ always represent powers of $b^i$ starting at index $0$ from right to left.
- **Summation vs Multiplication:** Always add positional terms $(d_1 \cdot 16^1) + (d_0 \cdot 16^0)$.
- **Speed Tip:** Memorize hex letters $A=10$ through $F=15$ and utilize `int("0x...", 16)` or `printf "%d\n" 0x...` for instant verification during competitions.

### 📚 References & Documentation
- [Wikipedia: Hexadecimal Numeral System](https://en.wikipedia.org/wiki/Hexadecimal)
- [Python Documentation: `int()` built-in function](https://docs.python.org/3/library/functions.html#int)
- [Bash Hackers Wiki: Shell Arithmetic Base Notation](https://guide.bash.academy/expansions/#arithmetic-expansion)
