[![Test Status](https://circleci.com/gh/sibson/ghinbox.svg?style=svg)](https://circleci.com/gh/sibson/ghinbox)
[![Code Climate](https://codeclimate.com/repos/568ca7c459754f7dc3000183/badges/f5f3486504565a83ecad/gpa.svg)](https://codeclimate.com/repos/568ca7c459754f7dc3000183/feed)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://sibson.mit-license.org)

# Deploy and Setup

  1. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
  1. Fill in the config vars with your GitHub credencials and repository info
  1. Ensure you scale up the worker dyno ```heroku ps:scale worker:1 -a app-name```
  1. Run ```heroku addons:open postmark -a app-name```
    1. Click through the wizard until you get to *Get Started with your New Server* 
    1. Select Process Inbound Mail
    1. Make note of the inbound email address
    1. Enter ```https://yourapp.herokuapp.com/hooks/postmark``` for the webhook URL
  1. Send an email to the inbound address provided by PostMark

# Usage
Any emails sent to the POSTMARK_INBOUND_ADDRESS will automatically be converted into a new GitHub issue in your repository.

You can always retrieve the email address to submit issues to by running

    heroku config:get POSTMARK_INBOUND_ADDRESS

You also might want to create an easily to remember email alias, rather than the random address Postmark provides.
Postmark has instructions to configure an alias using [Gmail](http://support.postmarkapp.com/article/785-configuring-a-custom-email-address-forward-with-gmail) or a [Custom Domain](http://developer.postmarkapp.com/developer-process-domain.html).

# Development

You can test the server locally by starting it with

    python webapp.py


You can use curl to simulate calling the webhook

    curl -H "Content-Type: application/json" -X POST http://localhost:5000/hooks/postmark -d '{"Subject": "test subject", "TextBody": "A long description"}' 

The worker can be run with

    rqworker
