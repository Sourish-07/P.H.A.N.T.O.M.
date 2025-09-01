from phantom_pqc.toy_lwe import ToyLWE

def test_toylwe_small():
    lwe = ToyLWE(n=2, q=11)
    msg = 3
    c = lwe.encrypt(msg)
    decrypted = lwe.decrypt(c)
    assert decrypted == msg

def test_toy_lwe_keygen():
    crypto = ToyLWE(n=4, q=97)
    sk, pk = crypto.keygen()
    assert len(sk) == 4, "Secret key length mismatch"
    assert len(pk) == 4, "Public key length mismatch"

def test_toy_lwe_encryption():
    crypto = ToyLWE(n=4, q=97)
    sk, pk = crypto.keygen()
    msg = 1
    ct = crypto.encrypt(msg)
    dec = crypto.decrypt(ct)
    assert dec == msg, "Toy LWE encryption failed"
