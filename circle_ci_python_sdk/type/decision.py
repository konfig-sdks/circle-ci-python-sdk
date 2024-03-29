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

from circle_ci_python_sdk.type.decision_enabled_rules import DecisionEnabledRules
from circle_ci_python_sdk.type.violation import Violation

class RequiredDecision(TypedDict):
    status: str

class OptionalDecision(TypedDict, total=False):
    enabled_rules: DecisionEnabledRules

    hard_failures: typing.List[Violation]

    reason: str

    soft_failures: typing.List[Violation]

class Decision(RequiredDecision, OptionalDecision):
    pass
