def transition_transversion_ratio(seq1, seq2):
    transitions = transversions = 0
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}
    
    for a, b in zip(seq1, seq2):
        if a != b:
            if (a in purines and b in purines) or (a in pyrimidines and b in pyrimidines):
                transitions += 1
            else:
                transversions += 1
    return transitions / transversions

if __name__ == "__main__":
    seq1 = "GCAAGACG"
    seq2 = "GGAAGACA"
    result = transition_transversion_ratio(seq1, seq2)
    print(f"{result:.11f}")