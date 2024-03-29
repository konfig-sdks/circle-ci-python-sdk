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
from pydantic import BaseModel, Field, RootModel

from circle_ci_python_sdk.pydantic.workflow_rerun_workflow_request_jobs import WorkflowRerunWorkflowRequestJobs

class WorkflowRerunWorkflowRequest(BaseModel):
    # Whether to enable SSH access for the triggering user on the newly-rerun job. Requires the jobs parameter to be used and so is mutually exclusive with the from_failed parameter.
    enable_ssh: typing.Optional[bool] = Field(None, alias='enable_ssh')

    # Whether to rerun the workflow from the failed job. Mutually exclusive with the jobs parameter.
    from_failed: typing.Optional[bool] = Field(None, alias='from_failed')

    jobs: typing.Optional[WorkflowRerunWorkflowRequestJobs] = Field(None, alias='jobs')

    # Completes rerun using sparse trees logic, an optimization for workflows that have disconnected subgraphs. Requires jobs parameter and so is mutually exclusive with the from_failed parameter.
    sparse_tree: typing.Optional[bool] = Field(None, alias='sparse_tree')
    class Config:
        arbitrary_types_allowed = True
