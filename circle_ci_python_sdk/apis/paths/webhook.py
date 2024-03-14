from circle_ci_python_sdk.paths.webhook.get import ApiForget
from circle_ci_python_sdk.paths.webhook.post import ApiForpost


class Webhook(
    ApiForget,
    ApiForpost,
):
    pass
