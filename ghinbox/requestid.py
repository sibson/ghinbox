from flask import request

from structlog import get_logger

from ghinbox import app


logger = get_logger()


@app.before_request
def handle_request_id():
    request.id = request.headers.get('X-Request-ID')
    if request.id:
        global logger
        logger = logger.new(request_id=request.id)
