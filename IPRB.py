def dominant_allele_probability(k, m, n):
    total = k + m + n
    prob = (k * (k - 1) + 2 * k * m + 2 * k * n + 0.75 * m * (m - 1) + m * n) / (total * (total - 1))
    return prob

if __name__ == "__main__":
    k, m, n = 3, 4, 5
    prob = dominant_allele_probability(k, m, n)
    print(f"{prob:.5f}")