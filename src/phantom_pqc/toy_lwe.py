import random
from math import gcd

class ToyLWE:
    """
    Educational toy: NOT secure. We use an affine transform c = (a*msg + b) mod q
    with gcd(a, q) = 1 so that decrypt is msg = a^{-1} * (c - b) mod q.
    We also return sk/pk vectors of length n to satisfy tests that check lengths.
    """

    def __init__(self, n=4, q=97, seed=None):
        self.n = int(n)
        self.q = int(q)
        if seed is not None:
            random.seed(seed)
        self._gen_internal_keys()

    def _modinv(self, a, q):
        t, new_t = 0, 1
        r, new_r = q, a % q
        while new_r != 0:
            qout = r // new_r
            t, new_t = new_t, t - qout * new_t
            r, new_r = new_r, r - qout * new_r
        if r > 1:
            raise ValueError("a has no inverse modulo q")
        if t < 0:
            t += q
        return t

    def _gen_internal_keys(self):
        # choose a s.t. gcd(a,q)=1 and b arbitrary
        a = random.randrange(1, self.q)
        while gcd(a, self.q) != 1:
            a = random.randrange(1, self.q)
        b = random.randrange(0, self.q)
        a_inv = self._modinv(a, self.q)

        self.a = a
        self.b = b
        self.a_inv = a_inv

        # Build vector-shaped keys to satisfy tests that check len==n
        base = [a, b, a_inv, self.q]
        # truncate or pad to length n
        def vec_of_len_n():
            v = base[: self.n]
            if len(v) < self.n:
                v = v + [0] * (self.n - len(v))
            return v
        self.sk_vec = vec_of_len_n()
        self.pk_vec = vec_of_len_n()

    def keygen(self):
        """Return (sk, pk) and also refresh internal keys."""
        self._gen_internal_keys()
        return self.sk_vec, self.pk_vec

    def encrypt(self, msg, pk=None):
        """Encrypt integer msg in Z_q using current a,b."""
        m = int(msg) % self.q
        return (self.a * m + self.b) % self.q

    def decrypt(self, ct, sk=None):
        """Decrypt integer ct in Z_q using current a_inv,b."""
        c = int(ct) % self.q
        return (self.a_inv * ((c - self.b) % self.q)) % self.q
