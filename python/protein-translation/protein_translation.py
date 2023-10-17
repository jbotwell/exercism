rna_protein_mappings = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand):
    codons = slice_into_codons(strand)
    amino_acids = []
    for c in codons:
        aa = rna_protein_mappings[c]
        if aa == "STOP":
            break
        else:
            amino_acids.append(aa)
    return amino_acids


def slice_into_codons(strand):
    return [strand[i : i + 3] for i in range(0, len(strand), 3)]
