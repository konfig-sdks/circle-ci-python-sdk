# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from circle_ci_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CONTEXT = "/context"
    CONTEXT_CONTEXTID = "/context/{context-id}"
    CONTEXT_CONTEXTID_ENVIRONMENTVARIABLE = "/context/{context-id}/environment-variable"
    CONTEXT_CONTEXTID_ENVIRONMENTVARIABLE_ENVVARNAME = "/context/{context-id}/environment-variable/{env-var-name}"
    INSIGHTS_PAGES_PROJECTSLUG_SUMMARY = "/insights/pages/{project-slug}/summary"
    INSIGHTS_TIMESERIES_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_JOBS = "/insights/time-series/{project-slug}/workflows/{workflow-name}/jobs"
    INSIGHTS_ORGSLUG_SUMMARY = "/insights/{org-slug}/summary"
    INSIGHTS_PROJECTSLUG_BRANCHES = "/insights/{project-slug}/branches"
    INSIGHTS_PROJECTSLUG_FLAKYTESTS = "/insights/{project-slug}/flaky-tests"
    INSIGHTS_PROJECTSLUG_WORKFLOWS = "/insights/{project-slug}/workflows"
    INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME = "/insights/{project-slug}/workflows/{workflow-name}"
    INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_JOBS = "/insights/{project-slug}/workflows/{workflow-name}/jobs"
    INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_SUMMARY = "/insights/{project-slug}/workflows/{workflow-name}/summary"
    INSIGHTS_PROJECTSLUG_WORKFLOWS_WORKFLOWNAME_TESTMETRICS = "/insights/{project-slug}/workflows/{workflow-name}/test-metrics"
    ME = "/me"
    ME_COLLABORATIONS = "/me/collaborations"
    PIPELINE = "/pipeline"
    PIPELINE_CONTINUE = "/pipeline/continue"
    PIPELINE_PIPELINEID = "/pipeline/{pipeline-id}"
    PIPELINE_PIPELINEID_CONFIG = "/pipeline/{pipeline-id}/config"
    PIPELINE_PIPELINEID_WORKFLOW = "/pipeline/{pipeline-id}/workflow"
    PROJECT_PROJECTSLUG = "/project/{project-slug}"
    PROJECT_PROJECTSLUG_CHECKOUTKEY = "/project/{project-slug}/checkout-key"
    PROJECT_PROJECTSLUG_CHECKOUTKEY_FINGERPRINT = "/project/{project-slug}/checkout-key/{fingerprint}"
    PROJECT_PROJECTSLUG_ENVVAR = "/project/{project-slug}/envvar"
    PROJECT_PROJECTSLUG_ENVVAR_NAME = "/project/{project-slug}/envvar/{name}"
    PROJECT_PROJECTSLUG_JOB_JOBNUMBER = "/project/{project-slug}/job/{job-number}"
    PROJECT_PROJECTSLUG_JOB_JOBNUMBER_CANCEL = "/project/{project-slug}/job/{job-number}/cancel"
    PROJECT_PROJECTSLUG_PIPELINE = "/project/{project-slug}/pipeline"
    PROJECT_PROJECTSLUG_PIPELINE_MINE = "/project/{project-slug}/pipeline/mine"
    PROJECT_PROJECTSLUG_PIPELINE_PIPELINENUMBER = "/project/{project-slug}/pipeline/{pipeline-number}"
    PROJECT_PROJECTSLUG_SCHEDULE = "/project/{project-slug}/schedule"
    PROJECT_PROJECTSLUG_JOBNUMBER_ARTIFACTS = "/project/{project-slug}/{job-number}/artifacts"
    PROJECT_PROJECTSLUG_JOBNUMBER_TESTS = "/project/{project-slug}/{job-number}/tests"
    SCHEDULE_SCHEDULEID = "/schedule/{schedule-id}"
    USER_ID = "/user/{id}"
    WEBHOOK = "/webhook"
    WEBHOOK_WEBHOOKID = "/webhook/{webhook-id}"
    WORKFLOW_ID = "/workflow/{id}"
    WORKFLOW_ID_APPROVE_APPROVAL_REQUEST_ID = "/workflow/{id}/approve/{approval_request_id}"
    WORKFLOW_ID_CANCEL = "/workflow/{id}/cancel"
    WORKFLOW_ID_JOB = "/workflow/{id}/job"
    WORKFLOW_ID_RERUN = "/workflow/{id}/rerun"
    ORG_ORG_ID_OIDCCUSTOMCLAIMS = "/org/{orgID}/oidc-custom-claims"
    ORG_ORG_ID_PROJECT_PROJECT_ID_OIDCCUSTOMCLAIMS = "/org/{orgID}/project/{projectID}/oidc-custom-claims"
    OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION = "/owner/{ownerID}/context/{context}/decision"
    OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_SETTINGS = "/owner/{ownerID}/context/{context}/decision/settings"
    OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_DECISION_ID = "/owner/{ownerID}/context/{context}/decision/{decisionID}"
    OWNER_OWNER_ID_CONTEXT_CONTEXT_DECISION_DECISION_ID_POLICYBUNDLE = "/owner/{ownerID}/context/{context}/decision/{decisionID}/policy-bundle"
    OWNER_OWNER_ID_CONTEXT_CONTEXT_POLICYBUNDLE = "/owner/{ownerID}/context/{context}/policy-bundle"
    OWNER_OWNER_ID_CONTEXT_CONTEXT_POLICYBUNDLE_POLICY_NAME = "/owner/{ownerID}/context/{context}/policy-bundle/{policyName}"
    CONTEXT_CONTEXT_ID_RESTRICTIONS = "/context/{context_id}/restrictions"
    CONTEXT_CONTEXT_ID_RESTRICTIONS_RESTRICTION_ID = "/context/{context_id}/restrictions/{restriction_id}"
    PROJECT_PROVIDER_ORGANIZATION_PROJECT = "/project/{provider}/{organization}/{project}"
    PROJECT_PROVIDER_ORGANIZATION_PROJECT_SETTINGS = "/project/{provider}/{organization}/{project}/settings"