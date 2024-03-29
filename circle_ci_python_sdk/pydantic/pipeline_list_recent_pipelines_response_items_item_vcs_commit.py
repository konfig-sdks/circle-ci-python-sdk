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


class PipelineListRecentPipelinesResponseItemsItemVcsCommit(BaseModel):
    # The subject of the commit message.
    subject: typing.Optional[str] = Field(alias='subject')

    # The body of the commit message.
    body: typing.Optional[str] = Field(alias='body')
    class Config:
        arbitrary_types_allowed = True
