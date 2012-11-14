#
# testRnaTranscription.py
#
# This file contains the tests for the RNA transcription problem
# at http://rosalind.info/problems/as-table/ 
# ID: RNA
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
    return "GATGGAACTTGACTACGTAAATT"

def EXPECTED_STR():
    return "GAUGGAACUUGACUACGUAAAUU"

class RnaTranscriptionTestClass(TestCase):


    def testDnaToRnaTranscriptionUpperCase(self):
        transStr = dnaStringLibrary.dnaToRnaTranscription(TEST_STR())

        self.assertEqual(EXPECTED_STR(), transStr)

    def testDnaToRnaTranscriptionLowerCase(self):
        testStr = TEST_STR().lower()
        transStr = dnaStringLibrary.dnaToRnaTranscription(testStr)
        
        self.assertEqual(EXPECTED_STR(), transStr)

    def testDnaToRnaTranscriptionNoneStr(self):
        testStr = 3.1415
        self.assertRaises(dnaStringLibrary.InvalidDnaString, 
                          dnaStringLibrary.dnaToRnaTranscription, 
                          testStr)

    def testDnaToRnaTranscriptionInvalidStr(self):
        testStr = "ACGU"
        self.assertRaises(dnaStringLibrary.InvalidDnaString, 
                          dnaStringLibrary.dnaToRnaTranscription, 
                          testStr)
