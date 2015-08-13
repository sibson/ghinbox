from flask import Flask
app = Flask(__name__)

import ghinbox.webhooks  # noqa
import ghinbox.requestid  # noqa
