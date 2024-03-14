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


class InsightsGetProjectSummaryMetricsResponseProjectDataMetrics(BaseModel):
    # The total number of runs, including runs that are still on-hold or running.
    total_runs: int = Field(alias='total_runs')

    # Total duration, in seconds.
    total_duration_secs: int = Field(alias='total_duration_secs')

    # The total credits consumed over the current timeseries interval.
    total_credits_used: int = Field(alias='total_credits_used')

    success_rate: typing.Union[int, float] = Field(alias='success_rate')

    # The average number of runs per day.
    throughput: typing.Union[int, float] = Field(alias='throughput')
    class Config:
        arbitrary_types_allowed = True