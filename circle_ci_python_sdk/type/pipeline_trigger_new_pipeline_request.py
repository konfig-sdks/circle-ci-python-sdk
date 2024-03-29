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

from circle_ci_python_sdk.type.pipeline_trigger_new_pipeline_request_parameters import PipelineTriggerNewPipelineRequestParameters

class RequiredPipelineTriggerNewPipelineRequest(TypedDict):
    pass

class OptionalPipelineTriggerNewPipelineRequest(TypedDict, total=False):
    parameters: PipelineTriggerNewPipelineRequestParameters

    # The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).
    branch: str

    # The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.
    tag: str

class PipelineTriggerNewPipelineRequest(RequiredPipelineTriggerNewPipelineRequest, OptionalPipelineTriggerNewPipelineRequest):
    pass
