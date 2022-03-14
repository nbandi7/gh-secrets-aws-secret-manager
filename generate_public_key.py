import requests

headers = {
    'Authorization': 'token <Bearer Token>',
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/nbandi7/gh-secrets-aws-secret-manager/actions/secrets/public-key', headers=headers)

print(response.text)