import numpy as np

def consensus_and_profile(sequences):
    profile = np.zeros((4, len(sequences[0])), dtype=int)
    nucleotides = 'ACGT'
    for sequence in sequences:
        for index, nucleotide in enumerate(sequence):
            profile[nucleotides.index(nucleotide), index] += 1

    consensus = ''.join(nucleotides[np.argmax(profile[:, i])] for i in range(profile.shape[1]))
    return consensus, profile

if __name__ == "__main__":
    sequences = [
        "ATCCAGCT",
        "GGGCAACT",
        "ATGGATCT",
        "AAGCAACC",
        "TTGGAACT",
        "ATGCCATT",
        "ATGGCACT"
    ]
    consensus, profile = consensus_and_profile(sequences)
    print(consensus)
    for i, nucleotide in enumerate('ACGT'):
        print(f"{nucleotide}: {' '.join(map(str, profile[i]))}")