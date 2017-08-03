#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:00:52 2017

@author: mcc
""" 
 
 
aa = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

HEMEFILES = ['uniprot-erythrocruorin.fasta',
             'uniprot-hemerythrin.fasta',
             'uniprot-hemocyanin.fasta',
             'uniprot-hemoglobin.fasta',
             'uniprot-leghemoglobin.fasta',
             'uniprot-myoglobin.fasta']

NONHEMEFILES = []

WORKINGDIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/uniprot_1/"
OUTPUTDIR = "/home/mcc/Dropbox/git_projects/random_forest_dk_project/clean_proteins/"

# Modules/Dependencies
#############################
#import time
#import errno
import os
#############################

def findpe12(fasta, input_dir, out_dir):
    
    
def convrtfasta(fasta_files, input_dir, output_dir, output_name):
    
    
def create_dipeptides(aa, outputname, output_dir):
    dipeptides = []
    for count1 in enumerate(aa):
        for count2 in enumerate(aa):
            dipeptides.extend(count1 + count2)
    return(dipeptides)        
    
    
def assign_class(protein_class, output_dir)    
    
    
    