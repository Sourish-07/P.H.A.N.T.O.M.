import matplotlib.pyplot as plt

schemes = {
    "ToyLWE": {"keysize": 256, "runtime": 0.01, "memory": 1},
    "NTRU": {"keysize": 1024, "runtime": 0.005, "memory": 2},
    "KyberLite": {"keysize": 800, "runtime": 0.007, "memory": 1.5},
    "DilithiumLite": {"keysize": 2000, "runtime": 0.02, "memory": 5},
    "RSA-2048": {"keysize": 2048, "runtime": 0.1, "memory": 10},
}

# Trade-off chart
x = [schemes[s]["keysize"] for s in schemes]
y = [schemes[s]["runtime"] for s in schemes]
labels = list(schemes.keys())

plt.scatter(x, y)
for i, lbl in enumerate(labels):
    plt.annotate(lbl, (x[i], y[i]))
plt.xlabel("Key size (bits)")
plt.ylabel("Runtime (s)")
plt.title("Security Trade-offs (Toy Data)")
plt.show()
