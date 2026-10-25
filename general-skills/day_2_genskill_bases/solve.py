#!/usr/bin/env python3
"""
Solution script for Day 2: Bases (Base64 Decoding)
Platform: picoCTF
Category: General Skills
Date: 2026-10-25
"""

import base64

def solve():
    encoded_str = "bDNhcm5fdGgzX3IwcDM1"
    
    # Base64 decode to bytes, then decode to ASCII string
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_text = decoded_bytes.decode("utf-8")
    
    flag = f"picoCTF{{{decoded_text}}}"
    
    print(f"[*] Encoded input:   {encoded_str}")
    print(f"[*] Decoded payload: {decoded_text}")
    print(f"[+] Flag recovered:  {flag}")
    
    assert decoded_text == "l3arn_th3_r0p35", f"Unexpected decoded text: {decoded_text}"
    return flag

if __name__ == "__main__":
    solve()
