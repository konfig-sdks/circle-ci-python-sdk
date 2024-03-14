# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from circle_ci_python_sdk.paths.project_project_slug_checkout_key.post import CreateCheckoutKey
from circle_ci_python_sdk.paths.project_project_slug_envvar.post import CreateEnvVar
from circle_ci_python_sdk.paths.project_provider_organization_project.post import CreateProjectDefaultSettings
from circle_ci_python_sdk.paths.project_project_slug_checkout_key_fingerprint.delete import DeleteCheckoutKeyByFingerprint
from circle_ci_python_sdk.paths.project_project_slug_envvar_name.delete import DeleteEnvironmentVariable
from circle_ci_python_sdk.paths.project_project_slug.get import GetBySlug
from circle_ci_python_sdk.paths.project_project_slug_checkout_key_fingerprint.get import GetCheckoutKeyByFingerprint
from circle_ci_python_sdk.paths.project_project_slug_envvar_name.get import GetMaskedEnvVar
from circle_ci_python_sdk.paths.project_provider_organization_project_settings.get import GetSettings
from circle_ci_python_sdk.paths.project_project_slug_checkout_key.get import ListCheckoutKeys
from circle_ci_python_sdk.paths.project_project_slug_envvar.get import ListEnvVarValues
from circle_ci_python_sdk.paths.project_provider_organization_project_settings.patch import UpdateSettings
from circle_ci_python_sdk.apis.tags.project_api_raw import ProjectApiRaw


class ProjectApi(
    CreateCheckoutKey,
    CreateEnvVar,
    CreateProjectDefaultSettings,
    DeleteCheckoutKeyByFingerprint,
    DeleteEnvironmentVariable,
    GetBySlug,
    GetCheckoutKeyByFingerprint,
    GetMaskedEnvVar,
    GetSettings,
    ListCheckoutKeys,
    ListEnvVarValues,
    UpdateSettings,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectApiRaw(api_client)