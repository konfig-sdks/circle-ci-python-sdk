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


class InsightsGetProjectSummaryMetricsResponseProjectWorkflowData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of metrics and trends data for workflows for a given project.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem']:
            return InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem'], typing.List['InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InsightsGetProjectSummaryMetricsResponseProjectWorkflowData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem':
        return super().__getitem__(i)

from circle_ci_python_sdk.model.insights_get_project_summary_metrics_response_project_workflow_data_item import InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItem
