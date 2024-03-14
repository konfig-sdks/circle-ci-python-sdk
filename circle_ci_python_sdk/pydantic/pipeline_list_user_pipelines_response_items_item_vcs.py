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

from circle_ci_python_sdk.pydantic.pipeline_list_user_pipelines_response_items_item_vcs_commit import PipelineListUserPipelinesResponseItemsItemVcsCommit

class PipelineListUserPipelinesResponseItemsItemVcs(BaseModel):
    # Name of the VCS provider (e.g. GitHub, Bitbucket).
    provider_name: str = Field(alias='provider_name')

    # URL for the repository the trigger targets (i.e. the repository where the PR will be merged). For fork-PR pipelines, this is the URL to the parent repo. For other pipelines, the `origin_` and `target_repository_url`s will be the same.
    target_repository_url: str = Field(alias='target_repository_url')

    # The code revision the pipeline ran.
    revision: str = Field(alias='revision')

    # URL for the repository where the trigger originated. For fork-PR pipelines, this is the URL to the fork. For other pipelines the `origin_` and `target_repository_url`s will be the same.
    origin_repository_url: str = Field(alias='origin_repository_url')

    # The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).
    branch: typing.Optional[str] = Field(None, alias='branch')

    # The code review id.
    review_id: typing.Optional[str] = Field(None, alias='review_id')

    # The code review URL.
    review_url: typing.Optional[str] = Field(None, alias='review_url')

    # The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.
    tag: typing.Optional[str] = Field(None, alias='tag')

    commit: typing.Optional[PipelineListUserPipelinesResponseItemsItemVcsCommit] = Field(None, alias='commit')
    class Config:
        arbitrary_types_allowed = True
