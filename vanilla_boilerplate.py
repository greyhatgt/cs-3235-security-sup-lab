#!/usr/bin/env python3
# usage: python3 vanilla_boilerplate.py | ./pwnme

# Distribute this to students as boilerplate

import sys

# Create your bytes data
payload = b''

payload += b'John'   # your payload here! 

payload += b'\n'     # ending newline to terminate gets() read


sys.stdout.buffer.write(payload)
