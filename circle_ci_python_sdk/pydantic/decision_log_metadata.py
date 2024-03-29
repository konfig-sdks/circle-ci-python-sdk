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

from circle_ci_python_sdk.pydantic.decision_log_metadata_vcs import DecisionLogMetadataVcs

class DecisionLogMetadata(BaseModel):
    build_number: typing.Optional[int] = Field(None, alias='build_number')

    project_id: typing.Optional[str] = Field(None, alias='project_id')

    ssh_rerun: typing.Optional[bool] = Field(None, alias='ssh_rerun')

    vcs: typing.Optional[DecisionLogMetadataVcs] = Field(None, alias='vcs')
    class Config:
        arbitrary_types_allowed = True
