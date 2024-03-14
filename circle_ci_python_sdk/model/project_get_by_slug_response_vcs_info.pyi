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


class ProjectGetBySlugResponseVcsInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the VCS that hosts the project source code.
    """


    class MetaOapg:
        required = {
            "provider",
            "vcs_url",
            "default_branch",
        }
        
        class properties:
            vcs_url = schemas.StrSchema
            
            
            class provider(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BITBUCKET(cls):
                    return cls("Bitbucket")
                
                @schemas.classproperty
                def CIRCLE_CI(cls):
                    return cls("CircleCI")
                
                @schemas.classproperty
                def GIT_HUB(cls):
                    return cls("GitHub")
            default_branch = schemas.StrSchema
            __annotations__ = {
                "vcs_url": vcs_url,
                "provider": provider,
                "default_branch": default_branch,
            }
    
    provider: MetaOapg.properties.provider
    vcs_url: MetaOapg.properties.vcs_url
    default_branch: MetaOapg.properties.default_branch
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vcs_url"]) -> MetaOapg.properties.vcs_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_branch"]) -> MetaOapg.properties.default_branch: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["vcs_url", "provider", "default_branch", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vcs_url"]) -> MetaOapg.properties.vcs_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_branch"]) -> MetaOapg.properties.default_branch: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vcs_url", "provider", "default_branch", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        provider: typing.Union[MetaOapg.properties.provider, str, ],
        vcs_url: typing.Union[MetaOapg.properties.vcs_url, str, ],
        default_branch: typing.Union[MetaOapg.properties.default_branch, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectGetBySlugResponseVcsInfo':
        return super().__new__(
            cls,
            *args,
            provider=provider,
            vcs_url=vcs_url,
            default_branch=default_branch,
            _configuration=_configuration,
            **kwargs,
        )