# P.H.A.N.T.O.M.
**Post-Quantum Hardened Algorithms for Next-Generation Trustworthy Operations in Mathematics**

![CI](https://github.com/Sourish-07/P.H.A.N.T.O.M./actions/workflows/tests.yml/badge.svg)
![Docs](https://img.shields.io/badge/docs-gh--pages-blue)
![PyPI](https://img.shields.io/pypi/v/phantom-pqc.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![DOI](https://img.shields.io/badge/DOI-Zenodo-informational)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue)

---

🔐 **P.H.A.N.T.O.M.** is a research + implementation project on **Post-Quantum Cryptography (PQC)** with a focus on **lattice-based cryptography**.  
It explores the full cycle: **theory → implementation → benchmarking → security analysis.**

---

## 🚀 Goals
- Implement a working lattice-based cryptosystem (toy + real schemes like Kyber/NTRU).  
- Benchmark security & performance against RSA/ECC.  
- Document results in a research-style paper.  
- Publish open-source code + paper for student research journals and arXiv.  

---

## 📂 Repository Structure
src/ → Core cryptographic implementations
examples/ → Demo scripts (Alice/Bob key exchange, encryption)
benchmarks/ → Benchmarking tools (speed, key size, memory)
attacks/ → Attack simulations (basis reduction, brute force)
paper/ → Research write-ups + notebooks

yaml
Copy code

---

## 🔑 Features
- Educational **LWE-based toy encryption** in Python.  
- Full pipeline: key generation → encryption → decryption.  
- Side-by-side comparison with classical crypto (RSA, ECC).  
- Extendable to standardized PQC schemes (Kyber, NTRU, Dilithium).  

---

## 📦 Installation
```bash
git clone https://github.com/Sourish-07/P.H.A.N.T.O.M.
cd P.H.A.N.T.O.M.
pip install -r requirements.txt
🖥️ Example Usage
bash
Copy code
python examples/demo.py
🔄 Encryption Flow (Toy LWE)
lua
Copy code
Alice (Sender)                               Bob (Receiver)
----------------                               ----------------
m ∈ {0,1}                                     secret s ∈ Z_q^n
       │                                              │
       │  sample A ∈ Z_q^n, small error e             │
       ├───────────────────────────────┐              │
       │ compute: b = <A, s> + e + m⋅⌊q/2⌋ (mod q)    │
       │                                │             │
       └──────────── send (A, b) ───────┼─────────────┘
                                        │
                              compute: inner = (b − <A, s>) mod q
                                        │
                    if |inner| < q/4 → decode 0 else decode 1
📖 References
O. Regev, On lattices, learning with errors, random linear codes, and cryptography (2005).

NIST Post-Quantum Cryptography Project — standardization updates and specifications.

CRYSTALS-Kyber: Module-LWE KEM (NIST PQC winner for key encapsulation).

CRYSTALS-Dilithium, Falcon: lattice-based signatures (NIST PQC winners).

📓 Notebooks
paper/notebooks/lwe_intro.ipynb — math + code walkthrough of Toy LWE.

📜 License
This project is licensed under the MIT License.
