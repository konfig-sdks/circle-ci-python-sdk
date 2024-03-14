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


class PipelineListRecentPipelinesResponseItemsItemTrigger(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A summary of the trigger.
    """


    class MetaOapg:
        required = {
            "actor",
            "received_at",
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SCHEDULED_PIPELINE(cls):
                    return cls("scheduled_pipeline")
                
                @schemas.classproperty
                def EXPLICIT(cls):
                    return cls("explicit")
                
                @schemas.classproperty
                def API(cls):
                    return cls("api")
                
                @schemas.classproperty
                def WEBHOOK(cls):
                    return cls("webhook")
            received_at = schemas.DateTimeSchema
        
            @staticmethod
            def actor() -> typing.Type['PipelineListRecentPipelinesResponseItemsItemTriggerActor']:
                return PipelineListRecentPipelinesResponseItemsItemTriggerActor
            __annotations__ = {
                "type": type,
                "received_at": received_at,
                "actor": actor,
            }
    
    actor: 'PipelineListRecentPipelinesResponseItemsItemTriggerActor'
    received_at: MetaOapg.properties.received_at
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["received_at"]) -> MetaOapg.properties.received_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor"]) -> 'PipelineListRecentPipelinesResponseItemsItemTriggerActor': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "received_at", "actor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["received_at"]) -> MetaOapg.properties.received_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor"]) -> 'PipelineListRecentPipelinesResponseItemsItemTriggerActor': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "received_at", "actor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        actor: 'PipelineListRecentPipelinesResponseItemsItemTriggerActor',
        received_at: typing.Union[MetaOapg.properties.received_at, str, datetime, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PipelineListRecentPipelinesResponseItemsItemTrigger':
        return super().__new__(
            cls,
            *args,
            actor=actor,
            received_at=received_at,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.pipeline_list_recent_pipelines_response_items_item_trigger_actor import PipelineListRecentPipelinesResponseItemsItemTriggerActor