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

from circle_ci_python_sdk.type.insights_get_project_workflow_test_metrics_response_test_runs_item import InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem

InsightsGetProjectWorkflowTestMetricsResponseTestRuns = typing.List[InsightsGetProjectWorkflowTestMetricsResponseTestRunsItem]
