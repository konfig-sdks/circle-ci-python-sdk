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


class DecisionLogMetadataVcs(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            branch = schemas.StrSchema
            origin_repository_url = schemas.StrSchema
            release_tag = schemas.StrSchema
            target_repository_url = schemas.StrSchema
            __annotations__ = {
                "branch": branch,
                "origin_repository_url": origin_repository_url,
                "release_tag": release_tag,
                "target_repository_url": target_repository_url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branch"]) -> MetaOapg.properties.branch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_repository_url"]) -> MetaOapg.properties.origin_repository_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["release_tag"]) -> MetaOapg.properties.release_tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_repository_url"]) -> MetaOapg.properties.target_repository_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["branch", "origin_repository_url", "release_tag", "target_repository_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branch"]) -> typing.Union[MetaOapg.properties.branch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_repository_url"]) -> typing.Union[MetaOapg.properties.origin_repository_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["release_tag"]) -> typing.Union[MetaOapg.properties.release_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_repository_url"]) -> typing.Union[MetaOapg.properties.target_repository_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["branch", "origin_repository_url", "release_tag", "target_repository_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        branch: typing.Union[MetaOapg.properties.branch, str, schemas.Unset] = schemas.unset,
        origin_repository_url: typing.Union[MetaOapg.properties.origin_repository_url, str, schemas.Unset] = schemas.unset,
        release_tag: typing.Union[MetaOapg.properties.release_tag, str, schemas.Unset] = schemas.unset,
        target_repository_url: typing.Union[MetaOapg.properties.target_repository_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DecisionLogMetadataVcs':
        return super().__new__(
            cls,
            *args,
            branch=branch,
            origin_repository_url=origin_repository_url,
            release_tag=release_tag,
            target_repository_url=target_repository_url,
            _configuration=_configuration,
            **kwargs,
        )