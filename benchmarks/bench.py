import time
from src.toy_lwe import ToyLWE
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import numpy as np

def bench_toy_lwe():
    crypto = ToyLWE(n=4, q=97)
    msg = 1
    start = time.time()
    ct = crypto.encrypt(msg)
    enc_time = time.time() - start

    start = time.time()
    dec = crypto.decrypt(ct)
    dec_time = time.time() - start

    return enc_time, dec_time

def bench_rsa():
    key = RSA.generate(1024)
    cipher = PKCS1_OAEP.new(key)

    msg = b"1"
    start = time.time()
    ct = cipher.encrypt(msg)
    enc_time = time.time() - start

    start = time.time()
    pt = cipher.decrypt(ct)
    dec_time = time.time() - start

    return enc_time, dec_time

if __name__ == "__main__":
    lwe_enc, lwe_dec = bench_toy_lwe()
    rsa_enc, rsa_dec = bench_rsa()

    print("=== Benchmark Results (seconds) ===")
    print(f"LWE  → Encrypt: {lwe_enc:.6f}, Decrypt: {lwe_dec:.6f}")
    print(f"RSA  → Encrypt: {rsa_enc:.6f}, Decrypt: {rsa_dec:.6f}")
