# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from circle_ci_python_sdk.type.insights_get_flaky_tests_response_flaky_tests import InsightsGetFlakyTestsResponseFlakyTests

RequiredInsightsGetFlakyTestsResponse = TypedDict("RequiredInsightsGetFlakyTestsResponse", {
    "flaky-tests": InsightsGetFlakyTestsResponseFlakyTests,

    # A count of unique tests that have failed. If your project has N tests that have flaked multiple times each, this will be equal to N.
    "total-flaky-tests": typing.Union[int, float],
    })

OptionalInsightsGetFlakyTestsResponse = TypedDict("OptionalInsightsGetFlakyTestsResponse", {
    }, total=False)

class InsightsGetFlakyTestsResponse(RequiredInsightsGetFlakyTestsResponse, OptionalInsightsGetFlakyTestsResponse):
    pass
