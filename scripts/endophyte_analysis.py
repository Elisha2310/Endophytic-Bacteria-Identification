#!/usr/bin/env python3
"""
Endophytic Bacteria Identification Analysis Script

This script performs basic analysis of 16S rRNA sequences to identify endophytic bacteria.
"""

import os
from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd
import matplotlib.pyplot as plt

def load_sequences(input_file):
    """Load and parse FASTA sequences"""
    print(f"Loading sequences from {input_file}")
    sequences = list(SeqIO.parse(input_file, "fasta"))
    print(f"Successfully loaded {len(sequences)} sequences")
    return sequences

def analyze_sequences(sequences):
    """Perform basic sequence analysis"""
    results = []
    
    for seq in sequences:
        seq_data = {
            'ID': seq.id,
            'Length': len(seq.seq),
            'GC_Content': GC(seq.seq),
            'First_10_bases': str(seq.seq[:10])
        }
        results.append(seq_data)
    
    return pd.DataFrame(results)

def save_results(results_df, output_file):
    """Save analysis results to CSV"""
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

def plot_gc_content(results_df):
    """Create visualization of GC content"""
    plt.figure(figsize=(10, 5))
    results_df['GC_Content'].plot(kind='bar')
    plt.title('GC Content of Endophytic Bacteria Sequences')
    plt.ylabel('GC Content (%)')
    plt.xlabel('Sequence ID')
    plt.tight_layout()
    plt.savefig('results/gc_content.png')
    print("GC content plot saved to results/gc_content.png")

def main():
    # Define file paths
    input_file = os.path.join('data', 'sample_sequences.fasta')
    output_file = os.path.join('results', 'analysis_results.csv')
    
    # Create results directory if it doesn't exist
    os.makedirs('results', exist_ok=True)
    
    # Run the analysis pipeline
    sequences = load_sequences(input_file)
    results_df = analyze_sequences(sequences)
    save_results(results_df, output_file)
    plot_gc_content(results_df)
    
    # Print summary
    print("\nAnalysis Summary:")
    print(results_df.describe())

if _name_ == "_main_":
    main()
