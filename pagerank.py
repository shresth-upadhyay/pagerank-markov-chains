
import numpy as np
import matplotlib.pyplot as plt

websites = ["A", "B", "C", "D"]

P = np.array([
    [0, 0.5, 0.5, 0],
    [0, 0,   1,   0],
    [0, 0,   0,   1],
    [1, 0,   0,   0]
])

n = len(websites)

damping_factors = [0.50, 0.85, 0.95, 0.99]

tolerance = 1e-8
max_iterations = 1000

results = {}

for d in damping_factors:
    G = d * P + (1 - d) * np.ones((n, n)) / n

    p = np.ones(n) / n
    changes = []

    for i in range(max_iterations):
        new_p = p @ G

        difference = np.max(np.abs(new_p - p))
        changes.append(difference)

        p = new_p

        if difference < tolerance:
            break

    results[d] = (p.copy(), i + 1, changes)

    print(f"\nDAMPING FACTOR: {d}")
    print("-------------------------")

    for website, probability in zip(websites, p):
        print(f"{website}: {probability * 100:.4f}%")

    print(f"Iterations: {i + 1}")
    print(f"Highest ranked: {websites[np.argmax(p)]}")

for d, (p, iterations, changes) in results.items():
    plt.semilogy(
        range(1, iterations + 1),
        changes,
        label=f"d = {d}"
    )

plt.axhline(
    tolerance,
    color="black",
    linestyle="--",
    label="Tolerance"
)

plt.xlabel("Iteration")
plt.ylabel("Maximum change in probability")
plt.title("PageRank Convergence vs Damping Factor")

plt.legend()
plt.grid(True)
plt.show()

