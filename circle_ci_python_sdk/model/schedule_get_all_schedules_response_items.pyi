# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from circle_ci_python_sdk import schemas  # noqa: F401


class ScheduleGetAllSchedulesResponseItems(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ScheduleGetAllSchedulesResponseItemsItem']:
            return ScheduleGetAllSchedulesResponseItemsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ScheduleGetAllSchedulesResponseItemsItem'], typing.List['ScheduleGetAllSchedulesResponseItemsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ScheduleGetAllSchedulesResponseItems':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ScheduleGetAllSchedulesResponseItemsItem':
        return super().__getitem__(i)

from circle_ci_python_sdk.model.schedule_get_all_schedules_response_items_item import ScheduleGetAllSchedulesResponseItemsItem