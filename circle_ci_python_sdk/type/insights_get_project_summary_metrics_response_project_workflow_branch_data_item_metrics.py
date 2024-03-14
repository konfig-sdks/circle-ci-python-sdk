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


class RequiredInsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics(TypedDict):
    # The total credits consumed over the current timeseries interval.
    total_credits_used: int

    # The 95th percentile duration among a group of workflow runs.
    p95_duration_secs: typing.Union[int, float]

    # The total number of runs, including runs that are still on-hold or running.
    total_runs: int

    success_rate: typing.Union[int, float]

class OptionalInsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics(TypedDict, total=False):
    pass

class InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics(RequiredInsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics, OptionalInsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics):
    pass