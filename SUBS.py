def find_motif(s, t):
    positions = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            positions.append(i + 1)
    return positions

if __name__ == "__main__":
    s = "TCTTCTGCTCGCTGCGCTGCGT"
    t = "GCT"
    positions = find_motif(s, t)
    print(" ".join(map(str, positions)))