# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from circle_ci_python_sdk import CircleCi

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        circleci = CircleCi(
        
                        api_key_header = 'YOUR_API_KEY',
        
                        api_key_query = 'YOUR_API_KEY',
        
            username = 'YOUR_USERNAME',
            password = 'YOUR_PASSWORD'
        )
        self.assertIsNotNone(circleci)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
