def dna_to_rna(dna):
    return dna.replace('T', 'U')

if __name__ == "__main__":
    dna = "GATGGAACTTGACTACGTAAATT"
    rna = dna_to_rna(dna)
    print(rna)