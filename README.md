# 🚩 Daily CTF Journey & Solutions

[![Daily CTF Streak](https://img.shields.io/badge/Daily%20Streak-Active%20🔥-orange.svg)](#-daily-activity-log)
[![Challenges Solved](https://img.shields.io/badge/Challenges%20Solved-0-brightgreen.svg)](#-daily-activity-log)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A dedicated repository documenting my daily journey of tackling Capture The Flag (CTF) challenges across cryptography, forensics, reverse engineering, binary exploitation, web security, and general Linux/scripting skills.

---

## 🧭 Category Navigation

| Category | Description | Index & Cheatsheet |
|---|---|:---:|
| 🛠️ **General Skills** | Linux shell, CLI piping, encoding/decoding, regex, scripting | [View Category](general-skills/README.md) |
| 🔐 **Cryptography** | Classical ciphers, RSA, AES, ECC, PRNGs, math-based attacks | [View Category](cryptography/README.md) |
| 🔎 **Forensics** | PCAP analysis, file carving, memory dumps, steganography | [View Category](forensics/README.md) |
| 🌐 **Web Exploitation** | XSS, SQLi, SSRF, SSTI, authentication bypass, IDOR, deserialization | [View Category](web-exploitation/README.md) |
| 🔄 **Reverse Engineering** | Disassembly, decompilation, binary patching, static & dynamic analysis | [View Category](reverse-engineering/README.md) |
| 💥 **Binary Exploitation** | Buffer overflows, ROP chains, format strings, heap exploitation | [View Category](binary-exploitation/README.md) |

---

## ⚡ Quick Start: Adding Today's Challenge

We maintain a built-in helper script to scaffold today's challenge files, writeup markdown, and solver script with one command:

```bash
# General syntax:
python scripts/new_challenge.py -c <category> -n "<challenge_name>" -p "<platform>" -d "<difficulty>"

# Example:
python scripts/new_challenge.py -c crypto -n "Caesar 101" -p picoCTF -d Easy
```

This automatically:
1. Creates `<category>/<platform>-<challenge-name>/`
2. Generates a pre-filled `README.md` writeup template
3. Generates a boilerplate `solve.py` script
4. Adds a ready entry into the **Daily Activity Log** below!

### Commit & Push Workflow
```bash
git add .
git commit -m "feat(crypto): solve picoCTF Caesar 101"
git push origin main
```

---

## 📅 Daily Activity Log

| Date | Platform | Challenge Name | Category | Difficulty | Flag Status |
|:---:|:---:|---|:---:|:---:|:---:|
<!-- ACTIVITY_LOG_START -->

*(Challenges solved each day will appear here automatically when running the scaffolder script)*

---

## 📂 Repository Structure

```text
CTF_for_everyone/
├── .gitignore
├── README.md                      # Repository dashboard & activity log
├── templates/
│   └── challenge-template.md      # Standard writeup structure
├── scripts/
│   └── new_challenge.py           # Scaffolding tool for daily challenges
├── general-skills/                # Linux, shell, encoding, regex
├── cryptography/                  # Ciphers, RSA, math, hash breaking
├── forensics/                     # PCAPs, disk carving, memory, stego
├── web-exploitation/              # Web apps, APIs, injections
├── reverse-engineering/           # Static & dynamic binary analysis
└── binary-exploitation/           # Pwn, ROP, memory corruption
```

---

## 🎯 Target Platforms

- [picoCTF](https://play.picoctf.org/)
- [Hack The Box](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [OverTheWire](https://overthewire.org/wargames/)
- [Cryptohack](https://cryptohack.org/)
- [pwnable.kr](https://pwnable.kr/) / [pwnable.tw](https://pwnable.tw/)

---

## ⚖️ License & Disclaimer

All writeups and exploit scripts in this repository are created strictly for educational purposes, defensive learning, and authorized CTF practice.
