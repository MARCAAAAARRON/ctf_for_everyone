# 🔐 Cryptography

A comprehensive reference hub and challenge archive covering classical cryptosystems, modern symmetric and asymmetric cryptography, modular arithmetic, lattice-based attacks, and pseudo-random number generator (PRNG) analysis.

---

## 🧭 Core Sub-Domains & Attack Vectors

| Sub-Domain | Core Concepts & Primitives | Common CTF Attack Vectors |
|---|---|---|
| **Classical & Substitution** | Caesar, ROT13, Vigenère, Affine, Atbash, Substitution, Rail Fence | Frequency analysis, index of coincidence (IC), Kasiski examination, crib dragging |
| **Modular Arithmetic & Math** | GCD, Extended Euclidean Algorithm, Chinese Remainder Theorem (CRT), Euler's Totient $\phi(n)$ | Modulus reduction, small roots, discrete logarithms |
| **Asymmetric (RSA)** | $e$, $d$, $n = p \cdot q$, Euler's totient, PKCS#1 padding | Small $e$ ($e=3$ broadcast/Hastad), Wiener's attack (small $d$), Boneh-Durfee, Fermat factorization ($p \approx q$), common modulus, Pollard's $p-1$ |
| **Symmetric (AES / DES)** | ECB, CBC, CTR, GCM, OFB, CFB block cipher modes | ECB byte-at-a-time ECB penguin, CBC padding oracle attacks, bit-flipping attacks, IV reuse |
| **Hash Functions & MACs** | MD5, SHA-1, SHA-256, HMAC | Length extension attacks (HashPump), hash collisions, rainbow tables, weak salt placement |
| **Elliptic Curve Cryptography** | Weierstrass curves, secp256k1, point addition, scalar multiplication | Singular curves, Pohlig-Hellman, Smart's attack (anomalous curves), invalid curve attacks |
| **PRNGs & Randomness** | Linear Congruential Generators (LCG), Mersenne Twister (MT19937) | State recovery (624 MT states with `randcrack`), seed brute-force, predictability |

---

## ⚡ First 5 Minutes: Cryptanalysis Triage Playbook

When starting a CTF cryptography challenge, follow this systematic workflow:

```text
1. Inspect Ciphertext & Artifacts
   ├── Check alphabet (hexadecimal, base64, base58, raw bytes, printable ASCII)
   └── Determine if it is encoded (Base64/Hex/URL) before being encrypted.

2. Identify Cipher Family
   ├── Length preserved & uppercase/lowercase structure kept? ──> Classical / Substitution
   ├── Length is multiple of 16 bytes (128 bits)? ──────────────> Block cipher (AES)
   ├── Public parameters provided (n, e, c)? ──────────────────> RSA
   ├── Elliptic curve parameters provided (a, b, p, G)? ────────> ECC
   └── Key generation involves `random` / `seed`? ──────────────> PRNG state recovery

3. Formulate Attack Hypothesis
   ├── Factor modulus n using factordb.com or SageMath.
   ├── Check for small exponents (e = 3) or small private keys (d < 1/3 * n^(1/4)).
   └── If XOR-based, search for known plaintext cribs (e.g., flag prefixes like "flag{").
```

---

## 🧰 Essential Tools & Frameworks

| Tool / Library | Installation / Source | Purpose |
|---|---|---|
| **PyCryptodome** | `pip install pycryptodome` | Standard Python cryptographic primitives (AES, RSA, DES, hashes) |
| **SymPy** | `pip install sympy` | Symbolic mathematics, prime testing, discrete log, modular inverses |
| **gmpy2** | `pip install gmpy2` | High-performance multi-precision arithmetic for fast factorizations |
| **SageMath** | [sagemath.org](https://www.sagemath.org/) | Advanced mathematical cryptanalysis (LLL, Coppersmith, lattices) |
| **RsaCtfTool** | [GitHub](https://github.com/RsaCtfTool/RsaCtfTool) | Automated RSA key attacks (Wiener, Boneh-Durfee, ECM, Fermat) |
| **CyberChef** | [GCHQ CyberChef](https://gchq.github.io/CyberChef/) | Web-based visual pipeline for rapid encoding/decoding and ciphers |
| **Hashcat** / **John** | `apt install hashcat john` | High-speed GPU/CPU hash recovery and dictionary attacks |
| **dcode.fr** | [dcode.fr](https://www.dcode.fr/en) | Online cipher identifier and classical cryptanalysis solver |

---

## 📚 Solved Challenges

| Date | Platform | Challenge Name | Difficulty | Key Technique | Writeup Link |
|---|---|---|---|---|---|
<!-- CHALLENGE_LIST_START -->
| 2026-10-24 | HTB Academy | [ROT13](day_1_cryp_rot/README.md) | Very Easy | Caesar/ROT13 Involutory Property | [Writeup & Solution](day_1_cryp_rot/README.md) |

---

## 📖 Curated Learning Resources

- [CryptoHack](https://cryptohack.org/) — Interactive platform for learning modern cryptography.
- [Factordb](http://factordb.com/) — Online database of known factorizations for RSA integers.
- [FeatherDuster](https://github.com/nccgroup/featherduster) — Automated cryptanalysis tool.
- [A Graduate Course in Applied Cryptography (Boneh & Shoup)](https://toc.cryptobook.us/) — Comprehensive reference textbook.
