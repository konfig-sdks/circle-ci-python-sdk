import typing_extensions

from circle_ci_python_sdk.apis.tags import TagValues
from circle_ci_python_sdk.apis.tags.project_api import ProjectApi
from circle_ci_python_sdk.apis.tags.context_api import ContextApi
from circle_ci_python_sdk.apis.tags.insights_api import InsightsApi
from circle_ci_python_sdk.apis.tags.pipeline_api import PipelineApi
from circle_ci_python_sdk.apis.tags.policy_management_api import PolicyManagementApi
from circle_ci_python_sdk.apis.tags.oidc_token_management_api import OIDCTokenManagementApi
from circle_ci_python_sdk.apis.tags.workflow_api import WorkflowApi
from circle_ci_python_sdk.apis.tags.webhook_api import WebhookApi
from circle_ci_python_sdk.apis.tags.schedule_api import ScheduleApi
from circle_ci_python_sdk.apis.tags.job_api import JobApi
from circle_ci_python_sdk.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROJECT: ProjectApi,
        TagValues.CONTEXT: ContextApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.PIPELINE: PipelineApi,
        TagValues.POLICY_MANAGEMENT: PolicyManagementApi,
        TagValues.OIDC_TOKEN_MANAGEMENT: OIDCTokenManagementApi,
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.SCHEDULE: ScheduleApi,
        TagValues.JOB: JobApi,
        TagValues.USER: UserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROJECT: ProjectApi,
        TagValues.CONTEXT: ContextApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.PIPELINE: PipelineApi,
        TagValues.POLICY_MANAGEMENT: PolicyManagementApi,
        TagValues.OIDC_TOKEN_MANAGEMENT: OIDCTokenManagementApi,
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.SCHEDULE: ScheduleApi,
        TagValues.JOB: JobApi,
        TagValues.USER: UserApi,
    }
)
