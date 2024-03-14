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


class InsightsGetWorkflowSummaryMetricsResponseMetricsDurationMetrics(BaseModel):
    # The minimum duration, in seconds, among a group of runs.
    min: typing.Optional[int] = Field(alias='min')

    # The mean duration, in seconds, among a group of runs.
    mean: typing.Optional[int] = Field(alias='mean')

    # The median duration, in seconds, among a group of runs.
    median: typing.Optional[int] = Field(alias='median')

    # The 95th percentile duration, in seconds, among a group of runs.
    p95: typing.Optional[int] = Field(alias='p95')

    # The max duration, in seconds, among a group of runs.
    max: typing.Optional[int] = Field(alias='max')

    # The standard deviation, in seconds, among a group of runs.
    standard_deviation: typing.Optional[typing.Union[int, float]] = Field(alias='standard_deviation')
    class Config:
        arbitrary_types_allowed = True
