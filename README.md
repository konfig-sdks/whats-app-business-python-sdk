<div align="center">

[![Visit Whatsapp](./header.png)](https://developers.facebook.com&#x2F;docs&#x2F;whatsapp)

# Whatsapp<a id="whatsapp"></a>

See https://developers.facebook.com/docs/whatsapp


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`whatsappbusiness.application.get_settings`](#whatsappbusinessapplicationget_settings)
  * [`whatsappbusiness.application.list_media_providers`](#whatsappbusinessapplicationlist_media_providers)
  * [`whatsappbusiness.application.remove_provider`](#whatsappbusinessapplicationremove_provider)
  * [`whatsappbusiness.application.reset_settings`](#whatsappbusinessapplicationreset_settings)
  * [`whatsappbusiness.application.set_shards`](#whatsappbusinessapplicationset_shards)
  * [`whatsappbusiness.application.update_media_providers`](#whatsappbusinessapplicationupdate_media_providers)
  * [`whatsappbusiness.application.update_settings`](#whatsappbusinessapplicationupdate_settings)
  * [`whatsappbusiness.backup/restore.settings_post`](#whatsappbusinessbackuprestoresettings_post)
  * [`whatsappbusiness.backup/restore.settings_post_0`](#whatsappbusinessbackuprestoresettings_post_0)
  * [`whatsappbusiness.business_profile.get`](#whatsappbusinessbusiness_profileget)
  * [`whatsappbusiness.business_profile.update`](#whatsappbusinessbusiness_profileupdate)
  * [`whatsappbusiness.certificates.delete_webhook_ca`](#whatsappbusinesscertificatesdelete_webhook_ca)
  * [`whatsappbusiness.certificates.download_ca_certificate`](#whatsappbusinesscertificatesdownload_ca_certificate)
  * [`whatsappbusiness.certificates.download_webhook_ca_certificate`](#whatsappbusinesscertificatesdownload_webhook_ca_certificate)
  * [`whatsappbusiness.certificates.upload_external_certificate`](#whatsappbusinesscertificatesupload_external_certificate)
  * [`whatsappbusiness.certificates.upload_webhook_ca_certificate`](#whatsappbusinesscertificatesupload_webhook_ca_certificate)
  * [`whatsappbusiness.contacts.create_contact`](#whatsappbusinesscontactscreate_contact)
  * [`whatsappbusiness.groups.create_group`](#whatsappbusinessgroupscreate_group)
  * [`whatsappbusiness.groups.delete_group_icon`](#whatsappbusinessgroupsdelete_group_icon)
  * [`whatsappbusiness.groups.delete_invite`](#whatsappbusinessgroupsdelete_invite)
  * [`whatsappbusiness.groups.demote_admin`](#whatsappbusinessgroupsdemote_admin)
  * [`whatsappbusiness.groups.get_all`](#whatsappbusinessgroupsget_all)
  * [`whatsappbusiness.groups.get_icon_binary`](#whatsappbusinessgroupsget_icon_binary)
  * [`whatsappbusiness.groups.get_info`](#whatsappbusinessgroupsget_info)
  * [`whatsappbusiness.groups.get_invite_details`](#whatsappbusinessgroupsget_invite_details)
  * [`whatsappbusiness.groups.leave_group`](#whatsappbusinessgroupsleave_group)
  * [`whatsappbusiness.groups.promote_to_admin`](#whatsappbusinessgroupspromote_to_admin)
  * [`whatsappbusiness.groups.remove_participant`](#whatsappbusinessgroupsremove_participant)
  * [`whatsappbusiness.groups.set_group_icon`](#whatsappbusinessgroupsset_group_icon)
  * [`whatsappbusiness.groups.update_info`](#whatsappbusinessgroupsupdate_info)
  * [`whatsappbusiness.health.check_status`](#whatsappbusinesshealthcheck_status)
  * [`whatsappbusiness.health.get_app_stats`](#whatsappbusinesshealthget_app_stats)
  * [`whatsappbusiness.health.get_db_stats`](#whatsappbusinesshealthget_db_stats)
  * [`whatsappbusiness.health.get_metrics_data`](#whatsappbusinesshealthget_metrics_data)
  * [`whatsappbusiness.health.get_support_info`](#whatsappbusinesshealthget_support_info)
  * [`whatsappbusiness.media.download`](#whatsappbusinessmediadownload)
  * [`whatsappbusiness.media.remove_media`](#whatsappbusinessmediaremove_media)
  * [`whatsappbusiness.media.upload_media`](#whatsappbusinessmediaupload_media)
  * [`whatsappbusiness.messages.mark_as_read`](#whatsappbusinessmessagesmark_as_read)
  * [`whatsappbusiness.messages.send_message`](#whatsappbusinessmessagessend_message)
  * [`whatsappbusiness.profile.get_about`](#whatsappbusinessprofileget_about)
  * [`whatsappbusiness.profile.get_photo`](#whatsappbusinessprofileget_photo)
  * [`whatsappbusiness.profile.remove_photo`](#whatsappbusinessprofileremove_photo)
  * [`whatsappbusiness.profile.update_about`](#whatsappbusinessprofileupdate_about)
  * [`whatsappbusiness.profile.update_photo`](#whatsappbusinessprofileupdate_photo)
  * [`whatsappbusiness.registration.request_code`](#whatsappbusinessregistrationrequest_code)
  * [`whatsappbusiness.registration.verify_account`](#whatsappbusinessregistrationverify_account)
  * [`whatsappbusiness.two_step_verification.disable`](#whatsappbusinesstwo_step_verificationdisable)
  * [`whatsappbusiness.two_step_verification.enable_account`](#whatsappbusinesstwo_step_verificationenable_account)
  * [`whatsappbusiness.users.create_user`](#whatsappbusinessuserscreate_user)
  * [`whatsappbusiness.users.get_by_username`](#whatsappbusinessusersget_by_username)
  * [`whatsappbusiness.users.perform_login`](#whatsappbusinessusersperform_login)
  * [`whatsappbusiness.users.perform_logout`](#whatsappbusinessusersperform_logout)
  * [`whatsappbusiness.users.remove_user`](#whatsappbusinessusersremove_user)
  * [`whatsappbusiness.users.update_user`](#whatsappbusinessusersupdate_user)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=WhatsApp&%20serviceName=Business%20&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from whats_app_business_python_sdk import WhatsAppBusiness, ApiException

whatsappbusiness = WhatsAppBusiness(access_token="YOUR_BEARER_TOKEN")

try:
    # Get-Application-Settings
    get_settings_response = whatsappbusiness.application.get_settings()
    print(get_settings_response)
except ApiException as e:
    print("Exception when calling ApplicationApi.get_settings: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from whats_app_business_python_sdk import WhatsAppBusiness, ApiException

whatsappbusiness = WhatsAppBusiness(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Get-Application-Settings
        get_settings_response = await whatsappbusiness.application.aget_settings()
        print(get_settings_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi.get_settings: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from whats_app_business_python_sdk import WhatsAppBusiness, ApiException

whatsappbusiness = WhatsAppBusiness(access_token="YOUR_BEARER_TOKEN")

try:
    # Get-Application-Settings
    get_settings_response = whatsappbusiness.application.raw.get_settings()
    pprint(get_settings_response.body)
    pprint(get_settings_response.body["callback_backoff_delay_ms"])
    pprint(get_settings_response.body["callback_persist"])
    pprint(get_settings_response.body["heartbeat_interval"])
    pprint(get_settings_response.body["max_callback_backoff_delay_ms"])
    pprint(get_settings_response.body["media"])
    pprint(get_settings_response.body["on_call_pager"])
    pprint(get_settings_response.body["pass_through"])
    pprint(get_settings_response.body["sent_status"])
    pprint(get_settings_response.body["unhealthy_interval"])
    pprint(get_settings_response.body["webhooks"])
    pprint(get_settings_response.headers)
    pprint(get_settings_response.status)
    pprint(get_settings_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApplicationApi.get_settings: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `whatsappbusiness.application.get_settings`<a id="whatsappbusinessapplicationget_settings"></a>

Get-Application-Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = whatsappbusiness.application.get_settings()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationSettings`](./whats_app_business_python_sdk/pydantic/application_settings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/application` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.application.list_media_providers`<a id="whatsappbusinessapplicationlist_media_providers"></a>

Get-Media-Providers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_media_providers_response = whatsappbusiness.application.list_media_providers()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetMediaProvidersResponse`](./whats_app_business_python_sdk/pydantic/get_media_providers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/application/media/providers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.application.remove_provider`<a id="whatsappbusinessapplicationremove_provider"></a>

Delete-Media-Providers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.application.remove_provider(
    provider_name="ProviderName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_name: `str`<a id="provider_name-str"></a>

Provider Name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/application/media/providers/{ProviderName}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.application.reset_settings`<a id="whatsappbusinessapplicationreset_settings"></a>

Reset-Application-Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.application.reset_settings()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/application` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.application.set_shards`<a id="whatsappbusinessapplicationset_shards"></a>

Set-Shards

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.application.set_shards(
    cc="<Country Code>",
    phone_number="<Phone Number>",
    pin="<Two-Step PIN>",
    shards=32,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cc: `str`<a id="cc-str"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### pin: `str`<a id="pin-str"></a>

##### shards: `int`<a id="shards-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SetShardsRequestBody`](./whats_app_business_python_sdk/type/set_shards_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/shards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.application.update_media_providers`<a id="whatsappbusinessapplicationupdate_media_providers"></a>

Update-Media-Providers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.application.update_media_providers(
    body=[
        {
            "config": {"bearer": "<Bearer Auth Token>"},
            "name": "<Provider Name>",
            "type": "www",
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationUpdateMediaProvidersRequest`](./whats_app_business_python_sdk/type/application_update_media_providers_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/application/media/providers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.application.update_settings`<a id="whatsappbusinessapplicationupdate_settings"></a>

If a field is not present in the request, no change is made to that setting. For example, if on_call_pager is not sent with the request, the existing configuration for on_call_pager is unchanged.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_settings_response = whatsappbusiness.application.update_settings(
    callback_backoff_delay_ms="3000",
    callback_persist=True,
    heartbeat_interval=5,
    max_callback_backoff_delay_ms="900000",
    media={
        "auto_download": ["audio"],
    },
    on_call_pager="<WA_ID of valid WhatsApp contact>",
    pass_through=True,
    sent_status=False,
    unhealthy_interval=30,
    webhooks={
        "max_concurrent_requests": 6,
        "url": "<Webhook URL, https>",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### callback_backoff_delay_ms: `str`<a id="callback_backoff_delay_ms-str"></a>

Backoff delay for a failed callback in milliseconds This setting is used to configure the amount of time the backoff delays before retrying a failed callback. The backoff delay increases linearly by this value each time a callback fails to get a HTTPS 200 OK response. The backoff delay is capped by the max_callback_backoff_delay_ms setting.

##### callback_persist: `bool`<a id="callback_persist-bool"></a>

Stores callbacks on disk until they are successfully acknowledged by the Webhook or not. Restart required.

##### heartbeat_interval: `int`<a id="heartbeat_interval-int"></a>

Multiconnect: Interval of the Master node monitoring of Coreapp nodes in seconds

##### max_callback_backoff_delay_ms: `str`<a id="max_callback_backoff_delay_ms-str"></a>

Maximum delay for a failed callback in milliseconds

##### media: [`Media`](./whats_app_business_python_sdk/type/media.py)<a id="media-mediawhats_app_business_python_sdktypemediapy"></a>


##### on_call_pager: `str`<a id="on_call_pager-str"></a>

Set to valid WhatsApp Group with users who wish to see alerts for critical errors and messages.

##### pass_through: `bool`<a id="pass_through-bool"></a>

When true, removes messages from the local database after they are delivered to or read by the recipient. When false, saves all messages on local storage until they are explicitly deleted. When messages are sent, they are stored in a local database. This database is used as the application's history. Since the business keeps its own history, you can specify whether you want message pass_through or not. Restart required.

##### sent_status: `bool`<a id="sent_status-bool"></a>

Receive a notification that a message is sent to server. When true, you will receive a message indicating that a message has been sent. If false (default), you will not receive notification.

##### unhealthy_interval: `int`<a id="unhealthy_interval-int"></a>

Multiconnect: Maximum amount of seconds a Master node waits for a Coreapp node to respond to a heartbeat before considering it unhealthy and starting the failover process.

##### webhooks: [`Webhooks`](./whats_app_business_python_sdk/type/webhooks.py)<a id="webhooks-webhookswhats_app_business_python_sdktypewebhookspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationSettings`](./whats_app_business_python_sdk/type/application_settings.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Response`](./whats_app_business_python_sdk/pydantic/response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/application` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.backup/restore.settings_post`<a id="whatsappbusinessbackuprestoresettings_post"></a>

Backup-Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
settings_post_response = whatsappbusiness.backup / restore.settings_post(
    password="<Password for Backup>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

Used to encrypt backup data for security

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BackupSettingsRequestBody`](./whats_app_business_python_sdk/type/backup_settings_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BackupSettingsResponse`](./whats_app_business_python_sdk/pydantic/backup_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/backup` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.backup/restore.settings_post_0`<a id="whatsappbusinessbackuprestoresettings_post_0"></a>

Restore-Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.backup / restore.settings_post_0(
    data="<Data to Restore, from Backup API>",
    password="<Password for Backup>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `str`<a id="data-str"></a>

The data that was returned by the /v1/settings/backup API call

##### password: `str`<a id="password-str"></a>

The password you used in the /v1/settings/backup API call to encrypt the backup data

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RestoreSettingsRequestBody`](./whats_app_business_python_sdk/type/restore_settings_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/restore` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.business_profile.get`<a id="whatsappbusinessbusiness_profileget"></a>

Get-Business-Profile

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = whatsappbusiness.business_profile.get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetBusinessProfileResponse`](./whats_app_business_python_sdk/pydantic/get_business_profile_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/business/profile` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.business_profile.update`<a id="whatsappbusinessbusiness_profileupdate"></a>

Update-Business-Profile

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.business_profile.update(
    description="<Business Profile Description>",
    address="<Business Profile Address>",
    email="<Business Profile Email>",
    vertical="<Business Profile Vertical>",
    websites=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description of the business Maximum of 256 characters

##### address: `str`<a id="address-str"></a>

Address of the business Maximum of 256 characters

##### email: `str`<a id="email-str"></a>

Email address to contact the business Maximum of 128 characters

##### vertical: `str`<a id="vertical-str"></a>

Industry of the business Maximum of 128 characters

##### websites: [`BusinessProfileWebsites`](./whats_app_business_python_sdk/type/business_profile_websites.py)<a id="websites-businessprofilewebsiteswhats_app_business_python_sdktypebusiness_profile_websitespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessProfile`](./whats_app_business_python_sdk/type/business_profile.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/business/profile` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.certificates.delete_webhook_ca`<a id="whatsappbusinesscertificatesdelete_webhook_ca"></a>

Delete Webhook CA Certificate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.certificates.delete_webhook_ca()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/webhooks/ca` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.certificates.download_ca_certificate`<a id="whatsappbusinesscertificatesdownload_ca_certificate"></a>

Download-CA-Certificate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_ca_certificate_response = (
    whatsappbusiness.certificates.download_ca_certificate()
)
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/external/ca` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.certificates.download_webhook_ca_certificate`<a id="whatsappbusinesscertificatesdownload_webhook_ca_certificate"></a>

Download Webhook CA Certificate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_webhook_ca_certificate_response = (
    whatsappbusiness.certificates.download_webhook_ca_certificate()
)
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/webhooks/ca` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.certificates.upload_external_certificate`<a id="whatsappbusinesscertificatesupload_external_certificate"></a>

Upload-Certificate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.certificates.upload_external_certificate(
    body=open("/path/to/file", "rb"),
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`IO`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/external` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.certificates.upload_webhook_ca_certificate`<a id="whatsappbusinesscertificatesupload_webhook_ca_certificate"></a>

Upload Webhook CA Certificate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.certificates.upload_webhook_ca_certificate(
    body=open("/path/to/file", "rb"),
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`IO`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/certificates/webhooks/ca` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.contacts.create_contact`<a id="whatsappbusinesscontactscreate_contact"></a>

Check-Contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_contact_response = whatsappbusiness.contacts.create_contact(
    contacts=["string_example"],
    blocking="no_wait",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contacts: [`CheckContactRequestBodyContacts`](./whats_app_business_python_sdk/type/check_contact_request_body_contacts.py)<a id="contacts-checkcontactrequestbodycontactswhats_app_business_python_sdktypecheck_contact_request_body_contactspy"></a>

##### blocking: `str`<a id="blocking-str"></a>

Blocking determines whether the request should wait for the processing to complete (synchronous) or not (asynchronous).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckContactRequestBody`](./whats_app_business_python_sdk/type/check_contact_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckContactResponse`](./whats_app_business_python_sdk/pydantic/check_contact_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.create_group`<a id="whatsappbusinessgroupscreate_group"></a>

Create-Group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_group_response = whatsappbusiness.groups.create_group(
    subject="<Group Subject>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subject: `str`<a id="subject-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateGroupRequestBody`](./whats_app_business_python_sdk/type/create_group_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupsResponse`](./whats_app_business_python_sdk/pydantic/groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.delete_group_icon`<a id="whatsappbusinessgroupsdelete_group_icon"></a>

Delete-Group-Icon

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.delete_group_icon(
    group_id="GroupId_example",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsDeleteGroupIconRequest`](./whats_app_business_python_sdk/type/groups_delete_group_icon_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/icon` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.delete_invite`<a id="whatsappbusinessgroupsdelete_invite"></a>

Delete-Group-Invite

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.delete_invite(
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/invite` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.demote_admin`<a id="whatsappbusinessgroupsdemote_admin"></a>

Demote-Group-Admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.demote_admin(
    wa_ids=["string_example"],
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### wa_ids: [`GroupAdminRequestBodyWaIds`](./whats_app_business_python_sdk/type/group_admin_request_body_wa_ids.py)<a id="wa_ids-groupadminrequestbodywaidswhats_app_business_python_sdktypegroup_admin_request_body_wa_idspy"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupAdminRequestBody`](./whats_app_business_python_sdk/type/group_admin_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/admins` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.get_all`<a id="whatsappbusinessgroupsget_all"></a>

Get-All-Groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = whatsappbusiness.groups.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GroupsResponse`](./whats_app_business_python_sdk/pydantic/groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.get_icon_binary`<a id="whatsappbusinessgroupsget_icon_binary"></a>

Get-Group-Icon-Binary

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.get_icon_binary(
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/icon` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.get_info`<a id="whatsappbusinessgroupsget_info"></a>

Get-Group-Info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = whatsappbusiness.groups.get_info(
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupResponse`](./whats_app_business_python_sdk/pydantic/group_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.get_invite_details`<a id="whatsappbusinessgroupsget_invite_details"></a>

Get-Group-Invite

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_invite_details_response = whatsappbusiness.groups.get_invite_details(
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GroupInviteResponse`](./whats_app_business_python_sdk/pydantic/group_invite_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/invite` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.leave_group`<a id="whatsappbusinessgroupsleave_group"></a>

Leave-Group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.leave_group(
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/leave` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.promote_to_admin`<a id="whatsappbusinessgroupspromote_to_admin"></a>

Promote-To-Group-Admin

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.promote_to_admin(
    wa_ids=["string_example"],
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### wa_ids: [`GroupAdminRequestBodyWaIds`](./whats_app_business_python_sdk/type/group_admin_request_body_wa_ids.py)<a id="wa_ids-groupadminrequestbodywaidswhats_app_business_python_sdktypegroup_admin_request_body_wa_idspy"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupAdminRequestBody`](./whats_app_business_python_sdk/type/group_admin_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/admins` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.remove_participant`<a id="whatsappbusinessgroupsremove_participant"></a>

Remove-Group-Participant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.remove_participant(
    wa_ids=["string_example"],
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### wa_ids: [`RemoveGroupParticipantRequestBodyWaIds`](./whats_app_business_python_sdk/type/remove_group_participant_request_body_wa_ids.py)<a id="wa_ids-removegroupparticipantrequestbodywaidswhats_app_business_python_sdktyperemove_group_participant_request_body_wa_idspy"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RemoveGroupParticipantRequestBody`](./whats_app_business_python_sdk/type/remove_group_participant_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/participants` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.set_group_icon`<a id="whatsappbusinessgroupsset_group_icon"></a>

Set-Group-Icon

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.set_group_icon(
    group_id="GroupId_example",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsSetGroupIconRequest`](./whats_app_business_python_sdk/type/groups_set_group_icon_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}/icon` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.groups.update_info`<a id="whatsappbusinessgroupsupdate_info"></a>

Update-Group-Info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.groups.update_info(
    subject="<New Group Subject>",
    group_id="GroupId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subject: `str`<a id="subject-str"></a>

##### group_id: `str`<a id="group_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateGroupInfoRequestBody`](./whats_app_business_python_sdk/type/update_group_info_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{GroupId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.health.check_status`<a id="whatsappbusinesshealthcheck_status"></a>

Check-Health

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.health.check_status()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.health.get_app_stats`<a id="whatsappbusinesshealthget_app_stats"></a>

Get-App-Stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_app_stats_response = whatsappbusiness.health.get_app_stats(
    format="prometheus",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stats/app` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.health.get_db_stats`<a id="whatsappbusinesshealthget_db_stats"></a>

Get-DB-Stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_db_stats_response = whatsappbusiness.health.get_db_stats(
    format="prometheus",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stats/db` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.health.get_metrics_data`<a id="whatsappbusinesshealthget_metrics_data"></a>

Get-Metrics (since v2.21.3)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metrics_data_response = whatsappbusiness.health.get_metrics_data(
    format="prometheus",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metrics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.health.get_support_info`<a id="whatsappbusinesshealthget_support_info"></a>

Get-Support-Info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_support_info_response = whatsappbusiness.health.get_support_info()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/support` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.media.download`<a id="whatsappbusinessmediadownload"></a>

Download-Media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_response = whatsappbusiness.media.download(
    media_id="MediaId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### media_id: `str`<a id="media_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/media/{MediaId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.media.remove_media`<a id="whatsappbusinessmediaremove_media"></a>

Delete-Media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.media.remove_media(
    media_id="MediaId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### media_id: `str`<a id="media_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/media/{MediaId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.media.upload_media`<a id="whatsappbusinessmediaupload_media"></a>

Upload-Media

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_media_response = whatsappbusiness.media.upload_media(
    body=open("/path/to/file", "rb"),
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`IO`
#### 🔄 Return<a id="🔄-return"></a>

[`UploadMediaResponse`](./whats_app_business_python_sdk/pydantic/upload_media_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/media` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.messages.mark_as_read`<a id="whatsappbusinessmessagesmark_as_read"></a>

Mark-Message-As-Read

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.messages.mark_as_read(
    status="read",
    message_id="MessageID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID from Webhook

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MarkMessageAsReadRequestBody`](./whats_app_business_python_sdk/type/mark_message_as_read_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messages/{MessageID}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.messages.send_message`<a id="whatsappbusinessmessagessend_message"></a>

Send-Message

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_message_response = whatsappbusiness.messages.send_message(
    to="{whatsapp-id}",
    audio={},
    contacts=[
        {
            "birthday": "2012-08-18T00:00:00.000Z",
        }
    ],
    document={},
    hsm={
        "element_name": "hello_world",
        "language": {
            "code": "en",
            "policy": "deterministic",
        },
        "localizable_params": [
            {
                "default": "<param value>",
            }
        ],
        "namespace": "business_a_namespace",
    },
    image={},
    location={
        "address": "<Location's Address>",
        "latitude": "<Latitude>",
        "longitude": "<Longitude>",
        "name": "<Location Name>",
    },
    preview_url=True,
    recipient_type="individual",
    text={
        "body": "your-text-message-content",
    },
    ttl={},
    type="text",
    video={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### to: `str`<a id="to-str"></a>

When recipient_type is individual, this field is the WhatsApp ID (phone number) returned from contacts endpoint. When recipient_type is group, this field is the WhatsApp group ID.

##### audio: [`Audio`](./whats_app_business_python_sdk/type/audio.py)<a id="audio-audiowhats_app_business_python_sdktypeaudiopy"></a>


##### contacts: List[`Contact`]<a id="contacts-listcontact"></a>

##### document: [`Document`](./whats_app_business_python_sdk/type/document.py)<a id="document-documentwhats_app_business_python_sdktypedocumentpy"></a>


##### hsm: [`Hsm`](./whats_app_business_python_sdk/type/hsm.py)<a id="hsm-hsmwhats_app_business_python_sdktypehsmpy"></a>


##### image: [`Image`](./whats_app_business_python_sdk/type/image.py)<a id="image-imagewhats_app_business_python_sdktypeimagepy"></a>


##### location: [`Location`](./whats_app_business_python_sdk/type/location.py)<a id="location-locationwhats_app_business_python_sdktypelocationpy"></a>


##### preview_url: `bool`<a id="preview_url-bool"></a>

Specifying preview_url in the request is optional when not including a URL in your message. To include a URL preview, set preview_url to true in the message body and make sure the URL begins with http:// or https://. For more information, see the Sending URLs in Text Messages section.

##### recipient_type: `str`<a id="recipient_type-str"></a>

Determines whether the recipient is an individual or a group Specifying recipient_type in the request is optional when the value is individual. However, recipient_type is required when using group. If sending a text message to a group, see the Sending Group Messages documentation.

##### text: [`Text`](./whats_app_business_python_sdk/type/text.py)<a id="text-textwhats_app_business_python_sdktypetextpy"></a>


##### ttl: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="ttl-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### type: [`MessageType`](./whats_app_business_python_sdk/type/message_type.py)<a id="type-messagetypewhats_app_business_python_sdktypemessage_typepy"></a>

##### video: [`Video`](./whats_app_business_python_sdk/type/video.py)<a id="video-videowhats_app_business_python_sdktypevideopy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SendMessageRequestBody`](./whats_app_business_python_sdk/type/send_message_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./whats_app_business_python_sdk/pydantic/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.profile.get_about`<a id="whatsappbusinessprofileget_about"></a>

Get-Profile-About

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_about_response = whatsappbusiness.profile.get_about()
```

#### 🔄 Return<a id="🔄-return"></a>

[`GetProfileAboutResponse`](./whats_app_business_python_sdk/pydantic/get_profile_about_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/profile/about` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.profile.get_photo`<a id="whatsappbusinessprofileget_photo"></a>

Get-Profile-Photo

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_photo_response = whatsappbusiness.profile.get_photo(
    format="link",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### format: `str`<a id="format-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GetProfilePhotoResponse`](./whats_app_business_python_sdk/pydantic/get_profile_photo_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/profile/photo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.profile.remove_photo`<a id="whatsappbusinessprofileremove_photo"></a>

Delete-Profile-Photo

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.profile.remove_photo()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/profile/photo` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.profile.update_about`<a id="whatsappbusinessprofileupdate_about"></a>

Update-Profile-About

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.profile.update_about(
    text="your-profile-about-text",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

Text to display in your profile's About section The max length for the string is 139 characters.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProfileAbout`](./whats_app_business_python_sdk/type/profile_about.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/profile/about` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.profile.update_photo`<a id="whatsappbusinessprofileupdate_photo"></a>

Update-Profile-Photo

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.profile.update_photo(
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProfileUpdatePhotoRequest`](./whats_app_business_python_sdk/type/profile_update_photo_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/profile/photo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.registration.request_code`<a id="whatsappbusinessregistrationrequest_code"></a>

Request-Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.registration.request_code(
    cc="<Country Code>",
    cert="<Valid Cert from Business Manager>",
    method="< sms | voice >",
    phone_number="<Phone Number>",
    pin="<Two-Step Verification PIN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cc: `str`<a id="cc-str"></a>

Numerical country code for the phone number you are registering

##### cert: `str`<a id="cert-str"></a>

Base64-encoded Verified Name certificate

##### method: `str`<a id="method-str"></a>

Method of receiving your registration code

##### phone_number: `str`<a id="phone_number-str"></a>

Phone number you are registering, without the country code or plus symbol (+)

##### pin: `str`<a id="pin-str"></a>

Existing 6-digit PIN — This is only required when two-factor verification is enabled on this account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RequestCodeRequestBody`](./whats_app_business_python_sdk/type/request_code_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.registration.verify_account`<a id="whatsappbusinessregistrationverify_account"></a>

Register-Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.registration.verify_account(
    code="your-registration-code-received-by-sms-or-voice-call",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RegisterAccountRequestBody`](./whats_app_business_python_sdk/type/register_account_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.two_step_verification.disable`<a id="whatsappbusinesstwo_step_verificationdisable"></a>

Disable-Two-Step

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.two_step_verification.disable()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/account/two-step` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.two_step_verification.enable_account`<a id="whatsappbusinesstwo_step_verificationenable_account"></a>

Enable-Two-Step

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.two_step_verification.enable_account(
    pin="your-6-digit-pin",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pin: `str`<a id="pin-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EnableTwoStepRequestBody`](./whats_app_business_python_sdk/type/enable_two_step_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/settings/account/two-step` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.users.create_user`<a id="whatsappbusinessuserscreate_user"></a>

Create-User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_response = whatsappbusiness.users.create_user(
    password="password",
    username="username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

username

##### username: `str`<a id="username-str"></a>

password

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateUserRequestBody`](./whats_app_business_python_sdk/type/create_user_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserResponse`](./whats_app_business_python_sdk/pydantic/user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.users.get_by_username`<a id="whatsappbusinessusersget_by_username"></a>

Get-User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_username_response = whatsappbusiness.users.get_by_username(
    user_username="UserUsername_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_username: `str`<a id="user_username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DetailedUserResponse`](./whats_app_business_python_sdk/pydantic/detailed_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{UserUsername}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.users.perform_login`<a id="whatsappbusinessusersperform_login"></a>

Login-User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_login_response = whatsappbusiness.users.perform_login(
    new_password="<New Admin Password>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_password: `str`<a id="new_password-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LoginAdminRequestBody`](./whats_app_business_python_sdk/type/login_admin_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserLoginResponse`](./whats_app_business_python_sdk/pydantic/user_login_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/login` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.users.perform_logout`<a id="whatsappbusinessusersperform_logout"></a>

Logout-User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
whatsappbusiness.users.perform_logout()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/logout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.users.remove_user`<a id="whatsappbusinessusersremove_user"></a>

Delete-User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_user_response = whatsappbusiness.users.remove_user(
    user_username="UserUsername_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_username: `str`<a id="user_username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserResponse`](./whats_app_business_python_sdk/pydantic/user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{UserUsername}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `whatsappbusiness.users.update_user`<a id="whatsappbusinessusersupdate_user"></a>

Update-User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_response = whatsappbusiness.users.update_user(
    password="New Password",
    user_username="UserUsername_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

password

##### user_username: `str`<a id="user_username-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateUserRequestBody`](./whats_app_business_python_sdk/type/update_user_request_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserResponse`](./whats_app_business_python_sdk/pydantic/user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{UserUsername}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
