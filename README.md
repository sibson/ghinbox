# Deploy and Setup

  1. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
  1. Fill in the config vars with your GitHub credencials and repository
  1. Run ```heroku addons:open postmark -a app-name```
  1. Select Inbound Mail from the webpage opened in the previous step
  1. Enter ```https://yourapp.herokuapp.com/hooks/postmark``` for the webhook URL

# Usage
You can always retrieve the email address to submit issue to by running

    heroku config:get POSTMARK_INBOUND_ADDRESS

It can also be helpful to create an easy to remember email address that forwards to the POSTMARK_INBOUND_ADDRESS.

Now any emails sent to the POSTMARK_INBOUND_ADDRESS will automatically be converted into a new GitHub issue in your repository.
