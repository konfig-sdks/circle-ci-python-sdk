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


class PatchClaimsRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def audience() -> typing.Type['PatchClaimsRequestAudience']:
                return PatchClaimsRequestAudience
        
            @staticmethod
            def ttl() -> typing.Type['JSONDuration']:
                return JSONDuration
            __annotations__ = {
                "audience": audience,
                "ttl": ttl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience"]) -> 'PatchClaimsRequestAudience': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> 'JSONDuration': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["audience", "ttl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience"]) -> typing.Union['PatchClaimsRequestAudience', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union['JSONDuration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["audience", "ttl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        audience: typing.Union['PatchClaimsRequestAudience', schemas.Unset] = schemas.unset,
        ttl: typing.Union['JSONDuration', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PatchClaimsRequest':
        return super().__new__(
            cls,
            *args,
            audience=audience,
            ttl=ttl,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.json_duration import JSONDuration
from circle_ci_python_sdk.model.patch_claims_request_audience import PatchClaimsRequestAudience