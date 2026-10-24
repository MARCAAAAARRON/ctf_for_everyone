# Day 1: ROT13 Cipher

- **Platform:** HTB Academy
- **Category:** Cryptography
- **Difficulty:** Very Easy
- **Points:** 10
- **Date Solved:** 2026-10-24
- **Challenge Type:** Classical Substitution / Caesar Cipher

---

## 📌 Description

We are provided with a ciphertext string and a hint indicating that it was encoded using a rotational cipher:

```text
npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}
```

Hint provided: `this is a ROT13`.

### Attached Files
- [`values.txt`](values.txt) - The original challenge values.
- [`rot.py`](rot.py) - Interactive Python Caesar cipher tool.
- [`solve.py`](solve.py) - Automated non-interactive solution script.

---

## 💡 TL;DR
The ciphertext is encoded using **ROT13** (Rotate by 13 places), a symmetric monoalphabetic substitution cipher. Because the Latin alphabet has 26 letters and $13 + 13 = 26 \equiv 0 \pmod{26}$, applying ROT13 once more restores the plaintext flag directly.

---

## 🔍 Detailed Analysis & Methodology

### 1. Cryptographic Theory: Caesar & ROT13

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted down the alphabet by a fixed number of positions $k$:

$$C_i = (P_i + k) \pmod{26}$$

**ROT13** is a special case of the Caesar cipher where the shift key is fixed at $k = 13$:

$$C_i = (P_i + 13) \pmod{26}$$

#### Involutory Property (Self-Inverse)
Because there are 26 letters in the English alphabet:

$$(P_i + 13 + 13) \pmod{26} = (P_i + 26) \pmod{26} \equiv P_i \pmod{26}$$

This means that **encryption and decryption are the exact same function**:
$$\text{ROT13}(\text{ROT13}(M)) = M$$

---

### 2. Manual Tracing (Flag Prefix Check)

Examining the ciphertext prefix `npnqrzl{...}`:
- `n` (13) + 13 = 26 $\rightarrow$ `a` (0)
- `p` (15) + 13 = 28 $\equiv 2 \rightarrow$ `c`
- `n` (13) + 13 = 26 $\rightarrow$ `a`
- `q` (16) + 13 = 29 $\equiv 3 \rightarrow$ `d`
- `r` (17) + 13 = 30 $\equiv 4 \rightarrow$ `e`
- `z` (25) + 13 = 38 $\equiv 12 \rightarrow$ `m`
- `l` (11) + 13 = 24 $\rightarrow$ `y`

Decrypted prefix: **`academy{`**, matching the Hack The Box Academy flag format.

---

### 3. Solving Methods

#### Option A: Linux Terminal / One-liner
Using `tr`:
```bash
echo "npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

#### Option B: Python `codecs`
```python
import codecs
codecs.decode("npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}", "rot_13")
```

#### Option C: Automated Script
Run the included solver:
```bash
python solve.py
```

---

## 💻 Exploit / Solution Script

See [`solve.py`](solve.py):

```python
#!/usr/bin/env python3
import codecs
from pathlib import Path

def main():
    values_file = Path(__file__).resolve().parent / "values.txt"
    ciphertext = values_file.read_text(encoding="utf-8").strip().splitlines()[0]
    flag = codecs.decode(ciphertext, 'rot_13')
    print(f"[+] Flag recovered: {flag}")

if __name__ == "__main__":
    main()
```

---

## 🚩 Flag

```text
academy{next_time_I'll_try_2_rounds_of_rot13_5c5f5b36}
```

---

## 🧠 Key Takeaways & Learned Concepts
1. **ROT13 is self-inverse**: The encryption and decryption algorithms are identical.
2. **Frequency & Preserved Structure**: ROT13 preserves spaces, digits, punctuation, and capitalization. Only alphabetical characters are transformed.
3. **Common CTF Recognition**: Look for common prefixes when rotated (e.g. `picoCTF` rotated by 13 is `cvpbPGS`, `academy` is `npnqrzl`).
