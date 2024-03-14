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

from circle_ci_python_sdk.type.bundle_diff_created import BundleDiffCreated
from circle_ci_python_sdk.type.bundle_diff_deleted import BundleDiffDeleted
from circle_ci_python_sdk.type.bundle_diff_modified import BundleDiffModified

class RequiredBundleDiff(TypedDict):
    pass

class OptionalBundleDiff(TypedDict, total=False):
    created: BundleDiffCreated

    deleted: BundleDiffDeleted

    modified: BundleDiffModified

class BundleDiff(RequiredBundleDiff, OptionalBundleDiff):
    pass