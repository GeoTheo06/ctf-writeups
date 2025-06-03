#!/usr/bin/env python3
import os
import struct

FILENAME = "LICENSE.EXE"

try:
    filesize = os.path.getsize(FILENAME)
except FileNotFoundError:
    print(f"[!] ERROR: '{FILENAME}' not found in this directory.")
    exit(1)

with open(FILENAME, "rb") as f:
    data = f.read(64)
    if data[:2] != b"MZ" or len(data) < 64:
        print("[!] ERROR: Not a valid DOS‐MZ EXE.")
        exit(1)
    size_header_paras = struct.unpack_from("<H", data, 0x08)[0]
    header_size_bytes = size_header_paras * 16

print(f"[+] '{FILENAME}' size             = 0x{filesize:04X} ({filesize} bytes)")
print(f"[+] DOS header's size_of_header = 0x{size_header_paras:04X}")
print(f"[+] → header_size_bytes         = 0x{header_size_bytes:04X} ({header_size_bytes})")
