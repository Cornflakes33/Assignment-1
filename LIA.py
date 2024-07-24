def binomial_coefficient(n, k):
    from math import comb
    return comb(n, k)

def probability_of_at_least_k(n, k, p):
    probability = 0
    for i in range(k, n+1):
        probability += binomial_coefficient(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return probability

if __name__ == "__main__":
    k, N = 3, 2
    probability = probability_of_at_least_k(2**k, N, 0.25)
    print(f"{probability:.3f}")