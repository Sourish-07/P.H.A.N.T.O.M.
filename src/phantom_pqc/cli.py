import argparse
from src.toy_lwe import ToyLWE

def main():
    parser = argparse.ArgumentParser(description="PHANTOM PQC CLI")
    parser.add_argument("mode", choices=["keygen","encrypt","decrypt"])
    parser.add_argument("--msg", type=int, help="Message to encrypt (0/1)")
    args = parser.parse_args()

    lwe = ToyLWE()
    pk, sk = lwe.keygen()

    if args.mode == "keygen":
        print("Public Key:", pk)
        print("Secret Key:", sk)
    elif args.mode == "encrypt":
        ct = lwe.encrypt(args.msg, pk)
        print("Ciphertext:", ct)
    elif args.mode == "decrypt":
        print("Provide ciphertext in code for now.")

if __name__ == "__main__":
    main()
