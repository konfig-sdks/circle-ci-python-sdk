# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from circle_ci_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PROJECT = "Project"
    CONTEXT = "Context"
    INSIGHTS = "Insights"
    PIPELINE = "Pipeline"
    POLICY_MANAGEMENT = "Policy Management"
    OIDC_TOKEN_MANAGEMENT = "OIDC Token Management"
    WORKFLOW = "Workflow"
    WEBHOOK = "Webhook"
    SCHEDULE = "Schedule"
    JOB = "Job"
    USER = "User"
