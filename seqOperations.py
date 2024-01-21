#!/usr/bin/python

############################################## About Author #########################################
# Created by: Alsamman M. Alsamman                                                                  #
# Emails: smahmoud [at] ageri.sci.eg or A.Alsamman [at] cgiar.org or SammanMohammed [at] gmail.com  #
# License: MIT License - https://opensource.org/licenses/MIT                                        #
# Disclaimer: The script comes with no warranty, use at your own risk                               #
# This script is not intended for commercial use                                                    #
#####################################################################################################

import sys
import re
 
def readFasta(filename):
    fastaData = open(filename, 'r')
    seqDict = {}
    header = ""
    for line in fastaData:
        line = line.rstrip()
        if line.startswith(">"):
            header = line
            seqDict[header] = ""
        else:
            seqDict[header] = seqDict[header] + line.strip()
    fastaData.close()
    return seqDict

def getFastaLen(filename = "", fastaDict={}):
    if filename != "":
        fastaDict = readFasta(filename)
    elif fastaDict == {}: # if both filename and fastaDict are empty
        print("Please provide either a filename or a fasta dictionary")
        return None
    SeqLenDict = {}
    for header in fastaDict:
        SeqLenDict[header] = len(fastaDict[header])
    return SeqLenDict

def getGCPercent(filename = "", fastaDict={}):
    if filename != "":
        fastaDict = readFasta(filename)
    elif fastaDict == {}: # if both filename and fastaDict are empty
        print("Please provide either a filename or a fasta dictionary")
        return None
    GCPercentDict = {}
    for header in fastaDict:
        seq = fastaDict[header]
        GCPercentDict[header] = (seq.count("G") + seq.count("C")) / len(seq)
    return GCPercentDict

def getStartCodon(filename = "", fastaDict={}):
    if filename != "":
        fastaDict = readFasta(filename)
    elif fastaDict == {}: # if both filename and fastaDict are empty
        print("Please provide either a filename or a fasta dictionary")
        return None
    startCodonDict = {}
    for header in fastaDict:
        seq = fastaDict[header]
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            if codon == "ATG":
                startCodonDict[header] = i
                break
    return startCodonDict

def getSeqCount(filename = "", fastaDict={}):
    fastaDict = {}
    if filename != "":
        fastaDict = readFasta(filename)
    elif fastaDict == {}: # if both filename and fastaDict are empty
        print("Please provide either a filename or a fasta dictionary")
        return None
    return len(fastaDict)

def getAAtable(filename = "", fastaDict={}):
    if filename != "":
        fastaDict = readFasta(filename)
    elif fastaDict == {}: # if both filename and fastaDict are empty
        print("Please provide either a filename or a fasta dictionary")
        return None
    AAtable = {} # Dictionary of Dictionaries
    for header in fastaDict:
        proteinseq = fastaDict[header]
        AAtable[header] = {}
        for i in range(0, len(proteinseq)):
            aa = proteinseq[i]
            if aa not in AAtable[header]:
                AAtable[header][aa] = 0
            AAtable[header][aa] += 1
    return AAtable

            
