# PageRank: Markov Chains & Power Iteration

### Exploring the mathematics behind Google's PageRank algorithm using Python, linear algebra and probability theory.

---

## Overview

How can we mathematically determine the importance of a webpage?

Google's original PageRank algorithm approaches this problem by analysing the structure of links between webpages, rather than simply counting how many links point to each page.

In this project, I implemented a simplified version of PageRank using a network of four webpages.

By modelling web navigation as a **Markov chain**, I used **power iteration** to approximate the stationary probability distribution and investigated how the **damping factor** influences webpage rankings and convergence.

The project combines:

- **Linear Algebra** — matrices, eigenvectors and stationary distributions.
- **Probability Theory** — Markov chains and transition probabilities.
- **Numerical Methods** — power iteration and convergence analysis.
- **Python** — implementing and visualising the algorithm.

The implementation uses NumPy and Matplotlib without relying on a pre-built PageRank function.

---

## 1. Modelling the Network

Consider a network containing four webpages: **A, B, C and D**.

The connections are defined as follows:

- **A** links to B and C with equal probability.
- **B** links to C.
- **C** links to D.
- **D** links back to A.

These connections can be represented using a **transition matrix**, P.

### Transition Matrix

| From / To | A | B | C | D |
|:---:|:---:|:---:|:---:|:---:|
| **A** | 0 | 0.5 | 0.5 | 0 |
| **B** | 0 | 0 | 1 | 0 |
| **C** | 0 | 0 | 0 | 1 |
| **D** | 1 | 0 | 0 | 0 |

Each entry represents the probability of transitioning from one webpage to another.

For example, a visitor on webpage A has:

- A 50% probability of moving to B.
- A 50% probability of moving to C.

Every row sums to 1 because the visitor must move to one of the available destinations.

Therefore, **P is a row-stochastic matrix**.

---

## 2. Mathematical Foundations

### Markov Chains

A Markov chain is a stochastic process in which the probability of the next state depends only on the current state, rather than the entire history of previous states.

In this project:

- Each webpage represents a state.
- Each hyperlink represents a possible transition.
- The transition matrix determines the probability of moving between states.

This allows web navigation to be modelled mathematically.

### The Google Matrix

In reality, a visitor does not always follow an existing hyperlink.

They might instead navigate randomly to another webpage.

To model this behaviour, PageRank introduces a **damping factor**, denoted by `d`.

The Google matrix is defined as:

**G = dP + (1 - d)J/n**

Where:

| Symbol | Meaning |
|:---:|---|
| G | Google matrix |
| P | Original transition matrix |
| d | Damping factor |
| J | Matrix containing only ones |
| n | Number of webpages |

For example, when **d = 0.85**:

- There is an 85% probability of following an existing hyperlink.
- There is a 15% probability of jumping randomly to any webpage.

This random-jump mechanism helps ensure that the algorithm converges towards a unique stationary distribution.

### Power Iteration

Initially, every webpage is assigned an equal probability.

The starting probability vector is:

`p₀ = [0.25, 0.25, 0.25, 0.25]`

The algorithm repeatedly multiplies the current probability vector by the Google matrix:

**pₖ₊₁ = pₖG**

This process is known as **power iteration**.

As the number of iterations increases, the probability distribution approaches a stationary distribution.

A stationary distribution satisfies:

**πG = π**

This means that multiplying the stationary distribution by the Google matrix leaves it unchanged.

### Connection to Eigenvectors

The stationary distribution has an important connection to linear algebra.

The standard eigenvector equation is:

**Av = λv**

Since the stationary distribution satisfies:

**πG = π**

It follows that **π is a left eigenvector of G corresponding to eigenvalue 1**.

The entries of this stationary distribution represent the long-run probabilities of visiting each webpage.

These probabilities become the final **PageRank scores**.

---

## 3. Experimental Investigation

I investigated how changing the damping factor affects both the final PageRank scores and the rate of convergence.

Four damping factors were tested:

**0.50, 0.85, 0.95 and 0.99**

For each damping factor, the program:

