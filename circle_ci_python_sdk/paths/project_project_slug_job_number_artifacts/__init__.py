# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from circle_ci_python_sdk.paths.project_project_slug_job_number_artifacts import Api

from circle_ci_python_sdk.paths import PathValues

path = PathValues.PROJECT_PROJECTSLUG_JOBNUMBER_ARTIFACTS