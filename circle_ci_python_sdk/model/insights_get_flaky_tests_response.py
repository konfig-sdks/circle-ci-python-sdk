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


class InsightsGetFlakyTestsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Flaky tests response
    """


    class MetaOapg:
        required = {
            "total-flaky-tests",
            "flaky-tests",
        }
        
        class properties:
        
            @staticmethod
            def flaky_tests() -> typing.Type['InsightsGetFlakyTestsResponseFlakyTests']:
                return InsightsGetFlakyTestsResponseFlakyTests
            total_flaky_tests = schemas.Float64Schema
            __annotations__ = {
                "flaky-tests": flaky_tests,
                "total-flaky-tests": total_flaky_tests,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flaky-tests"]) -> 'InsightsGetFlakyTestsResponseFlakyTests': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total-flaky-tests"]) -> MetaOapg.properties.total_flaky_tests: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["flaky-tests", "total-flaky-tests", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flaky-tests"]) -> 'InsightsGetFlakyTestsResponseFlakyTests': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total-flaky-tests"]) -> MetaOapg.properties.total_flaky_tests: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["flaky-tests", "total-flaky-tests", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetFlakyTestsResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.insights_get_flaky_tests_response_flaky_tests import InsightsGetFlakyTestsResponseFlakyTests