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


class PipelineListUserPipelinesResponseItemsItemTriggerActor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The user who triggered the Pipeline.
    """


    class MetaOapg:
        required = {
            "avatar_url",
            "login",
        }
        
        class properties:
            login = schemas.StrSchema
            avatar_url = schemas.StrSchema
            __annotations__ = {
                "login": login,
                "avatar_url": avatar_url,
            }
    
    avatar_url: MetaOapg.properties.avatar_url
    login: MetaOapg.properties.login
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_url"]) -> MetaOapg.properties.avatar_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["login", "avatar_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_url"]) -> MetaOapg.properties.avatar_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["login", "avatar_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        avatar_url: typing.Union[MetaOapg.properties.avatar_url, str, ],
        login: typing.Union[MetaOapg.properties.login, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PipelineListUserPipelinesResponseItemsItemTriggerActor':
        return super().__new__(
            cls,
            *args,
            avatar_url=avatar_url,
            login=login,
            _configuration=_configuration,
            **kwargs,
        )
