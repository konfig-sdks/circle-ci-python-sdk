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
from circle_ci_python_sdk.paths.owner_owner_id_context_context_decision_decision_id_policy_bundle import get
from circle_ci_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOwnerOwnerIDContextContextDecisionDecisionIDPolicyBundle(ApiTestMixin, unittest.TestCase):
    """
    OwnerOwnerIDContextContextDecisionDecisionIDPolicyBundle unit test stubs
        Retrieves Policy Bundle for a given decision log ID
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
