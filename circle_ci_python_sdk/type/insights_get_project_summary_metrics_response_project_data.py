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

from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_project_data_metrics import InsightsGetProjectSummaryMetricsResponseProjectDataMetrics
from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_project_data_trends import InsightsGetProjectSummaryMetricsResponseProjectDataTrends

class RequiredInsightsGetProjectSummaryMetricsResponseProjectData(TypedDict):
    metrics: InsightsGetProjectSummaryMetricsResponseProjectDataMetrics

    trends: InsightsGetProjectSummaryMetricsResponseProjectDataTrends

class OptionalInsightsGetProjectSummaryMetricsResponseProjectData(TypedDict, total=False):
    pass

class InsightsGetProjectSummaryMetricsResponseProjectData(RequiredInsightsGetProjectSummaryMetricsResponseProjectData, OptionalInsightsGetProjectSummaryMetricsResponseProjectData):
    pass
