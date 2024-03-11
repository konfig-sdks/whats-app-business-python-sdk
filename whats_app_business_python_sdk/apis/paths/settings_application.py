from whats_app_business_python_sdk.paths.settings_application.get import ApiForget
from whats_app_business_python_sdk.paths.settings_application.delete import ApiFordelete
from whats_app_business_python_sdk.paths.settings_application.patch import ApiForpatch


class SettingsApplication(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
