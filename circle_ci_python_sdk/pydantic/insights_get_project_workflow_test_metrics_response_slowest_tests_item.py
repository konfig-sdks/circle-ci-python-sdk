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


class InsightsGetProjectWorkflowTestMetricsResponseSlowestTestsItem(BaseModel):
    # The 95th percentile duration, in seconds, among a group of test runs.
    p95_duration: typing.Optional[typing.Union[int, float]] = Field(alias='p95_duration')

    # The total number of times the test was run.
    total_runs: int = Field(alias='total_runs')

    # The class the test belongs to.
    classname: typing.Optional[str] = Field(alias='classname')

    # The number of times the test failed
    failed_runs: int = Field(alias='failed_runs')

    # Whether the test is flaky.
    flaky: bool = Field(alias='flaky')

    # The source of the test.
    source: typing.Optional[str] = Field(alias='source')

    # The file the test belongs to.
    file: typing.Optional[str] = Field(alias='file')

    # The name of the job.
    job_name: str = Field(alias='job_name')

    # The name of the test.
    test_name: str = Field(alias='test_name')
    class Config:
        arbitrary_types_allowed = True
