# Google Hangouts Chat bot for Reddit Memes

## Installation (steps 1-4 are optional)
1. Create a `settings.py`
2. Add this line: `subreddit = '<subreddit, e.g., ProgrammerHumor>'`
3. Add this line: `hangouts_webhook_url = '<hangouts webhook url>'`
4. Add this line: `log_filename = 'memes.log'`
5. Install `python3`, `pip`, and run `pip install requests`

## Running
### Running with settings.py
Run `python sawaw_puas.py`. Make sure that you've followed steps 1-4 above.

### Running with args
Alternatively, you can run it without touching a settings.py by specifying the subreddit and hangouts webhook url via args.
`python sawaw_puas.py <subreddit> <hangouts webhook url> <log_filename>`
