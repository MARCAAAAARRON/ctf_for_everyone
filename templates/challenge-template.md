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

### Attached Files & Artifacts
- `{{FILES}}`

---

## 💡 TL;DR
> Short 1-2 sentence explanation of the vulnerability, root cause, and attack vector (e.g., *"Exploited an insecure deserialization in Python `pickle` to achieve remote code execution and extract `/flag.txt`"*).

---

## 🔍 Detailed Analysis & Methodology

### 1. Initial Reconnaissance & Triage
- File identification, headers, architecture, and preliminary inspection.
- Target network endpoints, ports, or web endpoints.

```bash
# Reconnaissance commands
file ./challenge
checksec --file=./challenge
strings -n 8 ./challenge | head -n 30
```

### 2. Vulnerability Discovery & Root Cause
- Detailed examination of the flawed logic, cryptographic vulnerability, memory corruption condition, or web vulnerability.
- Code snippets or assembly highlights pointing directly to the flaw.

### 3. Mathematical / Theoretical Background (If Applicable)
- Mathematical equations, cipher schemes, modular reduction, or heap memory layouts relevant to the exploit.

### 4. Step-by-Step Exploitation Walkthrough
1. **Stage 1: Setup & Input Preparation** — How payloads or inputs are crafted.
2. **Stage 2: Triggering the Vulnerability** — Executing the attack path locally or remotely.
3. **Stage 3: Flag Extraction** — Parsing the response and obtaining the flag.

---

## 💻 Exploit / Solution Script

The complete, automated solver is available in [`solve.py`](solve.py):

```python
#!/usr/bin/env python3
"""
Solution script for {{CHALLENGE_NAME}} ({{PLATFORM}})
Category: {{CATEGORY}}
"""

import sys
from pathlib import Path

def solve():
    # Insert solution logic here
    flag = "FLAG{...}"
    print(f"[+] Flag recovered: {flag}")

if __name__ == "__main__":
    solve()
```

---

## 🚩 Flag

```text
{{FLAG}}
```

---

## 🧠 Key Takeaways & Lessons Learned

- **Core Concept:** Summary of primary concept reinforced.
- **Defensive Countermeasure:** How the developers or system administrators could mitigate or patch this vulnerability.
- **Helpful Tools & One-Liners:** Quick commands or libraries discovered during this challenge.

### 📚 References & Documentation
- [Official Documentation / Advisory](https://example.com)
- [Writeup / Tool Repository](https://example.com)
