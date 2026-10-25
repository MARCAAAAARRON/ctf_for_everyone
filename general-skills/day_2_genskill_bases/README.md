# Day 2: Bases (Base64 Decoding)

- **Platform:** picoCTF
- **Category:** General Skills
- **Difficulty:** Easy
- **Points:** 100
- **Date Solved:** 2026-10-25
- **Challenge Type:** Binary-to-Text Encodings / Base64

---

## 📌 Description

We are provided with an encoded string and a hint pointing to number bases:

> **What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.**

### Attached Files & Artifacts
- [`values.txt`](values.txt) — Original challenge prompt.
- [`solve.py`](solve.py) — Standalone automated solver script.

---

## 💡 TL;DR

The string `bDNhcm5fdGgzX3IwcDM1` is encoded using **Base64**, a binary-to-text encoding scheme. Decoding the 6-bit chunks back into 8-bit ASCII characters reveals the plaintext `l3arn_th3_r0p35` (leetspeak for *"learn the ropes"*), yielding the flag `picoCTF{l3arn_th3_r0p35}`.

---

## 🔍 Detailed Analysis & Methodology

### 1. Radix Counting Systems vs. Transmission Encodings

A critical distinction in computer science and CTFs:

| Category | Systems | Purpose & Character Set |
|---|---|---|
| **Counting Systems (Numeral Radices)** | Base 2 (Binary: `0-1`), Base 8 (Octal: `0-7`), Base 10 (Decimal: `0-9`), Base 16 (Hex: `0-9, A-F`) | Positional arithmetic representing numeric magnitudes and hardware states. |
| **Transmission Encodings (Binary-to-Text)** | Base 32, Base 64, Base 58, Base 85 | Translates arbitrary raw binary bytes into printable, network-safe ASCII characters that won't be corrupted by legacy communication protocols (e.g., SMTP email, URLs). |

---

### 2. Theoretical Background: How Base64 & Base32 Work

#### Why Base64 ($2^6 = 64$)?
- Each Base64 character represents **6 bits** of data because $2^6 = 64$.
- Standard Alphabet (RFC 4648):
  - `A`–`Z` (indices 0–25)
  - `a`–`z` (indices 26–51)
  - `0`–`9` (indices 52–61)
  - `+` (index 62)
  - `/` (index 63)
- **Grouping:** Every 3 bytes (24 bits) are divided into 4 groups of 6 bits:
  $$3 \text{ bytes} \times 8 \text{ bits} = 24 \text{ bits} = 4 \times 6 \text{ bits}$$
- **Padding (`=`):** If the input byte length is not divisible by 3, one or two `=` characters are appended to pad the encoded output to a multiple of 4 characters.

#### Comparison with Base32 ($2^5 = 32$)
- Each Base32 character represents **5 bits** ($2^5 = 32$).
- **Alphabet:** `A`–`Z` (26) + `2`–`7` (6) = 32 characters.
- **Why are `0`, `1`, `8`, and `9` omitted?**
  - To prevent human reading ambiguity: `0` can look like `O`, `1` can look like `I` or `l`, and `8` can look like `B`.

---

### 3. Decoding `bDNhcm5fdGgzX3IwcDM1`

The challenge string has a length of 20 characters (a multiple of 4, with no padding required) and contains mixed uppercase, lowercase, and numbers:
- `bDNh` $\rightarrow$ `l3a`
- `cm5f` $\rightarrow$ `rn_`
- `dGgz` $\rightarrow$ `th3`
- `X3Iw` $\rightarrow$ `_r0`
- `cDM1` $\rightarrow$ `p35`

Concatenated plaintext: **`l3arn_th3_r0p35`**

---

### 4. Fast CLI & Programmatic Decoders

#### Linux / macOS / WSL Bash
```bash
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
# Output: l3arn_th3_r0p35
```

#### Windows PowerShell
```powershell
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("bDNhcm5fdGgzX3IwcDM1"))
# Output: l3arn_th3_r0p35
```

#### Python One-Liner
```bash
python3 -c "import base64; print(base64.b64decode('bDNhcm5fdGgzX3IwcDM1').decode())"
```

---

## 💻 Exploit / Solution Script

The complete standalone solver is available in [`solve.py`](solve.py):

```python
#!/usr/bin/env python3
"""
Solution script for Day 2: Bases (Base64 Decoding)
Platform: picoCTF
Category: General Skills
"""

import base64

def solve():
    encoded_str = "bDNhcm5fdGgzX3IwcDM1"
    decoded_text = base64.b64decode(encoded_str).decode("utf-8")
    flag = f"picoCTF{{{decoded_text}}}"
    
    print(f"[*] Decoded payload: {decoded_text}")
    print(f"[+] Flag recovered:  {flag}")
    return flag

if __name__ == "__main__":
    solve()
```

---

## 🚩 Flag

```text
picoCTF{l3arn_th3_r0p35}
```

---

## 🧠 Key Takeaways & Lessons Learned

- **Pattern Recognition:** Strings with mixed alphanumeric characters (`a-z`, `A-Z`, `0-9`), lengths divisible by 4, and trailing `=` padding are almost always Base64.
- **Bit Allocation:**
  - Base64 encodes **6 bits/char** ($2^6 = 64$).
  - Base32 encodes **5 bits/char** ($2^5 = 32$).
  - Hexadecimal encodes **4 bits/char** (nibble, $2^4 = 16$).
- **Leetspeak Reading:** CTF flags routinely substitute letters with visually similar numbers (`3` for `e`, `0` for `o`, `5` for `s`).

### 📚 References & Documentation
- [RFC 4648: The Base16, Base32, and Base64 Data Encodings](https://datatracker.ietf.org/doc/html/rfc4648)
- [CyberChef: The Cyber Swiss Army Knife](https://gchq.github.io/CyberChef/)
- [Python `base64` Standard Library](https://docs.python.org/3/library/base64.html)
