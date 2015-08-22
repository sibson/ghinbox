import os

from flask import Flask
from flask_rq import RQ


app = Flask(__name__)
rq = RQ(app)

app.config['ghuser'] = os.environ.get('GH_USERNAME')
app.config['ghpassword'] = os.environ.get('GH_PASSWORD')
app.config['ghrepository'] = os.environ.get('GH_REPOSITORY')
app.config['RQ_DEFAULT_URL'] = os.environ.get('REDIS_URL', 'redis://')
app.config['ROLLBAR_ACCESS_TOKEN'] = os.environ.get('ROLLBAR_ACCESS_TOKEN')

import ghinbox.webhooks  # noqa
import ghinbox.requestid  # noqa
