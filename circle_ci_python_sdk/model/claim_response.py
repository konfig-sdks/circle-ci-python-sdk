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


class ClaimResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "org_id",
        }
        
        class properties:
            org_id = schemas.UUIDSchema
        
            @staticmethod
            def audience() -> typing.Type['ClaimResponseAudience']:
                return ClaimResponseAudience
            audience_updated_at = schemas.DateTimeSchema
            project_id = schemas.UUIDSchema
        
            @staticmethod
            def ttl() -> typing.Type['JSONDuration']:
                return JSONDuration
            ttl_updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "org_id": org_id,
                "audience": audience,
                "audience_updated_at": audience_updated_at,
                "project_id": project_id,
                "ttl": ttl,
                "ttl_updated_at": ttl_updated_at,
            }
    
    org_id: MetaOapg.properties.org_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience"]) -> 'ClaimResponseAudience': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience_updated_at"]) -> MetaOapg.properties.audience_updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> 'JSONDuration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl_updated_at"]) -> MetaOapg.properties.ttl_updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["org_id", "audience", "audience_updated_at", "project_id", "ttl", "ttl_updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience"]) -> typing.Union['ClaimResponseAudience', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience_updated_at"]) -> typing.Union[MetaOapg.properties.audience_updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> typing.Union[MetaOapg.properties.project_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union['JSONDuration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl_updated_at"]) -> typing.Union[MetaOapg.properties.ttl_updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["org_id", "audience", "audience_updated_at", "project_id", "ttl", "ttl_updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        org_id: typing.Union[MetaOapg.properties.org_id, str, uuid.UUID, ],
        audience: typing.Union['ClaimResponseAudience', schemas.Unset] = schemas.unset,
        audience_updated_at: typing.Union[MetaOapg.properties.audience_updated_at, str, datetime, schemas.Unset] = schemas.unset,
        project_id: typing.Union[MetaOapg.properties.project_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        ttl: typing.Union['JSONDuration', schemas.Unset] = schemas.unset,
        ttl_updated_at: typing.Union[MetaOapg.properties.ttl_updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClaimResponse':
        return super().__new__(
            cls,
            *args,
            org_id=org_id,
            audience=audience,
            audience_updated_at=audience_updated_at,
            project_id=project_id,
            ttl=ttl,
            ttl_updated_at=ttl_updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.claim_response_audience import ClaimResponseAudience
from circle_ci_python_sdk.model.json_duration import JSONDuration