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

from circle_ci_python_sdk.model.project_settings_advanced import ProjectSettingsAdvanced as ProjectSettingsAdvancedSchema
from circle_ci_python_sdk.model.project_create_project_default_settings403_response import ProjectCreateProjectDefaultSettings403Response as ProjectCreateProjectDefaultSettings403ResponseSchema
from circle_ci_python_sdk.model.project_settings import ProjectSettings as ProjectSettingsSchema
from circle_ci_python_sdk.model.context_get_restrictions500_response import ContextGetRestrictions500Response as ContextGetRestrictions500ResponseSchema
from circle_ci_python_sdk.model.project_update_settings_response import ProjectUpdateSettingsResponse as ProjectUpdateSettingsResponseSchema
from circle_ci_python_sdk.model.project_get_settings_response import ProjectGetSettingsResponse as ProjectGetSettingsResponseSchema
from circle_ci_python_sdk.model.context_get_restrictions429_response import ContextGetRestrictions429Response as ContextGetRestrictions429ResponseSchema
from circle_ci_python_sdk.model.context_get_restrictions401_response import ContextGetRestrictions401Response as ContextGetRestrictions401ResponseSchema

from circle_ci_python_sdk.type.project_update_settings_response import ProjectUpdateSettingsResponse
from circle_ci_python_sdk.type.project_get_settings_response import ProjectGetSettingsResponse
from circle_ci_python_sdk.type.project_settings_advanced import ProjectSettingsAdvanced
from circle_ci_python_sdk.type.context_get_restrictions401_response import ContextGetRestrictions401Response
from circle_ci_python_sdk.type.context_get_restrictions500_response import ContextGetRestrictions500Response
from circle_ci_python_sdk.type.project_create_project_default_settings403_response import ProjectCreateProjectDefaultSettings403Response
from circle_ci_python_sdk.type.project_settings import ProjectSettings
from circle_ci_python_sdk.type.context_get_restrictions429_response import ContextGetRestrictions429Response

from ...api_client import Dictionary
from circle_ci_python_sdk.pydantic.project_update_settings_response import ProjectUpdateSettingsResponse as ProjectUpdateSettingsResponsePydantic
from circle_ci_python_sdk.pydantic.context_get_restrictions500_response import ContextGetRestrictions500Response as ContextGetRestrictions500ResponsePydantic
from circle_ci_python_sdk.pydantic.project_create_project_default_settings403_response import ProjectCreateProjectDefaultSettings403Response as ProjectCreateProjectDefaultSettings403ResponsePydantic
from circle_ci_python_sdk.pydantic.project_settings import ProjectSettings as ProjectSettingsPydantic
from circle_ci_python_sdk.pydantic.context_get_restrictions429_response import ContextGetRestrictions429Response as ContextGetRestrictions429ResponsePydantic
from circle_ci_python_sdk.pydantic.project_settings_advanced import ProjectSettingsAdvanced as ProjectSettingsAdvancedPydantic
from circle_ci_python_sdk.pydantic.project_get_settings_response import ProjectGetSettingsResponse as ProjectGetSettingsResponsePydantic
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
# body param
SchemaForRequestBodyApplicationJson = ProjectSettingsSchema


request_body_project_settings = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_key_header',
    'api_key_query',
    'basic_auth',
]
SchemaFor200ResponseBodyApplicationJson = ProjectSettingsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProjectSettings


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProjectSettings


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ProjectUpdateSettingsResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ProjectUpdateSettingsResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ProjectUpdateSettingsResponse


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
SchemaFor404ResponseBodyApplicationJson = ProjectGetSettingsResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ProjectGetSettingsResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ProjectGetSettingsResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
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
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_settings_mapped_args(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if advanced is not None:
            _body["advanced"] = advanced
        args.body = _body
        if provider is not None:
            _path_params["provider"] = provider
        if organization is not None:
            _path_params["organization"] = organization
        if project is not None:
            _path_params["project"] = project
        args.path = _path_params
        return args

    async def _aupdate_settings_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        🧪 Update project settings
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/project/{provider}/{organization}/{project}/settings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_project_settings.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _update_settings_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        🧪 Update project settings
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/project/{provider}/{organization}/{project}/settings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_project_settings.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class UpdateSettingsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
            advanced=advanced,
        )
        return await self._aupdate_settings_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
            advanced=advanced,
        )
        return self._update_settings_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateSettings(BaseApi):

    async def aupdate_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProjectSettingsPydantic:
        raw_response = await self.raw.aupdate_settings(
            provider=provider,
            organization=organization,
            project=project,
            advanced=advanced,
            **kwargs,
        )
        if validate:
            return ProjectSettingsPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectSettingsPydantic, raw_response.body)
    
    
    def update_settings(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
        validate: bool = False,
    ) -> ProjectSettingsPydantic:
        raw_response = self.raw.update_settings(
            provider=provider,
            organization=organization,
            project=project,
            advanced=advanced,
        )
        if validate:
            return ProjectSettingsPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectSettingsPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
            advanced=advanced,
        )
        return await self._aupdate_settings_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        provider: str,
        organization: str,
        project: str,
        advanced: typing.Optional[ProjectSettingsAdvanced] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_settings_mapped_args(
            provider=provider,
            organization=organization,
            project=project,
            advanced=advanced,
        )
        return self._update_settings_oapg(
            body=args.body,
            path_params=args.path,
        )

