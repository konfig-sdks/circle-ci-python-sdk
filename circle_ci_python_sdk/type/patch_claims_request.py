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

from circle_ci_python_sdk.type.json_duration import JSONDuration
from circle_ci_python_sdk.type.patch_claims_request_audience import PatchClaimsRequestAudience

class RequiredPatchClaimsRequest(TypedDict):
    pass

class OptionalPatchClaimsRequest(TypedDict, total=False):
    audience: PatchClaimsRequestAudience

    ttl: JSONDuration

class PatchClaimsRequest(RequiredPatchClaimsRequest, OptionalPatchClaimsRequest):
    pass
