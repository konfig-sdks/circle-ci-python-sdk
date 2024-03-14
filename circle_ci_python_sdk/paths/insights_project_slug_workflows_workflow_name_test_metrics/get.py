# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from circle_ci_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from circle_ci_python_sdk.api_response import AsyncGeneratorResponse
from circle_ci_python_sdk import api_client, exceptions
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

from circle_ci_python_sdk.model.insights_get_project_workflow_test_metricsdefault_response import InsightsGetProjectWorkflowTestMetricsdefaultResponse as InsightsGetProjectWorkflowTestMetricsdefaultResponseSchema
from circle_ci_python_sdk.model.insights_get_project_workflow_test_metrics_response import InsightsGetProjectWorkflowTestMetricsResponse as InsightsGetProjectWorkflowTestMetricsResponseSchema

from circle_ci_python_sdk.type.insights_get_project_workflow_test_metricsdefault_response import InsightsGetProjectWorkflowTestMetricsdefaultResponse
from circle_ci_python_sdk.type.insights_get_project_workflow_test_metrics_response import InsightsGetProjectWorkflowTestMetricsResponse

from ...api_client import Dictionary
from circle_ci_python_sdk.pydantic.insights_get_project_workflow_test_metrics_response import InsightsGetProjectWorkflowTestMetricsResponse as InsightsGetProjectWorkflowTestMetricsResponsePydantic
from circle_ci_python_sdk.pydantic.insights_get_project_workflow_test_metricsdefault_response import InsightsGetProjectWorkflowTestMetricsdefaultResponse as InsightsGetProjectWorkflowTestMetricsdefaultResponsePydantic

from . import path

# Query params
BranchSchema = schemas.StrSchema
AllBranchesSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'branch': typing.Union[BranchSchema, str, ],
        'all-branches': typing.Union[AllBranchesSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_branch = api_client.QueryParameter(
    name="branch",
    style=api_client.ParameterStyle.FORM,
    schema=BranchSchema,
    explode=True,
)
request_query_all_branches = api_client.QueryParameter(
    name="all-branches",
    style=api_client.ParameterStyle.FORM,
    schema=AllBranchesSchema,
    explode=True,
)
# Path params
ProjectSlugSchema = schemas.StrSchema
WorkflowNameSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'project-slug': typing.Union[ProjectSlugSchema, str, ],
        'workflow-name': typing.Union[WorkflowNameSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_project_slug = api_client.PathParameter(
    name="project-slug",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectSlugSchema,
    required=True,
)
request_path_workflow_name = api_client.PathParameter(
    name="workflow-name",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WorkflowNameSchema,
    required=True,
)
_auth = [
    'api_key_header',
    'api_key_query',
    'basic_auth',
]
SchemaFor200ResponseBodyApplicationJson = InsightsGetProjectWorkflowTestMetricsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: InsightsGetProjectWorkflowTestMetricsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: InsightsGetProjectWorkflowTestMetricsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = InsightsGetProjectWorkflowTestMetricsdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: InsightsGetProjectWorkflowTestMetricsdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: InsightsGetProjectWorkflowTestMetricsdefaultResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_project_workflow_test_metrics_mapped_args(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if branch is not None:
            _query_params["branch"] = branch
        if all_branches is not None:
            _query_params["all-branches"] = all_branches
        if project_slug is not None:
            _path_params["project-slug"] = project_slug
        if workflow_name is not None:
            _path_params["workflow-name"] = workflow_name
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_project_workflow_test_metrics_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get test metrics for a project&#x27;s workflows
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_slug,
            request_path_workflow_name,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_branch,
            request_query_all_branches,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/insights/{project-slug}/workflows/{workflow-name}/test-metrics',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_project_workflow_test_metrics_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get test metrics for a project&#x27;s workflows
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_slug,
            request_path_workflow_name,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_branch,
            request_query_all_branches,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/insights/{project-slug}/workflows/{workflow-name}/test-metrics',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetProjectWorkflowTestMetricsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_project_workflow_test_metrics(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_project_workflow_test_metrics_mapped_args(
            project_slug=project_slug,
            workflow_name=workflow_name,
            branch=branch,
            all_branches=all_branches,
        )
        return await self._aget_project_workflow_test_metrics_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_project_workflow_test_metrics(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_project_workflow_test_metrics_mapped_args(
            project_slug=project_slug,
            workflow_name=workflow_name,
            branch=branch,
            all_branches=all_branches,
        )
        return self._get_project_workflow_test_metrics_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetProjectWorkflowTestMetrics(BaseApi):

    async def aget_project_workflow_test_metrics(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> InsightsGetProjectWorkflowTestMetricsResponsePydantic:
        raw_response = await self.raw.aget_project_workflow_test_metrics(
            project_slug=project_slug,
            workflow_name=workflow_name,
            branch=branch,
            all_branches=all_branches,
            **kwargs,
        )
        if validate:
            return InsightsGetProjectWorkflowTestMetricsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(InsightsGetProjectWorkflowTestMetricsResponsePydantic, raw_response.body)
    
    
    def get_project_workflow_test_metrics(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> InsightsGetProjectWorkflowTestMetricsResponsePydantic:
        raw_response = self.raw.get_project_workflow_test_metrics(
            project_slug=project_slug,
            workflow_name=workflow_name,
            branch=branch,
            all_branches=all_branches,
        )
        if validate:
            return InsightsGetProjectWorkflowTestMetricsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(InsightsGetProjectWorkflowTestMetricsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_project_workflow_test_metrics_mapped_args(
            project_slug=project_slug,
            workflow_name=workflow_name,
            branch=branch,
            all_branches=all_branches,
        )
        return await self._aget_project_workflow_test_metrics_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        project_slug: str,
        workflow_name: str,
        branch: typing.Optional[str] = None,
        all_branches: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_project_workflow_test_metrics_mapped_args(
            project_slug=project_slug,
            workflow_name=workflow_name,
            branch=branch,
            all_branches=all_branches,
        )
        return self._get_project_workflow_test_metrics_oapg(
            query_params=args.query,
            path_params=args.path,
        )
