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

from circle_ci_python_sdk.model.patch_claims_request import PatchClaimsRequest as PatchClaimsRequestSchema
from circle_ci_python_sdk.model.oidc_token_management_delete_org_claims_response import OidcTokenManagementDeleteOrgClaimsResponse as OidcTokenManagementDeleteOrgClaimsResponseSchema
from circle_ci_python_sdk.model.claim_response import ClaimResponse as ClaimResponseSchema
from circle_ci_python_sdk.model.oidc_token_management_delete_org_claims403_response import OidcTokenManagementDeleteOrgClaims403Response as OidcTokenManagementDeleteOrgClaims403ResponseSchema
from circle_ci_python_sdk.model.oidc_token_management_delete_org_claims500_response import OidcTokenManagementDeleteOrgClaims500Response as OidcTokenManagementDeleteOrgClaims500ResponseSchema
from circle_ci_python_sdk.model.patch_claims_request_audience import PatchClaimsRequestAudience as PatchClaimsRequestAudienceSchema
from circle_ci_python_sdk.model.json_duration import JSONDuration as JSONDurationSchema

from circle_ci_python_sdk.type.oidc_token_management_delete_org_claims_response import OidcTokenManagementDeleteOrgClaimsResponse
from circle_ci_python_sdk.type.oidc_token_management_delete_org_claims403_response import OidcTokenManagementDeleteOrgClaims403Response
from circle_ci_python_sdk.type.patch_claims_request_audience import PatchClaimsRequestAudience
from circle_ci_python_sdk.type.patch_claims_request import PatchClaimsRequest
from circle_ci_python_sdk.type.json_duration import JSONDuration
from circle_ci_python_sdk.type.claim_response import ClaimResponse
from circle_ci_python_sdk.type.oidc_token_management_delete_org_claims500_response import OidcTokenManagementDeleteOrgClaims500Response

from ...api_client import Dictionary
from circle_ci_python_sdk.pydantic.patch_claims_request import PatchClaimsRequest as PatchClaimsRequestPydantic
from circle_ci_python_sdk.pydantic.json_duration import JSONDuration as JSONDurationPydantic
from circle_ci_python_sdk.pydantic.oidc_token_management_delete_org_claims403_response import OidcTokenManagementDeleteOrgClaims403Response as OidcTokenManagementDeleteOrgClaims403ResponsePydantic
from circle_ci_python_sdk.pydantic.claim_response import ClaimResponse as ClaimResponsePydantic
from circle_ci_python_sdk.pydantic.oidc_token_management_delete_org_claims500_response import OidcTokenManagementDeleteOrgClaims500Response as OidcTokenManagementDeleteOrgClaims500ResponsePydantic
from circle_ci_python_sdk.pydantic.oidc_token_management_delete_org_claims_response import OidcTokenManagementDeleteOrgClaimsResponse as OidcTokenManagementDeleteOrgClaimsResponsePydantic
from circle_ci_python_sdk.pydantic.patch_claims_request_audience import PatchClaimsRequestAudience as PatchClaimsRequestAudiencePydantic

from . import path

# Path params
OrgIDSchema = schemas.UUIDSchema
ProjectIDSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgID': typing.Union[OrgIDSchema, str, uuid.UUID, ],
        'projectID': typing.Union[ProjectIDSchema, str, uuid.UUID, ],
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


request_path_org_id = api_client.PathParameter(
    name="orgID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrgIDSchema,
    required=True,
)
request_path_project_id = api_client.PathParameter(
    name="projectID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectIDSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PatchClaimsRequestSchema


request_body_patch_claims_request = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = ClaimResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ClaimResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ClaimResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = OidcTokenManagementDeleteOrgClaimsResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OidcTokenManagementDeleteOrgClaimsResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OidcTokenManagementDeleteOrgClaimsResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = OidcTokenManagementDeleteOrgClaims403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: OidcTokenManagementDeleteOrgClaims403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: OidcTokenManagementDeleteOrgClaims403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = OidcTokenManagementDeleteOrgClaims500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: OidcTokenManagementDeleteOrgClaims500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: OidcTokenManagementDeleteOrgClaims500Response


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
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_project_claims_mapped_args(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if audience is not None:
            _body["audience"] = audience
        if ttl is not None:
            _body["ttl"] = ttl
        args.body = _body
        if org_id is not None:
            _path_params["orgID"] = org_id
        if project_id is not None:
            _path_params["projectID"] = project_id
        args.path = _path_params
        return args

    async def _aupdate_project_claims_oapg(
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
        Patch project-level claims
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_project_id,
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
            path_template='/org/{orgID}/project/{projectID}/oidc-custom-claims',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_patch_claims_request.serialize(body, content_type)
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


    def _update_project_claims_oapg(
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
        Patch project-level claims
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_project_id,
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
            path_template='/org/{orgID}/project/{projectID}/oidc-custom-claims',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_patch_claims_request.serialize(body, content_type)
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


class UpdateProjectClaimsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_project_claims(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_project_claims_mapped_args(
            org_id=org_id,
            project_id=project_id,
            audience=audience,
            ttl=ttl,
        )
        return await self._aupdate_project_claims_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_project_claims(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_project_claims_mapped_args(
            org_id=org_id,
            project_id=project_id,
            audience=audience,
            ttl=ttl,
        )
        return self._update_project_claims_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateProjectClaims(BaseApi):

    async def aupdate_project_claims(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
        validate: bool = False,
        **kwargs,
    ) -> ClaimResponsePydantic:
        raw_response = await self.raw.aupdate_project_claims(
            org_id=org_id,
            project_id=project_id,
            audience=audience,
            ttl=ttl,
            **kwargs,
        )
        if validate:
            return ClaimResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ClaimResponsePydantic, raw_response.body)
    
    
    def update_project_claims(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
        validate: bool = False,
    ) -> ClaimResponsePydantic:
        raw_response = self.raw.update_project_claims(
            org_id=org_id,
            project_id=project_id,
            audience=audience,
            ttl=ttl,
        )
        if validate:
            return ClaimResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ClaimResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_project_claims_mapped_args(
            org_id=org_id,
            project_id=project_id,
            audience=audience,
            ttl=ttl,
        )
        return await self._aupdate_project_claims_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        project_id: str,
        audience: typing.Optional[PatchClaimsRequestAudience] = None,
        ttl: typing.Optional[JSONDuration] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_project_claims_mapped_args(
            org_id=org_id,
            project_id=project_id,
            audience=audience,
            ttl=ttl,
        )
        return self._update_project_claims_oapg(
            body=args.body,
            path_params=args.path,
        )

