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

from circle_ci_python_sdk.type.insights_get_project_workflow_job_metrics_response_items_item_metrics_duration_metrics import InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics

class RequiredInsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics(TypedDict):
    # The total number of runs, including runs that are still on-hold or running.
    total_runs: int

    # The number of failed runs.
    failed_runs: int

    # The number of successful runs.
    successful_runs: int

    duration_metrics: InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetricsDurationMetrics

    success_rate: typing.Union[int, float]

    # The total credits consumed by the job in the aggregation window. Note that Insights is not a real time financial reporting tool and should not be used for credit reporting.
    total_credits_used: int

    # The average number of runs per day.
    throughput: typing.Union[int, float]

class OptionalInsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics(TypedDict, total=False):
    pass

class InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics(RequiredInsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics, OptionalInsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics):
    pass
