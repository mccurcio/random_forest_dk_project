#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:14:35 2017

@author: mcc
"""

# Modules/Dependencies
#############################
from itertools import groupby
import os
import sys

# Intial constants
#############################
AMINO_ACIDS = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
               'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

HEMEFILES = ['erythrocruorin.fasta',
             'hemerythrin.fasta',
             'hemocyanin.fasta',
             'hemoglobin.fasta',
             'leghemoglobin.fasta',
             'myoglobin.fasta']

NONHEMEFILES = []

WORKINGDIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"


##############################

def fasta_iter(fasta_name):
    """
    given a fasta file. yield tuples of header, sequence
    """
    fh = open(fasta_name)
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        # drop the ">"
        header = header.next()[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in faiter.next())
        yield header, seq



os.chdir(WORKINGDIR)

prot_id, prot_seq = fasta_iter("erythrocruorin.fasta")



print(">> Done!")
sys.exit("some error message")
