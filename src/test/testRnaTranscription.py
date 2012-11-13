#
#
# testRnaTranscription.py
#
# This file contains the tests for the RNA transcription problem
# at http://rosalind.info/problems/as-table/ 
# ID: RNA
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
