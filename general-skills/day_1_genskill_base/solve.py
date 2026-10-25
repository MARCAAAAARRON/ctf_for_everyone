#!/usr/bin/env python3
"""
Solution script for Day 1: Hexadecimal to Decimal Conversion (0x3D)
Category: General Skills
Date: 2026-10-25
"""

def hex_to_dec_manual(hex_str: str) -> int:
    """
    Demonstrates manual positional radix evaluation:
    sum(digit_val * 16^position)
    """
    cleaned = hex_str.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    
    hex_map = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15
    }
    
    total = 0
    length = len(cleaned)
    for idx, char in enumerate(cleaned):
        power = length - 1 - idx
        val = hex_map[char]
        total += val * (16 ** power)
    return total

def solve():
    challenge_input = "0x3D"
    
    # 1. Manual positional radix calculation: (3 * 16^1) + (13 * 16^0)
    manual_result = hex_to_dec_manual(challenge_input)
    
    # 2. Python standard conversion
    builtin_result = int(challenge_input, 16)
    
    assert manual_result == builtin_result == 61, f"Mismatch: {manual_result} != {builtin_result}"
    
    flag = str(manual_result)
    print(f"[*] Input: {challenge_input} (Base 16)")
    print(f"[*] Manual calculation: (3 * 16^1) + (13 * 16^0) = 48 + 13 = {manual_result}")
    print(f"[*] Python int(0x3D, 16): {builtin_result}")
    print(f"[+] Flag recovered: {flag}")

if __name__ == "__main__":
    solve()
