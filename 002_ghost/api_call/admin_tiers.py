import requests
import jwt
from datetime import datetime as date
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("api_url")
# Admin API admin_api_key goes here
admin_api_key = os.getenv("admin_api_key")

# Split the admin_api_key into ID and SECRET
id, secret = admin_api_key.split(':')

# Prepare header and payload
iat = int(date.now().timestamp())

header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
payload = {
    'iat': iat,
    'exp': iat + 5 * 60,
    'aud': '/admin/'
}

# Create the token (including decoding secret)
token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

# Make an authenticated request to create a post
url_tiers = f'{api_url}/ghost/api/admin/tiers/'
headers = {'Authorization': 'Ghost {}'.format(token)}
r = requests.get(url_tiers, headers=headers)

print(r.content)