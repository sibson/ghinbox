from flask import request

from structlog import get_logger

from ghinbox import app
from ghinbox.tasks import create_issue


logger = get_logger()


@app.route('/hooks/postmark', methods=['POST'])
def postmark_incomming_hook():
    # TODO #2 HTTP Basic Auth

    inbound = request.json
    if not inbound:
        return 'ERR', 400

    logger.debug('postmark', data=inbound)

    title = inbound['Subject']
    body = inbound['TextBody']

    logger.debug('creating issue', title=title)

    create_issue.delay(title, body)

    return 'OK'
