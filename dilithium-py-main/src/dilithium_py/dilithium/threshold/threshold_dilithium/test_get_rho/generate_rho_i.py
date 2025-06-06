import os
import sys

if len(sys.argv) != 2:
    print("Usage: python generate_rho_i.py <party_id>")
    exit(1)

party_id = sys.argv[1]
shared_dir = os.path.join(os.path.dirname(__file__), "test_shared_holder")
if not os.path.exists(shared_dir):
    os.makedirs(shared_dir)

rho_i = os.urandom(32)
file_path = os.path.join(shared_dir, "rho_%s.bin" % party_id)
with open(file_path, "wb") as f:
    f.write(rho_i)

print("Generated rho_%s.bin at: %s" % (party_id, file_path))
