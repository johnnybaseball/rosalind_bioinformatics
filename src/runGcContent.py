#
# runGcContent.py
#
# This file contains the code to solve the GC Content (label GC) problem on
# the Rosalind website:
# http://rosalind.info/problems/as-table/
#
# This code is distributed under the FreeBSD License
#
# Copyright (c) 2012, John Secord
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
##############################################################################

from dnaStringLibrary import readStringFromFile 
from dnaStringLibrary import calcGcContent
from dnaStringLibrary import parseFastaString
from dnaStringLibrary import InvalidFastaString
from dnaStringLibrary import InvalidDnaString

def calcMaxGc(fastaStr):
    """Given a FASTA string, find the label with the greatest GC content"""

    strandMap = parseFastaString(fastaStr)

    maxGcVal = -1
    maxLabel = None
    for key,val in strandMap.items():
        curGcVal = calcGcContent(val)
        if maxGcVal < curGcVal:
            maxGcVal = curGcVal
            maxLabel = key

    return "{0}\n{1:0.6f}%".format(maxLabel, maxGcVal*100)
    

def main():
    testStr = readStringFromFile("../data/gc.txt")
    
    print(calcMaxGc(testStr))
    
if __name__ == "__main__":
    main()

