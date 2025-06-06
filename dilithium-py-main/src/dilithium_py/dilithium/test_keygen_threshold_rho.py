import sys
sys.path.append('/home/spdz/Desktop/dilithium-py-main/src')
from dilithium_py.dilithium.dilithium import Dilithium

# Example parameter set for Dilithium2
parameter_set = {
    "d": 13,
    "k": 4,
    "l": 4,
    "eta": 2,
    "tau": 39,
    "omega": 80,
    "gamma_1": (1 << 17),
    "gamma_2": (1 << 19) // 88,
}

dilithium1 = Dilithium(parameter_set)
dilithium2 = Dilithium(parameter_set)

# Step 1: Each party generates a local rho_i
rho1 = dilithium1.generate_local_rho()
rho2 = dilithium2.generate_local_rho()

print("Party 1 rho_i:", rho1.hex())
print("Party 2 rho_i:", rho2.hex())

# Step 2: Combine rho_i to get the global rho
rho_global = Dilithium.combine_rho([rho1, rho2])
print("Global rho:", rho_global.hex())

# Step 3: Each party uses the global rho for keygen
pk1, sk1 = dilithium1.keygen(rho=rho_global)
pk2, sk2 = dilithium2.keygen(rho=rho_global)

print("Party 1 pk:", pk1.hex())
print("Party 2 pk:", pk2.hex())
