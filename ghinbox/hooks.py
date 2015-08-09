from flask import Flask, request

from structlog import get_logger

from ghinbox import app
from ghinbox.actions import create_issue



logger = get_logger()


@app.route('/hooks/postmark', methods=['POST'])
def postmark_incomming_hook():
    # TODO HTTP Basic Auth
    inbound = request.json

    logger.debug('postmark', data=inbound)

    title = inbound['Subject']
    body = inbound['TextBody']

    logger.debug('creating issue', title=title)

    print 'in create', create_issue
    # TODO taskify
    create_issue(title, body)

    return 'OK'
