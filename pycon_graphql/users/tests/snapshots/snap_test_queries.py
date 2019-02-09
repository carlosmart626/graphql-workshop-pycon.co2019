# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['UserAPITestCase::test_api_users 1'] = {
    'data': {
        'users': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 19,
                    'line': 2
                }
            ],
            'message': "'NoneType' object has no attribute 'user'",
            'path': [
                'users'
            ]
        }
    ]
}

snapshots['UserAPITestCase::test_register_user_already_registered_mutation 1'] = {
    'data': {
        'registerUser': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': "['This email is already registered (jhon@doe.com)']",
            'path': [
                'registerUser'
            ]
        }
    ]
}

snapshots['UserAPITestCase::test_register_user_already_registered_mutation 2'] = {
    'data': {
        'registerUser': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': 'A user already exist with the username/email provided',
            'path': [
                'registerUser'
            ]
        }
    ]
}

snapshots['UserAPITestCase::test_register_user_mutation 1'] = {
    'data': {
        'registerUser': {
            'user': {
                'email': 'me@carlosmart.co',
                'id': 'VXNlck5vZGU6Mg=='
            }
        }
    }
}

snapshots['UserAPITestCase::test_register_user_wrong_email 1'] = {
    'data': {
        'registerUser': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': "['Enter a valid email address.']",
            'path': [
                'registerUser'
            ]
        }
    ]
}
