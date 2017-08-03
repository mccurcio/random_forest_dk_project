#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:09:30 2017

@author: mcc
"""

import Bio.SeqIO
# from Bio.SeqIO.FastaIO import FastaIterator

def fasta_reader(filename):
    """
    """
    with open(filename) as handle:
        for record in FastaIterator(handle):
            yield record

DIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"
FILE = "erythrocruorin.fasta"
INPUT_FILE = DIR + FILE


for entry in fasta_reader(INPUT_FILE):
    print(entry.id) #This is header of fasta entry
    print(entry.seq) #This is sequence of specific fasta entry