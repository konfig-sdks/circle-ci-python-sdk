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


class InsightsGetWorkflowSummaryMetricsResponseTrends(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Trends for aggregated metrics across a workflow for a given time window.
    """


    class MetaOapg:
        required = {
            "total_runs",
            "mttr",
            "failed_runs",
            "total_credits_used",
            "throughput",
            "median_duration_secs",
            "p95_duration_secs",
            "success_rate",
        }
        
        class properties:
            total_runs = schemas.Float32Schema
            failed_runs = schemas.Float32Schema
            success_rate = schemas.Float32Schema
            p95_duration_secs = schemas.Float32Schema
            median_duration_secs = schemas.Float32Schema
            total_credits_used = schemas.Float32Schema
            mttr = schemas.Float32Schema
            throughput = schemas.Float32Schema
            __annotations__ = {
                "total_runs": total_runs,
                "failed_runs": failed_runs,
                "success_rate": success_rate,
                "p95_duration_secs": p95_duration_secs,
                "median_duration_secs": median_duration_secs,
                "total_credits_used": total_credits_used,
                "mttr": mttr,
                "throughput": throughput,
            }
    
    total_runs: MetaOapg.properties.total_runs
    mttr: MetaOapg.properties.mttr
    failed_runs: MetaOapg.properties.failed_runs
    total_credits_used: MetaOapg.properties.total_credits_used
    throughput: MetaOapg.properties.throughput
    median_duration_secs: MetaOapg.properties.median_duration_secs
    p95_duration_secs: MetaOapg.properties.p95_duration_secs
    success_rate: MetaOapg.properties.success_rate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_runs"]) -> MetaOapg.properties.total_runs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failed_runs"]) -> MetaOapg.properties.failed_runs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success_rate"]) -> MetaOapg.properties.success_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["p95_duration_secs"]) -> MetaOapg.properties.p95_duration_secs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["median_duration_secs"]) -> MetaOapg.properties.median_duration_secs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_credits_used"]) -> MetaOapg.properties.total_credits_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mttr"]) -> MetaOapg.properties.mttr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["throughput"]) -> MetaOapg.properties.throughput: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_runs", "failed_runs", "success_rate", "p95_duration_secs", "median_duration_secs", "total_credits_used", "mttr", "throughput", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_runs"]) -> MetaOapg.properties.total_runs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failed_runs"]) -> MetaOapg.properties.failed_runs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success_rate"]) -> MetaOapg.properties.success_rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["p95_duration_secs"]) -> MetaOapg.properties.p95_duration_secs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["median_duration_secs"]) -> MetaOapg.properties.median_duration_secs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_credits_used"]) -> MetaOapg.properties.total_credits_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mttr"]) -> MetaOapg.properties.mttr: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["throughput"]) -> MetaOapg.properties.throughput: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_runs", "failed_runs", "success_rate", "p95_duration_secs", "median_duration_secs", "total_credits_used", "mttr", "throughput", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total_runs: typing.Union[MetaOapg.properties.total_runs, decimal.Decimal, int, float, ],
        mttr: typing.Union[MetaOapg.properties.mttr, decimal.Decimal, int, float, ],
        failed_runs: typing.Union[MetaOapg.properties.failed_runs, decimal.Decimal, int, float, ],
        total_credits_used: typing.Union[MetaOapg.properties.total_credits_used, decimal.Decimal, int, float, ],
        throughput: typing.Union[MetaOapg.properties.throughput, decimal.Decimal, int, float, ],
        median_duration_secs: typing.Union[MetaOapg.properties.median_duration_secs, decimal.Decimal, int, float, ],
        p95_duration_secs: typing.Union[MetaOapg.properties.p95_duration_secs, decimal.Decimal, int, float, ],
        success_rate: typing.Union[MetaOapg.properties.success_rate, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetWorkflowSummaryMetricsResponseTrends':
        return super().__new__(
            cls,
            *args,
            total_runs=total_runs,
            mttr=mttr,
            failed_runs=failed_runs,
            total_credits_used=total_credits_used,
            throughput=throughput,
            median_duration_secs=median_duration_secs,
            p95_duration_secs=p95_duration_secs,
            success_rate=success_rate,
            _configuration=_configuration,
            **kwargs,
        )