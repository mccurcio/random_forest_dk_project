#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:00:52 2017

@author: mcc
"""

# Modules/Dependencies
#############################
#import time
#import errno
#import os
import sys
#############################

# Intial constants
#############################
AMINO_ACIDS = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
               'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

HEMEFILES = ['uniprot-erythrocruorin.fasta',
             'uniprot-hemerythrin.fasta',
             'uniprot-hemocyanin.fasta',
             'uniprot-hemoglobin.fasta',
             'uniprot-leghemoglobin.fasta',
             'uniprot-myoglobin.fasta']

NONHEMEFILES = []

WORKINGDIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/ \
              uniprot_1/"
OUTPUTDIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/ \
             clean_proteins/"

# Functions
#########################
# OK
def peel_off_filename(file_name):
    """
    Takes in "string1.string2" (must have ".") and returns "string1"
    """
    number_periods = file_name.count(".")
    if number_periods != 1:
        print("ERROR: FILENAME HAS TOO MANY PERIODS.")
    else:
        two_names = file_name.split(".")
    return two_names[0]

#protein_class = peel_off_filename("myoglbin.fasta")
#print(protein_class)

##########################
# NG
def findpe12(files, input_dir, out_dir):
    """
    Takes multiple fasta files, concatenates
    then pulls out only PE = 1 & 2 proteins
    Uses two string variables: files, input_dir
    then returns csv file with columns fasta id and the combined seq.
    """
    input_file = (WORKINGDIR + HEMEFILES)
    fasta_id = []
    combined_seq = []

    # Loop to read files
    for i in enumerate(input_file):
        fasta_file = open(input_file[i])
        seqs = {}
        for line in f:
            line = line.rstrip("\n") # discard the newline(\n)
            if line.startswith('>'):
                words=line.split()
                name = words[0][1:]
                seqs[name] = ‘’ # distinguish header from sequence
            else:  # sequence, not header
                seqs[name] = seqs[name] + line
close(input_file[i])

    print("start")

######################
# OK
def create_dipeptides(amio_acids, output_dir):
    """
    Produce a list dipeptides from a list
    input a list of 20 strings
    output a list of 400 strings
    """
    dipeptides = []
    for i in enumerate(amio_acids):
        for j in enumerate(amio_acids):
            dipeptides.append(amio_acids[i] + amio_acids[j])
            #print(i, j, amio_acids[i] + amio_acids[j])
    return dipeptides
# OK
di_peptides = create_dipeptides(AMINO_ACIDS)
print(di_peptides)

##############################
# NG
def count_aa_in_proteins():
    """
    docstring
    """
    print("start")

###############################
# NG
def assign_class(protein_class, output_dir):
    """
    docstring
    """
    print("start")

# NG
# Main program starts here
##########################

print("Main program starts here")

protein_class = peel_off_filename(file_name)







# EOF
sys.exit()