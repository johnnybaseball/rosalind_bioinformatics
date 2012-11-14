#
# testReverseCompliment.py
#
# This file contains the tests for the Reverse compliment problem
# at http://rosalind.info/problems/as-table/ 
# ID: REVC
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
from dnaStringLibrary import dnaReverseCompliment
from dnaStringLibrary import InvalidDnaString

def TEST_STR():
    return "AAAACCCGGT";

def EXPECTED_STR():
    return "ACCGGGTTTT";

class ReverseComplimentTestClass(TestCase):


    def testReverseComplimentUpperCase(self):
        transStr = dnaReverseCompliment(TEST_STR())

        self.assertEqual(EXPECTED_STR(), transStr)

    def testReverseComplimentLowerCase(self):
        testStr = TEST_STR().lower()
        transStr = dnaReverseCompliment(testStr)

        self.assertEqual(EXPECTED_STR(), transStr)

    def testReverseComplimentNoneStr(self):
        testStr = 3.1415
        self.assertRaises(InvalidDnaString, dnaReverseCompliment, testStr)

    def testReverseComplimentInvalidStr(self):
        testStr = "ABC"
        self.assertRaises(InvalidDnaString, dnaReverseCompliment, testStr)

    def testReverseComplimentEmptyStr(self):
        result = dnaReverseCompliment('')
        self.assertEqual('', result)
