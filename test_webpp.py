import json
from mock import patch
import unittest

from webapp import app


class GHInboxTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()


@patch('webapp.login')
class PostMarkInboundWebhookTestCase(GHInboxTestCase):

    def setUp(self):
        super(PostMarkInboundWebhookTestCase, self).setUp()
        app.config['ghuser'] = 'testuser'
        app.config['ghpassword'] = 'testpassword'
        app.config['ghrepo'] = 'testuser/testrepo'

    def test_creates_issue(self, login):
        data = {
            'subject': 'A test',
            'TextBody': 'Text Body',
        }
        self.app.post('/hooks/postmark', data=json.dumps(data), content_type='application/json')

        login.assert_called_with('testuser', 'testpassword')
        gh = login.return_value
        gh.repository.assert_called_with('testuser', 'testrepo')
        repo = gh.repository.return_value
        repo.create_issue.assert_called_with('A test', 'Text Body')
