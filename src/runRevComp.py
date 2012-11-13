#
# Script that runs solution to RNA problem
#
##############################################################################
import dnaStringLibrary

try:
    dnaStr = dnaStringLibrary.readStringFromFile("../data/rosalind_revc.txt")

    print(dnaStringLibrary.dnaReverseCompliment(dnaStr))

except Exception as e:
    print("Failed to run script: " + repr(e))



