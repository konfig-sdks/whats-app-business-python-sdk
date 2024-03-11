operation_parameter_map = {
    '/settings/application-GET': {
        'parameters': [
        ]
    },
    '/settings/application/media/providers-GET': {
        'parameters': [
        ]
    },
    '/settings/application/media/providers/{ProviderName}-DELETE': {
        'parameters': [
            {
                'name': 'ProviderName'
            },
        ]
    },
    '/settings/application-DELETE': {
        'parameters': [
        ]
    },
    '/account/shards-POST': {
        'parameters': [
            {
                'name': 'cc'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'pin'
            },
            {
                'name': 'shards'
            },
        ]
    },
    '/settings/application/media/providers-POST': {
        'parameters': [
        ]
    },
    '/settings/application-PATCH': {
        'parameters': [
            {
                'name': 'callback_backoff_delay_ms'
            },
            {
                'name': 'callback_persist'
            },
            {
                'name': 'heartbeat_interval'
            },
            {
                'name': 'max_callback_backoff_delay_ms'
            },
            {
                'name': 'media'
            },
            {
                'name': 'on_call_pager'
            },
            {
                'name': 'pass_through'
            },
            {
                'name': 'sent_status'
            },
            {
                'name': 'unhealthy_interval'
            },
            {
                'name': 'webhooks'
            },
        ]
    },
    '/settings/backup-POST': {
        'parameters': [
            {
                'name': 'password'
            },
        ]
    },
    '/settings/restore-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/settings/business/profile-GET': {
        'parameters': [
        ]
    },
    '/settings/business/profile-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'address'
            },
            {
                'name': 'email'
            },
            {
                'name': 'vertical'
            },
            {
                'name': 'websites'
            },
        ]
    },
    '/certificates/webhooks/ca-DELETE': {
        'parameters': [
        ]
    },
    '/certificates/external/ca-GET': {
        'parameters': [
        ]
    },
    '/certificates/webhooks/ca-GET': {
        'parameters': [
        ]
    },
    '/certificates/external-POST': {
        'parameters': [
        ]
    },
    '/certificates/webhooks/ca-POST': {
        'parameters': [
        ]
    },
    '/contacts-POST': {
        'parameters': [
            {
                'name': 'contacts'
            },
            {
                'name': 'blocking'
            },
        ]
    },
    '/groups-POST': {
        'parameters': [
            {
                'name': 'subject'
            },
        ]
    },
    '/groups/{GroupId}/icon-DELETE': {
        'parameters': [
            {
                'name': 'GroupId'
            },
            {
                'name': 'File'
            },
        ]
    },
    '/groups/{GroupId}/invite-DELETE': {
        'parameters': [
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}/admins-DELETE': {
        'parameters': [
            {
                'name': 'wa_ids'
            },
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups-GET': {
        'parameters': [
        ]
    },
    '/groups/{GroupId}/icon-GET': {
        'parameters': [
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}-GET': {
        'parameters': [
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}/invite-GET': {
        'parameters': [
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}/leave-POST': {
        'parameters': [
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}/admins-PATCH': {
        'parameters': [
            {
                'name': 'wa_ids'
            },
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}/participants-DELETE': {
        'parameters': [
            {
                'name': 'wa_ids'
            },
            {
                'name': 'GroupId'
            },
        ]
    },
    '/groups/{GroupId}/icon-POST': {
        'parameters': [
            {
                'name': 'GroupId'
            },
            {
                'name': 'File'
            },
        ]
    },
    '/groups/{GroupId}-PUT': {
        'parameters': [
            {
                'name': 'subject'
            },
            {
                'name': 'GroupId'
            },
        ]
    },
    '/health-GET': {
        'parameters': [
        ]
    },
    '/stats/app-GET': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/stats/db-GET': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/metrics-GET': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/support-GET': {
        'parameters': [
        ]
    },
    '/media/{MediaId}-GET': {
        'parameters': [
            {
                'name': 'MediaId'
            },
        ]
    },
    '/media/{MediaId}-DELETE': {
        'parameters': [
            {
                'name': 'MediaId'
            },
        ]
    },
    '/media-POST': {
        'parameters': [
        ]
    },
    '/messages/{MessageID}-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'MessageID'
            },
        ]
    },
    '/messages-POST': {
        'parameters': [
            {
                'name': 'to'
            },
            {
                'name': 'audio'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'document'
            },
            {
                'name': 'hsm'
            },
            {
                'name': 'image'
            },
            {
                'name': 'location'
            },
            {
                'name': 'preview_url'
            },
            {
                'name': 'recipient_type'
            },
            {
                'name': 'text'
            },
            {
                'name': 'ttl'
            },
            {
                'name': 'type'
            },
            {
                'name': 'video'
            },
        ]
    },
    '/settings/profile/about-GET': {
        'parameters': [
        ]
    },
    '/settings/profile/photo-GET': {
        'parameters': [
            {
                'name': 'format'
            },
        ]
    },
    '/settings/profile/photo-DELETE': {
        'parameters': [
        ]
    },
    '/settings/profile/about-PATCH': {
        'parameters': [
            {
                'name': 'text'
            },
        ]
    },
    '/settings/profile/photo-POST': {
        'parameters': [
            {
                'name': 'File'
            },
        ]
    },
    '/account-POST': {
        'parameters': [
            {
                'name': 'cc'
            },
            {
                'name': 'cert'
            },
            {
                'name': 'method'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'pin'
            },
        ]
    },
    '/account/verify-POST': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/settings/account/two-step-DELETE': {
        'parameters': [
        ]
    },
    '/settings/account/two-step-POST': {
        'parameters': [
            {
                'name': 'pin'
            },
        ]
    },
    '/users-POST': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/users/{UserUsername}-GET': {
        'parameters': [
            {
                'name': 'UserUsername'
            },
        ]
    },
    '/users/login-POST': {
        'parameters': [
            {
                'name': 'new_password'
            },
        ]
    },
    '/users/logout-POST': {
        'parameters': [
        ]
    },
    '/users/{UserUsername}-DELETE': {
        'parameters': [
            {
                'name': 'UserUsername'
            },
        ]
    },
    '/users/{UserUsername}-PUT': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'UserUsername'
            },
        ]
    },
};