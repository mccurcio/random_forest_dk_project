#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:12:54 2017

@author: mcc
"""

dir_path = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"

heme_files = ["uniprot-erythrocruorin.fasta",
              "uniprot-hemerythrin.fasta",
              "uniprot-hemocyanin.fasta",
              "uniprot-hemoglobin.fasta",
              "uniprot-leghemoglobin.fasta",
              "uniprot-myoglobin.fasta"]

number_of_files = len(heme_files)
print("Number of Files:", number_of_files)

#import time

for i in range(0, number_of_files):
    input_files = (dir_path + heme_files[i])
    print(i, "\b:", heme_files[i])
    try:
        f = open(input_files)
    except IOError:
        print("BREAK: Mis-spelling in files or dir_path")
        break
    
    proteins = {}
    name_tag = [] # open list for name_tags
    seqs = [] # open list for name_tags
    
    for line in f: 
        line = line.rstrip("\n") # Discard (\n) at end, if any
        if line.startswith('>'): # distinguish header from sequence
            name_tag = line[4:]
            print("i =", i, ", line =", name_tag)
#            time.sleep(1) # delays for 1 second
        else:  # sequence, not header
            print("i =", i, ", line =", line)
            line = line + line
#            time.sleep(1) # delays for 1 second
        proteins[name_tag] = line
    print("Added to dictionary")
#        time.sleep(1) # delays for 1 second    


# Write proteins dictionary to a csv file 
# with one line for every key value

#path = dir_path + "erythrocruorin.txt"
#outfile = open(path, 'w')
#for key, value in sorted(proteins.items()):
#    outfile.write(str(key) + ',' + str(value) + '\n')