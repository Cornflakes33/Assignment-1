def count_mrna_protein(protein):
    codon_table = {
        'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4,
        'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2,
        'H': 2, 'Q': 2, 'N': 2, 'K': 2, 'D': 2,
        'E': 2, 'C': 2, 'W': 1, 'R': 6, 'G': 4,
        'Stop': 3
    }
    count = 1
    for amino_acid in protein:
        count *= codon_table[amino_acid]
        count %= 1000000
    count *= codon_table['Stop']
    count %= 1000000
    return count

if __name__ == "__main__":
    protein = "GAV"
    result = count_mrna_protein(protein)
    print(result)