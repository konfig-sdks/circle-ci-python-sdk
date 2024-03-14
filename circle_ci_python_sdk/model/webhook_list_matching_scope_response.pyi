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


class WebhookListMatchingScopeResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of webhooks
    """


    class MetaOapg:
        required = {
            "next_page_token",
            "items",
        }
        
        class properties:
        
            @staticmethod
            def items() -> typing.Type['WebhookListMatchingScopeResponseItems']:
                return WebhookListMatchingScopeResponseItems
            next_page_token = schemas.StrSchema
            __annotations__ = {
                "items": items,
                "next_page_token": next_page_token,
            }
    
    next_page_token: MetaOapg.properties.next_page_token
    items: 'WebhookListMatchingScopeResponseItems'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> 'WebhookListMatchingScopeResponseItems': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_page_token"]) -> MetaOapg.properties.next_page_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["items", "next_page_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> 'WebhookListMatchingScopeResponseItems': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_page_token"]) -> MetaOapg.properties.next_page_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["items", "next_page_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        next_page_token: typing.Union[MetaOapg.properties.next_page_token, str, ],
        items: 'WebhookListMatchingScopeResponseItems',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookListMatchingScopeResponse':
        return super().__new__(
            cls,
            *args,
            next_page_token=next_page_token,
            items=items,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.webhook_list_matching_scope_response_items import WebhookListMatchingScopeResponseItems
