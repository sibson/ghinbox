[![Circle CI](https://circleci.com/gh/sibson/ghinbox.svg?style=svg)](https://circleci.com/gh/sibson/ghinbox)
[![Build Status](http://img.shields.io/travis/sibson/ghinbox.svg)](https://travis-ci.org/sibson/ghinbox)
[![Code Climate](http://img.shields.io/codeclimate/github/sibson/ghinbox.svg)](https://codeclimate.com/github/sibson/ghinbox)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://sibson.mit-license.org)

# Deploy and Setup

  1. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
  1. Fill in the config vars with your GitHub credencials and repository
  1. Run ```heroku addons:open postmark -a app-name```
  1. Select Inbound Mail from the webpage opened in the previous step
  1. Enter ```https://yourapp.herokuapp.com/hooks/postmark``` for the webhook URL
  1. Send an email to the address provided by PostMark

# Usage
Any emails sent to the POSTMARK_INBOUND_ADDRESS will automatically be converted into a new GitHub issue in your repository.

You can retrieve the email address to submit issue to by running

    heroku config:get POSTMARK_INBOUND_ADDRESS

It can also be helpful to create an easy to remember email address that forwards to the POSTMARK_INBOUND_ADDRESS.


# Development

You can test the server locally by starting it with

    python webapp.py

The worker can be run with

    rqworker

Finaly, you can use curl to simulate calling the webhook

    curl -H "Content-Type: application/json" -X POST http://localhost:5000/hooks/postmark -d '{"Subject": "test subject", "TextBody": "A long description"}' 
