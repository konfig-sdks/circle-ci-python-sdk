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

from circle_ci_python_sdk.model.schedule_update_scheduledefault_response import ScheduleUpdateScheduledefaultResponse as ScheduleUpdateScheduledefaultResponseSchema
from circle_ci_python_sdk.model.schedule_update_schedule_request_parameters import ScheduleUpdateScheduleRequestParameters as ScheduleUpdateScheduleRequestParametersSchema
from circle_ci_python_sdk.model.schedule_update_schedule_request_timetable import ScheduleUpdateScheduleRequestTimetable as ScheduleUpdateScheduleRequestTimetableSchema
from circle_ci_python_sdk.model.schedule_update_schedule_response import ScheduleUpdateScheduleResponse as ScheduleUpdateScheduleResponseSchema
from circle_ci_python_sdk.model.schedule_update_schedule_request import ScheduleUpdateScheduleRequest as ScheduleUpdateScheduleRequestSchema

from circle_ci_python_sdk.type.schedule_update_schedule_request_parameters import ScheduleUpdateScheduleRequestParameters
from circle_ci_python_sdk.type.schedule_update_scheduledefault_response import ScheduleUpdateScheduledefaultResponse
from circle_ci_python_sdk.type.schedule_update_schedule_request import ScheduleUpdateScheduleRequest
from circle_ci_python_sdk.type.schedule_update_schedule_request_timetable import ScheduleUpdateScheduleRequestTimetable
from circle_ci_python_sdk.type.schedule_update_schedule_response import ScheduleUpdateScheduleResponse

from ...api_client import Dictionary
from circle_ci_python_sdk.pydantic.schedule_update_scheduledefault_response import ScheduleUpdateScheduledefaultResponse as ScheduleUpdateScheduledefaultResponsePydantic
from circle_ci_python_sdk.pydantic.schedule_update_schedule_request import ScheduleUpdateScheduleRequest as ScheduleUpdateScheduleRequestPydantic
from circle_ci_python_sdk.pydantic.schedule_update_schedule_response import ScheduleUpdateScheduleResponse as ScheduleUpdateScheduleResponsePydantic
from circle_ci_python_sdk.pydantic.schedule_update_schedule_request_timetable import ScheduleUpdateScheduleRequestTimetable as ScheduleUpdateScheduleRequestTimetablePydantic
from circle_ci_python_sdk.pydantic.schedule_update_schedule_request_parameters import ScheduleUpdateScheduleRequestParameters as ScheduleUpdateScheduleRequestParametersPydantic

from . import path

# Path params
ScheduleIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'schedule-id': typing.Union[ScheduleIdSchema, str, uuid.UUID, ],
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


request_path_schedule_id = api_client.PathParameter(
    name="schedule-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ScheduleIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ScheduleUpdateScheduleRequestSchema


request_body_schedule_update_schedule_request = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = ScheduleUpdateScheduleResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ScheduleUpdateScheduleResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ScheduleUpdateScheduleResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ScheduleUpdateScheduledefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ScheduleUpdateScheduledefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ScheduleUpdateScheduledefaultResponse


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

    def _update_schedule_mapped_args(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if parameters is not None:
            _body["parameters"] = parameters
        if name is not None:
            _body["name"] = name
        if timetable is not None:
            _body["timetable"] = timetable
        if attribution_actor is not None:
            _body["attribution-actor"] = attribution_actor
        args.body = _body
        if schedule_id is not None:
            _path_params["schedule-id"] = schedule_id
        args.path = _path_params
        return args

    async def _aupdate_schedule_oapg(
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
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update a schedule
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_schedule_id,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/schedule/{schedule-id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_schedule_update_schedule_request.serialize(body, content_type)
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


    def _update_schedule_oapg(
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
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update a schedule
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_schedule_id,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/schedule/{schedule-id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_schedule_update_schedule_request.serialize(body, content_type)
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


class UpdateScheduleRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_schedule(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_schedule_mapped_args(
            schedule_id=schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
        )
        return await self._aupdate_schedule_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_schedule(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_schedule_mapped_args(
            schedule_id=schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
        )
        return self._update_schedule_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateSchedule(BaseApi):

    async def aupdate_schedule(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ScheduleUpdateScheduleResponsePydantic:
        raw_response = await self.raw.aupdate_schedule(
            schedule_id=schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
            **kwargs,
        )
        if validate:
            return ScheduleUpdateScheduleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ScheduleUpdateScheduleResponsePydantic, raw_response.body)
    
    
    def update_schedule(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ScheduleUpdateScheduleResponsePydantic:
        raw_response = self.raw.update_schedule(
            schedule_id=schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
        )
        if validate:
            return ScheduleUpdateScheduleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ScheduleUpdateScheduleResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_schedule_mapped_args(
            schedule_id=schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
        )
        return await self._aupdate_schedule_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        schedule_id: str,
        description: typing.Optional[typing.Optional[str]] = None,
        parameters: typing.Optional[ScheduleUpdateScheduleRequestParameters] = None,
        name: typing.Optional[str] = None,
        timetable: typing.Optional[ScheduleUpdateScheduleRequestTimetable] = None,
        attribution_actor: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_schedule_mapped_args(
            schedule_id=schedule_id,
            description=description,
            parameters=parameters,
            name=name,
            timetable=timetable,
            attribution_actor=attribution_actor,
        )
        return self._update_schedule_oapg(
            body=args.body,
            path_params=args.path,
        )

