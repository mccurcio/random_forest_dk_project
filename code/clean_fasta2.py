#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:57:52 2017

@author: mcc
"""

dir_path = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"

heme_files =  ("uniprot-erythrocruorin.fasta",
               "uniprot-hemerythrin.fasta",
               "uniprot-hemocyanin.fasta",
               "uniprot-hemoglobin.fasta",
               "uniprot-erythrocruorin.fasta",
               "uniprot-leghemoglobin.fasta",
               "uniprot-myoglobin.fasta")

number_of_files = len(heme_files)

print(dir_path)

def read_write_protein_files(dir_path, heme_files):
    """
    function reads multi-fasta files.
    func concatenates the multi-fasta by removing "\n" and placing
    header and sequence as dictionary key-value pair.
    Then returns one .txt file.
    It requires a directory path and list of files that it is to read.
    """
    for i in number_of_files:
#        seqs = {}
        input_files = (dir_path + heme_files[i])
        f = open(input_files)
        count = 0
#        output_file = (dir_path + heme_files[i] + ".txt")
#        g = open(output_file, "x")
        with open(input_files) as f:
            for line in f:
                if line.startswith('>'):
                    name = line[1:].rstrip('\n')
                    count = count + 1
                    seqs =[]
                else: # sequence, not header
                    seqs[name] = seqs[name] + line
#                    sequences += line[:-1]
#                    output_file = open("out_" + str(count) + "_.txt", "a")
#                    output_file.write(str(len(sequences)))
    print("Number of proteins read:" + count)
    f.close
    
if __name__ == '__main__':
    read_write_protein_files(dir_path, heme_files)
    