<div align="center">

[![Visit Circleci](./header.png)](https://circleci.com)

# Circleci<a id="circleci"></a>

This describes the resources that make up the CircleCI API v2.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`circleci.context.create_new_context`](#circlecicontextcreate_new_context)
  * [`circleci.context.create_restriction`](#circlecicontextcreate_restriction)
  * [`circleci.context.delete_restriction`](#circlecicontextdelete_restriction)
  * [`circleci.context.get_information`](#circlecicontextget_information)
  * [`circleci.context.get_restrictions`](#circlecicontextget_restrictions)
  * [`circleci.context.list_environment_variables`](#circlecicontextlist_environment_variables)
  * [`circleci.context.list_owner_contexts`](#circlecicontextlist_owner_contexts)
  * [`circleci.context.remove_context`](#circlecicontextremove_context)
  * [`circleci.context.remove_environment_variable`](#circlecicontextremove_environment_variable)
  * [`circleci.context.update_environment_variable`](#circlecicontextupdate_environment_variable)
  * [`circleci.insights.get_flaky_tests`](#circleciinsightsget_flaky_tests)
  * [`circleci.insights.get_job_timeseries_data`](#circleciinsightsget_job_timeseries_data)
  * [`circleci.insights.get_project_summary_metrics`](#circleciinsightsget_project_summary_metrics)
  * [`circleci.insights.get_project_workflow_job_metrics`](#circleciinsightsget_project_workflow_job_metrics)
  * [`circleci.insights.get_project_workflow_metrics`](#circleciinsightsget_project_workflow_metrics)
  * [`circleci.insights.get_project_workflow_test_metrics`](#circleciinsightsget_project_workflow_test_metrics)
  * [`circleci.insights.get_recent_workflow_runs`](#circleciinsightsget_recent_workflow_runs)
  * [`circleci.insights.get_summary_metrics_with_trends`](#circleciinsightsget_summary_metrics_with_trends)
  * [`circleci.insights.get_workflow_summary_metrics`](#circleciinsightsget_workflow_summary_metrics)
  * [`circleci.insights.list_project_branches`](#circleciinsightslist_project_branches)
  * [`circleci.job.cancel_with_number`](#circlecijobcancel_with_number)
  * [`circleci.job.get_artifacts`](#circlecijobget_artifacts)
  * [`circleci.job.get_details`](#circlecijobget_details)
  * [`circleci.job.get_test_metadata`](#circlecijobget_test_metadata)
  * [`circleci.oidc_token_management.delete_org_claims`](#circlecioidc_token_managementdelete_org_claims)
  * [`circleci.oidc_token_management.delete_project_claims`](#circlecioidc_token_managementdelete_project_claims)
  * [`circleci.oidc_token_management.get_org_claims`](#circlecioidc_token_managementget_org_claims)
  * [`circleci.oidc_token_management.get_project_claims`](#circlecioidc_token_managementget_project_claims)
  * [`circleci.oidc_token_management.update_org_claims`](#circlecioidc_token_managementupdate_org_claims)
  * [`circleci.oidc_token_management.update_project_claims`](#circlecioidc_token_managementupdate_project_claims)
  * [`circleci.pipeline.continue_execution`](#circlecipipelinecontinue_execution)
  * [`circleci.pipeline.get_all_pipelines`](#circlecipipelineget_all_pipelines)
  * [`circleci.pipeline.get_by_id`](#circlecipipelineget_by_id)
  * [`circleci.pipeline.get_by_number`](#circlecipipelineget_by_number)
  * [`circleci.pipeline.get_configuration_by_id`](#circlecipipelineget_configuration_by_id)
  * [`circleci.pipeline.list_recent_pipelines`](#circlecipipelinelist_recent_pipelines)
  * [`circleci.pipeline.list_user_pipelines`](#circlecipipelinelist_user_pipelines)
  * [`circleci.pipeline.list_workflows`](#circlecipipelinelist_workflows)
  * [`circleci.pipeline.trigger_new_pipeline`](#circlecipipelinetrigger_new_pipeline)
  * [`circleci.policy_management.create_policy_bundle_for_context`](#circlecipolicy_managementcreate_policy_bundle_for_context)
  * [`circleci.policy_management.evaluate_input_data`](#circlecipolicy_managementevaluate_input_data)
  * [`circleci.policy_management.get_decision_audit_log_by_given_id`](#circlecipolicy_managementget_decision_audit_log_by_given_id)
  * [`circleci.policy_management.get_decision_audit_logs`](#circlecipolicy_managementget_decision_audit_logs)
  * [`circleci.policy_management.get_decision_settings`](#circlecipolicy_managementget_decision_settings)
  * [`circleci.policy_management.get_document`](#circlecipolicy_managementget_document)
  * [`circleci.policy_management.get_policy_bundle`](#circlecipolicy_managementget_policy_bundle)
  * [`circleci.policy_management.get_policy_bundle_for_decision`](#circlecipolicy_managementget_policy_bundle_for_decision)
  * [`circleci.policy_management.modify_decision_settings`](#circlecipolicy_managementmodify_decision_settings)
  * [`circleci.project.create_checkout_key`](#circleciprojectcreate_checkout_key)
  * [`circleci.project.create_env_var`](#circleciprojectcreate_env_var)
  * [`circleci.project.create_project_default_settings`](#circleciprojectcreate_project_default_settings)
  * [`circleci.project.delete_checkout_key_by_fingerprint`](#circleciprojectdelete_checkout_key_by_fingerprint)
  * [`circleci.project.delete_environment_variable`](#circleciprojectdelete_environment_variable)
  * [`circleci.project.get_by_slug`](#circleciprojectget_by_slug)
  * [`circleci.project.get_checkout_key_by_fingerprint`](#circleciprojectget_checkout_key_by_fingerprint)
  * [`circleci.project.get_masked_env_var`](#circleciprojectget_masked_env_var)
  * [`circleci.project.get_settings`](#circleciprojectget_settings)
  * [`circleci.project.list_checkout_keys`](#circleciprojectlist_checkout_keys)
  * [`circleci.project.list_env_var_values`](#circleciprojectlist_env_var_values)
  * [`circleci.project.update_settings`](#circleciprojectupdate_settings)
  * [`circleci.schedule.create_new_schedule`](#circlecischedulecreate_new_schedule)
  * [`circleci.schedule.get_all_schedules`](#circlecischeduleget_all_schedules)
  * [`circleci.schedule.get_by_id`](#circlecischeduleget_by_id)
  * [`circleci.schedule.remove_by_id`](#circlecischeduleremove_by_id)
  * [`circleci.schedule.update_schedule`](#circlecischeduleupdate_schedule)
  * [`circleci.user.get_information`](#circleciuserget_information)
  * [`circleci.user.get_user_information`](#circleciuserget_user_information)
  * [`circleci.user.list_collaborations`](#circleciuserlist_collaborations)
  * [`circleci.webhook.create_outbound_webhook`](#circleciwebhookcreate_outbound_webhook)
  * [`circleci.webhook.delete_outbound_webhook`](#circleciwebhookdelete_outbound_webhook)
  * [`circleci.webhook.get_by_id`](#circleciwebhookget_by_id)
  * [`circleci.webhook.list_matching_scope`](#circleciwebhooklist_matching_scope)
  * [`circleci.webhook.update_outbound_webhook`](#circleciwebhookupdate_outbound_webhook)
  * [`circleci.workflow.approve_job`](#circleciworkflowapprove_job)
  * [`circleci.workflow.cancel_workflow`](#circleciworkflowcancel_workflow)
  * [`circleci.workflow.get_by_id`](#circleciworkflowget_by_id)
  * [`circleci.workflow.get_jobs`](#circleciworkflowget_jobs)
  * [`circleci.workflow.rerun_workflow`](#circleciworkflowrerun_workflow)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=CircleCI&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from circle_ci_python_sdk import CircleCi, ApiException

circleci = CircleCi(
    api_key_header="YOUR_API_KEY",
    api_key_query="YOUR_API_KEY",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)

try:
    # Create a new context
    create_new_context_response = circleci.context.create_new_context(
        name="string_example",
        owner=None,
    )
    print(create_new_context_response)
except ApiException as e:
    print("Exception when calling ContextApi.create_new_context: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from circle_ci_python_sdk import CircleCi, ApiException

circleci = CircleCi(
    api_key_header="YOUR_API_KEY",
    api_key_query="YOUR_API_KEY",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)


async def main():
    try:
        # Create a new context
        create_new_context_response = await circleci.context.acreate_new_context(
            name="string_example",
            owner=None,
        )
        print(create_new_context_response)
    except ApiException as e:
        print("Exception when calling ContextApi.create_new_context: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from circle_ci_python_sdk import CircleCi, ApiException

circleci = CircleCi(
    api_key_header="YOUR_API_KEY",
    api_key_query="YOUR_API_KEY",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)

try:
    # Create a new context
    create_new_context_response = circleci.context.raw.create_new_context(
        name="string_example",
        owner=None,
    )
    pprint(create_new_context_response.body)
    pprint(create_new_context_response.body["id"])
    pprint(create_new_context_response.body["name"])
    pprint(create_new_context_response.body["created_at"])
    pprint(create_new_context_response.headers)
    pprint(create_new_context_response.status)
    pprint(create_new_context_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ContextApi.create_new_context: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `circleci.context.create_new_context`<a id="circlecicontextcreate_new_context"></a>

Creates a new context.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_context_response = circleci.context.create_new_context(
    name="string_example",
    owner=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The user defined name of the context.

##### owner: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="owner-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContextCreateNewContextRequest`](./circle_ci_python_sdk/type/context_create_new_context_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContextCreateNewContextResponse`](./circle_ci_python_sdk/pydantic/context_create_new_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.create_restriction`<a id="circlecicontextcreate_restriction"></a>

[__EXPERIMENTAL__] Creates project restriction on a context.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_restriction_response = circleci.context.create_restriction(
    context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
    project_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    restriction_type="string_example",
    restriction_value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_id: `str`<a id="context_id-str"></a>

An opaque identifier of a context.

##### project_id: `str`<a id="project_id-str"></a>

Deprecated - Use \\\"restriction_type\\\" and \\\"restriction_value\\\" instead.  The project ID to use for a project restriction. This is mutually exclusive with restriction_type and restriction_value and implies restriction_type is \\\"project\\\". 

##### restriction_type: `str`<a id="restriction_type-str"></a>

##### restriction_value: `str`<a id="restriction_value-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContextCreateRestrictionRequest`](./circle_ci_python_sdk/type/context_create_restriction_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RestrictionCreated`](./circle_ci_python_sdk/pydantic/restriction_created.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context_id}/restrictions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.delete_restriction`<a id="circlecicontextdelete_restriction"></a>

[__EXPERIMENTAL__] Deletes a project restriction on a context.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_restriction_response = circleci.context.delete_restriction(
    context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
    restriction_id="1c23d2cb-07b1-4a28-8af3-e369732050ed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_id: `str`<a id="context_id-str"></a>

An opaque identifier of a context.

##### restriction_id: `str`<a id="restriction_id-str"></a>

An opaque identifier of a context restriction.

#### 🔄 Return<a id="🔄-return"></a>

[`RestrictionDeleted`](./circle_ci_python_sdk/pydantic/restriction_deleted.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context_id}/restrictions/{restriction_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.get_information`<a id="circlecicontextget_information"></a>

Returns basic information about a context.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = circleci.context.get_information(
    context_id="context-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_id: `str`<a id="context_id-str"></a>

ID of the context (UUID)

#### 🔄 Return<a id="🔄-return"></a>

[`ContextGetInformationResponse`](./circle_ci_python_sdk/pydantic/context_get_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.get_restrictions`<a id="circlecicontextget_restrictions"></a>

[__EXPERIMENTAL__] Gets a list of project restrictions associated with a context.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_restrictions_response = circleci.context.get_restrictions(
    context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_id: `str`<a id="context_id-str"></a>

An opaque identifier of a context.

#### 🔄 Return<a id="🔄-return"></a>

[`ContextProjectRestrictionsList`](./circle_ci_python_sdk/pydantic/context_project_restrictions_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context_id}/restrictions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.list_environment_variables`<a id="circlecicontextlist_environment_variables"></a>

List information about environment variables in a context, not including their values.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_environment_variables_response = circleci.context.list_environment_variables(
    context_id="context-id_example",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_id: `str`<a id="context_id-str"></a>

ID of the context (UUID)

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

#### 🔄 Return<a id="🔄-return"></a>

[`ContextListEnvironmentVariablesResponse`](./circle_ci_python_sdk/pydantic/context_list_environment_variables_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context-id}/environment-variable` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.list_owner_contexts`<a id="circlecicontextlist_owner_contexts"></a>

List all contexts for an owner.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_owner_contexts_response = circleci.context.list_owner_contexts(
    owner_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    owner_slug="string_example",
    owner_type="account",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

The unique ID of the owner of the context. Specify either this or owner-slug.

##### owner_slug: `str`<a id="owner_slug-str"></a>

A string that represents an organization. Specify either this or owner-id. Cannot be used for accounts.

##### owner_type: `str`<a id="owner_type-str"></a>

The type of the owner. Defaults to \"organization\". Accounts are only used as context owners in server.

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

#### 🔄 Return<a id="🔄-return"></a>

[`ContextListOwnerContextsResponse`](./circle_ci_python_sdk/pydantic/context_list_owner_contexts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.remove_context`<a id="circlecicontextremove_context"></a>

Delete a context

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_context_response = circleci.context.remove_context(
    context_id="context-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### context_id: `str`<a id="context_id-str"></a>

ID of the context (UUID)

#### 🔄 Return<a id="🔄-return"></a>

[`ContextRemoveContextResponse`](./circle_ci_python_sdk/pydantic/context_remove_context_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.remove_environment_variable`<a id="circlecicontextremove_environment_variable"></a>

Delete an environment variable from a context.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_environment_variable_response = circleci.context.remove_environment_variable(
    env_var_name="POSTGRES_USER",
    context_id="context-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### env_var_name: `str`<a id="env_var_name-str"></a>

The name of the environment variable

##### context_id: `str`<a id="context_id-str"></a>

ID of the context (UUID)

#### 🔄 Return<a id="🔄-return"></a>

[`ContextRemoveEnvironmentVariableResponse`](./circle_ci_python_sdk/pydantic/context_remove_environment_variable_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context-id}/environment-variable/{env-var-name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.context.update_environment_variable`<a id="circlecicontextupdate_environment_variable"></a>

Create or update an environment variable within a context. Returns information about the environment variable, not including its value.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_environment_variable_response = circleci.context.update_environment_variable(
    value="some-secret-value",
    context_id="context-id_example",
    env_var_name="POSTGRES_USER",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### value: `str`<a id="value-str"></a>

The value of the environment variable

##### context_id: `str`<a id="context_id-str"></a>

ID of the context (UUID)

##### env_var_name: `str`<a id="env_var_name-str"></a>

The name of the environment variable

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContextUpdateEnvironmentVariableRequest`](./circle_ci_python_sdk/type/context_update_environment_variable_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ContextUpdateEnvironmentVariableResponse`](./circle_ci_python_sdk/pydantic/context_update_environment_variable_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/context/{context-id}/environment-variable/{env-var-name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_flaky_tests`<a id="circleciinsightsget_flaky_tests"></a>

Get a list of flaky tests for a given project. Flaky tests are branch agnostic.
             A flaky test is a test that passed and failed in the same commit.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_flaky_tests_response = circleci.insights.get_flaky_tests(
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetFlakyTestsResponse`](./circle_ci_python_sdk/pydantic/insights_get_flaky_tests_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/flaky-tests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_job_timeseries_data`<a id="circleciinsightsget_job_timeseries_data"></a>

Get timeseries data for all jobs within a workflow. Hourly granularity data is only retained for 48 hours while daily granularity data is retained for 90 days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_timeseries_data_response = circleci.insights.get_job_timeseries_data(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
    branch="string_example",
    granularity="hourly",
    start_date="2020-08-21T13:26:29Z",
    end_date="2020-09-04T13:26:29Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### workflow_name: `str`<a id="workflow_name-str"></a>

The name of the workflow.

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch. If not passed we will scope the API call to the default branch.

##### granularity: `str`<a id="granularity-str"></a>

The granularity for which to query timeseries data.

##### start_date: `datetime`<a id="start_date-datetime"></a>

Include only executions that started at or after this date. This must be specified if an end-date is provided.

##### end_date: `datetime`<a id="end_date-datetime"></a>

Include only executions that started before this date. This date can be at most 90 days after the start-date.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetJobTimeseriesDataResponse`](./circle_ci_python_sdk/pydantic/insights_get_job_timeseries_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/time-series/{project-slug}/workflows/{workflow-name}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_project_summary_metrics`<a id="circleciinsightsget_project_summary_metrics"></a>

Get summary metrics and trends for a project at workflow and branch level.
             Workflow runs going back at most 90 days are included in the aggregation window.
             Trends are only supported upto last 30 days.
             Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_summary_metrics_response = circleci.insights.get_project_summary_metrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    reporting_window="last-90-days",
    branches={},
    workflow_names={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### reporting_window: `str`<a id="reporting_window-str"></a>

The time window used to calculate summary metrics. If not provided, defaults to last-90-days

##### branches: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="branches-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The names of VCS branches to include in branch-level workflow metrics.

##### workflow_names: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="workflow_names-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The names of workflows to include in workflow-level metrics.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetProjectSummaryMetricsResponse`](./circle_ci_python_sdk/pydantic/insights_get_project_summary_metrics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/pages/{project-slug}/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_project_workflow_job_metrics`<a id="circleciinsightsget_project_workflow_job_metrics"></a>

Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_workflow_job_metrics_response = (
    circleci.insights.get_project_workflow_job_metrics(
        project_slug="gh/CircleCI-Public/api-preview-docs",
        workflow_name="build-and-test",
        page_token="string_example",
        all_branches=True,
        branch="string_example",
        reporting_window="last-90-days",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### workflow_name: `str`<a id="workflow_name-str"></a>

The name of the workflow.

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

##### all_branches: `bool`<a id="all_branches-bool"></a>

Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch. If not passed we will scope the API call to the default branch.

##### reporting_window: `str`<a id="reporting_window-str"></a>

The time window used to calculate summary metrics. If not provided, defaults to last-90-days

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetProjectWorkflowJobMetricsResponse`](./circle_ci_python_sdk/pydantic/insights_get_project_workflow_job_metrics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/workflows/{workflow-name}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_project_workflow_metrics`<a id="circleciinsightsget_project_workflow_metrics"></a>

Get summary metrics for a project's workflows.  Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours.  Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_workflow_metrics_response = circleci.insights.get_project_workflow_metrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    page_token="string_example",
    all_branches=True,
    branch="string_example",
    reporting_window="last-90-days",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

##### all_branches: `bool`<a id="all_branches-bool"></a>

Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch. If not passed we will scope the API call to the default branch.

##### reporting_window: `str`<a id="reporting_window-str"></a>

The time window used to calculate summary metrics. If not provided, defaults to last-90-days

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetProjectWorkflowMetricsResponse`](./circle_ci_python_sdk/pydantic/insights_get_project_workflow_metrics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/workflows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_project_workflow_test_metrics`<a id="circleciinsightsget_project_workflow_test_metrics"></a>

Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_workflow_test_metrics_response = (
    circleci.insights.get_project_workflow_test_metrics(
        project_slug="gh/CircleCI-Public/api-preview-docs",
        workflow_name="build-and-test",
        branch="string_example",
        all_branches=True,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### workflow_name: `str`<a id="workflow_name-str"></a>

The name of the workflow.

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch. If not passed we will scope the API call to the default branch.

##### all_branches: `bool`<a id="all_branches-bool"></a>

Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetProjectWorkflowTestMetricsResponse`](./circle_ci_python_sdk/pydantic/insights_get_project_workflow_test_metrics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/workflows/{workflow-name}/test-metrics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_recent_workflow_runs`<a id="circleciinsightsget_recent_workflow_runs"></a>

Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_workflow_runs_response = circleci.insights.get_recent_workflow_runs(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
    all_branches=True,
    branch="string_example",
    page_token="string_example",
    start_date="2020-08-21T13:26:29Z",
    end_date="2020-09-04T13:26:29Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### workflow_name: `str`<a id="workflow_name-str"></a>

The name of the workflow.

##### all_branches: `bool`<a id="all_branches-bool"></a>

Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch. If not passed we will scope the API call to the default branch.

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

##### start_date: `datetime`<a id="start_date-datetime"></a>

Include only executions that started at or after this date. This must be specified if an end-date is provided.

##### end_date: `datetime`<a id="end_date-datetime"></a>

Include only executions that started before this date. This date can be at most 90 days after the start-date.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetRecentWorkflowRunsResponse`](./circle_ci_python_sdk/pydantic/insights_get_recent_workflow_runs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/workflows/{workflow-name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_summary_metrics_with_trends`<a id="circleciinsightsget_summary_metrics_with_trends"></a>

Gets aggregated summary metrics with trends for the entire org.
              Also gets aggregated metrics and trends for each project belonging to the org.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_summary_metrics_with_trends_response = (
    circleci.insights.get_summary_metrics_with_trends(
        org_slug="gh/CircleCI-Public",
        reporting_window="last-90-days",
        project_names={},
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_slug: `str`<a id="org_slug-str"></a>

Org slug in the form `vcs-slug/org-name`. The `/` characters may be URL-escaped.

##### reporting_window: `str`<a id="reporting_window-str"></a>

The time window used to calculate summary metrics. If not provided, defaults to last-90-days

##### project_names: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="project_names-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

List of project names.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetSummaryMetricsWithTrendsResponse`](./circle_ci_python_sdk/pydantic/insights_get_summary_metrics_with_trends_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{org-slug}/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.get_workflow_summary_metrics`<a id="circleciinsightsget_workflow_summary_metrics"></a>

Get the metrics and trends for a particular workflow on a single branch or all branches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workflow_summary_metrics_response = circleci.insights.get_workflow_summary_metrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
    all_branches=True,
    branch="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### workflow_name: `str`<a id="workflow_name-str"></a>

The name of the workflow.

##### all_branches: `bool`<a id="all_branches-bool"></a>

Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch. If not passed we will scope the API call to the default branch.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsGetWorkflowSummaryMetricsResponse`](./circle_ci_python_sdk/pydantic/insights_get_workflow_summary_metrics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/workflows/{workflow-name}/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.insights.list_project_branches`<a id="circleciinsightslist_project_branches"></a>

Get a list of all branches for a specified project. The list will only contain branches currently available within Insights. The maximum number of branches returned by this endpoint is 5,000.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_project_branches_response = circleci.insights.list_project_branches(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### workflow_name: `str`<a id="workflow_name-str"></a>

The name of a workflow. If not passed we will scope the API call to the project.

#### 🔄 Return<a id="🔄-return"></a>

[`InsightsListProjectBranchesResponse`](./circle_ci_python_sdk/pydantic/insights_list_project_branches_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/insights/{project-slug}/branches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.job.cancel_with_number`<a id="circlecijobcancel_with_number"></a>

Cancel job with a given job number.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_with_number_response = circleci.job.cancel_with_number(
    job_number=None,
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./circle_ci_python_sdk/type/.py)<a id="job_number-unionbool-date-datetime-dict-float-int-list-str-nonecircle_ci_python_sdktypepy"></a>

The number of the job.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`JobCancelWithNumberResponse`](./circle_ci_python_sdk/pydantic/job_cancel_with_number_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/job/{job-number}/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.job.get_artifacts`<a id="circlecijobget_artifacts"></a>

Returns a job's artifacts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_artifacts_response = circleci.job.get_artifacts(
    job_number=None,
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./circle_ci_python_sdk/type/.py)<a id="job_number-unionbool-date-datetime-dict-float-int-list-str-nonecircle_ci_python_sdktypepy"></a>

The number of the job.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`JobGetArtifactsResponse`](./circle_ci_python_sdk/pydantic/job_get_artifacts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/{job-number}/artifacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.job.get_details`<a id="circlecijobget_details"></a>

Returns job details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = circleci.job.get_details(
    job_number=None,
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./circle_ci_python_sdk/type/.py)<a id="job_number-unionbool-date-datetime-dict-float-int-list-str-nonecircle_ci_python_sdktypepy"></a>

The number of the job.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`JobGetDetailsResponse`](./circle_ci_python_sdk/pydantic/job_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/job/{job-number}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.job.get_test_metadata`<a id="circlecijobget_test_metadata"></a>

Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_test_metadata_response = circleci.job.get_test_metadata(
    job_number=None,
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./circle_ci_python_sdk/type/.py)<a id="job_number-unionbool-date-datetime-dict-float-int-list-str-nonecircle_ci_python_sdktypepy"></a>

The number of the job.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`JobGetTestMetadataResponse`](./circle_ci_python_sdk/pydantic/job_get_test_metadata_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/{job-number}/tests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.oidc_token_management.delete_org_claims`<a id="circlecioidc_token_managementdelete_org_claims"></a>

Deletes org-level custom claims of OIDC identity tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_org_claims_response = circleci.oidc_token_management.delete_org_claims(
    org_id="orgID_example",
    claims="claims_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### claims: `str`<a id="claims-str"></a>

comma separated list of claims to delete. Valid values are \"audience\" and \"ttl\".

#### 🔄 Return<a id="🔄-return"></a>

[`ClaimResponse`](./circle_ci_python_sdk/pydantic/claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{orgID}/oidc-custom-claims` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.oidc_token_management.delete_project_claims`<a id="circlecioidc_token_managementdelete_project_claims"></a>

Deletes project-level custom claims of OIDC identity tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_project_claims_response = circleci.oidc_token_management.delete_project_claims(
    org_id="orgID_example",
    project_id="projectID_example",
    claims="claims_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### project_id: `str`<a id="project_id-str"></a>

##### claims: `str`<a id="claims-str"></a>

comma separated list of claims to delete. Valid values are \"audience\" and \"ttl\".

#### 🔄 Return<a id="🔄-return"></a>

[`ClaimResponse`](./circle_ci_python_sdk/pydantic/claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{orgID}/project/{projectID}/oidc-custom-claims` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.oidc_token_management.get_org_claims`<a id="circlecioidc_token_managementget_org_claims"></a>

Fetches org-level custom claims of OIDC identity tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_org_claims_response = circleci.oidc_token_management.get_org_claims(
    org_id="orgID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ClaimResponse`](./circle_ci_python_sdk/pydantic/claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{orgID}/oidc-custom-claims` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.oidc_token_management.get_project_claims`<a id="circlecioidc_token_managementget_project_claims"></a>

Fetches project-level custom claims of OIDC identity tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_claims_response = circleci.oidc_token_management.get_project_claims(
    org_id="orgID_example",
    project_id="projectID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### project_id: `str`<a id="project_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ClaimResponse`](./circle_ci_python_sdk/pydantic/claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{orgID}/project/{projectID}/oidc-custom-claims` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.oidc_token_management.update_org_claims`<a id="circlecioidc_token_managementupdate_org_claims"></a>

Creates/Updates org-level custom claims of OIDC identity tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_org_claims_response = circleci.oidc_token_management.update_org_claims(
    org_id="orgID_example",
    audience=["string_example"],
    ttl="80728m0015280217980962255008507620686293393339756506851391026912917327294786014820265d1272755041757701929816286488291663322877d21919116647837856387556598683615248784425528468720999697682157936442848967131857636391s382249351630745068057172793570606620664962415415434479790599868759540626151494012626w19118476173237968022090825677715773090491175877238622700367804481067589385995284318716971w809437255518186242126631124808712420936114222s",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### audience: [`PatchClaimsRequestAudience`](./circle_ci_python_sdk/type/patch_claims_request_audience.py)<a id="audience-patchclaimsrequestaudiencecircle_ci_python_sdktypepatch_claims_request_audiencepy"></a>

##### ttl: [`JSONDuration`](./circle_ci_python_sdk/type/json_duration.py)<a id="ttl-jsondurationcircle_ci_python_sdktypejson_durationpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchClaimsRequest`](./circle_ci_python_sdk/type/patch_claims_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClaimResponse`](./circle_ci_python_sdk/pydantic/claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{orgID}/oidc-custom-claims` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.oidc_token_management.update_project_claims`<a id="circlecioidc_token_managementupdate_project_claims"></a>

Creates/Updates project-level custom claims of OIDC identity tokens

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_project_claims_response = circleci.oidc_token_management.update_project_claims(
    org_id="orgID_example",
    project_id="projectID_example",
    audience=["string_example"],
    ttl="80728m0015280217980962255008507620686293393339756506851391026912917327294786014820265d1272755041757701929816286488291663322877d21919116647837856387556598683615248784425528468720999697682157936442848967131857636391s382249351630745068057172793570606620664962415415434479790599868759540626151494012626w19118476173237968022090825677715773090491175877238622700367804481067589385995284318716971w809437255518186242126631124808712420936114222s",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_id: `str`<a id="org_id-str"></a>

##### project_id: `str`<a id="project_id-str"></a>

##### audience: [`PatchClaimsRequestAudience`](./circle_ci_python_sdk/type/patch_claims_request_audience.py)<a id="audience-patchclaimsrequestaudiencecircle_ci_python_sdktypepatch_claims_request_audiencepy"></a>

##### ttl: [`JSONDuration`](./circle_ci_python_sdk/type/json_duration.py)<a id="ttl-jsondurationcircle_ci_python_sdktypejson_durationpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchClaimsRequest`](./circle_ci_python_sdk/type/patch_claims_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClaimResponse`](./circle_ci_python_sdk/pydantic/claim_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/org/{orgID}/project/{projectID}/oidc-custom-claims` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.continue_execution`<a id="circlecipipelinecontinue_execution"></a>

Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
continue_execution_response = circleci.pipeline.continue_execution(
    continuation_key="string_example",
    configuration="string_example",
    parameters={
        "key": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### continuation_key: `str`<a id="continuation_key-str"></a>

A pipeline continuation key.

##### configuration: `str`<a id="configuration-str"></a>

A configuration string for the pipeline.

##### parameters: [`PipelineContinueExecutionRequestParameters`](./circle_ci_python_sdk/type/pipeline_continue_execution_request_parameters.py)<a id="parameters-pipelinecontinueexecutionrequestparameterscircle_ci_python_sdktypepipeline_continue_execution_request_parameterspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PipelineContinueExecutionRequest`](./circle_ci_python_sdk/type/pipeline_continue_execution_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PipelineContinueExecutionResponse`](./circle_ci_python_sdk/pydantic/pipeline_continue_execution_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pipeline/continue` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.get_all_pipelines`<a id="circlecipipelineget_all_pipelines"></a>

Returns all pipelines for this project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_pipelines_response = circleci.pipeline.get_all_pipelines(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    branch="string_example",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### branch: `str`<a id="branch-str"></a>

The name of a vcs branch.

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineGetAllPipelinesResponse`](./circle_ci_python_sdk/pydantic/pipeline_get_all_pipelines_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/pipeline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.get_by_id`<a id="circlecipipelineget_by_id"></a>

Returns a pipeline by the pipeline ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = circleci.pipeline.get_by_id(
    pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pipeline_id: `str`<a id="pipeline_id-str"></a>

The unique ID of the pipeline.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineGetByIdResponse`](./circle_ci_python_sdk/pydantic/pipeline_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pipeline/{pipeline-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.get_by_number`<a id="circlecipipelineget_by_number"></a>

Returns a pipeline by the pipeline number.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_number_response = circleci.pipeline.get_by_number(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    pipeline_number=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### pipeline_number: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./circle_ci_python_sdk/type/.py)<a id="pipeline_number-unionbool-date-datetime-dict-float-int-list-str-nonecircle_ci_python_sdktypepy"></a>

The number of the pipeline.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineGetByNumberResponse`](./circle_ci_python_sdk/pydantic/pipeline_get_by_number_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/pipeline/{pipeline-number}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.get_configuration_by_id`<a id="circlecipipelineget_configuration_by_id"></a>

Returns a pipeline's configuration by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configuration_by_id_response = circleci.pipeline.get_configuration_by_id(
    pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pipeline_id: `str`<a id="pipeline_id-str"></a>

The unique ID of the pipeline.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineGetConfigurationByIdResponse`](./circle_ci_python_sdk/pydantic/pipeline_get_configuration_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pipeline/{pipeline-id}/config` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.list_recent_pipelines`<a id="circlecipipelinelist_recent_pipelines"></a>

Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_recent_pipelines_response = circleci.pipeline.list_recent_pipelines(
    org_slug="gh/CircleCI-Public",
    page_token="string_example",
    mine=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### org_slug: `str`<a id="org_slug-str"></a>

Org slug in the form `vcs-slug/org-name`. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug` and replace the `org-name` with the organization ID (found in Organization Settings).

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

##### mine: `bool`<a id="mine-bool"></a>

Only include entries created by your user.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineListRecentPipelinesResponse`](./circle_ci_python_sdk/pydantic/pipeline_list_recent_pipelines_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pipeline` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.list_user_pipelines`<a id="circlecipipelinelist_user_pipelines"></a>

Returns a sequence of all pipelines for this project triggered by the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_pipelines_response = circleci.pipeline.list_user_pipelines(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineListUserPipelinesResponse`](./circle_ci_python_sdk/pydantic/pipeline_list_user_pipelines_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/pipeline/mine` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.list_workflows`<a id="circlecipipelinelist_workflows"></a>

Returns a paginated list of workflows by pipeline ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_workflows_response = circleci.pipeline.list_workflows(
    pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pipeline_id: `str`<a id="pipeline_id-str"></a>

The unique ID of the pipeline.

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

#### 🔄 Return<a id="🔄-return"></a>

[`PipelineListWorkflowsResponse`](./circle_ci_python_sdk/pydantic/pipeline_list_workflows_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pipeline/{pipeline-id}/workflow` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.pipeline.trigger_new_pipeline`<a id="circlecipipelinetrigger_new_pipeline"></a>

Not yet available to projects that use GitLab or GitHub App. Triggers a new pipeline on the project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_new_pipeline_response = circleci.pipeline.trigger_new_pipeline(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    parameters={
        "key": 1,
    },
    branch="feature/design-new-api",
    tag="v3.1.4159",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### parameters: [`PipelineTriggerNewPipelineRequestParameters`](./circle_ci_python_sdk/type/pipeline_trigger_new_pipeline_request_parameters.py)<a id="parameters-pipelinetriggernewpipelinerequestparameterscircle_ci_python_sdktypepipeline_trigger_new_pipeline_request_parameterspy"></a>

##### branch: `str`<a id="branch-str"></a>

The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).

##### tag: `str`<a id="tag-str"></a>

The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PipelineTriggerNewPipelineRequest`](./circle_ci_python_sdk/type/pipeline_trigger_new_pipeline_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PipelineTriggerNewPipelineResponse`](./circle_ci_python_sdk/pydantic/pipeline_trigger_new_pipeline_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/pipeline` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.create_policy_bundle_for_context`<a id="circlecipolicy_managementcreate_policy_bundle_for_context"></a>

This endpoint replaces the current policy bundle with the provided policy bundle

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_policy_bundle_for_context_response = (
    circleci.policy_management.create_policy_bundle_for_context(
        owner_id="ownerID_example",
        context="context_example",
        policies={
            "key": "string_example",
        },
        dry=True,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### policies: [`BundlePayloadPolicies`](./circle_ci_python_sdk/type/bundle_payload_policies.py)<a id="policies-bundlepayloadpoliciescircle_ci_python_sdktypebundle_payload_policiespy"></a>

##### dry: `bool`<a id="dry-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BundlePayload`](./circle_ci_python_sdk/type/bundle_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BundleDiff`](./circle_ci_python_sdk/pydantic/bundle_diff.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/policy-bundle` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.evaluate_input_data`<a id="circlecipolicy_managementevaluate_input_data"></a>

This endpoint will evaluate input data (config+metadata) against owner's stored policies and return a decision.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
evaluate_input_data_response = circleci.policy_management.evaluate_input_data(
    input="string_example",
    owner_id="ownerID_example",
    context="context_example",
    metadata={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### input: `str`<a id="input-str"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PolicyManagementEvaluateInputDataRequest`](./circle_ci_python_sdk/type/policy_management_evaluate_input_data_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Decision`](./circle_ci_python_sdk/pydantic/decision.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/decision` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.get_decision_audit_log_by_given_id`<a id="circlecipolicy_managementget_decision_audit_log_by_given_id"></a>

This endpoint will retrieve a decision for a given decision log ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_decision_audit_log_by_given_id_response = (
    circleci.policy_management.get_decision_audit_log_by_given_id(
        owner_id="ownerID_example",
        context="context_example",
        decision_id="decisionID_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### decision_id: `str`<a id="decision_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DecisionLog`](./circle_ci_python_sdk/pydantic/decision_log.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/decision/{decisionID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.get_decision_audit_logs`<a id="circlecipolicy_managementget_decision_audit_logs"></a>

This endpoint will return a list of decision audit logs that were made using this owner's policies.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_decision_audit_logs_response = circleci.policy_management.get_decision_audit_logs(
    owner_id="ownerID_example",
    context="context_example",
    status="string_example",
    after="1970-01-01T00:00:00.00Z",
    before="1970-01-01T00:00:00.00Z",
    branch="string_example",
    project_id="string_example",
    build_number="string_example",
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### status: `str`<a id="status-str"></a>

Return decisions matching this decision status.

##### after: `datetime`<a id="after-datetime"></a>

Return decisions made after this date.

##### before: `datetime`<a id="before-datetime"></a>

Return decisions made before this date.

##### branch: `str`<a id="branch-str"></a>

Return decisions made on this branch.

##### project_id: `str`<a id="project_id-str"></a>

Return decisions made for this project.

##### build_number: `str`<a id="build_number-str"></a>

Return decisions made for this build number.

##### offset: `int`<a id="offset-int"></a>

Sets the offset when retrieving the decisions, for paging.

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyManagementGetDecisionAuditLogsResponse`](./circle_ci_python_sdk/pydantic/policy_management_get_decision_audit_logs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/decision` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.get_decision_settings`<a id="circlecipolicy_managementget_decision_settings"></a>

This endpoint retrieves the current decision settings (eg enable/disable policy evaluation)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_decision_settings_response = circleci.policy_management.get_decision_settings(
    owner_id="ownerID_example",
    context="context_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DecisionSettings`](./circle_ci_python_sdk/pydantic/decision_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/decision/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.get_document`<a id="circlecipolicy_managementget_document"></a>

This endpoint will retrieve a policy document.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_response = circleci.policy_management.get_document(
    owner_id="ownerID_example",
    context="context_example",
    policy_name="policyName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### policy_name: `str`<a id="policy_name-str"></a>

the policy name set by the rego policy_name rule

#### 🔄 Return<a id="🔄-return"></a>

[`Policy`](./circle_ci_python_sdk/pydantic/policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/policy-bundle/{policyName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.get_policy_bundle`<a id="circlecipolicy_managementget_policy_bundle"></a>

This endpoint will retrieve a policy bundle

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_bundle_response = circleci.policy_management.get_policy_bundle(
    owner_id="ownerID_example",
    context="context_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyBundle`](./circle_ci_python_sdk/pydantic/policy_bundle.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/policy-bundle` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.get_policy_bundle_for_decision`<a id="circlecipolicy_managementget_policy_bundle_for_decision"></a>

This endpoint will retrieve a policy bundle for a given decision log ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_bundle_for_decision_response = (
    circleci.policy_management.get_policy_bundle_for_decision(
        owner_id="ownerID_example",
        context="context_example",
        decision_id="decisionID_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### decision_id: `str`<a id="decision_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PolicyBundle`](./circle_ci_python_sdk/pydantic/policy_bundle.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/decision/{decisionID}/policy-bundle` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.policy_management.modify_decision_settings`<a id="circlecipolicy_managementmodify_decision_settings"></a>

This endpoint allows modifying decision settings (eg enable/disable policy evaluation)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
modify_decision_settings_response = circleci.policy_management.modify_decision_settings(
    owner_id="ownerID_example",
    context="context_example",
    enabled=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: `str`<a id="owner_id-str"></a>

##### context: `str`<a id="context-str"></a>

##### enabled: `bool`<a id="enabled-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DecisionSettings`](./circle_ci_python_sdk/type/decision_settings.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DecisionSettings`](./circle_ci_python_sdk/pydantic/decision_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/owner/{ownerID}/context/{context}/decision/settings` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.create_checkout_key`<a id="circleciprojectcreate_checkout_key"></a>

Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token.
                           Please ensure that you have authorized your account with GitHub before creating user keys.
                           This is necessary to give CircleCI the permission to create a user key associated with
                           your GitHub user account. You can find this page by visiting Project Settings > Checkout SSH Keys

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_checkout_key_response = circleci.project.create_checkout_key(
    type="deploy-key",
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

The type of checkout key to create. This may be either `deploy-key` or `user-key`.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectCreateCheckoutKeyRequest`](./circle_ci_python_sdk/type/project_create_checkout_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProjectCreateCheckoutKeyResponse`](./circle_ci_python_sdk/pydantic/project_create_checkout_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/checkout-key` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.create_env_var`<a id="circleciprojectcreate_env_var"></a>

Creates a new environment variable.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_env_var_response = circleci.project.create_env_var(
    name="foo",
    value="xxxx1234",
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the environment variable.

##### value: `str`<a id="value-str"></a>

The value of the environment variable.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectCreateEnvVarRequest`](./circle_ci_python_sdk/type/project_create_env_var_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProjectCreateEnvVarResponse`](./circle_ci_python_sdk/pydantic/project_create_env_var_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/envvar` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.create_project_default_settings`<a id="circleciprojectcreate_project_default_settings"></a>

[__EXPERIMENTAL__]  Creates a new CircleCI project, and returns a list of the default advanced settings. Can only be called on a repo with a main branch and an existing config.yml file. Not yet available to projects that use GitLab or GitHub App.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_project_default_settings_response = (
    circleci.project.create_project_default_settings(
        provider="gh",
        organization="CircleCI-Public",
        project="api-preview-docs",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

##### organization: `str`<a id="organization-str"></a>

The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

##### project: `str`<a id="project-str"></a>

The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectSettings`](./circle_ci_python_sdk/pydantic/project_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{provider}/{organization}/{project}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.delete_checkout_key_by_fingerprint`<a id="circleciprojectdelete_checkout_key_by_fingerprint"></a>

Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_checkout_key_by_fingerprint_response = (
    circleci.project.delete_checkout_key_by_fingerprint(
        project_slug="gh/CircleCI-Public/api-preview-docs",
        fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### fingerprint: `str`<a id="fingerprint-str"></a>

An SSH key fingerprint.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectDeleteCheckoutKeyByFingerprintResponse`](./circle_ci_python_sdk/pydantic/project_delete_checkout_key_by_fingerprint_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/checkout-key/{fingerprint}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.delete_environment_variable`<a id="circleciprojectdelete_environment_variable"></a>

Deletes the environment variable named :name.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_environment_variable_response = circleci.project.delete_environment_variable(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    name="foo",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### name: `str`<a id="name-str"></a>

The name of the environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectDeleteEnvironmentVariableResponse`](./circle_ci_python_sdk/pydantic/project_delete_environment_variable_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/envvar/{name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.get_by_slug`<a id="circleciprojectget_by_slug"></a>

Retrieves a project by project slug.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_slug_response = circleci.project.get_by_slug(
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectGetBySlugResponse`](./circle_ci_python_sdk/pydantic/project_get_by_slug_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.get_checkout_key_by_fingerprint`<a id="circleciprojectget_checkout_key_by_fingerprint"></a>

Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_checkout_key_by_fingerprint_response = (
    circleci.project.get_checkout_key_by_fingerprint(
        project_slug="gh/CircleCI-Public/api-preview-docs",
        fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### fingerprint: `str`<a id="fingerprint-str"></a>

An SSH key fingerprint.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectGetCheckoutKeyByFingerprintResponse`](./circle_ci_python_sdk/pydantic/project_get_checkout_key_by_fingerprint_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/checkout-key/{fingerprint}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.get_masked_env_var`<a id="circleciprojectget_masked_env_var"></a>

Returns the masked value of environment variable :name.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_masked_env_var_response = circleci.project.get_masked_env_var(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    name="foo",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### name: `str`<a id="name-str"></a>

The name of the environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectGetMaskedEnvVarResponse`](./circle_ci_python_sdk/pydantic/project_get_masked_env_var_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/envvar/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.get_settings`<a id="circleciprojectget_settings"></a>

[__EXPERIMENTAL__] Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = circleci.project.get_settings(
    provider="gh",
    organization="CircleCI-Public",
    project="api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

##### organization: `str`<a id="organization-str"></a>

The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

##### project: `str`<a id="project-str"></a>

The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectSettings`](./circle_ci_python_sdk/pydantic/project_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{provider}/{organization}/{project}/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.list_checkout_keys`<a id="circleciprojectlist_checkout_keys"></a>

Returns a sequence of checkout keys for `:project`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_checkout_keys_response = circleci.project.list_checkout_keys(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    digest="sha256",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### digest: `str`<a id="digest-str"></a>

The fingerprint digest type to return. This may be either `md5` or `sha256`. If not passed, defaults to `md5`.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectListCheckoutKeysResponse`](./circle_ci_python_sdk/pydantic/project_list_checkout_keys_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/checkout-key` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.list_env_var_values`<a id="circleciprojectlist_env_var_values"></a>

Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_env_var_values_response = circleci.project.list_env_var_values(
    project_slug="gh/CircleCI-Public/api-preview-docs",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectListEnvVarValuesResponse`](./circle_ci_python_sdk/pydantic/project_list_env_var_values_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/envvar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.project.update_settings`<a id="circleciprojectupdate_settings"></a>

[__EXPERIMENTAL__] Updates one or more of the advanced settings for a CircleCI project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_settings_response = circleci.project.update_settings(
    provider="gh",
    organization="CircleCI-Public",
    project="api-preview-docs",
    advanced={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

##### organization: `str`<a id="organization-str"></a>

The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

##### project: `str`<a id="project-str"></a>

The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

##### advanced: [`ProjectSettingsAdvanced`](./circle_ci_python_sdk/type/project_settings_advanced.py)<a id="advanced-projectsettingsadvancedcircle_ci_python_sdktypeproject_settings_advancedpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectSettings`](./circle_ci_python_sdk/type/project_settings.py)
The setting(s) to update, including one or more fields in the JSON object. Note that `oss: true` will only be set on projects whose underlying repositories are actually open source.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectSettings`](./circle_ci_python_sdk/pydantic/project_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{provider}/{organization}/{project}/settings` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.schedule.create_new_schedule`<a id="circlecischedulecreate_new_schedule"></a>

Not yet available to projects that use GitLab or GitHub App. Creates a schedule and returns the created schedule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_schedule_response = circleci.schedule.create_new_schedule(
    parameters={
        "key": 1,
    },
    name="string_example",
    timetable={
        "per_hour": 1,
        "hours_of_day": [1],
        "days_of_week": ["TUE"],
    },
    attribution_actor="current",
    project_slug="gh/CircleCI-Public/api-preview-docs",
    description="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parameters: [`ScheduleCreateNewScheduleRequestParameters`](./circle_ci_python_sdk/type/schedule_create_new_schedule_request_parameters.py)<a id="parameters-schedulecreatenewschedulerequestparameterscircle_ci_python_sdktypeschedule_create_new_schedule_request_parameterspy"></a>

##### name: `str`<a id="name-str"></a>

Name of the schedule.

##### timetable: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="timetable-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>


Timetable that specifies when a schedule triggers.

##### attribution_actor: `str`<a id="attribution_actor-str"></a>

The attribution-actor of the scheduled pipeline.

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Description of the schedule.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ScheduleCreateNewScheduleRequest`](./circle_ci_python_sdk/type/schedule_create_new_schedule_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleCreateNewScheduleResponse`](./circle_ci_python_sdk/pydantic/schedule_create_new_schedule_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/schedule` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.schedule.get_all_schedules`<a id="circlecischeduleget_all_schedules"></a>

Returns all schedules for this project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_schedules_response = circleci.schedule.get_all_schedules(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_slug: `str`<a id="project_slug-str"></a>

Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

##### page_token: `str`<a id="page_token-str"></a>

A token to retrieve the next page of results.

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleGetAllSchedulesResponse`](./circle_ci_python_sdk/pydantic/schedule_get_all_schedules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{project-slug}/schedule` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.schedule.get_by_id`<a id="circlecischeduleget_by_id"></a>

Get a schedule by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = circleci.schedule.get_by_id(
    schedule_id="schedule-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### schedule_id: `str`<a id="schedule_id-str"></a>

The unique ID of the schedule.

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleGetByIdResponse`](./circle_ci_python_sdk/pydantic/schedule_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schedule/{schedule-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.schedule.remove_by_id`<a id="circlecischeduleremove_by_id"></a>

Not yet available to projects that use GitLab or GitHub App. Deletes the schedule by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_by_id_response = circleci.schedule.remove_by_id(
    schedule_id="schedule-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### schedule_id: `str`<a id="schedule_id-str"></a>

The unique ID of the schedule.

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleRemoveByIdResponse`](./circle_ci_python_sdk/pydantic/schedule_remove_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schedule/{schedule-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.schedule.update_schedule`<a id="circlecischeduleupdate_schedule"></a>

Not yet available to projects that use GitLab or GitHub App. Updates a schedule and returns the updated schedule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_schedule_response = circleci.schedule.update_schedule(
    schedule_id="schedule-id_example",
    description="string_example",
    parameters={
        "key": 1,
    },
    name="string_example",
    timetable={},
    attribution_actor="current",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### schedule_id: `str`<a id="schedule_id-str"></a>

The unique ID of the schedule.

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Description of the schedule.

##### parameters: [`ScheduleUpdateScheduleRequestParameters`](./circle_ci_python_sdk/type/schedule_update_schedule_request_parameters.py)<a id="parameters-scheduleupdateschedulerequestparameterscircle_ci_python_sdktypeschedule_update_schedule_request_parameterspy"></a>

##### name: `str`<a id="name-str"></a>

Name of the schedule.

##### timetable: [`ScheduleUpdateScheduleRequestTimetable`](./circle_ci_python_sdk/type/schedule_update_schedule_request_timetable.py)<a id="timetable-scheduleupdateschedulerequesttimetablecircle_ci_python_sdktypeschedule_update_schedule_request_timetablepy"></a>


##### attribution_actor: `str`<a id="attribution_actor-str"></a>

The attribution-actor of the scheduled pipeline.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ScheduleUpdateScheduleRequest`](./circle_ci_python_sdk/type/schedule_update_schedule_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleUpdateScheduleResponse`](./circle_ci_python_sdk/pydantic/schedule_update_schedule_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schedule/{schedule-id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.user.get_information`<a id="circleciuserget_information"></a>

Provides information about the user that is currently signed in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = circleci.user.get_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserGetInformationResponse`](./circle_ci_python_sdk/pydantic/user_get_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.user.get_user_information`<a id="circleciuserget_user_information"></a>

Provides information about the user with the given ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_information_response = circleci.user.get_user_information(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique ID of the user.

#### 🔄 Return<a id="🔄-return"></a>

[`UserGetUserInformationResponse`](./circle_ci_python_sdk/pydantic/user_get_user_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.user.list_collaborations`<a id="circleciuserlist_collaborations"></a>

Provides the set of organizations of which a user is a member or a collaborator.

The set of organizations that a user can collaborate on is composed of:

* Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
* The parent organization of repository that the user can collaborate on, but is not necessarily a member of
* The organization of the current user's account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collaborations_response = circleci.user.list_collaborations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserListCollaborationsResponse`](./circle_ci_python_sdk/pydantic/user_list_collaborations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/me/collaborations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.webhook.create_outbound_webhook`<a id="circleciwebhookcreate_outbound_webhook"></a>

Creates an outbound webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_outbound_webhook_response = circleci.webhook.create_outbound_webhook(
    name="string_example",
    events=["string_example"],
    url="string_example",
    verify_tls=True,
    signing_secret="string_example",
    scope={
        "id": "id_example",
        "type": "project",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the webhook

##### events: [`WebhookCreateOutboundWebhookRequestEvents`](./circle_ci_python_sdk/type/webhook_create_outbound_webhook_request_events.py)<a id="events-webhookcreateoutboundwebhookrequesteventscircle_ci_python_sdktypewebhook_create_outbound_webhook_request_eventspy"></a>

##### url: `str`<a id="url-str"></a>

URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

##### verify_tls: `bool`<a id="verify_tls-bool"></a>

Whether to enforce TLS certificate verification when delivering the webhook

##### signing_secret: `str`<a id="signing_secret-str"></a>

Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

##### scope: [`WebhookCreateOutboundWebhookRequestScope`](./circle_ci_python_sdk/type/webhook_create_outbound_webhook_request_scope.py)<a id="scope-webhookcreateoutboundwebhookrequestscopecircle_ci_python_sdktypewebhook_create_outbound_webhook_request_scopepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookCreateOutboundWebhookRequest`](./circle_ci_python_sdk/type/webhook_create_outbound_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookCreateOutboundWebhookResponse`](./circle_ci_python_sdk/pydantic/webhook_create_outbound_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.webhook.delete_outbound_webhook`<a id="circleciwebhookdelete_outbound_webhook"></a>

Deletes an outbound webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_outbound_webhook_response = circleci.webhook.delete_outbound_webhook(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

ID of the webhook (UUID)

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookDeleteOutboundWebhookResponse`](./circle_ci_python_sdk/pydantic/webhook_delete_outbound_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook/{webhook-id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.webhook.get_by_id`<a id="circleciwebhookget_by_id"></a>

Get an outbound webhook by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = circleci.webhook.get_by_id(
    webhook_id="webhook-id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

ID of the webhook (UUID)

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookGetByIdResponse`](./circle_ci_python_sdk/pydantic/webhook_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook/{webhook-id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.webhook.list_matching_scope`<a id="circleciwebhooklist_matching_scope"></a>

Get a list of outbound webhooks that match the given scope-type and scope-id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_matching_scope_response = circleci.webhook.list_matching_scope(
    scope_id="scope-id_example",
    scope_type="project",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope_id: `str`<a id="scope_id-str"></a>

ID of the scope being used (at the moment, only project ID is supported)

##### scope_type: `str`<a id="scope_type-str"></a>

Type of the scope being used

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookListMatchingScopeResponse`](./circle_ci_python_sdk/pydantic/webhook_list_matching_scope_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.webhook.update_outbound_webhook`<a id="circleciwebhookupdate_outbound_webhook"></a>

Updates an outbound webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_outbound_webhook_response = circleci.webhook.update_outbound_webhook(
    webhook_id="webhook-id_example",
    name="string_example",
    events=["string_example"],
    url="string_example",
    signing_secret="string_example",
    verify_tls=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

ID of the webhook (UUID)

##### name: `str`<a id="name-str"></a>

Name of the webhook

##### events: [`WebhookUpdateOutboundWebhookRequestEvents`](./circle_ci_python_sdk/type/webhook_update_outbound_webhook_request_events.py)<a id="events-webhookupdateoutboundwebhookrequesteventscircle_ci_python_sdktypewebhook_update_outbound_webhook_request_eventspy"></a>

##### url: `str`<a id="url-str"></a>

URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

##### signing_secret: `str`<a id="signing_secret-str"></a>

Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

##### verify_tls: `bool`<a id="verify_tls-bool"></a>

Whether to enforce TLS certificate verification when delivering the webhook

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookUpdateOutboundWebhookRequest`](./circle_ci_python_sdk/type/webhook_update_outbound_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookUpdateOutboundWebhookResponse`](./circle_ci_python_sdk/pydantic/webhook_update_outbound_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhook/{webhook-id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.workflow.approve_job`<a id="circleciworkflowapprove_job"></a>

Approves a pending approval job in a workflow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_job_response = circleci.workflow.approve_job(
    approval_request_id="approval_request_id_example",
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### approval_request_id: `str`<a id="approval_request_id-str"></a>

The ID of the job being approved.

##### id: `str`<a id="id-str"></a>

The unique ID of the workflow.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowApproveJobResponse`](./circle_ci_python_sdk/pydantic/workflow_approve_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflow/{id}/approve/{approval_request_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.workflow.cancel_workflow`<a id="circleciworkflowcancel_workflow"></a>

Cancels a running workflow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_workflow_response = circleci.workflow.cancel_workflow(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique ID of the workflow.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowCancelWorkflowResponse`](./circle_ci_python_sdk/pydantic/workflow_cancel_workflow_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflow/{id}/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.workflow.get_by_id`<a id="circleciworkflowget_by_id"></a>

Returns summary fields of a workflow by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = circleci.workflow.get_by_id(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique ID of the workflow.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowGetByIdResponse`](./circle_ci_python_sdk/pydantic/workflow_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflow/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.workflow.get_jobs`<a id="circleciworkflowget_jobs"></a>

Returns a sequence of jobs for a workflow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_jobs_response = circleci.workflow.get_jobs(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique ID of the workflow.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowGetJobsResponse`](./circle_ci_python_sdk/pydantic/workflow_get_jobs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflow/{id}/job` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `circleci.workflow.rerun_workflow`<a id="circleciworkflowrerun_workflow"></a>

Reruns a workflow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rerun_workflow_response = circleci.workflow.rerun_workflow(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
    enable_ssh=False,
    from_failed=False,
    jobs=[
        "c65b68ef-e73b-4bf2-be9a-7a322a9df150",
        "5e957edd-5e8c-4985-9178-5d0d69561822",
    ],
    sparse_tree=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique ID of the workflow.

##### enable_ssh: `bool`<a id="enable_ssh-bool"></a>

Whether to enable SSH access for the triggering user on the newly-rerun job. Requires the jobs parameter to be used and so is mutually exclusive with the from_failed parameter.

##### from_failed: `bool`<a id="from_failed-bool"></a>

Whether to rerun the workflow from the failed job. Mutually exclusive with the jobs parameter.

##### jobs: [`WorkflowRerunWorkflowRequestJobs`](./circle_ci_python_sdk/type/workflow_rerun_workflow_request_jobs.py)<a id="jobs-workflowrerunworkflowrequestjobscircle_ci_python_sdktypeworkflow_rerun_workflow_request_jobspy"></a>

##### sparse_tree: `bool`<a id="sparse_tree-bool"></a>

Completes rerun using sparse trees logic, an optimization for workflows that have disconnected subgraphs. Requires jobs parameter and so is mutually exclusive with the from_failed parameter.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowRerunWorkflowRequest`](./circle_ci_python_sdk/type/workflow_rerun_workflow_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowRerunWorkflowResponse`](./circle_ci_python_sdk/pydantic/workflow_rerun_workflow_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflow/{id}/rerun` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
