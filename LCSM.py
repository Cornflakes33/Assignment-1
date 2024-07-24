def longest_common_substring(sequences):
    substr = ""
    if len(sequences) > 1 and len(sequences[0]) > 0:
        for i in range(len(sequences[0])):
            for j in range(len(sequences[0]) - i + 1):
                if j > len(substr) and all(sequences[0][i:i+j] in x for x in sequences):
                    substr = sequences[0][i:i+j]
    return substr

if __name__ == "__main__":
    sequences = [
        "GATTACA",
        "TAGACCA",
        "ATACA"
    ]
    result = longest_common_substring(sequences)
    print(result)