from flask.ext.rq import job
from github3 import login
from structlog import get_logger

from ghinbox import app


logger = get_logger()


@job
def create_issue(title, body):
    gh = login(app.config['ghuser'], app.config['ghpassword'])
    repo = gh.repository(*app.config['ghrepository'].split('/'))
    repo.create_issue(title, body)
