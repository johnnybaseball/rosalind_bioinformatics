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

class InvalidDnaString(Exception):
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
