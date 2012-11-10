#
# Script that runs solution to DNA problem
#
##############################################################################
import dnaStringLibrary

try:
    testStr = dnaStringLibrary.readStringFromFile("../data/rosalind_dna.txt")

    print(dnaStringLibrary.getBaseCountString(testStr))

except Exception as e:
    print("Failed to run script: " + repr(e))

