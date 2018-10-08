# Google Hangouts Chat bot for Reddit Memes

## Installation (steps 2-5 are optional)
1. Setup a webhook in your Google Chat channel by `Channel Header > Configure webhooks`
2. Create a `settings.py`
3. Add this line: `subreddit = '<subreddit, e.g., ProgrammerHumor>'`
4. Add this line: `hangouts_webhook_url = '<hangouts webhook url>'`
5. Add this line: `log_filename = 'memes.log'`
6. Install `python3`, `pip`, and run `pip install requests`

## Running
### Running with settings.py
Run `python sawaw_puas.py`. Make sure that you've followed steps 2-5 above.

### Running with args
Alternatively, you can run it without touching a settings.py by specifying the subreddit and hangouts webhook url via args.
`python sawaw_puas.py <subreddit> <hangouts webhook url> <log_filename>`

#### Example:

`
python sawaw_puas.py ProgrammerHumor https://chat.googleapis.com/v1/spaces/xxyy/messages\?key\=1234\&token\=asdf memes.log
`
