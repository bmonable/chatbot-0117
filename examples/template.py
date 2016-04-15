from wit import Wit

access_token = 'YOUR_ACCESS_TOKEN'


def say(session_id, msg):
    print(msg)


def merge(session_id, context, entities, msg):
    return context


def error(session_id, context):
    print('Oops, I don\'t know what to do.')

actions = {
    'say': say,
    'merge': merge,
    'error': error,
}
client = Wit(access_token, actions)

session_id = 'my-user-id-42'
client.run_actions(session_id, 'your message', {})
