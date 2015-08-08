import os

from flask import Flask, request

from github3 import login
import structlog


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG') in ('1', 'y', 'True', 'true')
app.config['ghuser'] = os.environ.get('GH_USERNAME')
app.config['ghpassword'] = os.environ.get('GH_PASSWORD')
app.config['ghrepository'] = os.environ.get('GH_REPOSITORY')

logger = structlog.get_logger()


def create_issue(title, body):
    gh = login(app.config['ghuser'], app.config['ghpassword'])
    repo = gh.repository(*app.config['ghrepository'].split('/'))
    repo.create_issue(title, body)


@app.route('/hooks/postmark', methods=['POST'])
def postmark_incomming_hook():
    # TODO HTTP Basic Auth
    inbound = request.json

    logger.debug('postmark', data=inbound)

    title = inbound['Subject']
    body = inbound['TextBody']

    logger.debug('creating issue', title=title)

    # TODO taskify
    create_issue(title, body)

    return 'OK'


if __name__ == '__main__':
    from structlog.stdlib import LoggerFactory
    from structlog.threadlocal import wrap_dict
    import logging

    structlog.configure(
        context_class=wrap_dict(dict),
        logger_factory=LoggerFactory(),
    )
    logging.basicConfig(level=logging.DEBUG)
    app.run()
