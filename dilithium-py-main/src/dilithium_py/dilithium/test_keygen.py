import sys
sys.path.append('/home/spdz/Desktop/dilithium-py-main/src')
from dilithium_py.dilithium.dilithium import Dilithium

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

dil = Dilithium(parameter_set)
pk, sk = dil.keygen()
print("public key(pk):", pk.hex())
print("secret key(sk):", sk.hex())
