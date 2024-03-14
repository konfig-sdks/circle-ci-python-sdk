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

from circle_ci_python_sdk.type.insights_get_summary_metrics_with_trends_response_all_projects import InsightsGetSummaryMetricsWithTrendsResponseAllProjects
from circle_ci_python_sdk.type.insights_get_summary_metrics_with_trends_response_org_data import InsightsGetSummaryMetricsWithTrendsResponseOrgData
from circle_ci_python_sdk.type.insights_get_summary_metrics_with_trends_response_org_project_data import InsightsGetSummaryMetricsWithTrendsResponseOrgProjectData

class RequiredInsightsGetSummaryMetricsWithTrendsResponse(TypedDict):
    org_data: InsightsGetSummaryMetricsWithTrendsResponseOrgData

    org_project_data: InsightsGetSummaryMetricsWithTrendsResponseOrgProjectData

    all_projects: InsightsGetSummaryMetricsWithTrendsResponseAllProjects

class OptionalInsightsGetSummaryMetricsWithTrendsResponse(TypedDict, total=False):
    pass

class InsightsGetSummaryMetricsWithTrendsResponse(RequiredInsightsGetSummaryMetricsWithTrendsResponse, OptionalInsightsGetSummaryMetricsWithTrendsResponse):
    pass