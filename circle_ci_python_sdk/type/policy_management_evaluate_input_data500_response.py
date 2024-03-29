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


class RequiredPolicyManagementEvaluateInputData500Response(TypedDict):
    error: str

class OptionalPolicyManagementEvaluateInputData500Response(TypedDict, total=False):
    pass

class PolicyManagementEvaluateInputData500Response(RequiredPolicyManagementEvaluateInputData500Response, OptionalPolicyManagementEvaluateInputData500Response):
    pass
