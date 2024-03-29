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


class RequiredPipelineTriggerNewPipelineResponse(TypedDict):
    # The unique ID of the pipeline.
    id: str

    # The current state of the pipeline.
    state: str

    # The number of the pipeline.
    number: int

    # The date and time the pipeline was created.
    created_at: datetime

class OptionalPipelineTriggerNewPipelineResponse(TypedDict, total=False):
    pass

class PipelineTriggerNewPipelineResponse(RequiredPipelineTriggerNewPipelineResponse, OptionalPipelineTriggerNewPipelineResponse):
    pass
