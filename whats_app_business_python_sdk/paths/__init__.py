# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from whats_app_business_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNT = "/account"
    ACCOUNT_SHARDS = "/account/shards"
    ACCOUNT_VERIFY = "/account/verify"
    CERTIFICATES_EXTERNAL = "/certificates/external"
    CERTIFICATES_EXTERNAL_CA = "/certificates/external/ca"
    CERTIFICATES_WEBHOOKS_CA = "/certificates/webhooks/ca"
    CONTACTS = "/contacts"
    GROUPS = "/groups"
    GROUPS_GROUP_ID = "/groups/{GroupId}"
    GROUPS_GROUP_ID_ADMINS = "/groups/{GroupId}/admins"
    GROUPS_GROUP_ID_ICON = "/groups/{GroupId}/icon"
    GROUPS_GROUP_ID_INVITE = "/groups/{GroupId}/invite"
    GROUPS_GROUP_ID_LEAVE = "/groups/{GroupId}/leave"
    GROUPS_GROUP_ID_PARTICIPANTS = "/groups/{GroupId}/participants"
    HEALTH = "/health"
    MEDIA = "/media"
    MEDIA_MEDIA_ID = "/media/{MediaId}"
    MESSAGES = "/messages"
    MESSAGES_MESSAGE_ID = "/messages/{MessageID}"
    METRICS = "/metrics"
    SETTINGS_ACCOUNT_TWOSTEP = "/settings/account/two-step"
    SETTINGS_APPLICATION = "/settings/application"
    SETTINGS_APPLICATION_MEDIA_PROVIDERS = "/settings/application/media/providers"
    SETTINGS_APPLICATION_MEDIA_PROVIDERS_PROVIDER_NAME = "/settings/application/media/providers/{ProviderName}"
    SETTINGS_BACKUP = "/settings/backup"
    SETTINGS_BUSINESS_PROFILE = "/settings/business/profile"
    SETTINGS_PROFILE_ABOUT = "/settings/profile/about"
    SETTINGS_PROFILE_PHOTO = "/settings/profile/photo"
    SETTINGS_RESTORE = "/settings/restore"
    STATS_APP = "/stats/app"
    STATS_DB = "/stats/db"
    SUPPORT = "/support"
    USERS = "/users"
    USERS_LOGIN = "/users/login"
    USERS_LOGOUT = "/users/logout"
    USERS_USER_USERNAME = "/users/{UserUsername}"
