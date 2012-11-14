#
# testCountingNucleotides.py
#
# This file contains the tests for the counting nucleotides problem
# at http://rosalind.info/problems/as-table/
# ID: DNA
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
import dnaStringLibrary

def TEST_STR():
    return "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

class CountingNucleotidesTestCase(TestCase):


    def testNucleotideCountUpperCase(self):
        numA,numC,numG,numT = dnaStringLibrary.countBases(TEST_STR())

        self.assertEqual(20,numA)
        self.assertEqual(12,numC)
        self.assertEqual(17,numG)
        self.assertEqual(21,numT)

    def testNucleotideCountLowerCase(self):
        testStr = TEST_STR().lower()

        numA,numC,numG,numT = dnaStringLibrary.countBases(testStr)

        self.assertEqual(20,numA)
        self.assertEqual(12,numC)
        self.assertEqual(17,numG)
        self.assertEqual(21,numT)

    def testGetBaseCountString(self):
        self.assertEqual("20 12 17 21", dnaStringLibrary.getBaseCountString(TEST_STR()))

    def testReadDnaStringFromFile(self):
        strFileName = "test/testFile.txt"

        self.assertEqual(TEST_STR(), dnaStringLibrary.readStringFromFile(strFileName))

    def testNucleotideCountNonString(self):
        testStr = 3.1415

        self.assertRaises(dnaStringLibrary.InvalidDnaString, dnaStringLibrary.countBases, testStr)

    def testNucleotideCountInvalidString(self):
        testStr = "ABC"

        self.assertRaises(dnaStringLibrary.InvalidDnaString, dnaStringLibrary.countBases, testStr)

