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


class InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Test counts for a given pipeline number
    """


    class MetaOapg:
        required = {
            "total",
            "failure",
            "success",
            "error",
            "skipped",
        }
        
        class properties:
            
            
            class error(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class failure(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class skipped(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class success(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class total(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            __annotations__ = {
                "error": error,
                "failure": failure,
                "skipped": skipped,
                "success": success,
                "total": total,
            }
    
    total: MetaOapg.properties.total
    failure: MetaOapg.properties.failure
    success: MetaOapg.properties.success
    error: MetaOapg.properties.error
    skipped: MetaOapg.properties.skipped
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failure"]) -> MetaOapg.properties.failure: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skipped"]) -> MetaOapg.properties.skipped: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["error", "failure", "skipped", "success", "total", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failure"]) -> MetaOapg.properties.failure: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skipped"]) -> MetaOapg.properties.skipped: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["error", "failure", "skipped", "success", "total", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
        failure: typing.Union[MetaOapg.properties.failure, decimal.Decimal, int, ],
        success: typing.Union[MetaOapg.properties.success, decimal.Decimal, int, ],
        error: typing.Union[MetaOapg.properties.error, decimal.Decimal, int, ],
        skipped: typing.Union[MetaOapg.properties.skipped, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetProjectWorkflowTestMetricsResponseTestRunsItemTestCounts':
        return super().__new__(
            cls,
            *args,
            total=total,
            failure=failure,
            success=success,
            error=error,
            skipped=skipped,
            _configuration=_configuration,
            **kwargs,
        )
