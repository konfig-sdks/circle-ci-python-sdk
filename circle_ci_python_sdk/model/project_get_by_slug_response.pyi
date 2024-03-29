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


class ProjectGetBySlugResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    NOTE: The definition of Project is subject to change.
    """


    class MetaOapg:
        required = {
            "organization_id",
            "name",
            "organization_slug",
            "vcs_info",
            "id",
            "organization_name",
            "slug",
        }
        
        class properties:
            slug = schemas.StrSchema
            name = schemas.StrSchema
            id = schemas.UUIDSchema
            organization_name = schemas.StrSchema
            organization_slug = schemas.StrSchema
            organization_id = schemas.UUIDSchema
        
            @staticmethod
            def vcs_info() -> typing.Type['ProjectGetBySlugResponseVcsInfo']:
                return ProjectGetBySlugResponseVcsInfo
            __annotations__ = {
                "slug": slug,
                "name": name,
                "id": id,
                "organization_name": organization_name,
                "organization_slug": organization_slug,
                "organization_id": organization_id,
                "vcs_info": vcs_info,
            }
    
    organization_id: MetaOapg.properties.organization_id
    name: MetaOapg.properties.name
    organization_slug: MetaOapg.properties.organization_slug
    vcs_info: 'ProjectGetBySlugResponseVcsInfo'
    id: MetaOapg.properties.id
    organization_name: MetaOapg.properties.organization_name
    slug: MetaOapg.properties.slug
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_name"]) -> MetaOapg.properties.organization_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_slug"]) -> MetaOapg.properties.organization_slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_id"]) -> MetaOapg.properties.organization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vcs_info"]) -> 'ProjectGetBySlugResponseVcsInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["slug", "name", "id", "organization_name", "organization_slug", "organization_id", "vcs_info", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_name"]) -> MetaOapg.properties.organization_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_slug"]) -> MetaOapg.properties.organization_slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_id"]) -> MetaOapg.properties.organization_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vcs_info"]) -> 'ProjectGetBySlugResponseVcsInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["slug", "name", "id", "organization_name", "organization_slug", "organization_id", "vcs_info", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        organization_id: typing.Union[MetaOapg.properties.organization_id, str, uuid.UUID, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        organization_slug: typing.Union[MetaOapg.properties.organization_slug, str, ],
        vcs_info: 'ProjectGetBySlugResponseVcsInfo',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        organization_name: typing.Union[MetaOapg.properties.organization_name, str, ],
        slug: typing.Union[MetaOapg.properties.slug, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectGetBySlugResponse':
        return super().__new__(
            cls,
            *args,
            organization_id=organization_id,
            name=name,
            organization_slug=organization_slug,
            vcs_info=vcs_info,
            id=id,
            organization_name=organization_name,
            slug=slug,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.project_get_by_slug_response_vcs_info import ProjectGetBySlugResponseVcsInfo
