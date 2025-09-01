from setuptools import setup, find_packages

setup(
    name="phantom-pqc",
    version="2.0.0",
    description="Toy Post-Quantum Cryptography Schemes (LWE, NTRU, Kyber-lite, Signatures)",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "scipy",
        "sympy",
        "matplotlib",
    ],
    extras_require={
        "dev": ["pytest", "black"],
    },
    entry_points={
        "console_scripts": [
            "phantom=cli:main",
        ],
    },
    python_requires=">=3.9",
)
