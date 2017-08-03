#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:13:20 2017

@author: mcc
"""

# Depnedencies and Modules
#############################
#from itertools import groupby
import os


# Constants
#############################
WORKINGDIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"
HEMEFILES = ['erythrocruorin.fasta',
             'hemerythrin.fasta',
             'hemocyanin.fasta',
             'hemoglobin.fasta',
             'leghemoglobin.fasta',
             'myoglobin.fasta']


# Functions
##############################

def peel_off_prefix(file_name):
    """
    Takes a file name, rsplits off the ".ext" then replaces it with ".fa"
    """
    pf_name = file_name.rsplit('.')
    fa_file_name = pf_name[0] + ".fa"
    return fa_file_name

print(peel_off_prefix('erythrocruorin.fasta'))


def read_fasta_pe12(file_name):
    """
    This code looks for (PE=1 and PE=2) in FASTA files.
    If (PE=1 or PE=2) is found then it writes to file.
    (PE=1 and PE=2) represents protein existence,
    See: http://www.uniprot.org/help/fasta-headers

    """
    try: # test for file
        ifh = open(file_name)
    except IOError:
        print("FILE DOES NOT EXIST")

    output_file_name = peel_off_prefix(file_name) # Name output file
    ofh = open(output_file_name, "w")

    seq_id = ""
    seq = ""

    for line in ifh:
        line = line.rstrip() # discard the newline at the end
        if line[0] == ">":
            ofh.write("\n")
            if line in ("PE=1", "PE=2"):
                ofh.write(seq_id)
                ofh.write("\n")
                seq = ""
        else: # sequence, not header
            ofh.write(seq)
    file_name.close()


# Main program
###########################
os.chdir(WORKINGDIR)

read_fasta_pe12('erythrocruorin.fasta')
