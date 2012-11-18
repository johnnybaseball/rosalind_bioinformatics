#
# testEnumeratingGeneOrders.py
#
# This file contains the tests for the counting nucleotides problem
# at http://rosalind.info/problems/as-table/
# ID: PERM
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
from runPerm import calcNumPermutations
from runPerm import generatePermutations
from runPerm import enumerateGeneOrders

def EXPECTED_RES():
    return [(1,2,3),
            (1,3,2),
            (2,1,3),
            (2,3,1),
            (3,1,2),
            (3,2,1)]

def EXPECTED_STR():
    return """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1"""

class EnumeratingGeneOrdersTestCase(TestCase):
    
    def testCalcNumPermutations(self):
        self.assertEquals(2, calcNumPermutations(2))
        self.assertEquals(6, calcNumPermutations(3))
        self.assertEquals(24, calcNumPermutations(4))

    def testBuildPermutations(self):
        perms = generatePermutations(3)

        self.assertEquals(6, len(perms))
        for p in perms:
            self.assertTrue(p in EXPECTED_RES())

    def testEnumeratingGeneOrders(self):
        retVal = enumerateGeneOrders(3)

        self.assertEquals(EXPECTED_STR(), retVal)
