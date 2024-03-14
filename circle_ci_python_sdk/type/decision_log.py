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

from circle_ci_python_sdk.type.decision import Decision
from circle_ci_python_sdk.type.decision_log_metadata import DecisionLogMetadata
from circle_ci_python_sdk.type.decision_log_policies import DecisionLogPolicies

class RequiredDecisionLog(TypedDict):
    pass

class OptionalDecisionLog(TypedDict, total=False):
    created_at: datetime

    decision: Decision

    id: str

    metadata: DecisionLogMetadata

    policies: DecisionLogPolicies

    time_taken_ms: int

class DecisionLog(RequiredDecisionLog, OptionalDecisionLog):
    pass
