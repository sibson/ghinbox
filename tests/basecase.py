import unittest

from ghinbox import app


class GHInboxTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['ghuser'] = 'testuser'
        app.config['ghpassword'] = 'testpassword'
        app.config['ghrepository'] = 'testuser/testrepo'

        print app, app.config

        self.app = app.test_client()
