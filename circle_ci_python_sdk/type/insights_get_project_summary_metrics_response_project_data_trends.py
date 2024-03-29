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


class RequiredInsightsGetProjectSummaryMetricsResponseProjectDataTrends(TypedDict):
    # The trend value for total number of runs.
    total_runs: typing.Union[int, float]

    # Trend value for total duration.
    total_duration_secs: typing.Union[int, float]

    # The trend value for total credits consumed.
    total_credits_used: typing.Union[int, float]

    # The trend value for the success rate.
    success_rate: typing.Union[int, float]

    # Trend value for the average number of runs per day.
    throughput: typing.Union[int, float]

class OptionalInsightsGetProjectSummaryMetricsResponseProjectDataTrends(TypedDict, total=False):
    pass

class InsightsGetProjectSummaryMetricsResponseProjectDataTrends(RequiredInsightsGetProjectSummaryMetricsResponseProjectDataTrends, OptionalInsightsGetProjectSummaryMetricsResponseProjectDataTrends):
    pass
