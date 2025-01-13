# pip install -U pymupdf4llm

import pymupdf4llm

md_text = pymupdf4llm.to_markdown("/home/harry/Dev/Python/PasswordGenerator/The_Oxford_5000.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())
