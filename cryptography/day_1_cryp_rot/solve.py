#!/usr/bin/env python3
"""
Solution script for Day 1: ROT13 Cipher
Platform: HTB Academy
Category: Cryptography
"""

import codecs
from pathlib import Path


def rot_decrypt(text: str, shift: int = 13) -> str:
    """Decrypt text using Caesar/ROT cipher with a given shift."""
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)


def main():
    script_dir = Path(__file__).resolve().parent
    values_file = script_dir / "values.txt"

    if values_file.exists():
        raw_lines = values_file.read_text(encoding="utf-8").strip().splitlines()
        ciphertext = raw_lines[0].strip()
    else:
        # Fallback to direct string if values.txt is missing
        ciphertext = "npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}"

    print(f"[*] Ciphertext: {ciphertext}")

    # Method 1: Using custom modular arithmetic function
    custom_flag = rot_decrypt(ciphertext, shift=13)

    # Method 2: Using Python's built-in codecs rot_13
    codecs_flag = codecs.decode(ciphertext, 'rot_13')

    assert custom_flag == codecs_flag, "Decryption methods mismatch!"

    print(f"[+] Flag recovered: {custom_flag}")


if __name__ == "__main__":
    main()
