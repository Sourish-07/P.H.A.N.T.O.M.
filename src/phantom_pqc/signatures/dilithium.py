import os
import hashlib

def keygen():
    """
    Toy keygen: return (sk, pk) where pk == sk for simplicity.
    """
    sk = os.urandom(32)
    pk = sk
    return sk, pk

def sign(sk: bytes, msg: bytes) -> bytes:
    """
    Toy signature = H(sk || msg).
    """
    return hashlib.sha256(sk + msg).digest()

def verify(pk: bytes, msg: bytes, sig: bytes) -> bool:
    """
    Verify by recomputing H(pk || msg).
    Since pk == sk in this toy scheme, this matches sign().
    """
    expect = hashlib.sha256(pk + msg).digest()
    return expect == sig
