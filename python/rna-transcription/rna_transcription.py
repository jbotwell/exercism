def to_rna(dna_strand):
  return "".join(map(transcribe_nucleotide, dna_strand))


def transcribe_nucleotide(n):
  if n == 'A':
    return 'U'
  if n == 'T':
    return 'A'
  if n == 'C':
    return 'G'
  if n == 'G':
    return 'C'
