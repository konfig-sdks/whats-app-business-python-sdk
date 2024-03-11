# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from whats_app_business_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    GROUPS = "Groups"
    APPLICATION = "Application"
    USERS = "Users"
    PROFILE = "Profile"
    HEALTH = "Health"
    CERTIFICATES = "Certificates"
    MEDIA = "Media"
    BACKUP_RESTORE = "Backup/Restore"
    BUSINESS_PROFILE = "Business Profile"
    TWOSTEP_VERIFICATION = "Two-Step Verification"
    REGISTRATION = "Registration"
    MESSAGES = "Messages"
    CONTACTS = "Contacts"
