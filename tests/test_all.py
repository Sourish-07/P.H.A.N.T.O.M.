import pytest
from phantom_pqc import toy_lwe, ntru, kyber
from phantom_pqc.toy_lwe import ToyLWE
from phantom_pqc.signatures import dilithium

def test_toylwe_encrypt_decrypt():
    lwe = ToyLWE(n=4, q=17)
    msg = 5
    c = lwe.encrypt(msg)
    decrypted = lwe.decrypt(c)
    assert decrypted == msg

def test_module_imports():
    assert toy_lwe is not None
    assert ntru is not None
    assert kyber is not None

def test_toy_lwe_roundtrip():
    lwe = ToyLWE(n=8, q=97)
    msg = 42
    ct = lwe.encrypt(msg)
    dec = lwe.decrypt(ct)
    assert dec == msg, "Toy LWE encryption/decryption failed"

def test_ntru_exists():
    assert hasattr(ntru, "keygen"), "NTRU missing keygen"
    sk, pk = ntru.keygen()
    msg = 7
    ct = ntru.encrypt(pk, msg)
    dec = ntru.decrypt(sk, ct)
    assert dec == msg

def test_kyber_exists():
    assert hasattr(kyber, "keygen"), "Kyber missing keygen"
    sk, pk = kyber.keygen()
    ct = kyber.encrypt(pk, b"hello")
    dec = kyber.decrypt(sk, ct)
    assert dec == b"hello"

def test_signature_exists():
    sk, pk = dilithium.keygen()
    msg = b"phantom-test"
    sig = dilithium.sign(sk, msg)
    assert dilithium.verify(pk, msg, sig), "Signature verification failed"
