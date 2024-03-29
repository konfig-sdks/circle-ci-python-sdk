# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from circle_ci_python_sdk.paths.me.get import GetInformation
from circle_ci_python_sdk.paths.user_id.get import GetUserInformation
from circle_ci_python_sdk.paths.me_collaborations.get import ListCollaborations
from circle_ci_python_sdk.apis.tags.user_api_raw import UserApiRaw


class UserApi(
    GetInformation,
    GetUserInformation,
    ListCollaborations,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserApiRaw(api_client)
