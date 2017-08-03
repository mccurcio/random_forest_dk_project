#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:12:54 2017

@author: mcc
"""

# Modules/Dependencies
#############################
#import time
#import errno
import os
#############################


HEMEFILES = ["uniprot-erythrocruorin.fasta",
             "uniprot-hemerythrin.fasta",
             "uniprot-hemocyanin.fasta",
             "uniprot-hemoglobin.fasta",
             "uniprot-leghemoglobin.fasta",
             "uniprot-myoglobin.fasta"]





os.chdir(OUTPUTDIR)

#print("Number of Files:", number_of_files)

############################
# Clean files
############################

def clean_files(WORKINGDIR, HEMEFILES):
    """
    Takes a string variable, WORKINGDIR and
    a list of .fasta files then pulls out only 
    the fasta id and the combined seq.
    """
    input_file = (WORKINGDIR + HEMEFILES)
    number_files = len(HEMEFILES)
    # Loop to read files
    for i in range(0, number_files):
        print(i, "\b:", HEMEFILES[i])
        try:
            f = open(input_file)
        except IOError:
            print("BREAK: Mis-spelling in file or dir_path")
            break
        proteins = {} # dictionary for proteins
        name_tag = [] # open list for name_tags
    
        for line in f:
            line = line.rstrip("\n") # discard (\n) at end
            if line.startswith('>'): # find header
                name_tag = line[4:]  # cut off first 5
                print("i =", i, ", line =", name_tag)
            else:  # sequence, not header
                print("i =", i, ", line =", line)
                line = line + line
        proteins[name_tag] = line
    print("Added to dictionary")
    return(proteins, name_tag)






# Write proteins dictionary to a csv file 
# with one line for every key value



path = WORKINGDIR + "total.txt"
outfile = open(path, 'w')
pe1 = "PE=1"
pe2 = "PE=2"
for key, value in sorted(proteins.items()):
    if pe1 in str(key) or pe2 in str(key):
        if "Fragment" in str(key):
            outfile.write(str(key) + ',' + str(value) + '\n')
    else:
        pass
