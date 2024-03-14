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


class InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends(BaseModel):
    # The trend value for total credits consumed.
    total_credits_used: typing.Union[int, float] = Field(alias='total_credits_used')

    # The 95th percentile duration among a group of workflow runs.
    p95_duration_secs: typing.Union[int, float] = Field(alias='p95_duration_secs')

    # The trend value for total number of runs.
    total_runs: typing.Union[int, float] = Field(alias='total_runs')

    # The trend value for the success rate.
    success_rate: typing.Union[int, float] = Field(alias='success_rate')
    class Config:
        arbitrary_types_allowed = True
