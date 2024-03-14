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


class InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Metrics relating to the duration of runs for a workflow.
    """


    class MetaOapg:
        required = {
            "min",
            "median",
            "max",
            "mean",
            "standard_deviation",
            "p95",
        }
        
        class properties:
            
            
            class min(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class mean(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class median(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class p95(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class max(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            standard_deviation = schemas.Float32Schema
            __annotations__ = {
                "min": min,
                "mean": mean,
                "median": median,
                "p95": p95,
                "max": max,
                "standard_deviation": standard_deviation,
            }
    
    min: MetaOapg.properties.min
    median: MetaOapg.properties.median
    max: MetaOapg.properties.max
    mean: MetaOapg.properties.mean
    standard_deviation: MetaOapg.properties.standard_deviation
    p95: MetaOapg.properties.p95
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mean"]) -> MetaOapg.properties.mean: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["median"]) -> MetaOapg.properties.median: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["p95"]) -> MetaOapg.properties.p95: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standard_deviation"]) -> MetaOapg.properties.standard_deviation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["min", "mean", "median", "p95", "max", "standard_deviation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mean"]) -> MetaOapg.properties.mean: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["median"]) -> MetaOapg.properties.median: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["p95"]) -> MetaOapg.properties.p95: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standard_deviation"]) -> MetaOapg.properties.standard_deviation: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["min", "mean", "median", "p95", "max", "standard_deviation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, ],
        median: typing.Union[MetaOapg.properties.median, decimal.Decimal, int, ],
        max: typing.Union[MetaOapg.properties.max, decimal.Decimal, int, ],
        mean: typing.Union[MetaOapg.properties.mean, decimal.Decimal, int, ],
        standard_deviation: typing.Union[MetaOapg.properties.standard_deviation, decimal.Decimal, int, float, ],
        p95: typing.Union[MetaOapg.properties.p95, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics':
        return super().__new__(
            cls,
            *args,
            min=min,
            median=median,
            max=max,
            mean=mean,
            standard_deviation=standard_deviation,
            p95=p95,
            _configuration=_configuration,
            **kwargs,
        )