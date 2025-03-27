import subprocess

# Create your bytes data
payload = b''

payload += b'John\n'

# Run the command and pass bytes as input
result = subprocess.run(
    ["./vuln"],  # Command
    input=payload,                 # Bytes input
    capture_output=True                # Capture stdout and stderr
)

# Access the output
print('Output:', result.stdout)
print('Return Code:', result.returncode)

