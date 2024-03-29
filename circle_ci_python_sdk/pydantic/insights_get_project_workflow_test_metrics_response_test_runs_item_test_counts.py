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


class InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts(BaseModel):
    # The number of tests with the error status
    error: int = Field(alias='error')

    # The number of tests with the failure status
    failure: int = Field(alias='failure')

    # The number of tests with the skipped status
    skipped: int = Field(alias='skipped')

    # The number of tests with the success status
    success: int = Field(alias='success')

    # The total number of tests
    total: int = Field(alias='total')
    class Config:
        arbitrary_types_allowed = True
