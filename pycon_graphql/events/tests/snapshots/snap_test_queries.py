# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['EventAPITestCase::test_api_events 1'] = {
    'data': {
        'events': {
            'edges': [
                {
                    'node': {
                        'endHour': '15:00:00',
                        'eventDay': '2019-01-28',
                        'initialHour': '13:00:00',
                        'title': 'Pycon 2019 - GraphQL Workshop'
                    }
                }
            ]
        }
    }
}

snapshots['EventAPITestCase::test_enroll_user_mutation 1'] = {
    'data': {
        'enrollUserEvent': {
            'event': {
                'title': 'Pycon 2019 - GraphQL Workshop'
            },
            'invitee': {
                'user': {
                    'email': 'jhon@doe.com'
                }
            },
            'ok': True
        }
    }
}

snapshots['EventAPITestCase::test_enroll_user_not_valid_mutation 1'] = {
    'data': {
        'enrollUserEvent': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': "['User with id VXNlck5vZGU6OTk5OQ== does not exist']",
            'path': [
                'enrollUserEvent'
            ]
        }
    ]
}

snapshots['EventAPITestCase::test_enroll_user_not_valid_mutation 2'] = {
    'data': {
        'enrollUserEvent': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': "['Event with id 55d540ea-e708-4322-86e6-000000000000 does not exist']",
            'path': [
                'enrollUserEvent'
            ]
        }
    ]
}

snapshots['EventAPITestCase::test_api_events 2'] = {
    'data': {
        'organization': {
            'description': 'Python Bogotá description',
            'title': 'Python Bogotá'
        }
    }
}

snapshots['EventAPITestCase::test_enroll_user_mutation 2'] = {
    'data': {
        'enrollUserEvent': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': "['This user is already invited (jhon@doe.com)']",
            'path': [
                'enrollUserEvent'
            ]
        }
    ]
}
