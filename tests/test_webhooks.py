import json
from mock import patch

from basecase import GHInboxTestCase


@patch('ghinbox.webhooks.create_issue')
class PostMarkInboundWebhookTestCase(GHInboxTestCase):

    def test_postmark_creates_issue(self, create_issue):
        data = {
            'Subject': 'A test',
            'TextBody': 'Text Body',
        }
        self.app.post('/hooks/postmark', data=json.dumps(data), content_type='application/json')

        create_issue.assert_called_with('A test', 'Text Body')
