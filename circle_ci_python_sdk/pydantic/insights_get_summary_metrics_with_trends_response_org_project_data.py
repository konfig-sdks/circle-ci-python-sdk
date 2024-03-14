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

from circle_ci_python_sdk.pydantic.insights_get_summary_metrics_with_trends_response_org_project_data_item import InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem

InsightsGetSummaryMetricsWithTrendsResponseOrgProjectData = typing.List[InsightsGetSummaryMetricsWithTrendsResponseOrgProjectDataItem]