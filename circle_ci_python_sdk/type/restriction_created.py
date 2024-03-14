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


class RequiredRestrictionCreated(TypedDict):
    pass

class OptionalRestrictionCreated(TypedDict, total=False):
    # UUID of the project restriction
    id: str

    # Deprecated - For \"project\" restrictions read the project ID from \"restriction_value\" instead.  UUID of the project used in a project restriction. 
    project_id: str

    # Contains a human-readable reference for the restriction. For \"project\" restrictions this is the name of the project.  May be null. 
    name: str

    # Type of the restriction
    restriction_type: str

    # Value used to evaluate the restriction
    restriction_value: str

class RestrictionCreated(RequiredRestrictionCreated, OptionalRestrictionCreated):
    pass