# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from whats_app_business_python_sdk.paths.groups.post import CreateGroupRaw
from whats_app_business_python_sdk.paths.groups_group_id_icon.delete import DeleteGroupIconRaw
from whats_app_business_python_sdk.paths.groups_group_id_invite.delete import DeleteInviteRaw
from whats_app_business_python_sdk.paths.groups_group_id_admins.delete import DemoteAdminRaw
from whats_app_business_python_sdk.paths.groups.get import GetAllRaw
from whats_app_business_python_sdk.paths.groups_group_id_icon.get import GetIconBinaryRaw
from whats_app_business_python_sdk.paths.groups_group_id.get import GetInfoRaw
from whats_app_business_python_sdk.paths.groups_group_id_invite.get import GetInviteDetailsRaw
from whats_app_business_python_sdk.paths.groups_group_id_leave.post import LeaveGroupRaw
from whats_app_business_python_sdk.paths.groups_group_id_admins.patch import PromoteToAdminRaw
from whats_app_business_python_sdk.paths.groups_group_id_participants.delete import RemoveParticipantRaw
from whats_app_business_python_sdk.paths.groups_group_id_icon.post import SetGroupIconRaw
from whats_app_business_python_sdk.paths.groups_group_id.put import UpdateInfoRaw


class GroupsApiRaw(
    CreateGroupRaw,
    DeleteGroupIconRaw,
    DeleteInviteRaw,
    DemoteAdminRaw,
    GetAllRaw,
    GetIconBinaryRaw,
    GetInfoRaw,
    GetInviteDetailsRaw,
    LeaveGroupRaw,
    PromoteToAdminRaw,
    RemoveParticipantRaw,
    SetGroupIconRaw,
    UpdateInfoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
