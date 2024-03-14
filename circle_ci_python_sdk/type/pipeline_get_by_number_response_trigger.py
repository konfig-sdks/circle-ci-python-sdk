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

from circle_ci_python_sdk.type.pipeline_get_by_number_response_trigger_actor import PipelineGetByNumberResponseTriggerActor

class RequiredPipelineGetByNumberResponseTrigger(TypedDict):
    # The type of trigger.
    type: str

    # The date and time the trigger was received.
    received_at: datetime

    actor: PipelineGetByNumberResponseTriggerActor

class OptionalPipelineGetByNumberResponseTrigger(TypedDict, total=False):
    pass

class PipelineGetByNumberResponseTrigger(RequiredPipelineGetByNumberResponseTrigger, OptionalPipelineGetByNumberResponseTrigger):
    pass