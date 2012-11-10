#
# dnaStringLibrary
#
# This file contains a number of functions for manipulating and processing
# DNA string information
#
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
