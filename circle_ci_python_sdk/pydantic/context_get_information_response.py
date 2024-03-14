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


class ContextGetInformationResponse(BaseModel):
    # The unique ID of the context.
    id: str = Field(alias='id')

    # The user defined name of the context.
    name: str = Field(alias='name')

    # The date and time the context was created.
    created_at: datetime = Field(alias='created_at')
    class Config:
        arbitrary_types_allowed = True