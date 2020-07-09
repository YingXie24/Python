# DnaProcessing.py

The problem domain for this project involves deoxyribonucleic acid (DNA), the double-stranded molecule that encodes genetic information for living organisms.

DNA is made up of four type of nucleotides, adenine (A), guanine (G), cytosine (C), and thymine (T). Each strand of DNA is a sequence of nucleotides, for example AGCTAC.

DNA has 2 strands in a double helix. The nucleotides in one strand are bonded to the nucleotides in the other strand. A and T can be bonded together, and thus complement each other; similarly C and G are complements of each other. The two strand in DNA are complementary because each nucleotide in one strand is bonded with its complement in the other strand. Thus, given the DNA sequence ACGTACG, its complementary strand is TGCATCG.

In **DNAProcessing.py**, several functions were implemented:
* get_length(dna): returns the length of the DNA sequence data
* is_longer(dna1, dna2): returns True if dna1 is longer than dna2
* count_nucleotides(dna, nucleotide): returns the number of occurences of nucleotide in the DNA sequence dna
* contains_sequence(dna1, dna2): returns True if dna2 occurs in dna1
* is_valid_sequence(dna): return True if the dna sequence contains no other characters than 'A', 'T','C','G'
* insert_sequence(dna1, dna2, index): returns the dna sequence obtained by inserting dna2 into dna1 at the given index
* get_complement(nucleotide): return the nucleotide's complement
* get_complementary_sequence(dna): return the DNA sequence that is complementary to the given dna sequence.
