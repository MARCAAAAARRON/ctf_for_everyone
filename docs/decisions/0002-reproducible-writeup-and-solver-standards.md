# ADR-002: Reproducible Writeup and Standalone Solver Standards

## Status
Accepted

## Date
2026-10-24

## Context
CTF writeups frequently suffer from incomplete steps, missing context, and broken exploit scripts that only work in the author's local interactive session. To make this repository an authoritative learning resource and reliable personal knowledge base, every challenge solution must be verifiable, structured, and reproducible.

## Decision
All challenges added to the repository must adhere to the following standards:

1. **Standardized Writeup Layout (`README.md`):**
   - **Header Metadata:** Platform, Category, Difficulty, Points, Date Solved, Challenge URL.
   - **Description & Attached Files:** The original problem statement and links to target artifacts.
   - **TL;DR:** 1–2 sentence executive summary of the underlying vulnerability and key attack primitive.
   - **Detailed Analysis & Methodology:** Divided into Reconnaissance, Vulnerability Discovery, and Step-by-Step Exploitation.
   - **Mathematical / Theoretical Rigor:** Where applicable (crypto, pwn offsets, logic), state equations and underlying mechanisms.
   - **Exploit / Solution Code:** Clean, self-contained solver code embedded and linked.
   - **Flag Verification:** Stating the recovered flag (or redacted test flag).
   - **Key Takeaways & References:** Core concepts learned and links to external documentation.

2. **Standalone Solver Scripts (`solve.py`):**
   - Must run programmatically without interactive manual input.
   - Must parse challenge inputs from local challenge files or connect to remote sockets using environment variables/arguments.
   - Must print `[+] Flag recovered: <flag>` upon successful execution.

3. **Scaffolding Automation:**
   - The helper script `scripts/new_challenge.py` must enforce directory creation, template substitution, and automatic registration in the master activity tracker.

## Alternatives Considered

### Alternative 1: Free-form Markdown Writeups
- **Pros:** Lower friction when recording quick notes.
- **Cons:** Inconsistent quality; critical sections (such as recon or key takeaways) are frequently omitted.
- **Rejected:** Inconsistency degrades repository educational value and searchability.

### Alternative 2: Terminal Session Logs / Screenshots Only
- **Pros:** Fast to capture.
- **Cons:** Not searchable, difficult to copy commands from, does not explain the *why* or underlying vulnerability.
- **Rejected:** Screenshots cannot replace clean code and structured text analysis.

## Consequences
- Every challenge directory contains both human-readable explanations (`README.md`) and machine-executable code (`solve.py`).
- Clear quality bar makes onboarding and reviewing past challenges immediate and seamless.
- Scaffolding tooling streamlines adherence to the standard.
