import typing_extensions

from circle_ci_python_sdk.paths import PathValues
from circle_ci_python_sdk.apis.paths.context import Context
from circle_ci_python_sdk.apis.paths.context_context_id import ContextContextId
from circle_ci_python_sdk.apis.paths.context_context_id_environment_variable import ContextContextIdEnvironmentVariable
from circle_ci_python_sdk.apis.paths.context_context_id_environment_variable_env_var_name import ContextContextIdEnvironmentVariableEnvVarName
from circle_ci_python_sdk.apis.paths.insights_pages_project_slug_summary import InsightsPagesProjectSlugSummary
from circle_ci_python_sdk.apis.paths.insights_time_series_project_slug_workflows_workflow_name_jobs import InsightsTimeSeriesProjectSlugWorkflowsWorkflowNameJobs
from circle_ci_python_sdk.apis.paths.insights_org_slug_summary import InsightsOrgSlugSummary
from circle_ci_python_sdk.apis.paths.insights_project_slug_branches import InsightsProjectSlugBranches
from circle_ci_python_sdk.apis.paths.insights_project_slug_flaky_tests import InsightsProjectSlugFlakyTests
from circle_ci_python_sdk.apis.paths.insights_project_slug_workflows import InsightsProjectSlugWorkflows
from circle_ci_python_sdk.apis.paths.insights_project_slug_workflows_workflow_name import InsightsProjectSlugWorkflowsWorkflowName
from circle_ci_python_sdk.apis.paths.insights_project_slug_workflows_workflow_name_jobs import InsightsProjectSlugWorkflowsWorkflowNameJobs
from circle_ci_python_sdk.apis.paths.insights_project_slug_workflows_workflow_name_summary import InsightsProjectSlugWorkflowsWorkflowNameSummary
from circle_ci_python_sdk.apis.paths.insights_project_slug_workflows_workflow_name_test_metrics import InsightsProjectSlugWorkflowsWorkflowNameTestMetrics
from circle_ci_python_sdk.apis.paths.me import Me
from circle_ci_python_sdk.apis.paths.me_collaborations import MeCollaborations
from circle_ci_python_sdk.apis.paths.pipeline import Pipeline
from circle_ci_python_sdk.apis.paths.pipeline_continue import PipelineContinue
from circle_ci_python_sdk.apis.paths.pipeline_pipeline_id import PipelinePipelineId
from circle_ci_python_sdk.apis.paths.pipeline_pipeline_id_config import PipelinePipelineIdConfig
from circle_ci_python_sdk.apis.paths.pipeline_pipeline_id_workflow import PipelinePipelineIdWorkflow
from circle_ci_python_sdk.apis.paths.project_project_slug import ProjectProjectSlug
from circle_ci_python_sdk.apis.paths.project_project_slug_checkout_key import ProjectProjectSlugCheckoutKey
from circle_ci_python_sdk.apis.paths.project_project_slug_checkout_key_fingerprint import ProjectProjectSlugCheckoutKeyFingerprint
from circle_ci_python_sdk.apis.paths.project_project_slug_envvar import ProjectProjectSlugEnvvar
from circle_ci_python_sdk.apis.paths.project_project_slug_envvar_name import ProjectProjectSlugEnvvarName
from circle_ci_python_sdk.apis.paths.project_project_slug_job_job_number import ProjectProjectSlugJobJobNumber
from circle_ci_python_sdk.apis.paths.project_project_slug_job_job_number_cancel import ProjectProjectSlugJobJobNumberCancel
from circle_ci_python_sdk.apis.paths.project_project_slug_pipeline import ProjectProjectSlugPipeline
from circle_ci_python_sdk.apis.paths.project_project_slug_pipeline_mine import ProjectProjectSlugPipelineMine
from circle_ci_python_sdk.apis.paths.project_project_slug_pipeline_pipeline_number import ProjectProjectSlugPipelinePipelineNumber
from circle_ci_python_sdk.apis.paths.project_project_slug_schedule import ProjectProjectSlugSchedule
from circle_ci_python_sdk.apis.paths.project_project_slug_job_number_artifacts import ProjectProjectSlugJobNumberArtifacts
from circle_ci_python_sdk.apis.paths.project_project_slug_job_number_tests import ProjectProjectSlugJobNumberTests
from circle_ci_python_sdk.apis.paths.schedule_schedule_id import ScheduleScheduleId
from circle_ci_python_sdk.apis.paths.user_id import UserId
from circle_ci_python_sdk.apis.paths.webhook import Webhook
from circle_ci_python_sdk.apis.paths.webhook_webhook_id import WebhookWebhookId
from circle_ci_python_sdk.apis.paths.workflow_id import WorkflowId
from circle_ci_python_sdk.apis.paths.workflow_id_approve_approval_request_id import WorkflowIdApproveApprovalRequestId
from circle_ci_python_sdk.apis.paths.workflow_id_cancel import WorkflowIdCancel
from circle_ci_python_sdk.apis.paths.workflow_id_job import WorkflowIdJob
from circle_ci_python_sdk.apis.paths.workflow_id_rerun import WorkflowIdRerun
from circle_ci_python_sdk.apis.paths.org_org_id_oidc_custom_claims import OrgOrgIDOidcCustomClaims
from circle_ci_python_sdk.apis.paths.org_org_id_project_project_id_oidc_custom_claims import OrgOrgIDProjectProjectIDOidcCustomClaims
from circle_ci_python_sdk.apis.paths.owner_owner_id_context_context_decision import OwnerOwnerIDContextContextDecision
from circle_ci_python_sdk.apis.paths.owner_owner_id_context_context_decision_settings import OwnerOwnerIDContextContextDecisionSettings
from circle_ci_python_sdk.apis.paths.owner_owner_id_context_context_decision_decision_id import OwnerOwnerIDContextContextDecisionDecisionID
from circle_ci_python_sdk.apis.paths.owner_owner_id_context_context_decision_decision_id_policy_bundle import OwnerOwnerIDContextContextDecisionDecisionIDPolicyBundle
from circle_ci_python_sdk.apis.paths.owner_owner_id_context_context_policy_bundle import OwnerOwnerIDContextContextPolicyBundle
from circle_ci_python_sdk.apis.paths.owner_owner_id_context_context_policy_bundle_policy_name import OwnerOwnerIDContextContextPolicyBundlePolicyName
from circle_ci_python_sdk.apis.paths.context_context_id_restrictions import ContextContextIdRestrictions
from circle_ci_python_sdk.apis.paths.context_context_id_restrictions_restriction_id import ContextContextIdRestrictionsRestrictionId
from circle_ci_python_sdk.apis.paths.project_provider_organization_project import ProjectProviderOrganizationProject
from circle_ci_python_sdk.apis.paths.project_provider_organization_project_settings import ProjectProviderOrganizationProjectSettings

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CONTEXT: Context,
        PathValues.CONTEXT_CONTEXTID: ContextContextId,
        PathValues.CONTEXT_CONTEXTID_ENVIRONMENTVARIABLE: ContextContextIdEnvironmentVariable,
        PathValues.CONTEXT_CONTEXTID_ENVIRONMENTVARIABLE_ENVVARNAME: ContextContextIdEnvironmentVariableEnvVarName,
        PathValues.INSIGHTS_PAGES_PROJECTSLUG_SUMMARY: InsightsPagesProjectSlugSummary,
        PathValues.INSIGHTS_TIMESERIES_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_JOBS: InsightsTimeSeriesProjectSlugWorkflowsWorkflowNameJobs,
        PathValues.INSIGHTS_ORGSLUG_SUMMARY: InsightsOrgSlugSummary,
        PathValues.INSIGHTS_PROJECTSLUG_BRANCHES: InsightsProjectSlugBranches,
        PathValues.INSIGHTS_PROJECTSLUG_FLAKYTESTS: InsightsProjectSlugFlakyTests,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS: InsightsProjectSlugWorkflows,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME: InsightsProjectSlugWorkflowsWorkflowName,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_JOBS: InsightsProjectSlugWorkflowsWorkflowNameJobs,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_SUMMARY: InsightsProjectSlugWorkflowsWorkflowNameSummary,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_TESTMETRICS: InsightsProjectSlugWorkflowsWorkflowNameTestMetrics,
        PathValues.ME: Me,
        PathValues.ME_COLLABORATIONS: MeCollaborations,
        PathValues.PIPELINE: Pipeline,
        PathValues.PIPELINE_CONTINUE: PipelineContinue,
        PathValues.PIPELINE_PIPELINEID: PipelinePipelineId,
        PathValues.PIPELINE_PIPELINEID_CONFIG: PipelinePipelineIdConfig,
        PathValues.PIPELINE_PIPELINEID_WORKFLOW: PipelinePipelineIdWorkflow,
        PathValues.PROJECT_PROJECTSLUG: ProjectProjectSlug,
        PathValues.PROJECT_PROJECTSLUG_CHECKOUTKEY: ProjectProjectSlugCheckoutKey,
        PathValues.PROJECT_PROJECTSLUG_CHECKOUTKEY_FINGERPRINT: ProjectProjectSlugCheckoutKeyFingerprint,
        PathValues.PROJECT_PROJECTSLUG_ENVVAR: ProjectProjectSlugEnvvar,
        PathValues.PROJECT_PROJECTSLUG_ENVVAR_NAME: ProjectProjectSlugEnvvarName,
        PathValues.PROJECT_PROJECTSLUG_JOB_JOBNUMBER: ProjectProjectSlugJobJobNumber,
        PathValues.PROJECT_PROJECTSLUG_JOB_JOBNUMBER_CANCEL: ProjectProjectSlugJobJobNumberCancel,
        PathValues.PROJECT_PROJECTSLUG_PIPELINE: ProjectProjectSlugPipeline,
        PathValues.PROJECT_PROJECTSLUG_PIPELINE_MINE: ProjectProjectSlugPipelineMine,
        PathValues.PROJECT_PROJECTSLUG_PIPELINE_PIPELINENUMBER: ProjectProjectSlugPipelinePipelineNumber,
        PathValues.PROJECT_PROJECTSLUG_SCHEDULE: ProjectProjectSlugSchedule,
        PathValues.PROJECT_PROJECTSLUG_JOBNUMBER_ARTIFACTS: ProjectProjectSlugJobNumberArtifacts,
        PathValues.PROJECT_PROJECTSLUG_JOBNUMBER_TESTS: ProjectProjectSlugJobNumberTests,
        PathValues.SCHEDULE_SCHEDULEID: ScheduleScheduleId,
        PathValues.USER_ID: UserId,
        PathValues.WEBHOOK: Webhook,
        PathValues.WEBHOOK_WEBHOOKID: WebhookWebhookId,
        PathValues.WORKFLOW_ID: WorkflowId,
        PathValues.WORKFLOW_ID_APPROVE_APPROVAL_REQUEST_ID: WorkflowIdApproveApprovalRequestId,
        PathValues.WORKFLOW_ID_CANCEL: WorkflowIdCancel,
        PathValues.WORKFLOW_ID_JOB: WorkflowIdJob,
        PathValues.WORKFLOW_ID_RERUN: WorkflowIdRerun,
        PathValues.ORG_ORG_ID_OIDCCUSTOMCLAIMS: OrgOrgIDOidcCustomClaims,
        PathValues.ORG_ORG_ID_PROJECT_PROJECT_ID_OIDCCUSTOMCLAIMS: OrgOrgIDProjectProjectIDOidcCustomClaims,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION: OwnerOwnerIDContextContextDecision,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_SETTINGS: OwnerOwnerIDContextContextDecisionSettings,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_DECISION_ID: OwnerOwnerIDContextContextDecisionDecisionID,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_DECISION_ID_POLICYBUNDLE: OwnerOwnerIDContextContextDecisionDecisionIDPolicyBundle,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_POLICYBUNDLE: OwnerOwnerIDContextContextPolicyBundle,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_POLICYBUNDLE_POLICY_NAME: OwnerOwnerIDContextContextPolicyBundlePolicyName,
        PathValues.CONTEXT_CONTEXT_ID_RESTRICTIONS: ContextContextIdRestrictions,
        PathValues.CONTEXT_CONTEXT_ID_RESTRICTIONS_RESTRICTION_ID: ContextContextIdRestrictionsRestrictionId,
        PathValues.PROJECT_PROVIDER_ORGANIZATION_PROJECT: ProjectProviderOrganizationProject,
        PathValues.PROJECT_PROVIDER_ORGANIZATION_PROJECT_SETTINGS: ProjectProviderOrganizationProjectSettings,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CONTEXT: Context,
        PathValues.CONTEXT_CONTEXTID: ContextContextId,
        PathValues.CONTEXT_CONTEXTID_ENVIRONMENTVARIABLE: ContextContextIdEnvironmentVariable,
        PathValues.CONTEXT_CONTEXTID_ENVIRONMENTVARIABLE_ENVVARNAME: ContextContextIdEnvironmentVariableEnvVarName,
        PathValues.INSIGHTS_PAGES_PROJECTSLUG_SUMMARY: InsightsPagesProjectSlugSummary,
        PathValues.INSIGHTS_TIMESERIES_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_JOBS: InsightsTimeSeriesProjectSlugWorkflowsWorkflowNameJobs,
        PathValues.INSIGHTS_ORGSLUG_SUMMARY: InsightsOrgSlugSummary,
        PathValues.INSIGHTS_PROJECTSLUG_BRANCHES: InsightsProjectSlugBranches,
        PathValues.INSIGHTS_PROJECTSLUG_FLAKYTESTS: InsightsProjectSlugFlakyTests,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS: InsightsProjectSlugWorkflows,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME: InsightsProjectSlugWorkflowsWorkflowName,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_JOBS: InsightsProjectSlugWorkflowsWorkflowNameJobs,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_SUMMARY: InsightsProjectSlugWorkflowsWorkflowNameSummary,
        PathValues.INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_TESTMETRICS: InsightsProjectSlugWorkflowsWorkflowNameTestMetrics,
        PathValues.ME: Me,
        PathValues.ME_COLLABORATIONS: MeCollaborations,
        PathValues.PIPELINE: Pipeline,
        PathValues.PIPELINE_CONTINUE: PipelineContinue,
        PathValues.PIPELINE_PIPELINEID: PipelinePipelineId,
        PathValues.PIPELINE_PIPELINEID_CONFIG: PipelinePipelineIdConfig,
        PathValues.PIPELINE_PIPELINEID_WORKFLOW: PipelinePipelineIdWorkflow,
        PathValues.PROJECT_PROJECTSLUG: ProjectProjectSlug,
        PathValues.PROJECT_PROJECTSLUG_CHECKOUTKEY: ProjectProjectSlugCheckoutKey,
        PathValues.PROJECT_PROJECTSLUG_CHECKOUTKEY_FINGERPRINT: ProjectProjectSlugCheckoutKeyFingerprint,
        PathValues.PROJECT_PROJECTSLUG_ENVVAR: ProjectProjectSlugEnvvar,
        PathValues.PROJECT_PROJECTSLUG_ENVVAR_NAME: ProjectProjectSlugEnvvarName,
        PathValues.PROJECT_PROJECTSLUG_JOB_JOBNUMBER: ProjectProjectSlugJobJobNumber,
        PathValues.PROJECT_PROJECTSLUG_JOB_JOBNUMBER_CANCEL: ProjectProjectSlugJobJobNumberCancel,
        PathValues.PROJECT_PROJECTSLUG_PIPELINE: ProjectProjectSlugPipeline,
        PathValues.PROJECT_PROJECTSLUG_PIPELINE_MINE: ProjectProjectSlugPipelineMine,
        PathValues.PROJECT_PROJECTSLUG_PIPELINE_PIPELINENUMBER: ProjectProjectSlugPipelinePipelineNumber,
        PathValues.PROJECT_PROJECTSLUG_SCHEDULE: ProjectProjectSlugSchedule,
        PathValues.PROJECT_PROJECTSLUG_JOBNUMBER_ARTIFACTS: ProjectProjectSlugJobNumberArtifacts,
        PathValues.PROJECT_PROJECTSLUG_JOBNUMBER_TESTS: ProjectProjectSlugJobNumberTests,
        PathValues.SCHEDULE_SCHEDULEID: ScheduleScheduleId,
        PathValues.USER_ID: UserId,
        PathValues.WEBHOOK: Webhook,
        PathValues.WEBHOOK_WEBHOOKID: WebhookWebhookId,
        PathValues.WORKFLOW_ID: WorkflowId,
        PathValues.WORKFLOW_ID_APPROVE_APPROVAL_REQUEST_ID: WorkflowIdApproveApprovalRequestId,
        PathValues.WORKFLOW_ID_CANCEL: WorkflowIdCancel,
        PathValues.WORKFLOW_ID_JOB: WorkflowIdJob,
        PathValues.WORKFLOW_ID_RERUN: WorkflowIdRerun,
        PathValues.ORG_ORG_ID_OIDCCUSTOMCLAIMS: OrgOrgIDOidcCustomClaims,
        PathValues.ORG_ORG_ID_PROJECT_PROJECT_ID_OIDCCUSTOMCLAIMS: OrgOrgIDProjectProjectIDOidcCustomClaims,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION: OwnerOwnerIDContextContextDecision,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_SETTINGS: OwnerOwnerIDContextContextDecisionSettings,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_DECISION_ID: OwnerOwnerIDContextContextDecisionDecisionID,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_DECISION_ID_POLICYBUNDLE: OwnerOwnerIDContextContextDecisionDecisionIDPolicyBundle,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_POLICYBUNDLE: OwnerOwnerIDContextContextPolicyBundle,
        PathValues.OWNER_OWNER_ID_CONTEXT_CONTEXT_POLICYBUNDLE_POLICY_NAME: OwnerOwnerIDContextContextPolicyBundlePolicyName,
        PathValues.CONTEXT_CONTEXT_ID_RESTRICTIONS: ContextContextIdRestrictions,
        PathValues.CONTEXT_CONTEXT_ID_RESTRICTIONS_RESTRICTION_ID: ContextContextIdRestrictionsRestrictionId,
        PathValues.PROJECT_PROVIDER_ORGANIZATION_PROJECT: ProjectProviderOrganizationProject,
        PathValues.PROJECT_PROVIDER_ORGANIZATION_PROJECT_SETTINGS: ProjectProviderOrganizationProjectSettings,
    }
)