1. Constructs the corresponding Google matrix.
2. Initialises a uniform probability distribution.
3. Repeatedly multiplies the probability vector by the Google matrix.
4. Calculates the maximum absolute change between consecutive iterations.
5. Stops when this change falls below the convergence tolerance.
6. Records the final PageRank scores and iteration count.
7. Plots the convergence behaviour.

### Convergence Criterion

The convergence tolerance is set to:

**10⁻⁸ = 0.00000001**

The program stops when the maximum absolute difference between consecutive probability vectors falls below this threshold.

A maximum of 1,000 iterations is also imposed to prevent an indefinite loop.

---

## 4. Results

The following results were obtained using the four-page network.

### PageRank Scores

| Damping Factor | Page A | Page B | Page C | Page D |
|:---:|---:|---:|---:|---:|
| **0.50** | 25.8621% | 18.9655% | 28.4483% | 26.7241% |
| **0.85** | 27.6659% | 15.5080% | 28.6898% | 28.1363% |
| **0.95** | 28.2663% | 14.6765% | 28.6191% | 28.4382% |
| **0.99** | 28.5102% | 14.3626% | 28.5815% | 28.5457% |

### Convergence Results

| Damping Factor | Iterations Required | Highest-Ranked Page |
|:---:|---:|:---:|
| 0.50 | 21 | C |
| 0.85 | 57 | C |
| 0.95 | 92 | C |
| 0.99 | 119 | C |

### Key Observations

#### 1. Page C consistently achieves the highest PageRank.

Page C receives incoming links from both A and B.

Its position within the network gives it the highest long-run visiting probability across all four experiments.

This illustrates how PageRank depends on the structure of incoming links and the importance of the pages providing them.

#### 2. The damping factor influences the probability distribution.

Increasing the damping factor places greater emphasis on the original hyperlink structure rather than random navigation.

Although the numerical PageRank scores change, the ranking order remains the same throughout this experiment:

**C > D > A > B**

#### 3. Higher damping factors result in slower convergence for this network.

The number of iterations increases significantly as the damping factor approaches 1.

At d = 0.50, convergence requires just **21 iterations**.

At d = 0.99, convergence requires **119 iterations**.

This demonstrates how the choice of damping factor can influence the computational effort required to approximate a stationary distribution.

---

## 5. Convergence Visualisation

The program generates a graph comparing convergence behaviour across the four damping factors.

The graph displays:

- **Horizontal axis:** Iteration number.
- **Vertical axis:** Maximum change in probability.
- **Separate curves:** One for each damping factor.
- **Dashed horizontal line:** The convergence tolerance.

A logarithmic scale is used on the vertical axis to visualise changes across several orders of magnitude.

This makes it easier to compare how quickly the probability distributions approach their stationary values.

---

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Algorithm implementation |
| NumPy | Matrix multiplication and numerical computation |
| Matplotlib | Convergence visualisation |

The PageRank calculation is implemented directly using matrix multiplication rather than a pre-built PageRank function.

---

## 7. Running the Project

### Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the program:

```bash
python pagerank.py
```

The program will:

1. Calculate the PageRank scores for each damping factor.
2. Display the probability distribution as percentages.
3. Identify the highest-ranked webpage.
4. Print the number of iterations required for convergence.
5. Generate a graph comparing convergence behaviour.

---

## 8. Conclusions

This project demonstrates how mathematical concepts can be applied to a computational ranking problem.

In particular, it explores the connections between:

- **Probability theory**, through modelling random navigation.
- **Markov chains**, through transitions between webpages.
- **Linear algebra**, through matrices, eigenvectors and stationary distributions.
- **Numerical methods**, through iterative approximation and convergence analysis.

The most interesting mathematical connection is that the long-run behaviour of a random navigation process can be understood through an **eigenvector equation**.

Although the model contains only four webpages, the underlying mathematical principles extend to much larger networks.

Overall, this investigation helped me understand how probability theory and linear algebra can work together to solve problems in computer science.

---

**Keywords:** PageRank · Markov Chains · Linear Algebra · Eigenvectors · Power Iteration · Stationary Distributions · Python
