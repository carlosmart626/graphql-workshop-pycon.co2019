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
                        'eventDay': '2019-02-10',
                        'initialHour': '13:00:00',
                        'title': 'Pycon 2019 - GraphQL Workshop'
                    }
                }
            ]
        }
    }
}

snapshots['EventAPITestCase::test_api_events 2'] = {
    'data': {
        'organization': {
            'description': 'Python Bogotá description',
            'title': 'Python Bogotá'
        }
    }
}

snapshots['EventAPITestCase::test_enroll_user_mutation 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': 'Cannot query field "enrollUserEvent" on type "Mutations".'
        }
    ]
}

snapshots['EventAPITestCase::test_enroll_user_mutation 2'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': 'Cannot query field "enrollUserEvent" on type "Mutations".'
        }
    ]
}

snapshots['EventAPITestCase::test_enroll_user_not_valid_mutation 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': 'Cannot query field "enrollUserEvent" on type "Mutations".'
        }
    ]
}

snapshots['EventAPITestCase::test_enroll_user_not_valid_mutation 2'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 15,
                    'line': 3
                }
            ],
            'message': 'Cannot query field "enrollUserEvent" on type "Mutations".'
        }
    ]
}
