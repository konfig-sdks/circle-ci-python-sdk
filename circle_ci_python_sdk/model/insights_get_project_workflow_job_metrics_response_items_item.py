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


class InsightsGetProjectWorkflowJobMetricsResponseItemsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "window_end",
            "name",
            "window_start",
            "metrics",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def metrics() -> typing.Type['InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics']:
                return InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics
            window_start = schemas.DateTimeSchema
            window_end = schemas.DateTimeSchema
            __annotations__ = {
                "name": name,
                "metrics": metrics,
                "window_start": window_start,
                "window_end": window_end,
            }
    
    window_end: MetaOapg.properties.window_end
    name: MetaOapg.properties.name
    window_start: MetaOapg.properties.window_start
    metrics: 'InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metrics"]) -> 'InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["window_start"]) -> MetaOapg.properties.window_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["window_end"]) -> MetaOapg.properties.window_end: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "metrics", "window_start", "window_end", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metrics"]) -> 'InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["window_start"]) -> MetaOapg.properties.window_start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["window_end"]) -> MetaOapg.properties.window_end: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "metrics", "window_start", "window_end", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        window_end: typing.Union[MetaOapg.properties.window_end, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        window_start: typing.Union[MetaOapg.properties.window_start, str, datetime, ],
        metrics: 'InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsGetProjectWorkflowJobMetricsResponseItemsItem':
        return super().__new__(
            cls,
            *args,
            window_end=window_end,
            name=name,
            window_start=window_start,
            metrics=metrics,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.insights_get_project_workflow_job_metrics_response_items_item_metrics import InsightsGetProjectWorkflowJobMetricsResponseItemsItemMetrics
