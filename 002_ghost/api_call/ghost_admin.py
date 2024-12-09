import requests
import jwt
from datetime import datetime as date
import os
from dotenv import load_dotenv
import json


class GhostAdmin:
    def __init__(self):
        load_dotenv()
        self.url_base = os.getenv("base_url")
        self.url_tiers = f"{self.url_base}/ghost/api/admin/tiers/"
        self.url_posts = f"{self.url_base}/ghost/api/admin/posts/"

        self.api_key = os.getenv("admin_api_key")

        id, secret = self.api_key.split(":")
        iat = int(date.now().timestamp())
        payload = {"iat": iat, "exp": iat + 5 * 60, "aud": "/admin/"}
        token = jwt.encode(
            payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": id}
        )
        self.headers = {"Authorization": f"Ghost {token}"}

    def check_response(self, response):
        if response:
            return "Success!"
        else:
            raise Exception(f"non-success status code: {response.status_code}")

    def get_tiers(self, **kwargs):
        """https://ghost.org/docs/admin-api#tiers"""
        include = kwargs.get("include")
        url = f"{self.url_tiers}?include={include}" if include else self.url_tiers
        print("url:", url)
        print("headers:", self.headers)
        response = requests.get(url=url, headers=self.headers)
        self.check_response(response)
        return json.loads(response.content)

    def post_posts(self, source=None, posts=None):
        """https://ghost.org/docs/admin-api#creating-a-post"""
        if not isinstance(posts, list):
            raise Exception("posts should be a list type")
        url = f"{self.url_posts}?source=html" if source == "html" else self.url_posts
        response = requests.post(url=url, headers=self.headers, json={"posts": posts})
        return self.check_response(response)

    def post_post(self, source=None, post=None):
        if not isinstance(post, dict):
            raise Exception("post should be a dict type")
        posts = [post]
        return self.post_posts(source=source, posts=posts)
