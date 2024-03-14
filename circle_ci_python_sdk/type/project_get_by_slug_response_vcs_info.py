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


class RequiredProjectGetBySlugResponseVcsInfo(TypedDict):
    # URL to the repository hosting the project's code
    vcs_url: str

    # The VCS provider
    provider: str

    default_branch: str

class OptionalProjectGetBySlugResponseVcsInfo(TypedDict, total=False):
    pass

class ProjectGetBySlugResponseVcsInfo(RequiredProjectGetBySlugResponseVcsInfo, OptionalProjectGetBySlugResponseVcsInfo):
    pass