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
from circle_ci_python_sdk.paths.org_org_id_project_project_id_oidc_custom_claims import patch
from circle_ci_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrgOrgIDProjectProjectIDOidcCustomClaims(ApiTestMixin, unittest.TestCase):
    """
    OrgOrgIDProjectProjectIDOidcCustomClaims unit test stubs
        Patch project-level claims
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()