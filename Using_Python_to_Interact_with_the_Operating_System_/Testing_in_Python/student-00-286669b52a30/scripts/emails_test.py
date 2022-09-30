#!/usr/bin/env python3

import unittest
from emails import *

class EmailsTest(unittest.TestCase):
    """This is a test class to test the find_email function from the emils.py script"""

    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)

    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)

    def test_two_name(self):
      testcase = [None, "Roy","Cooper"]
      expected = "No email address found"
      self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
  unittest.main()
