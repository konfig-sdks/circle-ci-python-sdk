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


class JobGetTestMetadataResponseItemsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "result",
            "file",
            "classname",
            "run_time",
            "name",
            "source",
            "message",
        }
        
        class properties:
            message = schemas.StrSchema
            source = schemas.StrSchema
            run_time = schemas.Float64Schema
            file = schemas.StrSchema
            result = schemas.StrSchema
            name = schemas.StrSchema
            classname = schemas.StrSchema
            __annotations__ = {
                "message": message,
                "source": source,
                "run_time": run_time,
                "file": file,
                "result": result,
                "name": name,
                "classname": classname,
            }
    
    result: MetaOapg.properties.result
    file: MetaOapg.properties.file
    classname: MetaOapg.properties.classname
    run_time: MetaOapg.properties.run_time
    name: MetaOapg.properties.name
    source: MetaOapg.properties.source
    message: MetaOapg.properties.message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["run_time"]) -> MetaOapg.properties.run_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classname"]) -> MetaOapg.properties.classname: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "source", "run_time", "file", "result", "name", "classname", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["run_time"]) -> MetaOapg.properties.run_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classname"]) -> MetaOapg.properties.classname: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "source", "run_time", "file", "result", "name", "classname", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        result: typing.Union[MetaOapg.properties.result, str, ],
        file: typing.Union[MetaOapg.properties.file, str, ],
        classname: typing.Union[MetaOapg.properties.classname, str, ],
        run_time: typing.Union[MetaOapg.properties.run_time, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        source: typing.Union[MetaOapg.properties.source, str, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobGetTestMetadataResponseItemsItem':
        return super().__new__(
            cls,
            *args,
            result=result,
            file=file,
            classname=classname,
            run_time=run_time,
            name=name,
            source=source,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )
