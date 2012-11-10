#
#
# testCountingNucleotides.py
#
# This file contains the tests for the counting nucleotides problem
# at http://rosalind.info/problems/as-table/ 
# ID: DNA
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
        
        
