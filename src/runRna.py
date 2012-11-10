#
# Script that runs solution to RNA problem
#
##############################################################################
import dnaStringLibrary

try:
    testStr = dnaStringLibrary.readStringFromFile("../data/rosalind_rna.txt")

    print(dnaStringLibrary.dnaToRnaTranscription(testStr))

except Exception as e:
    print("Failed to run script: " + repr(e))



