# The NCBI is the National Center for Biotechnology Information
#
# File: The first is a strand of DNA and the second
# is the corresponding protein sequence of amino acids translated from this DNA.
#
# Google: NCBI
#
# Nucleotid NM_207618.2

# According to NCBI, what are the first 10 nucleotides of the gene with accession number NM_201917.1?
# taagtacgca
# tacaacaacg
# acatacaacg
# gtaacaacca <- correct
# taaacgtact

inputfile = "../dna2.txt"

f = open(inputfile, 'r')
seq = f.read()

seq = seq.replace("\n", "")
seq = seq.replace("\r", "")

print(seq[40:50])


def translate(seq):
    """
    :param seq: Translate a string containing a nucleotide sequence into a string
     containing the corresponding sequence of amino acids. Nucleotides are
      translated in triplets using the table dictionary; each amino acid
      is encoded with a string of length 1
    :return: protein
    """
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    # print(seq)
    # print(table['CCT'])
    protein = ""
    # Step1: Check that length of sequence is divisble by 3
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i: i + 3]
            protein += table[codon]

            # Step2: Look up each 3-letter string in table and store result

            # Step3: Continue lookups until reaching end of sequence


            # Python Console
            # import os
            # os.chdir('Week3_CaseStudiesPart1/Case1_DNATranslation/3_1_1')
            # os.getcwd()

    return protein


print(translate('GCC'))