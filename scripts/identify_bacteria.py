from Bio import SeqIO
from Bio.Blast import NCBIWWW

def analyze_sequences(input_file):
    """Basic sequence analysis for endophyte identification"""
    sequences = list(SeqIO.parse(input_file, "fasta"))
    
    print(f"Found {len(sequences)} sequences")
    
    for seq in sequences:
        print(f"\nAnalyzing {seq.id}")
        print(f"Sequence length: {len(seq.seq)} bp")
        
        # In a real project, you would do BLAST search here
        # result_handle = NCBIWWW.qblast("blastn", "nt", seq.seq)
        # But for beginners, we'll just print the first 20 bases
        print(f"First 20 bases: {seq.seq[:20]}")

if _name_ == "_main_":
    analyze_sequences("../data/sample_sequences.fasta")
added initial project structure
