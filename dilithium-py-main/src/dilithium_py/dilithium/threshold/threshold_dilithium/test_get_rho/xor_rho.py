import os
import sys
import time

try:
    from functools import reduce
except ImportError:
    pass  # Python 2 compatibility

if len(sys.argv) != 2:
    print("Usage: python xor_rho.py <n>")
    exit(1)

n = int(sys.argv[1])
shared_dir = os.path.join(os.path.dirname(__file__), "test_shared_holder")
rho_is = []

# Wait until all rho_i files are available
while True:
    ready = True
    for i in range(1, n+1):
        fpath = os.path.join(shared_dir, "rho_%d.bin" % i)
        if not os.path.exists(fpath):
            ready = False
            break
    if ready:
        break
    print("Waiting for all rho_i files to be present...")
    time.sleep(1)

for i in range(1, n+1):
    file_path = os.path.join(shared_dir, "rho_%d.bin" % i)
    with open(file_path, "rb") as f:
        data = f.read()
        if len(data) != 32:
            print("%s is not 32 bytes!" % file_path)
            exit(1)
        rho_is.append(data)

def xor_bytes(a, b):
    return bytes([ord(x)^ord(y) for x, y in zip(a, b)]) if sys.version_info[0] < 3 else bytes([x^y for x, y in zip(a, b)])

rho = reduce(xor_bytes, rho_is)
rho_hex = rho.encode("hex") if sys.version_info[0] < 3 else rho.hex()
print("XOR result rho (hex): %s" % rho_hex)

# Optional: save to file
with open(os.path.join(shared_dir, "rho.bin"), "wb") as f:
    f.write(rho)
