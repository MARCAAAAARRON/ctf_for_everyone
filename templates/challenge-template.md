# {{CHALLENGE_NAME}}

- **Platform:** {{PLATFORM}}
- **Category:** {{CATEGORY}}
- **Difficulty:** {{DIFFICULTY}}
- **Points:** {{POINTS}}
- **Date Solved:** {{DATE}}
- **Challenge URL:** [Link]({{URL}})

---

## 📌 Description

> {{DESCRIPTION}}

### Attached Files
- `{{FILES}}`

---

## 💡 TL;DR
> Short 1-2 sentence explanation of the vulnerability and attack vector (e.g., "Exploited an insecure deserialization in Python pickle to achieve RCE and read `/flag.txt`").

---

## 🔍 Detailed Analysis & Methodology

### 1. Initial Reconnaissance / Triage
- What type of service or binary is this?
- Inspection results (`file`, `checksec`, `nmap`, `strings`, `binwalk`, or inspecting source code).

```bash
# Recon commands
file ./challenge
checksec --file=./challenge
```

### 2. Vulnerability Discovery
- Explain the flaw found in logic, cryptography, format strings, buffer overflow, etc.

### 3. Exploitation Walkthrough
- Step-by-step instructions to reproduce the exploit.
- Calculation of offsets, key derivation, or reverse engineering logic.

---

## 💻 Exploit / Solution Script

```python
#!/usr/bin/env python3
"""
Solution script for {{CHALLENGE_NAME}} ({{PLATFORM}})
"""

from pwn import *

def solve():
    # Insert solution logic here
    pass

if __name__ == "__main__":
    solve()
```

---

## 🚩 Flag

```text
{{FLAG}}
```

---

## 🧠 Key Takeaways & Learned Concepts
- Concepts learned or reinforced.
- Useful tools or one-liners used.
- References / documentation:
  - [Reference Link](https://example.com)
