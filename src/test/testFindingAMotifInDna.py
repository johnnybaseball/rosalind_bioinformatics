#
# testFindingAMotifInDna.py
#
# This file contains the tests for the finding a motif in DNA problem
# at http://rosalind.info/problems/as-table/
# ID: SUBS
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
from dnaStringLibrary import findDnaSubstring 
import runSubs

def TEST_STR():
    return "ACGTACGTACGTACGT"

def TEST_MOTIF():
    return "GTA"

def TEST_FILE():
    return "../data/substring.test"

def EXPECTED_RESULT():
    return [3,7,11]

def TEST_STRING_OVERLAP():
    return "GATATATGCATATACTT"

def TEST_MOTIF_OVERLAP():
    return "ATAT"

def EXPECTED_RESULT_OVERLAP():
    return [2,4,10]

def EXPECTED_STRING():
    return "3 7 11"

class FindingAMotifInDnaTestCase(TestCase):


    def testFindingSubstrings(self):
        res = findDnaSubstring(TEST_STR(), TEST_MOTIF())

        self.assertEqual(EXPECTED_RESULT(), res)

    def testFindingOverlappingSubstrings(self):
        res = findDnaSubstring(TEST_STRING_OVERLAP(), TEST_MOTIF_OVERLAP())

        self.assertEqual(EXPECTED_RESULT_OVERLAP(), res)

    def testGeneratingOutput(self):
        self.assertEqual(EXPECTED_STRING(),runSubs.generateOutput(TEST_FILE()))
