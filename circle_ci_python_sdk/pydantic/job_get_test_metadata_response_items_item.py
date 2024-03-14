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


class JobGetTestMetadataResponseItemsItem(BaseModel):
    # The failure message associated with the test.
    message: typing.Optional[str] = Field(alias='message')

    # The program that generated the test results
    source: str = Field(alias='source')

    # The time it took to run the test in seconds
    run_time: typing.Union[int, float] = Field(alias='run_time')

    # The file in which the test is defined.
    file: str = Field(alias='file')

    # Indication of whether the test succeeded.
    result: str = Field(alias='result')

    # The name of the test.
    name: str = Field(alias='name')

    # The programmatic location of the test.
    classname: str = Field(alias='classname')
    class Config:
        arbitrary_types_allowed = True