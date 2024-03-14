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


class RestrictionCreated(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            project_id = schemas.UUIDSchema
            name = schemas.StrSchema
            
            
            class restriction_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PROJECT(cls):
                    return cls("project")
                
                @schemas.classproperty
                def EXPRESSION(cls):
                    return cls("expression")
            restriction_value = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "project_id": project_id,
                "name": name,
                "restriction_type": restriction_type,
                "restriction_value": restriction_value,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restriction_type"]) -> MetaOapg.properties.restriction_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restriction_value"]) -> MetaOapg.properties.restriction_value: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["project_id"], typing_extensions.Literal["name"], typing_extensions.Literal["restriction_type"], typing_extensions.Literal["restriction_value"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> typing.Union[MetaOapg.properties.project_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restriction_type"]) -> typing.Union[MetaOapg.properties.restriction_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restriction_value"]) -> typing.Union[MetaOapg.properties.restriction_value, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["project_id"], typing_extensions.Literal["name"], typing_extensions.Literal["restriction_type"], typing_extensions.Literal["restriction_value"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        project_id: typing.Union[MetaOapg.properties.project_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        restriction_type: typing.Union[MetaOapg.properties.restriction_type, str, schemas.Unset] = schemas.unset,
        restriction_value: typing.Union[MetaOapg.properties.restriction_value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'RestrictionCreated':
        return super().__new__(
            cls,
            *args,
            id=id,
            project_id=project_id,
            name=name,
            restriction_type=restriction_type,
            restriction_value=restriction_value,
            _configuration=_configuration,
        )