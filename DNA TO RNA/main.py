# Dna have Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T'), but
# Rna have In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# example: "GCAT"  Rna = "GCAU"
def dna_to_rna(dna):
    rna = []
    for x in dna:
        if x == "T":
            rna.append("U")
        else:
            rna.append(x)

    return "".join(rna)
dna = "GCATTTAT"
answer = dna_to_rna(dna)
print(answer)