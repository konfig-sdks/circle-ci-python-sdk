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

from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_all_branches import InsightsGetProjectSummaryMetricsResponseAllBranches
from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_all_workflows import InsightsGetProjectSummaryMetricsResponseAllWorkflows
from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_project_data import InsightsGetProjectSummaryMetricsResponseProjectData
from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_project_workflow_branch_data import InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchData
from circle_ci_python_sdk.type.insights_get_project_summary_metrics_response_project_workflow_data import InsightsGetProjectSummaryMetricsResponseProjectWorkflowData

class RequiredInsightsGetProjectSummaryMetricsResponse(TypedDict):
    pass

class OptionalInsightsGetProjectSummaryMetricsResponse(TypedDict, total=False):
    # The unique ID of the organization
    org_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The unique ID of the project
    project_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    project_data: InsightsGetProjectSummaryMetricsResponseProjectData

    project_workflow_data: InsightsGetProjectSummaryMetricsResponseProjectWorkflowData

    project_workflow_branch_data: InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchData

    all_branches: InsightsGetProjectSummaryMetricsResponseAllBranches

    all_workflows: InsightsGetProjectSummaryMetricsResponseAllWorkflows

class InsightsGetProjectSummaryMetricsResponse(RequiredInsightsGetProjectSummaryMetricsResponse, OptionalInsightsGetProjectSummaryMetricsResponse):
    pass