import os
import random

Q = 4099  

def keygen():
    """Return (sk, pk). For demo, pk == sk so decrypt works."""
    sk = random.randrange(1, Q)
    pk = sk
    return sk, pk

def encrypt(pk, msg: int):
    """Toy: c = (msg + pk) mod Q"""
    return (int(msg) + int(pk)) % Q

def decrypt(sk, ct: int):
    """Toy inverse: msg = (ct - sk) mod Q"""
    return (int(ct) - int(sk)) % Q
