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


class InsightsListProjectBranchesResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Project branches response.
    """


    class MetaOapg:
        required = {
            "project_id",
            "org_id",
            "branches",
        }
        
        class properties:
            org_id = schemas.AnyTypeSchema
            project_id = schemas.AnyTypeSchema
        
            @staticmethod
            def branches() -> typing.Type['InsightsListProjectBranchesResponseBranches']:
                return InsightsListProjectBranchesResponseBranches
            __annotations__ = {
                "org_id": org_id,
                "project_id": project_id,
                "branches": branches,
            }
    
    project_id: MetaOapg.properties.project_id
    org_id: MetaOapg.properties.org_id
    branches: 'InsightsListProjectBranchesResponseBranches'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branches"]) -> 'InsightsListProjectBranchesResponseBranches': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["org_id", "project_id", "branches", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branches"]) -> 'InsightsListProjectBranchesResponseBranches': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["org_id", "project_id", "branches", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        project_id: typing.Union[MetaOapg.properties.project_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        org_id: typing.Union[MetaOapg.properties.org_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        branches: 'InsightsListProjectBranchesResponseBranches',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightsListProjectBranchesResponse':
        return super().__new__(
            cls,
            *args,
            project_id=project_id,
            org_id=org_id,
            branches=branches,
            _configuration=_configuration,
            **kwargs,
        )

from circle_ci_python_sdk.model.insights_list_project_branches_response_branches import InsightsListProjectBranchesResponseBranches