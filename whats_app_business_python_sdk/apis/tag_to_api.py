import typing_extensions

from whats_app_business_python_sdk.apis.tags import TagValues
from whats_app_business_python_sdk.apis.tags.groups_api import GroupsApi
from whats_app_business_python_sdk.apis.tags.application_api import ApplicationApi
from whats_app_business_python_sdk.apis.tags.users_api import UsersApi
from whats_app_business_python_sdk.apis.tags.profile_api import ProfileApi
from whats_app_business_python_sdk.apis.tags.health_api import HealthApi
from whats_app_business_python_sdk.apis.tags.certificates_api import CertificatesApi
from whats_app_business_python_sdk.apis.tags.media_api import MediaApi
from whats_app_business_python_sdk.apis.tags.backup_restore_api import BackupRestoreApi
from whats_app_business_python_sdk.apis.tags.business_profile_api import BusinessProfileApi
from whats_app_business_python_sdk.apis.tags.two_step_verification_api import TwoStepVerificationApi
from whats_app_business_python_sdk.apis.tags.registration_api import RegistrationApi
from whats_app_business_python_sdk.apis.tags.messages_api import MessagesApi
from whats_app_business_python_sdk.apis.tags.contacts_api import ContactsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.GROUPS: GroupsApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.USERS: UsersApi,
        TagValues.PROFILE: ProfileApi,
        TagValues.HEALTH: HealthApi,
        TagValues.CERTIFICATES: CertificatesApi,
        TagValues.MEDIA: MediaApi,
        TagValues.BACKUP_RESTORE: BackupRestoreApi,
        TagValues.BUSINESS_PROFILE: BusinessProfileApi,
        TagValues.TWOSTEP_VERIFICATION: TwoStepVerificationApi,
        TagValues.REGISTRATION: RegistrationApi,
        TagValues.MESSAGES: MessagesApi,
        TagValues.CONTACTS: ContactsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.GROUPS: GroupsApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.USERS: UsersApi,
        TagValues.PROFILE: ProfileApi,
        TagValues.HEALTH: HealthApi,
        TagValues.CERTIFICATES: CertificatesApi,
        TagValues.MEDIA: MediaApi,
        TagValues.BACKUP_RESTORE: BackupRestoreApi,
        TagValues.BUSINESS_PROFILE: BusinessProfileApi,
        TagValues.TWOSTEP_VERIFICATION: TwoStepVerificationApi,
        TagValues.REGISTRATION: RegistrationApi,
        TagValues.MESSAGES: MessagesApi,
        TagValues.CONTACTS: ContactsApi,
    }
)
