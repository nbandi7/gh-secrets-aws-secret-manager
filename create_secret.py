import requests

headers = {
    'Authorization': 'token <bearer token>',
    'Accept': 'application/vnd.github.v3+json',
}

data = {
  '{"encrypted_value":"<encrypted value>", "key_id":"<public key id>"}'
}

response = requests.put('https://api.github.com/repos/nbandi7/gh-secrets-aws-secret-manager/actions/secrets/<Secret Name>', headers=headers, data=data)\

print(response.text)