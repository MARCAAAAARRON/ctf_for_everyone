# 🚩 Daily CTF Journey & Solutions

[![Daily CTF Streak](https://img.shields.io/badge/Daily%20Streak-Active%20🔥-orange.svg)](#-daily-activity-log)
[![Challenges Solved](https://img.shields.io/badge/Challenges%20Solved-3-brightgreen.svg)](#-daily-activity-log)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](requirements.txt)
[![Architecture Decisions](https://img.shields.io/badge/ADRs-Documented-purple.svg)](docs/decisions/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A dedicated, reproducible repository documenting my daily journey of tackling Capture The Flag (CTF) challenges across cryptography, forensics, reverse engineering, binary exploitation, web security, and Linux foundations. Every challenge includes an in-depth writeup, educational takeaways, and an automated standalone solver script.

---

## 📑 Table of Contents

- [🧭 Category Navigation](#-category-navigation)
- [⚡ Quick Start & Environment Setup](#-quick-start--environment-setup)
- [🛠️ Tooling & Command Reference](#-tooling--command-reference)
- [📅 Daily Activity Log](#-daily-activity-log)
- [📂 Repository Architecture](#-repository-architecture)
- [🏛️ Architecture Decision Records (ADRs)](#️-architecture-decision-records-adrs)
- [🤝 Standards & Contributing Guide](#-standards--contributing-guide)
- [🎯 Target Platforms](#-target-platforms)
- [⚖️ License & Ethical Disclaimer](#️-license--ethical-disclaimer)

---

## 🧭 Category Navigation

| Category | Primary Focus & Attack Vectors | Track Index & Playbook |
|---|---|:---:|
| 🛠️ **General Skills** | Linux shell mastery, regex, piping, binary/hex/base conversions, CLI automation | [Explore Category](general-skills/README.md) |
| 🔐 **Cryptography** | Classical ciphers, modular arithmetic, RSA, AES, ECC, PRNG predictability | [Explore Category](cryptography/README.md) |
| 🔎 **Forensics** | PCAP network analysis, memory forensics, file carving, steganography | [Explore Category](forensics/README.md) |
| 🌐 **Web Exploitation** | SQLi, XSS, SSRF, SSTI, authentication/JWT flaws, IDOR, deserialization | [Explore Category](web-exploitation/README.md) |
| 🔄 **Reverse Engineering** | Disassembly, decompilation, binary patching, bytecode (.NET/Java/Python), dynamic debugging | [Explore Category](reverse-engineering/README.md) |
| 💥 **Binary Exploitation** | Buffer overflows, ret2libc, ROP chains, format strings, heap exploitation | [Explore Category](binary-exploitation/README.md) |

---

## ⚡ Quick Start & Environment Setup

### 1. Prerequisites
- **Python 3.10+**
- **Git**
- Optional (for pwn & reversing): Linux environment or **WSL2** (Windows Subsystem for Linux)

### 2. Clone Repository & Setup Virtual Environment
```bash
# Clone the repository
git clone https://github.com/MARCAAAAARRON/ctf_for_everyone.git
cd ctf_for_everyone

# Create and activate a Python virtual environment
python -m venv venv

# On Linux / macOS / WSL:
source venv/bin/activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Install core dependencies
pip install -r requirements.txt
```

---

## 🛠️ Tooling & Command Reference

| Action | Command | Description |
|---|---|---|
| **Scaffold New Challenge** | `python scripts/new_challenge.py -c <category> -n "<name>" -p "<platform>" -d "<difficulty>"` | Creates directory, template writeup, solver, and registers entry in tracker |
| **Run Daily Challenge Solver** | `python cryptography/day_1_cryp_rot/solve.py` | Executes challenge-specific standalone Python solver |
| **Test Scaffolder (Dry Run)** | `python scripts/new_challenge.py -c crypto -n "Test Challenge" --test` | Runs scaffolding verification without mutating root tracker |
| **Interactive ROT Tool** | `python cryptography/day_1_cryp_rot/rot.py` | Interactive shift and substitution utility |

### Scaffolding Example:
```bash
python scripts/new_challenge.py -c crypto -n "Caesar 101" -p picoCTF -d Easy --points 100
```

---

## 📅 Daily Activity Log

| Date | Platform | Challenge Name | Category | Difficulty | Flag Status |
|:---:|:---:|---|:---:|:---:|:---:|
<!-- ACTIVITY_LOG_START -->
| 2026-10-25 | picoCTF | [Bases (Base64)](general-skills/day_2_genskill_bases/README.md) | General Skills | Easy | Solved ✅ |
| 2026-10-25 | picoCTF | [Base Conversion (0x3D)](general-skills/day_1_genskill_base/README.md) | General Skills | Easy | Solved ✅ |
| 2026-10-24 | HTB Academy | [ROT13](cryptography/day_1_cryp_rot/README.md) | Cryptography | Very Easy | Solved ✅ |

---

## 📂 Repository Architecture

```text
CTF_for_everyone/
├── .gitignore                         # Excludes compiled bytecode, virtual environments, large dumps
├── LICENSE                            # MIT License
├── README.md                          # Repository dashboard, activity log, quickstart
├── requirements.txt                   # Shared Python dependencies
├── docs/
│   └── decisions/                     # Architecture Decision Records (ADRs)
│       ├── README.md                  # Index of ADRs
│       ├── 0001-repository-architecture-and-category-taxonomy.md
│       └── 0002-reproducible-writeup-and-solver-standards.md
├── templates/
│   └── challenge-template.md          # Standard writeup structure
├── scripts/
│   └── new_challenge.py               # Scaffolding tool for daily challenges
├── general-skills/                    # Linux CLI, encoding, regex, shell automation
├── cryptography/                      # Classical ciphers, RSA, AES, math, PRNGs
├── forensics/                         # PCAPs, memory dumps, disk carving, steganography
├── web-exploitation/                  # Web applications, APIs, injections, bypasses
├── reverse-engineering/               # Static decompilation, dynamic debugging, bytecode
└── binary-exploitation/               # Pwn, memory corruption, ROP, heap exploitation
```

---

## 🏛️ Architecture Decision Records (ADRs)

We record significant architectural choices to maintain codebase consistency and preserve technical context. For detailed rationale and trade-offs, see [docs/decisions/README.md](docs/decisions/README.md):

- [**ADR-001: Repository Architecture and Category Taxonomy**](docs/decisions/0001-repository-architecture-and-category-taxonomy.md) — Explains the domain-first taxonomy, folder hierarchies, and CLI categorization aliases.
- [**ADR-002: Reproducible Writeup and Standalone Solver Standards**](docs/decisions/0002-reproducible-writeup-and-solver-standards.md) — Mandates the writeup format, mathematical rigor, and automated, non-interactive `solve.py` scripts.

---

## 🤝 Standards & Contributing Guide

When adding or updating challenge writeups, adhere to the following quality standards:

1. **Scaffold with Automation:** Always generate the skeleton via `python scripts/new_challenge.py`.
2. **Deterministic Solvers:** Every `solve.py` script must execute without human intervention and output `[+] Flag recovered: <flag>`.
3. **No Secret Leaks:** Do not commit proprietary binaries or private platform VPN tokens.
4. **Git Commit Convention:** Use Conventional Commits:
   ```bash
   git add .
   git commit -m "feat(crypto): solve HTB Academy ROT13 writeup and solver"
   git push origin main
   ```

---

## 🎯 Target Platforms

- [Hack The Box & HTB Academy](https://www.hackthebox.com/)
- [picoCTF](https://play.picoctf.org/)
- [TryHackMe](https://tryhackme.com/)
- [CryptoHack](https://cryptohack.org/)
- [OverTheWire Wargames](https://overthewire.org/wargames/)
- [pwnable.kr](https://pwnable.kr/) / [pwnable.tw](https://pwnable.tw/)

---

## ⚖️ License & Ethical Disclaimer

This repository is distributed under the [MIT License](LICENSE). 

All writeups, exploit payloads, and solver scripts are developed exclusively for educational purposes, defensive security research, and authorized Capture The Flag practice. Unauthorized testing against systems without prior written consent is strictly illegal.
