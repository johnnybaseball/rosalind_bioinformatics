#
# testGcContent.py
#
# This file contains the tests for the GC content problem
# at http://rosalind.info/problems/as-table/
# ID: GC
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

from unittest import TestCase
from math import fabs

import runGcContent
from dnaStringLibrary import parseFastaString
from dnaStringLibrary import InvalidFastaString
from dnaStringLibrary import InvalidDnaString
from dnaStringLibrary import calcGcContent


def TEST_STR():
    return """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

def TEST_GC_STR():
    return "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"    

def EXPECTED_GC_VALUE():
    return 0.60919540

def EXPECTED_LABELS():
    return ["Rosalind_6404",
            "Rosalind_5959",
            "Rosalind_0808"]

def EXPECTED_DNA_STRINGS():
    return ["CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
            "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
            "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"]

def EXPECTED_STR():
    return """Rosalind_0808
60.919540%"""

class ReverseComplimentTestClass(TestCase):



    def testFindFastaLabelsInValidData(self):
        strandMap = parseFastaString(TEST_STR())

        self.assertEqual(3,len(strandMap))
        for key in strandMap:
            self.assertTrue(key in EXPECTED_LABELS())

    def testFindFastaDnaStringsInValidData(self):
        strandMap = parseFastaString(TEST_STR())

        self.assertEqual(3,len(strandMap))
        for key,value in strandMap.items():
            self.assertTrue(value in EXPECTED_DNA_STRINGS())

    def testFindFastaLabelsInNoneStr(self):
        testStr = 3.1415
        self.assertRaises(InvalidFastaString, parseFastaString, testStr)

    def testFindFastaLabelsInEmptyStr(self):
        testStr = ""
        self.assertRaises(InvalidFastaString, parseFastaString, testStr)

    def testFindFastaLabelsInBadStr(self):
        testStr = "ABC"
        self.assertRaises(InvalidFastaString, parseFastaString, testStr)

    def testCalculateGcContent(self):
        gcVal = calcGcContent(TEST_GC_STR())
        self.assertTrue(fabs(gcVal - EXPECTED_GC_VALUE())<0.0001)

    def testCalcGcContentNoneStr(self):
        testStr = 3.1415
        self.assertRaises(InvalidDnaString, calcGcContent, testStr)
    
    def testCalcGcContentBadDnaStr(self):
        testStr = "ABC"
        self.assertRaises(InvalidDnaString, calcGcContent, testStr)

    def testGcConentFromFasta(self):
        retVal = runGcContent.calcMaxGc(TEST_STR())
        self.assertEqual(EXPECTED_STR(), retVal)
