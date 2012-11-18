#
# runDna.py
#
# Script that runs solution to PERM problem
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

# This problem is about basic combinitorics, so there is no need to update the
# dnaStringLibrary.  Python has math.factorial, and itertools.permutations to
# solve this problem

import math
import itertools
import StringIO

def calcNumPermutations(n):
    return math.factorial(n)

def generatePermutations(n):
    perms = []
    for p in itertools.permutations(range(1,n+1)):
        perms.append(p)

    return perms

def enumerateGeneOrders(n):
    retVal = StringIO.StringIO()
    retVal.write("{0}\n".format(calcNumPermutations(n)))

    for p in generatePermutations(n):
        line = StringIO.StringIO()
        for val in p:
            line.write("{0} ".format(val))
        retVal.write(line.getvalue().strip())
        retVal.write("\n")

    return retVal.getvalue().strip()


def main():
    value = int(raw_input("Please enter the length n: "))
    
    print(enumerateGeneOrders(value))
    
if __name__ == "__main__":
    main()

