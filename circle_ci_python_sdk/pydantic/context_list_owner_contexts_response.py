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

from circle_ci_python_sdk.pydantic.context_list_owner_contexts_response_items import ContextListOwnerContextsResponseItems

class ContextListOwnerContextsResponse(BaseModel):
    items: ContextListOwnerContextsResponseItems = Field(alias='items')

    # A token to pass as a `page-token` query parameter to return the next page of results.
    next_page_token: typing.Optional[str] = Field(alias='next_page_token')
    class Config:
        arbitrary_types_allowed = True
