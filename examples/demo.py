from src.toy_lwe import ToyLWE

def main():
    crypto = ToyLWE(n=4, q=97)

    print("🔑 Key generated (secret hidden).")
    message = 1
    print(f"Original message: {message}")

    ct = crypto.encrypt(message)
    print("📦 Ciphertext:", ct)

    dec = crypto.decrypt(ct)
    print(f"🔓 Decrypted message: {dec}")

if __name__ == "__main__":
    main()