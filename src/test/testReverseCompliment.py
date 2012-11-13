#
#
# testReverseCompliment.py
#
# This file contains the tests for the Reverse compliment problem
# at http://rosalind.info/problems/as-table/ 
# ID: REVC
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
