# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from circle_ci_python_sdk.paths.pipeline_continue import Api

from circle_ci_python_sdk.paths import PathValues

path = PathValues.PIPELINE_CONTINUE