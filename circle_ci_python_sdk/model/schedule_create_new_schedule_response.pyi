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


class ScheduleCreateNewScheduleResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A schedule response
    """


    class MetaOapg:
        required = {
            "actor",
            "project-slug",
            "updated-at",
            "name",
            "description",
            "created-at",
            "id",
            "parameters",
            "timetable",
        }
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def parameters() -> typing.Type['ScheduleCreateNewScheduleResponseParameters']:
                return ScheduleCreateNewScheduleResponseParameters
            id = schemas.UUIDSchema
            
            
            class timetable(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "per-hour",
                                "days-of-week",
                                "hours-of-day",
                            }
                            
                            class properties:
                                per_hour = schemas.IntSchema
                                
                                
                                class hours_of_day(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.IntSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'hours_of_day':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class days_of_week(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def TUE(cls):
                                                return cls("TUE")
                                            
                                            @schemas.classproperty
                                            def SAT(cls):
                                                return cls("SAT")
                                            
                                            @schemas.classproperty
                                            def SUN(cls):
                                                return cls("SUN")
                                            
                                            @schemas.classproperty
                                            def MON(cls):
                                                return cls("MON")
                                            
                                            @schemas.classproperty
                                            def THU(cls):
                                                return cls("THU")
                                            
                                            @schemas.classproperty
                                            def WED(cls):
                                                return cls("WED")
                                            
                                            @schemas.classproperty
                                            def FRI(cls):
                                                return cls("FRI")
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'days_of_week':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class days_of_month(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.IntSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'days_of_month':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class months(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def MAR(cls):
                                                return cls("MAR")
                                            
                                            @schemas.classproperty
                                            def NOV(cls):
                                                return cls("NOV")
                                            
                                            @schemas.classproperty
                                            def DEC(cls):
                                                return cls("DEC")
                                            
                                            @schemas.classproperty
                                            def JUN(cls):
                                                return cls("JUN")
                                            
                                            @schemas.classproperty
                                            def MAY(cls):
                                                return cls("MAY")
                                            
                                            @schemas.classproperty
                                            def OCT(cls):
                                                return cls("OCT")
                                            
                                            @schemas.classproperty
                                            def FEB(cls):
                                                return cls("FEB")
                                            
                                            @schemas.classproperty
                                            def APR(cls):
                                                return cls("APR")
                                            
                                            @schemas.classproperty
                                            def SEP(cls):
                                                return cls("SEP")
                                            
                                            @schemas.classproperty
                                            def AUG(cls):
                                                return cls("AUG")
                                            
                                            @schemas.classproperty
                                            def JAN(cls):
                                                return cls("JAN")
                                            
                                            @schemas.classproperty
                                            def JUL(cls):
                                                return cls("JUL")
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'months':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "per-hour": per_hour,
                                    "hours-of-day": hours_of_day,
                                    "days-of-week": days_of_week,
                                    "days-of-month": days_of_month,
                                    "months": months,
                                }
                        
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["per-hour"]) -> MetaOapg.properties.per_hour: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["hours-of-day"]) -> MetaOapg.properties.hours_of_day: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["days-of-week"]) -> MetaOapg.properties.days_of_week: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["days-of-month"]) -> MetaOapg.properties.days_of_month: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["months"]) -> MetaOapg.properties.months: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["per-hour", "hours-of-day", "days-of-week", "days-of-month", "months", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["per-hour"]) -> MetaOapg.properties.per_hour: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["hours-of-day"]) -> MetaOapg.properties.hours_of_day: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["days-of-week"]) -> MetaOapg.properties.days_of_week: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["days-of-month"]) -> typing.Union[MetaOapg.properties.days_of_month, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["months"]) -> typing.Union[MetaOapg.properties.months, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["per-hour", "hours-of-day", "days-of-week", "days-of-month", "months", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            months: typing.Union[MetaOapg.properties.months, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'any_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                months=months,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class any_of_1(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "days-of-month",
                                "per-hour",
                                "hours-of-day",
                            }
                            
                            class properties:
                                per_hour = schemas.IntSchema
                                
                                
                                class hours_of_day(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.IntSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'hours_of_day':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class days_of_month(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.IntSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'days_of_month':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class days_of_week(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def TUE(cls):
                                                return cls("TUE")
                                            
                                            @schemas.classproperty
                                            def SAT(cls):
                                                return cls("SAT")
                                            
                                            @schemas.classproperty
                                            def SUN(cls):
                                                return cls("SUN")
                                            
                                            @schemas.classproperty
                                            def MON(cls):
                                                return cls("MON")
                                            
                                            @schemas.classproperty
                                            def THU(cls):
                                                return cls("THU")
                                            
                                            @schemas.classproperty
                                            def WED(cls):
                                                return cls("WED")
                                            
                                            @schemas.classproperty
                                            def FRI(cls):
                                                return cls("FRI")
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'days_of_week':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class months(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def MAR(cls):
                                                return cls("MAR")
                                            
                                            @schemas.classproperty
                                            def NOV(cls):
                                                return cls("NOV")
                                            
                                            @schemas.classproperty
                                            def DEC(cls):
                                                return cls("DEC")
                                            
                                            @schemas.classproperty
                                            def JUN(cls):
                                                return cls("JUN")
                                            
                                            @schemas.classproperty
                                            def MAY(cls):
                                                return cls("MAY")
                                            
                                            @schemas.classproperty
                                            def OCT(cls):
                                                return cls("OCT")
                                            
                                            @schemas.classproperty
                                            def FEB(cls):
                                                return cls("FEB")
                                            
                                            @schemas.classproperty
                                            def APR(cls):
                                                return cls("APR")
                                            
                                            @schemas.classproperty
                                            def SEP(cls):
                                                return cls("SEP")
                                            
                                            @schemas.classproperty
                                            def AUG(cls):
                                                return cls("AUG")
                                            
                                            @schemas.classproperty
                                            def JAN(cls):
                                                return cls("JAN")
                                            
                                            @schemas.classproperty
                                            def JUL(cls):
                                                return cls("JUL")
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'months':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "per-hour": per_hour,
                                    "hours-of-day": hours_of_day,
                                    "days-of-month": days_of_month,
                                    "days-of-week": days_of_week,
                                    "months": months,
                                }
                        
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["per-hour"]) -> MetaOapg.properties.per_hour: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["hours-of-day"]) -> MetaOapg.properties.hours_of_day: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["days-of-month"]) -> MetaOapg.properties.days_of_month: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["days-of-week"]) -> MetaOapg.properties.days_of_week: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["months"]) -> MetaOapg.properties.months: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["per-hour", "hours-of-day", "days-of-month", "days-of-week", "months", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["per-hour"]) -> MetaOapg.properties.per_hour: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["hours-of-day"]) -> MetaOapg.properties.hours_of_day: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["days-of-month"]) -> MetaOapg.properties.days_of_month: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["days-of-week"]) -> typing.Union[MetaOapg.properties.days_of_week, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["months"]) -> typing.Union[MetaOapg.properties.months, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["per-hour", "hours-of-day", "days-of-month", "days-of-week", "months", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            months: typing.Union[MetaOapg.properties.months, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'any_of_1':
                            return super().__new__(
                                cls,
                                *args,
                                months=months,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'timetable':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            updated_at = schemas.DateTimeSchema
            name = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            project_slug = schemas.StrSchema
        
            @staticmethod
            def actor() -> typing.Type['ScheduleCreateNewScheduleResponseActor']:
                return ScheduleCreateNewScheduleResponseActor
            __annotations__ = {
                "description": description,
                "parameters": parameters,
                "id": id,
                "timetable": timetable,
                "updated-at": updated_at,
                "name": name,
                "created-at": created_at,
                "project-slug": project_slug,
                "actor": actor,
            }
    
    actor: 'ScheduleCreateNewScheduleResponseActor'
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    parameters: 'ScheduleCreateNewScheduleResponseParameters'
    timetable: MetaOapg.properties.timetable
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> 'ScheduleCreateNewScheduleResponseParameters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timetable"]) -> MetaOapg.properties.timetable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated-at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project-slug"]) -> MetaOapg.properties.project_slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor"]) -> 'ScheduleCreateNewScheduleResponseActor': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "parameters", "id", "timetable", "updated-at", "name", "created-at", "project-slug", "actor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> 'ScheduleCreateNewScheduleResponseParameters': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timetable"]) -> MetaOapg.properties.timetable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated-at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created-at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project-slug"]) -> MetaOapg.properties.project_slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor"]) -> 'ScheduleCreateNewScheduleResponseActor': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "parameters", "id", "timetable", "updated-at", "name", "created-at", "project-slug", "actor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        actor: 'ScheduleCreateNewScheduleResponseActor',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        parameters: 'ScheduleCreateNewScheduleResponseParameters',
        timetable: typing.Union[MetaOapg.properties.timetable, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScheduleCreateNewScheduleResponse':
        return super().__new__(
            cls,
            *args,
            actor=actor,
            name=name,
            description=description,
            id=id,
            parameters=parameters,
            timetable=timetable,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.schedule_create_new_schedule_response_actor import ScheduleCreateNewScheduleResponseActor
from circle_ci_python_sdk.model.schedule_create_new_schedule_response_parameters import ScheduleCreateNewScheduleResponseParameters
