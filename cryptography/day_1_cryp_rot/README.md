# Day 1: ROT13 Cipher

- **Platform:** HTB Academy
- **Category:** Cryptography
- **Difficulty:** Very Easy
- **Points:** 10
- **Date Solved:** 2026-10-24
- **Challenge Type:** Classical Substitution / Caesar Cipher

---

## 📌 Description

We are provided with an obfuscated ciphertext string along with a challenge hint indicating that a rotational substitution cipher was applied:

```text
npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}
```

**Challenge Hint:** `this is a ROT13`.

### Attached Files & Artifacts
- [`values.txt`](values.txt) — Original challenge ciphertext artifact.
- [`rot.py`](rot.py) — Interactive Python Caesar/ROT tool for custom shift values.
- [`solve.py`](solve.py) — Standalone non-interactive automated solver script.

---

## 💡 TL;DR

The ciphertext is encoded using **ROT13** (Rotate by 13 places), a symmetric monoalphabetic substitution cipher. Because the English Latin alphabet contains 26 letters and $13 + 13 = 26 \equiv 0 \pmod{26}$, applying the ROT13 transformation once more to the ciphertext directly restores the plaintext flag.

---

## 🔍 Detailed Analysis & Methodology

### 1. Cryptographic Theory: Caesar & ROT13

The Caesar cipher shifts each letter in plaintext $P$ down the alphabet by a fixed integer key $k \in \{0, \dots, 25\}$:

$$C_i = (P_i + k) \pmod{26}$$

**ROT13** is a specialized instance where $k = 13$:

$$C_i = (P_i + 13) \pmod{26}$$

#### Involutory Property (Self-Inverse)
Because there are 26 letters in the standard Latin alphabet:

$$(P_i + 13 + 13) \pmod{26} = (P_i + 26) \pmod{26} \equiv P_i \pmod{26}$$

This means the decryption operation is identical to the encryption operation:

$$\text{ROT13}(\text{ROT13}(M)) = M$$

---

### 2. Manual Tracing (Flag Format Verification)

Examining the ciphertext prefix `npnqrzl{...}`:

| Cipher Char | ASCII Value | Alphabet Index ($0$-indexed) | $(Index + 13) \pmod{26}$ | Plain Char |
|:---:|:---:|:---:|:---:|:---:|
| `n` | 110 | 13 | $(13 + 13) \pmod{26} = 0$ | `a` |
| `p` | 112 | 15 | $(15 + 13) \pmod{26} = 2$ | `c` |
| `n` | 110 | 13 | $(13 + 13) \pmod{26} = 0$ | `a` |
| `q` | 113 | 16 | $(16 + 13) \pmod{26} = 3$ | `d` |
| `r` | 114 | 17 | $(17 + 13) \pmod{26} = 4$ | `e` |
| `z` | 122 | 25 | $(25 + 13) \pmod{26} = 12$ | `m` |
| `l` | 108 | 11 | $(11 + 13) \pmod{26} = 24$ | `y` |

Decrypted prefix: **`academy{`**, matching the expected Hack The Box Academy flag format.

---

### 3. Solving Methods

#### Method A: Linux CLI / Shell One-Liner
Using the standard `tr` utility:
```bash
echo "npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

#### Method B: Python Standard Library (`codecs`)
```python
import codecs
flag = codecs.decode("npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}", "rot_13")
print(flag)
```

#### Method C: CyberChef Recipe
In CyberChef, load the recipe **ROT13** with amount `13`.

#### Method D: Automated Script
Execute the repository solver directly:
```bash
python solve.py
```

---

## 💻 Exploit / Solution Script

The automated solver is located at [`solve.py`](solve.py):

```python
#!/usr/bin/env python3
"""
Solution script for Day 1: ROT13 Cipher (HTB Academy)
Reads ciphertext from values.txt and decodes it using codecs rot_13.
"""

import codecs
from pathlib import Path

def main():
    values_file = Path(__file__).resolve().parent / "values.txt"
    if not values_file.exists():
        print(f"[-] Missing input file: {values_file}")
        return
    
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

## 🧠 Key Takeaways & Lessons Learned

1. **Obfuscation vs. Encryption:** ROT13 provides zero cryptographic confidentiality. It has a key space of size 1 ($k=13$) and is trivial to break even without knowing the shift value by trying all 25 possible Caesar shifts (or performing letter frequency analysis).
2. **Preserved Characters:** ROT13 preserves non-alphabetic characters (numbers, underscores, curly braces, apostrophes).
3. **Common CTF Signature:** Learning common rotated prefixes accelerates triage:
   - `cvpbPGS{...}` $\rightarrow$ `picoCTF{...}`
   - `npnqrzl{...}` $\rightarrow$ `academy{...}`
   - `synt{...}` $\rightarrow$ `flag{...}`
4. **Defensive Best Practice:** Always use authenticated, modern cryptographic schemes (such as AES-GCM or ChaCha20-Poly1305) when confidentiality and integrity are required. Never use classical or rotational ciphers for secure communication.

### 📚 References
- [Wikipedia: ROT13](https://en.wikipedia.org/wiki/ROT13)
- [HTB Academy: Cryptography Fundamentals](https://academy.hackthebox.com/)
- [CyberChef ROT13 Recipe](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13))
