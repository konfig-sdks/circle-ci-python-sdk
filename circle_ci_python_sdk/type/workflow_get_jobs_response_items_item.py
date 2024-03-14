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

from circle_ci_python_sdk.type.workflow_get_jobs_response_items_item_dependencies import WorkflowGetJobsResponseItemsItemDependencies

class RequiredWorkflowGetJobsResponseItemsItem(TypedDict):
    dependencies: WorkflowGetJobsResponseItemsItemDependencies

    # The unique ID of the job.
    id: str

    # The date and time the job started.
    started_at: datetime

    # The name of the job.
    name: str

    # The project-slug for the job.
    project_slug: str

    # The current status of the job.
    status: str

    # The type of job.
    type: str

class OptionalWorkflowGetJobsResponseItemsItem(TypedDict, total=False):
    # The unique ID of the user.
    canceled_by: str

    # The number of the job.
    job_number: int

    # The unique ID of the user.
    approved_by: str

    # The time when the job stopped.
    stopped_at: typing.Optional[datetime]

    # The unique ID of the job.
    approval_request_id: str

class WorkflowGetJobsResponseItemsItem(RequiredWorkflowGetJobsResponseItemsItem, OptionalWorkflowGetJobsResponseItemsItem):
    pass