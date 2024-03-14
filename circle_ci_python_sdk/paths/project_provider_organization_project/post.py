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

from circle_ci_python_sdk.model.project_create_project_default_settings405_response import ProjectCreateProjectDefaultSettings405Response as ProjectCreateProjectDefaultSettings405ResponseSchema
from circle_ci_python_sdk.model.project_create_project_default_settings403_response import ProjectCreateProjectDefaultSettings403Response as ProjectCreateProjectDefaultSettings403ResponseSchema
from circle_ci_python_sdk.model.project_create_project_default_settings_response import ProjectCreateProjectDefaultSettingsResponse as ProjectCreateProjectDefaultSettingsResponseSchema
from circle_ci_python_sdk.model.project_settings import ProjectSettings as ProjectSettingsSchema
from circle_ci_python_sdk.model.context_get_restrictions500_response import ContextGetRestrictions500Response as ContextGetRestrictions500ResponseSchema
from circle_ci_python_sdk.model.context_get_restrictions429_response import ContextGetRestrictions429Response as ContextGetRestrictions429ResponseSchema
from circle_ci_python_sdk.model.project_create_project_default_settings404_response import ProjectCreateProjectDefaultSettings404Response as ProjectCreateProjectDefaultSettings404ResponseSchema
from circle_ci_python_sdk.model.context_get_restrictions401_response import ContextGetRestrictions401Response as ContextGetRestrictions401ResponseSchema

from circle_ci_python_sdk.type.project_create_project_default_settings405_response import ProjectCreateProjectDefaultSettings405Response
from circle_ci_python_sdk.type.project_create_project_default_settings_response import ProjectCreateProjectDefaultSettingsResponse
from circle_ci_python_sdk.type.context_get_restrictions401_response import ContextGetRestrictions401Response
from circle_ci_python_sdk.type.context_get_restrictions500_response import ContextGetRestrictions500Response
from circle_ci_python_sdk.type.project_create_project_default_settings403_response import ProjectCreateProjectDefaultSettings403Response
from circle_ci_python_sdk.type.project_settings import ProjectSettings
from circle_ci_python_sdk.type.project_create_project_default_settings404_response import ProjectCreateProjectDefaultSettings404Response
from circle_ci_python_sdk.type.context_get_restrictions429_response import ContextGetRestrictions429Response

from ...api_client import Dictionary
from circle_ci_python_sdk.pydantic.context_get_restrictions500_response import ContextGetRestrictions500Response as ContextGetRestrictions500ResponsePydantic
from circle_ci_python_sdk.pydantic.project_create_project_default_settings_response import ProjectCreateProjectDefaultSettingsResponse as ProjectCreateProjectDefaultSettingsResponsePydantic
from circle_ci_python_sdk.pydantic.project_create_project_default_settings403_response import ProjectCreateProjectDefaultSettings403Response as ProjectCreateProjectDefaultSettings403ResponsePydantic
from circle_ci_python_sdk.pydantic.project_settings import ProjectSettings as ProjectSettingsPydantic
from circle_ci_python_sdk.pydantic.context_get_restrictions429_response import ContextGetRestrictions429Response as ContextGetRestrictions429ResponsePydantic
from circle_ci_python_sdk.pydantic.project_create_project_default_settings404_response import ProjectCreateProjectDefaultSettings404Response as ProjectCreateProjectDefaultSettings404ResponsePydantic
from circle_ci_python_sdk.pydantic.project_create_project_default_settings405_response import ProjectCreateProjectDefaultSettings405Response as ProjectCreateProjectDefaultSettings405ResponsePydantic
from circle_ci_python_sdk.pydantic.context_get_restrictions401_response import ContextGetRestrictions401Response as ContextGetRestrictions401ResponsePydantic

from . import path

# Path params
ProviderSchema = schemas.StrSchema
OrganizationSchema = schemas.StrSchema
ProjectSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'provider': typing.Union[ProviderSchema, str, ],
        'organization': typing.Union[OrganizationSchema, str, ],
        'project': typing.Union[ProjectSchema, str, ],
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


request_path_provider = api_client.PathParameter(
    name="provider",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProviderSchema,
    required=True,
)
request_path_organization = api_client.PathParameter(
    name="organization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrganizationSchema,
    required=True,
)
request_path_project = api_client.PathParameter(
    name="project",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectSchema,
    required=True,
)
_auth = [
    'api_key_header',
    'api_key_query',
    'basic_auth',
]
SchemaFor201ResponseBodyApplicationJson = ProjectSettingsSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ProjectSettings


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ProjectSettings


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ProjectCreateProjectDefaultSettingsResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ProjectCreateProjectDefaultSettingsResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ProjectCreateProjectDefaultSettingsResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ContextGetRestrictions401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ContextGetRestrictions401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ContextGetRestrictions401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ProjectCreateProjectDefaultSettings403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ProjectCreateProjectDefaultSettings403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ProjectCreateProjectDefaultSettings403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ProjectCreateProjectDefaultSettings404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ProjectCreateProjectDefaultSettings404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ProjectCreateProjectDefaultSettings404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor405ResponseBodyApplicationJson = ProjectCreateProjectDefaultSettings405ResponseSchema


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    body: ProjectCreateProjectDefaultSettings405Response


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: ProjectCreateProjectDefaultSettings405Response


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor405ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = ContextGetRestrictions429ResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: ContextGetRestrictions429Response


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: ContextGetRestrictions429Response


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ContextGetRestrictions500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ContextGetRestrictions500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ContextGetRestrictions500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '405': _response_for_405,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_project_default_settings_mapped_args(
        self,
        provider: str,
        organization: str,
        project: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if provider is not None:
            _path_params["provider"] = provider
        if organization is not None:
            _path_params["organization"] = organization
        if project is not None:
            _path_params["project"] = project
        args.path = _path_params
        return args

    async def _acreate_project_default_settings_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        🧪 Create a project
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_provider,
            request_path_organization,
            request_path_project,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/project/{provider}/{organization}/{project}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
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


    def _create_project_default_settings_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        🧪 Create a project
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_provider,
            request_path_organization,
            request_path_project,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/project/{provider}/{organization}/{project}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateProjectDefaultSettingsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_project_default_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_project_default_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
        )
        return await self._acreate_project_default_settings_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def create_project_default_settings(
        self,
        provider: str,
        organization: str,
        project: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_project_default_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
        )
        return self._create_project_default_settings_oapg(
            path_params=args.path,
        )

class CreateProjectDefaultSettings(BaseApi):

    async def acreate_project_default_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        validate: bool = False,
        **kwargs,
    ) -> ProjectSettingsPydantic:
        raw_response = await self.raw.acreate_project_default_settings(
            provider=provider,
            organization=organization,
            project=project,
            **kwargs,
        )
        if validate:
            return ProjectSettingsPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectSettingsPydantic, raw_response.body)
    
    
    def create_project_default_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        validate: bool = False,
    ) -> ProjectSettingsPydantic:
        raw_response = self.raw.create_project_default_settings(
            provider=provider,
            organization=organization,
            project=project,
        )
        if validate:
            return ProjectSettingsPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectSettingsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        provider: str,
        organization: str,
        project: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_project_default_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
        )
        return await self._acreate_project_default_settings_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        provider: str,
        organization: str,
        project: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_project_default_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
        )
        return self._create_project_default_settings_oapg(
            path_params=args.path,
        )

