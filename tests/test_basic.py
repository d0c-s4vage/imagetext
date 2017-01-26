#!/usr/bin/env python
# encoding: utf-8


"""
Perform basic tests of the imagetext module
"""


import os
import shutil
import sys
import tempfile
import unittest


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


import imagetext


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.tmpd = tempfile.mkdtemp()
        self.tmp_path = os.path.join(self.tmpd, "test.png")
    
    def tearDown(self):
        shutil.rmtree(self.tmpd)
    
    def test_image_create_and_read(self):
        """Ensure that imagetext can perform the basic operations
        of writing text into and reading text from an image.
        """
        test_data = "Hello world"
        imagetext.write(test_data, self.tmp_path)

        with open(self.tmp_path, "rb") as f:
            data = f.read()

        # should start with png magic bytes
        self.assertTrue(data.startswith("\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"))

        data = imagetext.read(self.tmp_path)
        self.assertEqual(data, test_data)
    
    def test_image_create_and_read2(self):
        """Ensure that imagetext can perform the basic operations
        of writing text into and reading text from an image.
        """
        test_data = "Hello world" * 100
        imagetext.write(test_data, self.tmp_path)

        with open(self.tmp_path, "rb") as f:
            data = f.read()

        # should start with png magic bytes
        self.assertTrue(data.startswith("\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"))

        data = imagetext.read(self.tmp_path)
        self.assertEqual(data, test_data)
    

if __name__ == "__main__":
    unittest.main()
