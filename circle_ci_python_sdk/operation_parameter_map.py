operation_parameter_map = {
    '/context-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'owner'
            },
        ]
    },
    '/context/{context_id}/restrictions-POST': {
        'parameters': [
            {
                'name': 'context_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'restriction_type'
            },
            {
                'name': 'restriction_value'
            },
        ]
    },
    '/context/{context_id}/restrictions/{restriction_id}-DELETE': {
        'parameters': [
            {
                'name': 'context_id'
            },
            {
                'name': 'restriction_id'
            },
        ]
    },
    '/context/{context-id}-GET': {
        'parameters': [
            {
                'name': 'context-id'
            },
        ]
    },
    '/context/{context_id}/restrictions-GET': {
        'parameters': [
            {
                'name': 'context_id'
            },
        ]
    },
    '/context/{context-id}/environment-variable-GET': {
        'parameters': [
            {
                'name': 'context-id'
            },
            {
                'name': 'page-token'
            },
        ]
    },
    '/context-GET': {
        'parameters': [
            {
                'name': 'owner-id'
            },
            {
                'name': 'owner-slug'
            },
            {
                'name': 'owner-type'
            },
            {
                'name': 'page-token'
            },
        ]
    },
    '/context/{context-id}-DELETE': {
        'parameters': [
            {
                'name': 'context-id'
            },
        ]
    },
    '/context/{context-id}/environment-variable/{env-var-name}-DELETE': {
        'parameters': [
            {
                'name': 'env-var-name'
            },
            {
                'name': 'context-id'
            },
        ]
    },
    '/context/{context-id}/environment-variable/{env-var-name}-PUT': {
        'parameters': [
            {
                'name': 'value'
            },
            {
                'name': 'context-id'
            },
            {
                'name': 'env-var-name'
            },
        ]
    },
    '/insights/{project-slug}/flaky-tests-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
        ]
    },
    '/insights/time-series/{project-slug}/workflows/{workflow-name}/jobs-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'workflow-name'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'granularity'
            },
            {
                'name': 'start-date'
            },
            {
                'name': 'end-date'
            },
        ]
    },
    '/insights/pages/{project-slug}/summary-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'reporting-window'
            },
            {
                'name': 'branches'
            },
            {
                'name': 'workflow-names'
            },
        ]
    },
    '/insights/{project-slug}/workflows/{workflow-name}/jobs-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'workflow-name'
            },
            {
                'name': 'page-token'
            },
            {
                'name': 'all-branches'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'reporting-window'
            },
        ]
    },
    '/insights/{project-slug}/workflows-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'page-token'
            },
            {
                'name': 'all-branches'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'reporting-window'
            },
        ]
    },
    '/insights/{project-slug}/workflows/{workflow-name}/test-metrics-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'workflow-name'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'all-branches'
            },
        ]
    },
    '/insights/{project-slug}/workflows/{workflow-name}-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'workflow-name'
            },
            {
                'name': 'all-branches'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'page-token'
            },
            {
                'name': 'start-date'
            },
            {
                'name': 'end-date'
            },
        ]
    },
    '/insights/{org-slug}/summary-GET': {
        'parameters': [
            {
                'name': 'org-slug'
            },
            {
                'name': 'reporting-window'
            },
            {
                'name': 'project-names'
            },
        ]
    },
    '/insights/{project-slug}/workflows/{workflow-name}/summary-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'workflow-name'
            },
            {
                'name': 'all-branches'
            },
            {
                'name': 'branch'
            },
        ]
    },
    '/insights/{project-slug}/branches-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'workflow-name'
            },
        ]
    },
    '/project/{project-slug}/job/{job-number}/cancel-POST': {
        'parameters': [
            {
                'name': 'job-number'
            },
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{project-slug}/{job-number}/artifacts-GET': {
        'parameters': [
            {
                'name': 'job-number'
            },
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{project-slug}/job/{job-number}-GET': {
        'parameters': [
            {
                'name': 'job-number'
            },
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{project-slug}/{job-number}/tests-GET': {
        'parameters': [
            {
                'name': 'job-number'
            },
            {
                'name': 'project-slug'
            },
        ]
    },
    '/org/{orgID}/oidc-custom-claims-DELETE': {
        'parameters': [
            {
                'name': 'orgID'
            },
            {
                'name': 'claims'
            },
        ]
    },
    '/org/{orgID}/project/{projectID}/oidc-custom-claims-DELETE': {
        'parameters': [
            {
                'name': 'orgID'
            },
            {
                'name': 'projectID'
            },
            {
                'name': 'claims'
            },
        ]
    },
    '/org/{orgID}/oidc-custom-claims-GET': {
        'parameters': [
            {
                'name': 'orgID'
            },
        ]
    },
    '/org/{orgID}/project/{projectID}/oidc-custom-claims-GET': {
        'parameters': [
            {
                'name': 'orgID'
            },
            {
                'name': 'projectID'
            },
        ]
    },
    '/org/{orgID}/oidc-custom-claims-PATCH': {
        'parameters': [
            {
                'name': 'orgID'
            },
            {
                'name': 'audience'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/org/{orgID}/project/{projectID}/oidc-custom-claims-PATCH': {
        'parameters': [
            {
                'name': 'orgID'
            },
            {
                'name': 'projectID'
            },
            {
                'name': 'audience'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/pipeline/continue-POST': {
        'parameters': [
            {
                'name': 'continuation-key'
            },
            {
                'name': 'configuration'
            },
            {
                'name': 'parameters'
            },
        ]
    },
    '/project/{project-slug}/pipeline-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'page-token'
            },
        ]
    },
    '/pipeline/{pipeline-id}-GET': {
        'parameters': [
            {
                'name': 'pipeline-id'
            },
        ]
    },
    '/project/{project-slug}/pipeline/{pipeline-number}-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'pipeline-number'
            },
        ]
    },
    '/pipeline/{pipeline-id}/config-GET': {
        'parameters': [
            {
                'name': 'pipeline-id'
            },
        ]
    },
    '/pipeline-GET': {
        'parameters': [
            {
                'name': 'org-slug'
            },
            {
                'name': 'page-token'
            },
            {
                'name': 'mine'
            },
        ]
    },
    '/project/{project-slug}/pipeline/mine-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'page-token'
            },
        ]
    },
    '/pipeline/{pipeline-id}/workflow-GET': {
        'parameters': [
            {
                'name': 'pipeline-id'
            },
            {
                'name': 'page-token'
            },
        ]
    },
    '/project/{project-slug}/pipeline-POST': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'parameters'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'tag'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/policy-bundle-POST': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'policies'
            },
            {
                'name': 'dry'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/decision-POST': {
        'parameters': [
            {
                'name': 'input'
            },
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/decision/{decisionID}-GET': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'decisionID'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/decision-GET': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'status'
            },
            {
                'name': 'after'
            },
            {
                'name': 'before'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'build_number'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/decision/settings-GET': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/policy-bundle/{policyName}-GET': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'policyName'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/policy-bundle-GET': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/decision/{decisionID}/policy-bundle-GET': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'decisionID'
            },
        ]
    },
    '/owner/{ownerID}/context/{context}/decision/settings-PATCH': {
        'parameters': [
            {
                'name': 'ownerID'
            },
            {
                'name': 'context'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/project/{project-slug}/checkout-key-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{project-slug}/envvar-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'value'
            },
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{provider}/{organization}/{project}-POST': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'project'
            },
        ]
    },
    '/project/{project-slug}/checkout-key/{fingerprint}-DELETE': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'fingerprint'
            },
        ]
    },
    '/project/{project-slug}/envvar/{name}-DELETE': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/project/{project-slug}-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{project-slug}/checkout-key/{fingerprint}-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'fingerprint'
            },
        ]
    },
    '/project/{project-slug}/envvar/{name}-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/project/{provider}/{organization}/{project}/settings-GET': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'project'
            },
        ]
    },
    '/project/{project-slug}/checkout-key-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'digest'
            },
        ]
    },
    '/project/{project-slug}/envvar-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
        ]
    },
    '/project/{provider}/{organization}/{project}/settings-PATCH': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'project'
            },
            {
                'name': 'advanced'
            },
        ]
    },
    '/project/{project-slug}/schedule-POST': {
        'parameters': [
            {
                'name': 'parameters'
            },
            {
                'name': 'name'
            },
            {
                'name': 'timetable'
            },
            {
                'name': 'attribution-actor'
            },
            {
                'name': 'project-slug'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/project/{project-slug}/schedule-GET': {
        'parameters': [
            {
                'name': 'project-slug'
            },
            {
                'name': 'page-token'
            },
        ]
    },
    '/schedule/{schedule-id}-GET': {
        'parameters': [
            {
                'name': 'schedule-id'
            },
        ]
    },
    '/schedule/{schedule-id}-DELETE': {
        'parameters': [
            {
                'name': 'schedule-id'
            },
        ]
    },
    '/schedule/{schedule-id}-PATCH': {
        'parameters': [
            {
                'name': 'schedule-id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parameters'
            },
            {
                'name': 'name'
            },
            {
                'name': 'timetable'
            },
            {
                'name': 'attribution-actor'
            },
        ]
    },
    '/me-GET': {
        'parameters': [
        ]
    },
    '/user/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/me/collaborations-GET': {
        'parameters': [
        ]
    },
    '/webhook-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'events'
            },
            {
                'name': 'url'
            },
            {
                'name': 'verify-tls'
            },
            {
                'name': 'signing-secret'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/webhook/{webhook-id}-DELETE': {
        'parameters': [
            {
                'name': 'webhook-id'
            },
        ]
    },
    '/webhook/{webhook-id}-GET': {
        'parameters': [
            {
                'name': 'webhook-id'
            },
        ]
    },
    '/webhook-GET': {
        'parameters': [
            {
                'name': 'scope-id'
            },
            {
                'name': 'scope-type'
            },
        ]
    },
    '/webhook/{webhook-id}-PUT': {
        'parameters': [
            {
                'name': 'webhook-id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'events'
            },
            {
                'name': 'url'
            },
            {
                'name': 'signing-secret'
            },
            {
                'name': 'verify-tls'
            },
        ]
    },
    '/workflow/{id}/approve/{approval_request_id}-POST': {
        'parameters': [
            {
                'name': 'approval_request_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/workflow/{id}/cancel-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/workflow/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/workflow/{id}/job-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/workflow/{id}/rerun-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'enable_ssh'
            },
            {
                'name': 'from_failed'
            },
            {
                'name': 'jobs'
            },
            {
                'name': 'sparse_tree'
            },
        ]
    },
};