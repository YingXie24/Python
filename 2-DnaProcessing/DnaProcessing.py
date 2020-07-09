def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)

  


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1)>len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotides = 0

    for char in dna:
        if char in nucleotide:
            num_nucleotides = num_nucleotides + 1

    return num_nucleotides      


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str)-> bool

    Return True if and only if the dna sequence is valid. That is, it contains no other characters
    other than 'A', 'T', 'G', 'C'.

    >>>is_valid_sequence('ATCGTCA')
    True
    >>>is_valid_sequence('ABTGT')
    False
    """
        

##    for char in dna:
##        if char in "ATCG":
##            a = 1
##        else:
##            return False
##
##    return True

    
        
    num_invalid_nucleotide = 0

    for char in dna:
        if char not in "ATCG":
            num_invalid_nucleotide = num_invalid_nucleotide + 1

    return num_invalid_nucleotide == 0


def insert_sequence(dna1,dna2,index):

    """(str,str,int)-> str
    
    Return the dna sequence obtained by inserting dna2 into dna1 at the given index.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('CCGG','AT',0)
    'ATCCGG'
    >>>insert_sequence('CCGG','AT',len('CCGG'))
    'CCGGAT'
    """

    new_dna = dna1[:index] + dna2 + dna1[index:]
    return new_dna

def get_complement(nucleotide):

    """ (str)-> str

    Return the nucleotide's complement.
    
    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    'G'
    """

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna):

    """ (str) -> str
    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('TCAG')
    'AGTC'
    """

    complementary_sequence = ''
    
    for char in dna:
        if char in 'ATCG':
            get_complement(char)
            complementary_sequence  = complementary_sequence + get_complement(char)
    return complementary_sequence
        

    
