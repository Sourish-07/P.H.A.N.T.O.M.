import time
from src.toy_lwe import ToyLWE
from src.ntru import NTRU
from src.kyber import KyberLite
from src.signatures.dilithium import DilithiumLite

def benchmark():
    print("=== Benchmarking ===")
    
    # LWE
    lwe = ToyLWE(n=32, q=97, sigma=2.0)
    pk, sk = lwe.keygen()
    start = time.time(); ct = lwe.encrypt(1, pk); _ = lwe.decrypt(ct, sk)
    print("ToyLWE time:", time.time()-start)
    
    # NTRU
    ntru = NTRU()
    h = ntru.keygen()
    start = time.time(); ct = ntru.encrypt([1]*ntru.N, h); _ = ntru.decrypt(ct)
    print("NTRU time:", time.time()-start)
    
    # Kyber-lite
    ky = KyberLite()
    pk, sk = ky.keygen()
    start = time.time(); ct = ky.encrypt(1, pk); _ = ky.decrypt(ct, sk)
    print("Kyber-lite time:", time.time()-start)
    
    # Dilithium-lite
    dil = DilithiumLite()
    pk, sk = dil.keygen()
    start = time.time(); sig = dil.sign(sk, b"test"); ok = dil.verify(pk, b"test", sig)
    print("Dilithium-lite sign/verify time:", time.time()-start)

if __name__ == "__main__":
    benchmark()
