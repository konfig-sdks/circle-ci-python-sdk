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


class WebhookUpdateOutboundWebhookResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "scope",
            "updated-at",
            "name",
            "signing-secret",
            "created-at",
            "id",
            "verify-tls",
            "events",
            "url",
        }
        
        class properties:
            url = schemas.StrSchema
            verify_tls = schemas.BoolSchema
            id = schemas.UUIDSchema
            signing_secret = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            name = schemas.StrSchema
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def scope() -> typing.Type['WebhookUpdateOutboundWebhookResponseScope']:
                return WebhookUpdateOutboundWebhookResponseScope
        
            @staticmethod
            def events() -> typing.Type['WebhookUpdateOutboundWebhookResponseEvents']:
                return WebhookUpdateOutboundWebhookResponseEvents
            __annotations__ = {
                "url": url,
                "verify-tls": verify_tls,
                "id": id,
                "signing-secret": signing_secret,
                "updated-at": updated_at,
                "name": name,
                "created-at": created_at,
                "scope": scope,
                "events": events,
            }
    
    scope: 'WebhookUpdateOutboundWebhookResponseScope'
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    events: 'WebhookUpdateOutboundWebhookResponseEvents'
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verify-tls"]) -> MetaOapg.properties.verify_tls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signing-secret"]) -> MetaOapg.properties.signing_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated-at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> 'WebhookUpdateOutboundWebhookResponseScope': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'WebhookUpdateOutboundWebhookResponseEvents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "verify-tls", "id", "signing-secret", "updated-at", "name", "created-at", "scope", "events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verify-tls"]) -> MetaOapg.properties.verify_tls: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signing-secret"]) -> MetaOapg.properties.signing_secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated-at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> 'WebhookUpdateOutboundWebhookResponseScope': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> 'WebhookUpdateOutboundWebhookResponseEvents': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "verify-tls", "id", "signing-secret", "updated-at", "name", "created-at", "scope", "events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scope: 'WebhookUpdateOutboundWebhookResponseScope',
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        events: 'WebhookUpdateOutboundWebhookResponseEvents',
        url: typing.Union[MetaOapg.properties.url, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookUpdateOutboundWebhookResponse':
        return super().__new__(
            cls,
            *args,
            scope=scope,
            name=name,
            id=id,
            events=events,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.webhook_update_outbound_webhook_response_events import WebhookUpdateOutboundWebhookResponseEvents
from circle_ci_python_sdk.model.webhook_update_outbound_webhook_response_scope import WebhookUpdateOutboundWebhookResponseScope