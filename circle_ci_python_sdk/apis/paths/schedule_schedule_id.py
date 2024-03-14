from circle_ci_python_sdk.paths.schedule_schedule_id.get import ApiForget
from circle_ci_python_sdk.paths.schedule_schedule_id.delete import ApiFordelete
from circle_ci_python_sdk.paths.schedule_schedule_id.patch import ApiForpatch


class ScheduleScheduleId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
