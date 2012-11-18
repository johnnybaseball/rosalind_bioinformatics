#
# dnaStringLibrary.py
#
# This file contains a number of functions for manipulating and processing
# DNA string information.  This library is used to solve problems on the
# rosalind website:
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

import os
from os import path
from cStringIO import StringIO

class InvalidDnaString(Exception):
    """A custom exception for when an invalid DNA string is used"""
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidFastaString(Exception):
    """A custom exception for when an invalid DNA string is used"""
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def countBases(dnaStr):
    numA = 0
    numC = 0
    numG = 0
    numT = 0

    try:
        for char in dnaStr.upper():
            if 'A' == char:
                numA = numA + 1
            elif 'C' == char:
                numC = numC + 1
            elif 'G' == char:
                numG = numG + 1
            elif 'T' == char:
                numT = numT + 1
            else:
                raise InvalidDnaString("Bad DNA String: " + dnaStr)
    except AttributeError as e:
        raise InvalidDnaString("Non string error: " + repr(e))

    return numA, numC, numG, numT

def getBaseCountString(dnaStr):
    numA, numC, numG, numT = countBases(dnaStr)

    retVal = "{0} {1} {2} {3}"
    return retVal.format(numA, numC, numG, numT).strip()

def readStringFromFile(fileNameStr):
    if not path.exists(fileNameStr) or not path.isfile(fileNameStr):
        raise TypeError("File name is invalid: " + repr(fileNameStr))

    f = open(fileNameStr)
    retVal = f.read().strip()
    f.close()

    return retVal

def dnaToRnaTranscription(dnaStr):
    try:
        dnaStr = dnaStr.upper()
        if not verifyDnaString(dnaStr):
            raise InvalidDnaString("Invalid dna string, \"{0}\"".format(dnaStr))

        return dnaStr.replace('T','U')

    except AttributeError as e:
        raise InvalidDnaString("Non string error: " + repr(e))

def dnaReverseCompliment(dnaStr):
    compStr = []
    try:
        for char in dnaStr.upper()[::-1]:
            if 'A' == char:
                compStr.append('T')
            elif 'C' == char:
                compStr.append('G')
            elif 'G' == char:
                compStr.append('C')
            elif 'T' == char:
                compStr.append('A')
            else:
                raise InvalidDnaString("Invalid DNA string, \"{0}\"".format(dnaStr))
    except Exception as e:
        raise InvalidDnaString("Invalid DNA string, \"{0}\"".format(dnaStr))

    return ''.join(compStr)

def verifyDnaString(dnaStr):
    retVal = True
    try:
        countBases(dnaStr)
    except InvalidDnaString:
        retVal = False

    return retVal

def parseFastaString(fastaStr):
    """Function that parses a Rosalind FASTA text blob into key, value pairs

    The key is the lable, e.g. Rosalind_6404 and the value would be the dna
    string.  This returns a dictionary with the key, value pairs.
    """
    retVal = {}
    
    try:
        strIo = StringIO(fastaStr)
        tempDnaStrList = []
        label = None
        for line in strIo:
            if '>' == line[0]:
                if label:
                    # Insert the string with the previous label, if None then
                    # there should be no data yet
                    retVal[label] = ''.join(tempDnaStrList).upper()
                
                # Reset the temporary string
                tempDnaStrList = []
                
                # Read the new label
                label = line[1:].strip()
                
            else:
                tempDnaStrList.append(line.strip())
        # Insert last string
        if label:
            retVal[label] = ''.join(tempDnaStrList).upper()
    except Exception as e:
        raise InvalidFastaString("Invalid FASTA string: {0}".format(fastaStr))

    if 0 == len(retVal):
        raise InvalidFastaString("Invalid FASTA string, no labels found: {0}".format(fastaStr))

    return retVal


def calcGcContent(dnaStr):
    if not verifyDnaString(dnaStr):
        raise InvalidDnaString("Invalid DNA string: {0}".format(dnaStr))

    try:
        return sum(base in ['G','C'] for base in dnaStr)/float(len(dnaStr))
    except Exception:
        raise InvalidDnaString("Invalid DNA string: {0}".format(dnaStr))


def hammingDistance(dnaStrA, dnaStrB):
    """Calculatings the Hamming distance

    see http://en.wikipedia.org/wiki/Hamming_distance
    """

    assert(len(dnaStrA) == len(dnaStrB))
    if not verifyDnaString(dnaStrA):
        raise InvalidDnaString("Invalid DNA string: {0}".format(dnaStrA))
    if not verifyDnaString(dnaStrB):
        raise InvalidDnaString("Invalid DNA string: {0}".format(dnaStrB))
    return sum(ch1 != ch2 for ch1, ch2 in zip(dnaStrA, dnaStrB))

