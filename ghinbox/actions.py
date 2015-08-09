from github3 import login

from ghinbox import app


def create_issue(title, body):
    gh = login(app.config['ghuser'], app.config['ghpassword'])
    repo = gh.repository(*app.config['ghrepository'].split('/'))
    repo.create_issue(title, body)
