#
# testCouningPointMutations.py
#
# This file contains the tests for the counting nucleotides problem
# at http://rosalind.info/problems/as-table/
# ID: HAMM
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
from dnaStringLibrary import hammingDistance
from dnaStringLibrary import InvalidDnaString
from runHamm import calcNumPointMutations

def TEST_STR_A():
    return "GAGCCTACTAACGGGAT"

def TEST_STR_B():
    return "CATCGTAATGACGGCCT"

def TEST_STR():
    return """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""


def EXPECTED_DISTANCE():
    return 7



class CountingPointMutationsTestCase(TestCase):


    def testHammingDistanceUpperCase(self):
        distance = hammingDistance(TEST_STR_A(), TEST_STR_B())

        self.assertEqual(EXPECTED_DISTANCE(),distance)


    def testDifferentLengthStrings(self):
        testStrC = "ABC"

        self.assertRaises(AssertionError, hammingDistance, TEST_STR_A(), testStrC)


    def testLowerCaseStrings(self):
        distance = hammingDistance(TEST_STR_A().lower(), TEST_STR_B().lower())

        self.assertEqual(EXPECTED_DISTANCE(), distance)

    def testInvalidDnaStrings(self):
        testStrD = "abc"
        testStrE = "abd"

        self.assertRaises(InvalidDnaString, hammingDistance, testStrD, testStrE)

    def testEmptyStrings(self):
        distance = hammingDistance("","")
        self.assertEqual(0,distance)

    def testCalcNumPointMutations(self):
        distance = calcNumPointMutations(TEST_STR())
        self.assertEqual(EXPECTED_DISTANCE(), distance)
