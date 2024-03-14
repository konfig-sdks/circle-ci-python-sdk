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

from circle_ci_python_sdk.type.job_get_details_response_contexts import JobGetDetailsResponseContexts
from circle_ci_python_sdk.type.job_get_details_response_executor import JobGetDetailsResponseExecutor
from circle_ci_python_sdk.type.job_get_details_response_latest_workflow import JobGetDetailsResponseLatestWorkflow
from circle_ci_python_sdk.type.job_get_details_response_messages import JobGetDetailsResponseMessages
from circle_ci_python_sdk.type.job_get_details_response_organization import JobGetDetailsResponseOrganization
from circle_ci_python_sdk.type.job_get_details_response_parallel_runs import JobGetDetailsResponseParallelRuns
from circle_ci_python_sdk.type.job_get_details_response_pipeline import JobGetDetailsResponsePipeline
from circle_ci_python_sdk.type.job_get_details_response_project import JobGetDetailsResponseProject

class RequiredJobGetDetailsResponse(TypedDict):
    # URL of the job in CircleCI Web UI.
    web_url: str

    project: JobGetDetailsResponseProject

    parallel_runs: JobGetDetailsResponseParallelRuns

    # The date and time the job started.
    started_at: datetime

    latest_workflow: JobGetDetailsResponseLatestWorkflow

    # The name of the job.
    name: str

    executor: JobGetDetailsResponseExecutor

    # A number of parallel runs the job has.
    parallelism: int

    # The current status of the job.
    status: str

    # The number of the job.
    number: int

    pipeline: JobGetDetailsResponsePipeline

    # Duration of a job in milliseconds.
    duration: typing.Optional[int]

    # The time when the job was created.
    created_at: datetime

    messages: JobGetDetailsResponseMessages

    contexts: JobGetDetailsResponseContexts

    organization: JobGetDetailsResponseOrganization

    # The time when the job was placed in a queue.
    queued_at: datetime

class OptionalJobGetDetailsResponse(TypedDict, total=False):
    # The time when the job stopped.
    stopped_at: typing.Optional[datetime]

class JobGetDetailsResponse(RequiredJobGetDetailsResponse, OptionalJobGetDetailsResponse):
    pass