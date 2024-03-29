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

from circle_ci_python_sdk.pydantic.insights_get_workflow_summary_metrics_response_metrics_duration_metrics import InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics

class InsightsGetWorkflowSummaryMetricsResponseMetrics(BaseModel):
    # The total number of runs, including runs that are still on-hold or running.
    total_runs: int = Field(alias='total_runs')

    # The number of successful runs.
    successful_runs: int = Field(alias='successful_runs')

    # The mean time to recovery (mean time between failures and their next success) in seconds.
    mttr: typing.Optional[int] = Field(alias='mttr')

    # The total credits consumed by the workflow in the aggregation window. Note that Insights is not a real time financial reporting tool and should not be used for credit reporting.
    total_credits_used: typing.Optional[int] = Field(alias='total_credits_used')

    # The number of failed runs.
    failed_runs: int = Field(alias='failed_runs')

    success_rate: typing.Union[int, float] = Field(alias='success_rate')

    # The number of runs that ran to completion within the aggregation window
    completed_runs: typing.Optional[int] = Field(alias='completed_runs')

    # The timestamp of the first build within the requested reporting window.
    window_start: datetime = Field(alias='window_start')

    duration_metrics: InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics = Field(alias='duration_metrics')

    # The timestamp of the last build within the requested reporting window.
    window_end: datetime = Field(alias='window_end')

    # The average number of runs per day.
    throughput: typing.Union[int, float] = Field(alias='throughput')
    class Config:
        arbitrary_types_allowed = True
