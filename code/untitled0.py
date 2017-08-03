#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:43:09 2017
@author: mccurcio
"""

dir_path = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"

heme_files = ("uniprot-erythrocruorin.fasta",
              "uniprot-hemerythrin.fasta",
              "uniprot-hemocyanin.fasta",
              "uniprot-hemoglobin.fasta",
              "uniprot-erythrocruorin.fasta",
              "uniprot-leghemoglobin.fasta",
              "uniprot-myoglobin.fasta")

number_of_files = len(heme_files) - 1
print(number_of_files)

seqs = {}
for i in range(0, number_of_files):
    input_files = (dir_path + heme_files[i])
    
    for line in f:
        # Discard the newline (\n) at the end, if any
        line = line.rstrip("\n") 
        # distinguish header from sequence
        if line.startswith('>'):
            words = line.lstrip('>')
            name = words[0][1:]
            seqs[name] = ""
        else:  # sequence, not header
            seqs[name] = seqs[name] + line
f.close

for j in range(0, number_of_files): 
    print(seqs[j])