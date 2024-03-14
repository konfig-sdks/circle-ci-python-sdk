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

from circle_ci_python_sdk.model.project_create_checkout_keydefault_response import ProjectCreateCheckoutKeydefaultResponse as ProjectCreateCheckoutKeydefaultResponseSchema
from circle_ci_python_sdk.model.project_create_checkout_key_request import ProjectCreateCheckoutKeyRequest as ProjectCreateCheckoutKeyRequestSchema
from circle_ci_python_sdk.model.project_create_checkout_key_response import ProjectCreateCheckoutKeyResponse as ProjectCreateCheckoutKeyResponseSchema

from circle_ci_python_sdk.type.project_create_checkout_keydefault_response import ProjectCreateCheckoutKeydefaultResponse
from circle_ci_python_sdk.type.project_create_checkout_key_response import ProjectCreateCheckoutKeyResponse
from circle_ci_python_sdk.type.project_create_checkout_key_request import ProjectCreateCheckoutKeyRequest

from ...api_client import Dictionary
from circle_ci_python_sdk.pydantic.project_create_checkout_key_request import ProjectCreateCheckoutKeyRequest as ProjectCreateCheckoutKeyRequestPydantic
from circle_ci_python_sdk.pydantic.project_create_checkout_keydefault_response import ProjectCreateCheckoutKeydefaultResponse as ProjectCreateCheckoutKeydefaultResponsePydantic
from circle_ci_python_sdk.pydantic.project_create_checkout_key_response import ProjectCreateCheckoutKeyResponse as ProjectCreateCheckoutKeyResponsePydantic

from . import path

# Path params
ProjectSlugSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'project-slug': typing.Union[ProjectSlugSchema, str, ],
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
# body param
SchemaForRequestBodyApplicationJson = ProjectCreateCheckoutKeyRequestSchema


request_body_project_create_checkout_key_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'api_key_header',
    'api_key_query',
    'basic_auth',
]
SchemaFor201ResponseBodyApplicationJson = ProjectCreateCheckoutKeyResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ProjectCreateCheckoutKeyResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ProjectCreateCheckoutKeyResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ProjectCreateCheckoutKeydefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ProjectCreateCheckoutKeydefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ProjectCreateCheckoutKeydefaultResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_checkout_key_mapped_args(
        self,
        type: str,
        project_slug: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if type is not None:
            _body["type"] = type
        args.body = _body
        if project_slug is not None:
            _path_params["project-slug"] = project_slug
        args.path = _path_params
        return args

    async def _acreate_checkout_key_oapg(
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
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new checkout key
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_slug,
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
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/project/{project-slug}/checkout-key',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_project_create_checkout_key_request.serialize(body, content_type)
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


    def _create_checkout_key_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new checkout key
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_slug,
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
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/project/{project-slug}/checkout-key',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_project_create_checkout_key_request.serialize(body, content_type)
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


class CreateCheckoutKeyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_checkout_key(
        self,
        type: str,
        project_slug: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_checkout_key_mapped_args(
            type=type,
            project_slug=project_slug,
        )
        return await self._acreate_checkout_key_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_checkout_key(
        self,
        type: str,
        project_slug: str,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_checkout_key_mapped_args(
            type=type,
            project_slug=project_slug,
        )
        return self._create_checkout_key_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateCheckoutKey(BaseApi):

    async def acreate_checkout_key(
        self,
        type: str,
        project_slug: str,
        validate: bool = False,
        **kwargs,
    ) -> ProjectCreateCheckoutKeyResponsePydantic:
        raw_response = await self.raw.acreate_checkout_key(
            type=type,
            project_slug=project_slug,
            **kwargs,
        )
        if validate:
            return ProjectCreateCheckoutKeyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectCreateCheckoutKeyResponsePydantic, raw_response.body)
    
    
    def create_checkout_key(
        self,
        type: str,
        project_slug: str,
        validate: bool = False,
    ) -> ProjectCreateCheckoutKeyResponsePydantic:
        raw_response = self.raw.create_checkout_key(
            type=type,
            project_slug=project_slug,
        )
        if validate:
            return ProjectCreateCheckoutKeyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectCreateCheckoutKeyResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        type: str,
        project_slug: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_checkout_key_mapped_args(
            type=type,
            project_slug=project_slug,
        )
        return await self._acreate_checkout_key_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        type: str,
        project_slug: str,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_checkout_key_mapped_args(
            type=type,
            project_slug=project_slug,
        )
        return self._create_checkout_key_oapg(
            body=args.body,
            path_params=args.path,
        )

