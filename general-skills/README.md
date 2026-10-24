# 🛠️ General Skills & Linux Foundations

A practical guide and solution directory focused on essential Linux shell navigation, text manipulation, data streams, encoding transformations, network sockets, and command-line automation.

---

## 🧭 Core Sub-Domains & Competencies

| Sub-Domain | Core Concepts & Utilities | CTF Application & Problem Types |
|---|---|---|
| **Linux Environment & Filesystem** | `find`, `ls -la`, permissions (`chmod`, `chown`), SUID/SGID, environment variables | Locating hidden challenge files, inspecting dotfiles, escalating shell privileges |
| **Text Processing & Filtering** | `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, `tr`, `xargs` | Parsing massive logs, extracting flag strings, cleaning datasets, tabular filtering |
| **Encodings & Number Systems** | Base64, Base32, Base58, Hexadecimal, Binary, Octal, ASCII, Big/Little Endian | Transforming encoded tokens, handling binary byte payloads, multi-base conversions |
| **Network Sockets & Data Streams** | `nc` (netcat), `socat`, `curl`, `wget`, SSH key auth, port forwarding | Interacting with remote challenge daemons, automating question-and-answer services |
| **Regex & Pattern Extraction** | PCRE regex, positive lookaheads, anchors, quantifiers | Locating specific flag patterns (`flag\{[A-Za-z0-9_]+\}`) across thousands of files |
| **CLI Automation & Scripting** | Bash loops, subshells, Python one-liners, arithmetic expansion | Automating 1,000 rapid socket calculations under strict timeouts |

---

## ⚡ First 5 Minutes: General Skills Triage Playbook

```text
1. Inspecting Data & Magic Bytes
   ├── $ file target_file              # Determine filetype regardless of extension
   ├── $ xxd target_file | head -n 10  # View raw hex and ASCII side-by-side
   └── $ strings target_file | grep -E "flag|CTF|pico|htb"

2. Searching Filesystem & Hidden Files
   ├── $ find . -type f -name ".*"     # Find hidden dotfiles
   ├── $ find / -perm -4000 2>/dev/null# Find SUID binaries
   └── $ grep -rnw "." -e "flag"       # Recursive search inside all text files

3. Quick Decoding Pipeline (CLI)
   ├── Base64:      $ echo "aGVsbG8=" | base64 -d
   ├── Hex to text: $ echo "68656c6c6f" | xxd -r -p
   ├── Binary:      $ echo "01100001" | perl -lape '$_=pack"(B8)*",@F'
   └── ROT13:       $ echo "synt" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

4. Socket Interaction & Scripting
   ├── Manual:      $ nc <ip> <port>
   └── Programmatic: Python `socket` or `pwntools.remote(host, port)`
```

---

## 🧰 Essential Tools & Commands Cheat Sheet

| Tool / Command | Example Invocation | Purpose |
|---|---|---|
| **grep** | `grep -rioP "flag\{.*?\}" .` | Fast recursive regex search across all files in directory |
| **awk** | `awk '{print $2}' file.txt` | Extract specific space/tab-delimited column from output |
| **sed** | `sed -i 's/old/new/g' file.txt` | In-place stream find-and-replace text manipulation |
| **xxd** | `xxd -p file.bin \| tr -d '\n'` | Dump binary content as continuous hex stream |
| **nc (netcat)** | `nc -nv 10.10.10.10 1337` | Connect to remote TCP port or listen on local port |
| **socat** | `socat TCP-LISTEN:1337,fork EXEC:./vuln` | Host binary on local port with fork isolation for pwn testing |
| **base64** | `echo -n "test" \| base64` | Fast CLI Base64 encoding/decoding |
| **tmux** | `tmux new -s ctf` | Persistent terminal sessions, split panes, and window multiplexing |

---

## 📚 Solved Challenges

| Date | Platform | Challenge Name | Difficulty | Key Technique | Writeup Link |
|---|---|---|---|---|---|
<!-- CHALLENGE_LIST_START -->
<!-- Solved challenges in this category will be indexed here -->

---

## 📖 Curated Learning Resources

- [OverTheWire: Bandit](https://overthewire.org/wargames/bandit/) — The gold-standard wargame for learning Linux terminal skills.
- [Linux Journey](https://linuxjourney.com/) — Structured lessons on Linux command line, permissions, and processes.
- [Regex101](https://regex101.com/) — Interactive regular expression debugger with detailed syntax explanations.
- [Explainshell](https://explainshell.com/) — Visual breakdown of complex shell command combinations and flags.
