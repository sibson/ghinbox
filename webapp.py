import os

from flask import Flask, request

import structlog


app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG') in ('1', 'y', 'True', 'true')
app.config['ghuser'] = os.environ.get('GH_USERNAME')
app.config['ghpassword'] = os.environ.get('GH_PASSWORD')
app.config['ghrepository'] = os.environ.get('GH_REPOSITORY')

logger = structlog.get_logger()


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
