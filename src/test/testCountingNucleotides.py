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

class CountingNucleotidesTestCase(TestCase):

    def testNucleotideCountUpperCase(self):
        testStr = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        
        numA,numC,numG,numT = dnaStringLibrary.countBases(testStr)

        self.assertEqual(20,numA)
        self.assertEqual(12,numC)
        self.assertEqual(17,numG)
        self.assertEqual(21,numT)

    def testNucleotideCountLowerCase(self):
        testStr = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        testStr = testStr.lower()

        numA,numC,numG,numT = dnaStringLibrary.countBases(testStr)

        self.assertEqual(20,numA)
        self.assertEqual(12,numC)
        self.assertEqual(17,numG)
        self.assertEqual(21,numT)
    
    def testNucleotideCountUpperCase(self):
        testStr = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        
        self.assertEqual("20 12 17 21", dnaStringLibrary.getBaseCountString(testStr))

    def testReadDnaStringFromFile(self):
        testStr = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        strFileName = "test/testFile.txt"

        self.assertEqual(testStr, dnaStringLibrary.readStringFromFile(strFileName))

    def testNucleotideCountNonString(self):
        testStr = 3.1415

        self.assertRaises(dnaStringLibrary.InvalidDnaString, dnaStringLibrary.countBases, testStr)