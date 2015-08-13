import os

import rollbar
import rollbar.contrib.flask
import structlog

from flask import Flask, got_request_exception

from ghinbox import app

logger = structlog.get_logger()


@app.before_first_request
def init_rollbar():
    rollbar.init(
        # access token for the demo app: https://rollbar.com/demo
        app.config['ROLLBAR_ACCESS_TOKEN'],
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


if __name__ == '__main__':
    from structlog.stdlib import LoggerFactory
    from structlog.threadlocal import wrap_dict
    import logging

    structlog.configure(
        context_class=wrap_dict(dict),
        logger_factory=LoggerFactory(),
    )
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
