#!/usr/bin/env python3
"""
Daily CTF Challenge Scaffolder
Creates a structured challenge directory, pre-fills the writeup template,
generates a starter solve.py script, and optionally appends a row to the master README.md tracker.
"""

import argparse
import datetime
import os
import re
import sys
from pathlib import Path

# Fix Windows console encoding issues
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

CATEGORY_MAP = {
    "general": "general-skills",
    "general-skills": "general-skills",
    "general_skills": "general-skills",
    "crypto": "cryptography",
    "cryptography": "cryptography",
    "forensics": "forensics",
    "forensic": "forensics",
    "web": "web-exploitation",
    "web-exploitation": "web-exploitation",
    "web_exploitation": "web-exploitation",
    "rev": "reverse-engineering",
    "reversing": "reverse-engineering",
    "reverse-engineering": "reverse-engineering",
    "reverse_engineering": "reverse-engineering",
    "pwn": "binary-exploitation",
    "binary": "binary-exploitation",
    "binary-exploitation": "binary-exploitation",
    "binary_exploitation": "binary-exploitation",
}

VALID_CATEGORIES = sorted(list(set(CATEGORY_MAP.values())))

SOLVE_PY_TEMPLATE = '''#!/usr/bin/env python3
"""
Solution script for {name}
Platform: {platform}
Category: {category}
Date: {date}
"""

# Example imports:
# from pwn import *
# import requests
# from Crypto.Util.number import *

def main():
    print("[*] Running exploit/solver for {name}...")
    # Add your exploit or solver logic here
    flag = "FLAG{{dummy_flag_here}}"
    print(f"[+] Flag recovered: {{flag}}")

if __name__ == "__main__":
    main()
'''


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new CTF daily challenge")
    parser.add_argument("-c", "--category", required=True, help=f"Category: {', '.join(VALID_CATEGORIES)}")
    parser.add_argument("-n", "--name", required=True, help="Challenge name (e.g. 'Mod 26', 'Buffer Overflow 1')")
    parser.add_argument("-p", "--platform", default="picoCTF", help="Platform name (default: picoCTF)")
    parser.add_argument("-d", "--difficulty", default="Easy", help="Difficulty level (Easy / Medium / Hard)")
    parser.add_argument("--points", default="100", help="Challenge points value")
    parser.add_argument("--url", default="", help="Link to challenge")
    parser.add_argument("--test", action="store_true", help="Run self-test without modifying root README")

    args = parser.parse_args()

    cat_key = slugify(args.category)
    if cat_key not in CATEGORY_MAP:
        print(f"[!] Invalid category: '{args.category}'")
        print(f"    Available: {', '.join(VALID_CATEGORIES)}")
        sys.exit(1)

    category_dir = CATEGORY_MAP[cat_key]
    today_str = datetime.date.today().isoformat()
    clean_platform = slugify(args.platform)
    clean_name = slugify(args.name)
    challenge_dir_name = f"{clean_platform}-{clean_name}" if clean_platform else clean_name

    repo_root = Path(__file__).resolve().parent.parent
    target_dir = repo_root / category_dir / challenge_dir_name

    if target_dir.exists():
        print(f"[!] Directory already exists: {target_dir}")
        if not args.test:
            sys.exit(1)

    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "files").mkdir(exist_ok=True)

    # 1. Write solve.py
    solve_file = target_dir / "solve.py"
    if not solve_file.exists():
        solve_content = SOLVE_PY_TEMPLATE.format(
            name=args.name,
            platform=args.platform,
            category=category_dir,
            date=today_str,
        )
        solve_file.write_text(solve_content, encoding="utf-8")
        print(f"[+] Created: {solve_file.relative_to(repo_root)}")

    # 2. Write README.md from template
    template_file = repo_root / "templates" / "challenge-template.md"
    readme_file = target_dir / "README.md"
    if template_file.exists():
        content = template_file.read_text(encoding="utf-8")
        content = content.replace("{{CHALLENGE_NAME}}", args.name)
        content = content.replace("{{PLATFORM}}", args.platform)
        content = content.replace("{{CATEGORY}}", category_dir.replace("-", " ").title())
        content = content.replace("{{DIFFICULTY}}", args.difficulty)
        content = content.replace("{{POINTS}}", str(args.points))
        content = content.replace("{{DATE}}", today_str)
        content = content.replace("{{URL}}", args.url if args.url else "#")
        content = content.replace("{{DESCRIPTION}}", "Enter challenge description here.")
        content = content.replace("{{FILES}}", "none")
        content = content.replace("{{FLAG}}", "FLAG{...}")
        readme_file.write_text(content, encoding="utf-8")
        print(f"[+] Created: {readme_file.relative_to(repo_root)}")
    else:
        print(f"[!] Warning: template not found at {template_file}")

    # 3. Append to master README.md activity table if present
    master_readme = repo_root / "README.md"
    if master_readme.exists() and not args.test:
        master_content = master_readme.read_text(encoding="utf-8")
        marker = "<!-- ACTIVITY_LOG_START -->"
        if marker in master_content:
            rel_link = f"[{args.name}]({category_dir}/{challenge_dir_name}/README.md)"
            new_row = f"| {today_str} | {args.platform} | {rel_link} | {category_dir.replace('-', ' ').title()} | {args.difficulty} | `FLAG{{...}}` |\n"
            parts = master_content.split(marker)
            updated_content = parts[0] + marker + "\n" + new_row + parts[1].lstrip("\n")
            master_readme.write_text(updated_content, encoding="utf-8")
            print(f"[+] Updated Activity Log in master README.md")

    print(f"\n[+] Successfully scaffolded challenge in: {target_dir.relative_to(repo_root)}")
    print(f"    - Writeup: {readme_file.relative_to(repo_root)}")
    print(f"    - Solver:  {solve_file.relative_to(repo_root)}")
    print(f"    - Files:   {target_dir.relative_to(repo_root)}/files/")


if __name__ == "__main__":
    main()
