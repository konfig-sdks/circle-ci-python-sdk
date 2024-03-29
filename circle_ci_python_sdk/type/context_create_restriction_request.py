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


class RequiredContextCreateRestrictionRequest(TypedDict):
    pass

class OptionalContextCreateRestrictionRequest(TypedDict, total=False):
    # Deprecated - Use \"restriction_type\" and \"restriction_value\" instead.  The project ID to use for a project restriction. This is mutually exclusive with restriction_type and restriction_value and implies restriction_type is \"project\". 
    project_id: str

    restriction_type: str

    restriction_value: str

class ContextCreateRestrictionRequest(RequiredContextCreateRestrictionRequest, OptionalContextCreateRestrictionRequest):
    pass
