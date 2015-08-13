from mock import patch

from ghinbox import app, actions

from basecase import GHInboxTestCase


class CreateIssueTestCase(GHInboxTestCase):

    @patch('ghinbox.actions.login')
    def test_create_issue(self, login):

        actions.create_issue('test subject', 'test body')

        login.assert_called_with('testuser', 'testpassword')
        gh = login.return_value
        gh.repository.assert_called_with('testuser', 'testrepo')
        repo = gh.repository.return_value
        repo.create_issue.assert_called_with('test subject', 'test body')
