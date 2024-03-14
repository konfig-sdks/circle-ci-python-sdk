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


class InsightsGetProjectSummaryMetricsResponseProjectDataMetrics(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Metrics aggregated across all workflows and branches for a project.
    """


    class MetaOapg:
        required = {
            "total_runs",
            "total_duration_secs",
            "total_credits_used",
            "throughput",
            "success_rate",
        }
        
        class properties:
            
            
            class total_runs(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class total_duration_secs(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class total_credits_used(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            success_rate = schemas.Float32Schema
            throughput = schemas.Float32Schema
            __annotations__ = {
                "total_runs": total_runs,
                "total_duration_secs": total_duration_secs,
                "total_credits_used": total_credits_used,
                "success_rate": success_rate,
                "throughput": throughput,
            }
    
    total_runs: MetaOapg.properties.total_runs
    total_duration_secs: MetaOapg.properties.total_duration_secs
    total_credits_used: MetaOapg.properties.total_credits_used
    throughput: MetaOapg.properties.throughput
    success_rate: MetaOapg.properties.success_rate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_runs"]) -> MetaOapg.properties.total_runs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_duration_secs"]) -> MetaOapg.properties.total_duration_secs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_credits_used"]) -> MetaOapg.properties.total_credits_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success_rate"]) -> MetaOapg.properties.success_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["throughput"]) -> MetaOapg.properties.throughput: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_runs", "total_duration_secs", "total_credits_used", "success_rate", "throughput", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_runs"]) -> MetaOapg.properties.total_runs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_duration_secs"]) -> MetaOapg.properties.total_duration_secs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_credits_used"]) -> MetaOapg.properties.total_credits_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success_rate"]) -> MetaOapg.properties.success_rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["throughput"]) -> MetaOapg.properties.throughput: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_runs", "total_duration_secs", "total_credits_used", "success_rate", "throughput", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total_runs: typing.Union[MetaOapg.properties.total_runs, decimal.Decimal, int, ],
        total_duration_secs: typing.Union[MetaOapg.properties.total_duration_secs, decimal.Decimal, int, ],
        total_credits_used: typing.Union[MetaOapg.properties.total_credits_used, decimal.Decimal, int, ],
        throughput: typing.Union[MetaOapg.properties.throughput, decimal.Decimal, int, float, ],
        success_rate: typing.Union[MetaOapg.properties.success_rate, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetProjectSummaryMetricsResponseProjectDataMetrics':
        return super().__new__(
            cls,
            *args,
            total_runs=total_runs,
            total_duration_secs=total_duration_secs,
            total_credits_used=total_credits_used,
            throughput=throughput,
            success_rate=success_rate,
            _configuration=_configuration,
            **kwargs,
        )
