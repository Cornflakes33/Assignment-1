def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return gc_count / len(dna) * 100

if __name__ == "__main__":
    sequences = [
        ">seq1\nCCTGCGGATAGCTGAACTAGCATGGCAGAAT\n",
        ">seq2\nCCATCGGCATCGAGCATAGGCCCTAGC\n",
        ">seq3\nCCACCCTCAGTGTGGTATGGCTAGGCAT"
    ]
    max_gc = 0
    max_id = ""
    for entry in sequences:
        parts = entry.split()
        seq_id = parts[0]
        seq = ''.join(parts[1:])
        gc = gc_content(seq)
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id
    print(max_id)
    print(f"{max_gc:.6f}")