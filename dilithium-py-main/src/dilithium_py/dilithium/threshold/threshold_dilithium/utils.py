# utils.py

"""
Utility functions for the Dilithium implementation.
Includes hash functions, conversions, and other helpers.
"""

try:
    from xoflib import shake256
except ImportError:
    from .shake.shake_wrapper import shake256

def hash_shake256(data: bytes, length: int) -> bytes:
    """
    Hash the input data using SHAKE256, returning the desired number of bytes.
    """
    return shake256(data).read(length)

# Add other utility functions as needed
