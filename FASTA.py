#!/usr/bin/python

############################################## About Author #########################################
# Created by: Alsamman M. Alsamman                                                                  #
# Emails: smahmoud [at] ageri.sci.eg or A.Alsamman [at] cgiar.org or SammanMohammed [at] gmail.com  #
# License: MIT License - https://opensource.org/licenses/MIT                                        #
# Disclaimer: The script comes with no warranty, use at your own risk                               #
# This script is not intended for commercial use                                                    #
#####################################################################################################

from seqOperations import *

class FASTA:
    def __init__(self,seqFile):
        print("FASTA object created")
        self.seqFile=seqFile
    
    def getSeqs(self):
        return readFasta(self.seqFile)
    
    def getSeqLen(self):
        return getFastaLen(self.seqFile)
    
    def getSummary(self):
        print("FASTA file name: ",self.seqFile)
        print("Number of sequences: ",getSeqCount(self.seqFile))

class Protein(FASTA):
    def __init__(self, seqFile):
        super().__init__(seqFile)
        
    def get_aa_table(self):
        return getAAtable(filename=self.seqFile)