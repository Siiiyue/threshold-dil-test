# randomness.py

"""
This module provides interfaces for randomness,
including system randomness and (optionally) deterministic DRBG.
"""

import os

# By default, use system randomness.
_random_bytes_func = os.urandom

def get_random_bytes(n):
    """
    Return n random bytes.
    """
    return _random_bytes_func(n)

def set_drbg_seed(seed):
    """
    Switch to a deterministic random bit generator (DRBG) seeded with 'seed'.
    This is useful for testing or deterministic operation.
    """
    global _random_bytes_func
    try:
        from .drbg.aes256_ctr_drbg import AES256_CTR_DRBG
        drbg = AES256_CTR_DRBG(seed)
        _random_bytes_func = drbg.random_bytes
    except ImportError as e:
        print(f"Error importing DRBG: {e}")
        raise RuntimeError("Cannot set DRBG seed. Please install required dependencies.")

def reset_to_system_random():
    """
    Restore the randomness source to system randomness.
    """
    global _random_bytes_func
    _random_bytes_func = os.urandom
