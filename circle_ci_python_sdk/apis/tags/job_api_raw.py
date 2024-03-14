# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from circle_ci_python_sdk.paths.project_project_slug_job_job_number_cancel.post import CancelWithNumberRaw
from circle_ci_python_sdk.paths.project_project_slug_job_number_artifacts.get import GetArtifactsRaw
from circle_ci_python_sdk.paths.project_project_slug_job_job_number.get import GetDetailsRaw
from circle_ci_python_sdk.paths.project_project_slug_job_number_tests.get import GetTestMetadataRaw


class JobApiRaw(
    CancelWithNumberRaw,
    GetArtifactsRaw,
    GetDetailsRaw,
    GetTestMetadataRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass