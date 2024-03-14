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


class PipelineGetByNumberResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A pipeline response.
    """


    class MetaOapg:
        required = {
            "number",
            "project_slug",
            "created_at",
            "id",
            "state",
            "trigger",
            "errors",
        }
        
        class properties:
            id = schemas.UUIDSchema
        
            @staticmethod
            def errors() -> typing.Type['PipelineGetByNumberResponseErrors']:
                return PipelineGetByNumberResponseErrors
            project_slug = schemas.StrSchema
            number = schemas.Int64Schema
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "created": "CREATED",
                        "errored": "ERRORED",
                        "setup-pending": "SETUPPENDING",
                        "setup": "SETUP",
                        "pending": "PENDING",
                    }
                
                @schemas.classproperty
                def CREATED(cls):
                    return cls("created")
                
                @schemas.classproperty
                def ERRORED(cls):
                    return cls("errored")
                
                @schemas.classproperty
                def SETUPPENDING(cls):
                    return cls("setup-pending")
                
                @schemas.classproperty
                def SETUP(cls):
                    return cls("setup")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def trigger() -> typing.Type['PipelineGetByNumberResponseTrigger']:
                return PipelineGetByNumberResponseTrigger
            updated_at = schemas.DateTimeSchema
        
            @staticmethod
            def trigger_parameters() -> typing.Type['PipelineGetByNumberResponseTriggerParameters']:
                return PipelineGetByNumberResponseTriggerParameters
        
            @staticmethod
            def vcs() -> typing.Type['PipelineGetByNumberResponseVcs']:
                return PipelineGetByNumberResponseVcs
            __annotations__ = {
                "id": id,
                "errors": errors,
                "project_slug": project_slug,
                "number": number,
                "state": state,
                "created_at": created_at,
                "trigger": trigger,
                "updated_at": updated_at,
                "trigger_parameters": trigger_parameters,
                "vcs": vcs,
            }
    
    number: MetaOapg.properties.number
    project_slug: MetaOapg.properties.project_slug
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    state: MetaOapg.properties.state
    trigger: 'PipelineGetByNumberResponseTrigger'
    errors: 'PipelineGetByNumberResponseErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'PipelineGetByNumberResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_slug"]) -> MetaOapg.properties.project_slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> 'PipelineGetByNumberResponseTrigger': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger_parameters"]) -> 'PipelineGetByNumberResponseTriggerParameters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vcs"]) -> 'PipelineGetByNumberResponseVcs': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "errors", "project_slug", "number", "state", "created_at", "trigger", "updated_at", "trigger_parameters", "vcs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'PipelineGetByNumberResponseErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_slug"]) -> MetaOapg.properties.project_slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> 'PipelineGetByNumberResponseTrigger': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger_parameters"]) -> typing.Union['PipelineGetByNumberResponseTriggerParameters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vcs"]) -> typing.Union['PipelineGetByNumberResponseVcs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "errors", "project_slug", "number", "state", "created_at", "trigger", "updated_at", "trigger_parameters", "vcs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, ],
        project_slug: typing.Union[MetaOapg.properties.project_slug, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        trigger: 'PipelineGetByNumberResponseTrigger',
        errors: 'PipelineGetByNumberResponseErrors',
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        trigger_parameters: typing.Union['PipelineGetByNumberResponseTriggerParameters', schemas.Unset] = schemas.unset,
        vcs: typing.Union['PipelineGetByNumberResponseVcs', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PipelineGetByNumberResponse':
        return super().__new__(
            cls,
            *args,
            number=number,
            project_slug=project_slug,
            created_at=created_at,
            id=id,
            state=state,
            trigger=trigger,
            errors=errors,
            updated_at=updated_at,
            trigger_parameters=trigger_parameters,
            vcs=vcs,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.pipeline_get_by_number_response_errors import PipelineGetByNumberResponseErrors
from circle_ci_python_sdk.model.pipeline_get_by_number_response_trigger import PipelineGetByNumberResponseTrigger
from circle_ci_python_sdk.model.pipeline_get_by_number_response_trigger_parameters import PipelineGetByNumberResponseTriggerParameters
from circle_ci_python_sdk.model.pipeline_get_by_number_response_vcs import PipelineGetByNumberResponseVcs
