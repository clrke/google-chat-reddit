import json
import requests
import settings
import sys

BOT_NAME = 'CHAT_REDDIT_BOT 0.1'
MEMES_LOG_FILENAME = 'memes.log'

def get_params():
    if len(sys.argv) > 1:
        if len(sys.argv) != 4:
            raise Exception(
                    'Incorrect format! python {0} [<subreddit> <chat_url> <log_filename>]'
                    .format(sys.argv[0])
            )
        return sys.argv[1:4]

    return (settings.subreddit, settings.hangouts_webhook_url, settings.log_filename)


def get_bot_history(log_filename):
    try:
        with open(log_filename, 'r') as f:
            return list(map(lambda s: s.strip(), f.readlines()))
    except FileNotFoundError:
        with open(MEMES_LOG_FILENAME, 'w') as f:
            return []


def append_to_bot_history(log_filename, id):
    with open(log_filename, 'a') as f:
        f.write(id)
        f.write('\n')


def send_memes():
    subreddit, chat_url, log_filename = get_params()

    subreddit_api_url = 'https://www.reddit.com/r/{0}/.json'.format(subreddit)
    response = requests.get(subreddit_api_url, headers = {'User-agent': BOT_NAME}).json()

    bot_history = get_bot_history(log_filename)

    valid_memes = list(filter(
            lambda m: len(m['data']['selftext']) == 0 and m['data']['id'] not in bot_history,
            response['data']['children']
    ))

    if not len(valid_memes):
        raise Exception('Sorry! Ran out of memes!')

    meme = valid_memes[0]

    message = '{0} <{1}>'.format(meme['data']['title'], meme['data']['url'])

    print(message)

    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    response = requests.post(chat_url, data=json.dumps({'text': message}), headers=headers).json()
    print(response)

    append_to_bot_history(log_filename, meme['data']['id'])


if __name__ == '__main__':
    send_memes()
