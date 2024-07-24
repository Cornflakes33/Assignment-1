def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

if __name__ == "__main__":
    s = "AGCTTAGCTAGCTACGTA"
    t = "AGCTTAGCTAGCTACGTG"
    distance = hamming_distance(s, t)
    print(distance)