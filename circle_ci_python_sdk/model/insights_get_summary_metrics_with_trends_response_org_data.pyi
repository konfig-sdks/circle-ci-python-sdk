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


class InsightsGetSummaryMetricsWithTrendsResponseOrgData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Aggregated metrics for an org, with trends.
    """


    class MetaOapg:
        required = {
            "metrics",
            "trends",
        }
        
        class properties:
        
            @staticmethod
            def metrics() -> typing.Type['InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics']:
                return InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics
        
            @staticmethod
            def trends() -> typing.Type['InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends']:
                return InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends
            __annotations__ = {
                "metrics": metrics,
                "trends": trends,
            }
    
    metrics: 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics'
    trends: 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metrics"]) -> 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trends"]) -> 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["metrics", "trends", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metrics"]) -> 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trends"]) -> 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["metrics", "trends", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        metrics: 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics',
        trends: 'InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetSummaryMetricsWithTrendsResponseOrgData':
        return super().__new__(
            cls,
            *args,
            metrics=metrics,
            trends=trends,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.insights_get_summary_metrics_with_trends_response_org_data_metrics import InsightsGetSummaryMetricsWithTrendsResponseOrgDataMetrics
from circle_ci_python_sdk.model.insights_get_summary_metrics_with_trends_response_org_data_trends import InsightsGetSummaryMetricsWithTrendsResponseOrgDataTrends