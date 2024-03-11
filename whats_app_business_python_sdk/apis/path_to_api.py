import typing_extensions

from whats_app_business_python_sdk.paths import PathValues
from whats_app_business_python_sdk.apis.paths.account import Account
from whats_app_business_python_sdk.apis.paths.account_shards import AccountShards
from whats_app_business_python_sdk.apis.paths.account_verify import AccountVerify
from whats_app_business_python_sdk.apis.paths.certificates_external import CertificatesExternal
from whats_app_business_python_sdk.apis.paths.certificates_external_ca import CertificatesExternalCa
from whats_app_business_python_sdk.apis.paths.certificates_webhooks_ca import CertificatesWebhooksCa
from whats_app_business_python_sdk.apis.paths.contacts import Contacts
from whats_app_business_python_sdk.apis.paths.groups import Groups
from whats_app_business_python_sdk.apis.paths.groups_group_id import GroupsGroupId
from whats_app_business_python_sdk.apis.paths.groups_group_id_admins import GroupsGroupIdAdmins
from whats_app_business_python_sdk.apis.paths.groups_group_id_icon import GroupsGroupIdIcon
from whats_app_business_python_sdk.apis.paths.groups_group_id_invite import GroupsGroupIdInvite
from whats_app_business_python_sdk.apis.paths.groups_group_id_leave import GroupsGroupIdLeave
from whats_app_business_python_sdk.apis.paths.groups_group_id_participants import GroupsGroupIdParticipants
from whats_app_business_python_sdk.apis.paths.health import Health
from whats_app_business_python_sdk.apis.paths.media import Media
from whats_app_business_python_sdk.apis.paths.media_media_id import MediaMediaId
from whats_app_business_python_sdk.apis.paths.messages import Messages
from whats_app_business_python_sdk.apis.paths.messages_message_id import MessagesMessageID
from whats_app_business_python_sdk.apis.paths.metrics import Metrics
from whats_app_business_python_sdk.apis.paths.settings_account_two_step import SettingsAccountTwoStep
from whats_app_business_python_sdk.apis.paths.settings_application import SettingsApplication
from whats_app_business_python_sdk.apis.paths.settings_application_media_providers import SettingsApplicationMediaProviders
from whats_app_business_python_sdk.apis.paths.settings_application_media_providers_provider_name import SettingsApplicationMediaProvidersProviderName
from whats_app_business_python_sdk.apis.paths.settings_backup import SettingsBackup
from whats_app_business_python_sdk.apis.paths.settings_business_profile import SettingsBusinessProfile
from whats_app_business_python_sdk.apis.paths.settings_profile_about import SettingsProfileAbout
from whats_app_business_python_sdk.apis.paths.settings_profile_photo import SettingsProfilePhoto
from whats_app_business_python_sdk.apis.paths.settings_restore import SettingsRestore
from whats_app_business_python_sdk.apis.paths.stats_app import StatsApp
from whats_app_business_python_sdk.apis.paths.stats_db import StatsDb
from whats_app_business_python_sdk.apis.paths.support import Support
from whats_app_business_python_sdk.apis.paths.users import Users
from whats_app_business_python_sdk.apis.paths.users_login import UsersLogin
from whats_app_business_python_sdk.apis.paths.users_logout import UsersLogout
from whats_app_business_python_sdk.apis.paths.users_user_username import UsersUserUsername

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNT: Account,
        PathValues.ACCOUNT_SHARDS: AccountShards,
        PathValues.ACCOUNT_VERIFY: AccountVerify,
        PathValues.CERTIFICATES_EXTERNAL: CertificatesExternal,
        PathValues.CERTIFICATES_EXTERNAL_CA: CertificatesExternalCa,
        PathValues.CERTIFICATES_WEBHOOKS_CA: CertificatesWebhooksCa,
        PathValues.CONTACTS: Contacts,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS_GROUP_ID_ADMINS: GroupsGroupIdAdmins,
        PathValues.GROUPS_GROUP_ID_ICON: GroupsGroupIdIcon,
        PathValues.GROUPS_GROUP_ID_INVITE: GroupsGroupIdInvite,
        PathValues.GROUPS_GROUP_ID_LEAVE: GroupsGroupIdLeave,
        PathValues.GROUPS_GROUP_ID_PARTICIPANTS: GroupsGroupIdParticipants,
        PathValues.HEALTH: Health,
        PathValues.MEDIA: Media,
        PathValues.MEDIA_MEDIA_ID: MediaMediaId,
        PathValues.MESSAGES: Messages,
        PathValues.MESSAGES_MESSAGE_ID: MessagesMessageID,
        PathValues.METRICS: Metrics,
        PathValues.SETTINGS_ACCOUNT_TWOSTEP: SettingsAccountTwoStep,
        PathValues.SETTINGS_APPLICATION: SettingsApplication,
        PathValues.SETTINGS_APPLICATION_MEDIA_PROVIDERS: SettingsApplicationMediaProviders,
        PathValues.SETTINGS_APPLICATION_MEDIA_PROVIDERS_PROVIDER_NAME: SettingsApplicationMediaProvidersProviderName,
        PathValues.SETTINGS_BACKUP: SettingsBackup,
        PathValues.SETTINGS_BUSINESS_PROFILE: SettingsBusinessProfile,
        PathValues.SETTINGS_PROFILE_ABOUT: SettingsProfileAbout,
        PathValues.SETTINGS_PROFILE_PHOTO: SettingsProfilePhoto,
        PathValues.SETTINGS_RESTORE: SettingsRestore,
        PathValues.STATS_APP: StatsApp,
        PathValues.STATS_DB: StatsDb,
        PathValues.SUPPORT: Support,
        PathValues.USERS: Users,
        PathValues.USERS_LOGIN: UsersLogin,
        PathValues.USERS_LOGOUT: UsersLogout,
        PathValues.USERS_USER_USERNAME: UsersUserUsername,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNT: Account,
        PathValues.ACCOUNT_SHARDS: AccountShards,
        PathValues.ACCOUNT_VERIFY: AccountVerify,
        PathValues.CERTIFICATES_EXTERNAL: CertificatesExternal,
        PathValues.CERTIFICATES_EXTERNAL_CA: CertificatesExternalCa,
        PathValues.CERTIFICATES_WEBHOOKS_CA: CertificatesWebhooksCa,
        PathValues.CONTACTS: Contacts,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS_GROUP_ID_ADMINS: GroupsGroupIdAdmins,
        PathValues.GROUPS_GROUP_ID_ICON: GroupsGroupIdIcon,
        PathValues.GROUPS_GROUP_ID_INVITE: GroupsGroupIdInvite,
        PathValues.GROUPS_GROUP_ID_LEAVE: GroupsGroupIdLeave,
        PathValues.GROUPS_GROUP_ID_PARTICIPANTS: GroupsGroupIdParticipants,
        PathValues.HEALTH: Health,
        PathValues.MEDIA: Media,
        PathValues.MEDIA_MEDIA_ID: MediaMediaId,
        PathValues.MESSAGES: Messages,
        PathValues.MESSAGES_MESSAGE_ID: MessagesMessageID,
        PathValues.METRICS: Metrics,
        PathValues.SETTINGS_ACCOUNT_TWOSTEP: SettingsAccountTwoStep,
        PathValues.SETTINGS_APPLICATION: SettingsApplication,
        PathValues.SETTINGS_APPLICATION_MEDIA_PROVIDERS: SettingsApplicationMediaProviders,
        PathValues.SETTINGS_APPLICATION_MEDIA_PROVIDERS_PROVIDER_NAME: SettingsApplicationMediaProvidersProviderName,
        PathValues.SETTINGS_BACKUP: SettingsBackup,
        PathValues.SETTINGS_BUSINESS_PROFILE: SettingsBusinessProfile,
        PathValues.SETTINGS_PROFILE_ABOUT: SettingsProfileAbout,
        PathValues.SETTINGS_PROFILE_PHOTO: SettingsProfilePhoto,
        PathValues.SETTINGS_RESTORE: SettingsRestore,
        PathValues.STATS_APP: StatsApp,
        PathValues.STATS_DB: StatsDb,
        PathValues.SUPPORT: Support,
        PathValues.USERS: Users,
        PathValues.USERS_LOGIN: UsersLogin,
        PathValues.USERS_LOGOUT: UsersLogout,
        PathValues.USERS_USER_USERNAME: UsersUserUsername,
    }
)
