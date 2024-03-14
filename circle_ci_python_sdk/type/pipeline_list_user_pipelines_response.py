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

from circle_ci_python_sdk.type.pipeline_list_user_pipelines_response_items import PipelineListUserPipelinesResponseItems

class RequiredPipelineListUserPipelinesResponse(TypedDict):
    items: PipelineListUserPipelinesResponseItems

    # A token to pass as a `page-token` query parameter to return the next page of results.
    next_page_token: typing.Optional[str]

class OptionalPipelineListUserPipelinesResponse(TypedDict, total=False):
    pass

class PipelineListUserPipelinesResponse(RequiredPipelineListUserPipelinesResponse, OptionalPipelineListUserPipelinesResponse):
    pass
