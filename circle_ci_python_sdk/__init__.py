# coding: utf-8

# flake8: noqa

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

__version__ = "v2"

# import ApiClient
from circle_ci_python_sdk.api_client import ApiClient

# import Configuration
from circle_ci_python_sdk.configuration import Configuration

# import exceptions
from circle_ci_python_sdk.exceptions import OpenApiException
from circle_ci_python_sdk.exceptions import ApiAttributeError
from circle_ci_python_sdk.exceptions import ApiTypeError
from circle_ci_python_sdk.exceptions import ApiValueError
from circle_ci_python_sdk.exceptions import ApiKeyError
from circle_ci_python_sdk.exceptions import ApiException

from circle_ci_python_sdk.client import CircleCi
