#
# testFileIo.py
#
# This file contains the tests for testing file io, specifically the 
# file_io_lib.
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
import file_io_lib

def TEST_STR():
    return "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def FILE_1():
    return "test/testFile.txt"

def FILE_2():
    return "test/testFile2.txt"

def LINES_IN_FILE_2():
    return 6;

def EXPECTED_FILE_LIST():
    return ["Line 1",
            "Line 2",
            "Line 3",
            "",
            "Line 5",
            "Line 6"]

class FileIOTestCase(TestCase):

    def testReadStringFromFile(self):
        self.assertEqual(TEST_STR(), file_io_lib.readStringFromFile(FILE_1()))

    def testBuildListFromFile(self):
        fileList = file_io_lib.readFileToList(FILE_2())

        self.assertEqual(LINES_IN_FILE_2(), len(fileList))
        self.assertEqual(EXPECTED_FILE_LIST(), fileList)

    def testBadFileName(self):
        self.assertRaises(IOError, file_io_lib.readFileToList, "bad_file_name")
