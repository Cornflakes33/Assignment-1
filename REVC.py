def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in reversed(dna))

if __name__ == "__main__":
    dna = "CGTACGTAGCTAGTTACGATCGTA"
    revc = reverse_complement(dna)
    print(revc)