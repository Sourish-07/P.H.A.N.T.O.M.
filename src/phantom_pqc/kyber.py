import hashlib

def _keystream(key_bytes: bytes, length: int) -> bytes:
    """Deterministic keystream by iterating SHA-256(key || counter)."""
    out = b""
    counter = 0
    while len(out) < length:
        h = hashlib.sha256(key_bytes + counter.to_bytes(4, "big")).digest()
        out += h
        counter += 1
    return out[:length]

def keygen():
    """
    Return (sk, pk). For this toy, pk == sk (bytes). The tests just need
    reversible encrypt/decrypt for bytes.
    """
    # Stable 32-byte "key" derived from a fixed string; swap to os.urandom(32)
    sk = hashlib.sha256(b"phantom-kyber-toy-key").digest()
    pk = sk
    return sk, pk

def encrypt(pk: bytes, plaintext: bytes) -> bytes:
    ks = _keystream(pk, len(plaintext))
    return bytes([p ^ k for p, k in zip(plaintext, ks)])

def decrypt(sk: bytes, ciphertext: bytes) -> bytes:
    ks = _keystream(sk, len(ciphertext))
    return bytes([c ^ k for c, k in zip(ciphertext, ks)])
