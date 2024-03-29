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

from circle_ci_python_sdk.pydantic.insights_list_project_branches_response_branches import InsightsListProjectBranchesResponseBranches

class InsightsListProjectBranchesResponse(BaseModel):
    # The unique ID of the organization
    org_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='org_id')

    # The unique ID of the project
    project_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='project_id')

    branches: InsightsListProjectBranchesResponseBranches = Field(alias='branches')
    class Config:
        arbitrary_types_allowed = True
