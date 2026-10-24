# 🔄 Reverse Engineering

A tactical reference guide and challenge repository dedicated to binary inspection, static decompilation, dynamic execution tracing, bytecode reversing, and algorithmic deobfuscation.

---

## 🧭 Core Sub-Domains & Analysis Disciplines

| Sub-Domain | Target Formats & Architectures | Core Objectives & Techniques |
|---|---|---|
| **Native Static Analysis** | ELF (Linux), PE (Windows), Mach-O (macOS) / x86, x86_64, ARM, MIPS | Disassembly, decompilation (C-like pseudocode), control flow graph (CFG) analysis, identifying validation algorithms and hardcoded keys |
| **Dynamic Debugging & Tracing** | Executable processes in memory | Setting breakpoints, inspecting registers/stack memory, function call tracing (`ltrace`, `strace`), modifying instruction pointers at runtime |
| **Bytecode & Managed Languages** | `.class` / `.jar` (Java), `.dll` / `.exe` (.NET), `.pyc` (Python), `.dex` / `.apk` (Android) | Pure source code decompilation, recovering class hierarchies, Android manifest examination, patching IL / smali bytecode |
| **Anti-Analysis & Deobfuscation** | Packed binaries (UPX), obfuscated control flow (OLLVM), anti-debug routines | Unpacking compressed executables, bypassing `ptrace` checks, defeating timing checks (`RDTSC`), decrypting obfuscated string tables |
| **Symbolic Execution & SMT Solving** | Complex validation functions with deep branching | Modeling program constraints using **angr** or **Z3** to automatically find inputs that reach the success state (`win` block) |

---

## ⚡ First 5 Minutes: Reverse Engineering Triage Playbook

```text
1. Identify Binary Format & Packing
   ├── $ file ./target_binary          # Architecture (32 vs 64-bit), stripped or unstripped?
   ├── $ strings -n 6 ./target_binary  # Look for prompts, error strings, UPX signatures
   └── $ checksec --file=./target_binary

2. Dynamic Tracing (Quick Wins)
   ├── $ ltrace ./target_binary input  # Inspect library calls (strcmp, strncmp, memcmp leaks!)
   └── $ strace ./target_binary input  # Inspect syscalls (open, read, write)

3. Static Decompilation
   ├── Open in Ghidra / IDA / Binary Ninja:
   │   ├── Find entry point -> navigate to `main()`
   │   ├── Identify key user inputs (`scanf`, `fgets`, `read`)
   │   └── Analyze the checking routine (XOR loops, character shifts, hash checks).

4. Managed Code Fast Path
   ├── .NET Binary?   ──> Open directly in dnSpy / ILSpy (near 100% decompilation)
   ├── Java / APK?    ──> Decompile via JADX GUI
   └── Python .pyc?   ──> Decompile using pycdc or decompyle++
```

---

## 🧰 Essential Tools & Frameworks

| Tool / Framework | Source / Installation | Purpose |
|---|---|---|
| **Ghidra** | [ghidra-sre.org](https://ghidra-sre.org/) | NSA's free, open-source decompiler, disassembler, and scripting engine |
| **IDA Free / Pro** | [hex-rays.com/ida-free](https://hex-rays.com/ida-free/) | Industry-standard disassembler and decompiler with robust graph views |
| **Binary Ninja** | [binary.ninja](https://binary.ninja/) | High-performance decompiler with Intermediate Language (BNIL) API |
| **x64dbg / x32dbg** | [x64dbg.com](https://x64dbg.com/) | Powerful open-source ring-3 debugger for Windows binaries |
| **GDB + pwndbg** | `apt install gdb` + [pwndbg](https://github.com/pwndbg/pwndbg) | Linux dynamic debugger with memory inspection, breakpoints, and register inspection |
| **angr** | `pip install angr` | Multi-architecture binary analysis framework and symbolic execution engine |
| **Z3 Solver** | `pip install z3-solver` | Microsoft's high-performance theorem prover and SMT solver |
| **JADX** | [skylot/jadx](https://github.com/skylot/jadx) | Fast Dex to Java decompiler with GUI and CLI for Android applications |
| **dnSpy / ILSpy** | [dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy) | .NET assembly debugger, decompiler, and real-time bytecode editor |
| **pycdc** | [zrax/pycdc](https://github.com/zrax/pycdc) | C++ Python bytecode disassembler and decompiler (Python 3.8+ compatible) |

---

## 📚 Solved Challenges

| Date | Platform | Challenge Name | Difficulty | Key Technique | Writeup Link |
|---|---|---|---|---|---|
<!-- CHALLENGE_LIST_START -->
<!-- Solved challenges in this category will be indexed here -->

---

## 📖 Curated Learning Resources

- [OpenSecurityTraining2: Architecture 1001 & 2001](https://ost2.fyi/) — Free high-quality courses on x86/x64 assembly and reversing.
- [Crackmes.one](https://crackmes.one/) — Community challenge platform to practice reverse engineering against real binary targets.
- [Begin.re](https://www.begin.re/) — Free, gentle reverse engineering tutorial for beginners.
- [Angr Documentation & Examples](https://docs.angr.io/) — Official guides and CTF challenge walkthroughs using symbolic execution.
