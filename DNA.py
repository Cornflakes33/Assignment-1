def count_nucleotides(dna):
    return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')

if __name__ == "__main__":
    dna = "ATGCGTAGCTAGCTAGCTAGCTAGCTA"
    counts = count_nucleotides(dna)
    print(" ".join(map(str, counts)))