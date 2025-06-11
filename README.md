# threshold-dil-test

This project holds the code for the testing phase of threshold dilithium.

## dilithium-py-main
This folder holds the code for the python implementation of dilithium. We can test the functionality of dilithium by executing the following command in ``/tests``:

```
python3.9 test_dilithium.py
```
The relevant code for dilithium is stored in ``/src/dilithium_py/dilithium/dilithium.py``.

The scheme consists three main parts: ``KeyGen, Sign, Verify``:
1. ``KeyGen->(pk, sk)``: generate a bit-packed keypair ``(pk, sk)``.
2. ``Sign(sk, msg)->sig``: generate a bit-packed signature ``sig`` from the message ``msg`` and bit-packed secret key ``sk``.
3. ``Verify(pk, sig, msg)``: verify that the bit-packed ``sig`` is valid for a given message ``msg`` and bit-packed public key ``pk``.


## mp-spdz-0.3.9
This folder holds the spdz code that we used during the implementation phase of the threshold function. The specific functional test code is stored in ``/Programs``.

## Threshold dilithium

Our goal is to develop a threshold dilithium signature scheme that enables the generation and verification of multi-party dilithium signatures.

