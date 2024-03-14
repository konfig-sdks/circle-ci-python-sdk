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

from circle_ci_python_sdk.pydantic.project_get_by_slug_response_vcs_info import ProjectGetBySlugResponseVcsInfo

class ProjectGetBySlugResponse(BaseModel):
    # Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    slug: str = Field(alias='slug')

    # The name of the project
    name: str = Field(alias='name')

    id: str = Field(alias='id')

    # The name of the organization the project belongs to
    organization_name: str = Field(alias='organization_name')

    # The slug of the organization the project belongs to
    organization_slug: str = Field(alias='organization_slug')

    # The id of the organization the project belongs to
    organization_id: str = Field(alias='organization_id')

    vcs_info: ProjectGetBySlugResponseVcsInfo = Field(alias='vcs_info')
    class Config:
        arbitrary_types_allowed = True
