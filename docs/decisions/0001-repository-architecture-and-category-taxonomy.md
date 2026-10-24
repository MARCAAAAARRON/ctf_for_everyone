# ADR-001: Repository Architecture and Category Taxonomy

## Status
Accepted

## Date
2026-10-24

## Context
Capture The Flag (CTF) competitions and training platforms span a wide range of security domains. As this repository grows daily with writeups, challenge attachments, exploit payloads, and solver scripts, we need an organized, scalable, and standard filesystem hierarchy. 

Without an agreed-upon structure:
- Challenges would be scattered across arbitrary folders or flat date-stamped directories.
- Searching for specific attack techniques (e.g., RSA Wiener attack or ROP chains) would be inefficient.
- Cross-referencing tooling and category cheatsheets would lack cohesion.

## Decision
We organize the repository by 6 primary CTF categories matching international competition conventions:
1. `general-skills/`: Shell commands, regex, piping, binary encodings, Linux environment triage.
2. `cryptography/`: Classical ciphers, modular arithmetic, RSA, AES, ECC, PRNG predictability.
3. `forensics/`: Network packet capture (PCAP), memory dumps, file carving, steganography.
4. `web-exploitation/`: OWASP Top 10 vulnerabilities, server-side and client-side web attacks, API security.
5. `reverse-engineering/`: Binary disassembly, decompilation, dynamic debugging, bytecode reverse engineering.
6. `binary-exploitation/`: Memory corruption, buffer overflows, format strings, ROP, heap exploitation.

Each category contains:
- A category `README.md` serving as an index of solved challenges, an essential tools table, attack methodology triage playbooks, and quick reference cheatsheets.
- Subdirectories for each challenge following the naming format: `<platform>-<challenge-name>` or `<day_N_category_topic>`.
- A dedicated `files/` directory inside each challenge folder for non-sensitive artifacts and target binaries.

Auxiliary directories:
- `templates/`: Houses standardized markdown writeup templates.
- `scripts/`: Automated scaffolding and management tools (e.g., `new_challenge.py`).
- `docs/decisions/`: Architecture Decision Records (ADRs).

## Alternatives Considered

### Alternative 1: Flat Date-Based Hierarchy (`YYYY/MM/DD/`)
- **Pros:** Chronological order is natural for daily streaks.
- **Cons:** Hard to find challenges by domain (e.g., finding all crypto challenges requires global search). Category-specific knowledge hubs and cheatsheets cannot be localized.
- **Rejected:** CTF skills grow domain-by-domain; categorizing by discipline delivers higher educational value.

### Alternative 2: Platform-First Hierarchy (`picoctf/`, `hackthebox/`, `tryhackme/`)
- **Pros:** Keeps challenges from the same platform grouped together.
- **Cons:** Fractures knowledge across platforms; techniques (e.g., SQLi) apply identically whether the challenge is from HTB or picoCTF.
- **Rejected:** Security concepts transcend platforms.

## Consequences
- Clean, predictable directory paths for automated tools.
- Scaffolding scripts can easily map CLI aliases (e.g., `-c crypto` -> `cryptography/`).
- Users can review progress and attack playbooks within any specific discipline directly from its category README.
