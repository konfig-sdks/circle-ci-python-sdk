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

from circle_ci_python_sdk.type.insights_get_project_workflow_job_metrics_response_items_item_metrics import InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics

class RequiredInsightsGetProjectWorkflowJobMetricsResponseItemsItem(TypedDict):
    # The name of the job.
    name: str

    metrics: InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics

    # The timestamp of the first build within the requested reporting window.
    window_start: datetime

    # The timestamp of the last build within the requested reporting window.
    window_end: datetime

class OptionalInsightsGetProjectWorkflowJobMetricsResponseItemsItem(TypedDict, total=False):
    pass

class InsightsGetProjectWorkflowJobMetricsResponseItemsItem(RequiredInsightsGetProjectWorkflowJobMetricsResponseItemsItem, OptionalInsightsGetProjectWorkflowJobMetricsResponseItemsItem):
    pass