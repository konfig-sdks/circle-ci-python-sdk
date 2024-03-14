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

from circle_ci_python_sdk.pydantic.insights_get_project_workflow_test_metrics_response_test_runs_item_test_counts import InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts

class InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem(BaseModel):
    # The number of the pipeline associated with the provided test counts
    pipeline_number: int = Field(alias='pipeline_number')

    # The ID of the workflow associated with the provided test counts
    workflow_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='workflow_id')

    # The success rate calculated from test counts
    success_rate: typing.Union[int, float] = Field(alias='success_rate')

    test_counts: InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts = Field(alias='test_counts')
    class Config:
        arbitrary_types_allowed = True
