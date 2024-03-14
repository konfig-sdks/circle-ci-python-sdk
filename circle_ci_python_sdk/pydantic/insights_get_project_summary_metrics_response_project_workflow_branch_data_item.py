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

from circle_ci_python_sdk.pydantic.insights_get_project_summary_metrics_response_project_workflow_branch_data_item_metrics import InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics
from circle_ci_python_sdk.pydantic.insights_get_project_summary_metrics_response_project_workflow_branch_data_item_trends import InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends

class InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItem(BaseModel):
    # The name of the workflow.
    workflow_name: str = Field(alias='workflow_name')

    # The VCS branch of a workflow's trigger.
    branch: str = Field(alias='branch')

    metrics: InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics = Field(alias='metrics')

    trends: InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemTrends = Field(alias='trends')
    class Config:
        arbitrary_types_allowed = True
