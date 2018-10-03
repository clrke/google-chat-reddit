import requests
import settings
import sys

BOT_NAME = 'CHAT_REDDIT_BOT 0.1'
MEMES_LOG_FILENAME = 'memes.log'

def get_params():
    if len(sys.argv) > 1:
        if len(sys.argv) != 3:
            raise Exception(
                    'Incorrect format! python {0} [<subreddit> <chat_url>]'
                    .format(sys.argv[0])
            )
        return sys.argv[1:3]

    return (settings.subreddit, settings.hangouts_webhook_url)


def get_bot_history():
    try:
        with open(MEMES_LOG_FILENAME, 'r') as f:
            return list(map(lambda s: s.strip(), f.readlines()))
    except FileNotFoundError:
        with open(MEMES_LOG_FILENAME, 'w') as f:
            return []


def append_to_bot_history(id):
    with open(MEMES_LOG_FILENAME, 'a') as f:
        f.write(id)
        f.write('\n')


def send_memes():
    subreddit, chat_url = get_params()

    subreddit_api_url = 'https://www.reddit.com/r/{0}/.json'.format(subreddit)
    response = requests.get(subreddit_api_url, headers = {'User-agent': BOT_NAME}).json()

    bot_history = get_bot_history()

    valid_memes = list(filter(
            lambda m: len(m['data']['selftext']) == 0 and m['data']['id'] not in bot_history,
            response['data']['children']
    ))

    if not len(valid_memes):
        raise Exception('Sorry! Ran out of memes!')

    meme = valid_memes[0]

    message = '{0} {1}'.format(meme['data']['title'], meme['data']['url'])

    print(message)

    # TODO: send the message

    append_to_bot_history(meme['data']['id'])


if __name__ == '__main__':
    send_memes()
