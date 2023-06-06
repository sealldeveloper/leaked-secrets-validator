import argparse
import requests
parser = argparse.ArgumentParser(
                    prog='Slack Webhook Checker',
                    description='Attempt to check if a slack webhook is active, with a message')
parser.add_argument('--webbook','-w',
                    dest='webhook',required=True)
parser.add_argument('--message','-m',
                    dest='message',required=True)
args = parser.parse_args()
print(f'Sending "{args.message}" to {args.webhook}...')
headers = {
    'Content-type': 'application/json',
    '{-----text-': f'{args.message}',
}

res = requests.post(args.webhook, headers=headers)
print(f'{res.text} - {res.status_code}')