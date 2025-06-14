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
    """Load and parse FASTA sequences
    
    Args:
        input_file (str): Path to input FASTA file
        
    Returns:
        list: List of Bio.SeqRecord objects
    """
    print(f"Loading sequences from {input_file}")
    try:
        sequences = list(SeqIO.parse(input_file, "fasta"))
        if not sequences:
            raise ValueError("No sequences found in the input file")
        print(f"Successfully loaded {len(sequences)} sequences")
        return sequences
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except Exception as e:
        raise Exception(f"Error loading sequences: {str(e)}")

def analyze_sequences(sequences):
    """Perform basic sequence analysis
    
    Args:
        sequences (list): List of Bio.SeqRecord objects
        
    Returns:
        pandas.DataFrame: DataFrame containing sequence analysis results
    """
    results = []
    
    for seq in sequences:
        seq_data = {
            'ID': seq.id,
            'Length': len(seq.seq),
            'GC_Content': GC(seq.seq),
            'First_10_bases': str(seq.seq[:10]),
            'Description': seq.description
        }
        results.append(seq_data)
    
    return pd.DataFrame(results)

def save_results(results_df, output_file):
    """Save analysis results to CSV
    
    Args:
        results_df (pandas.DataFrame): DataFrame containing results
        output_file (str): Path to output CSV file
    """
    try:
        results_df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results: {str(e)}")

def plot_gc_content(results_df):
    """Create visualization of GC content
    
    Args:
        results_df (pandas.DataFrame): DataFrame containing GC content data
    """
    try:
        plt.figure(figsize=(12, 6))
        plt.bar(results_df['ID'], results_df['GC_Content'])
        plt.title('GC Content of Endophytic Bacteria Sequences')
        plt.ylabel('GC Content (%)')
        plt.xlabel('Sequence ID')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Ensure results directory exists
        os.makedirs('results', exist_ok=True)
        
        plot_path = os.path.join('results', 'gc_content.png')
        plt.savefig(plot_path, dpi=300)
        print(f"GC content plot saved to {plot_path}")
        plt.close()
    except Exception as e:
        print(f"Error creating GC content plot: {str(e)}")

def main():
    """Main function to run the analysis pipeline"""
    try:
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
        
        # Additional summary statistics
        print("\nTop 5 sequences by GC content:")
        print(results_df.sort_values('GC_Content', ascending=False).head(5))
        
    except Exception as e:
        print(f"Error in analysis pipeline: {str(e)}")

if __name__ == "__main__":
    main()
