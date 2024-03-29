# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import circle_ci_python_sdk
from circle_ci_python_sdk.paths.insights_pages_project_slug_summary import get
from circle_ci_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestInsightsPagesProjectSlugSummary(ApiTestMixin, unittest.TestCase):
    """
    InsightsPagesProjectSlugSummary unit test stubs
        Get summary metrics and trends for a project across it's workflows and branches
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
