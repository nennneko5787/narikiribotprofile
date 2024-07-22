import os
from typing import Optional

import tweepy

if os.path.isfile(".env"):
    from dotenv import load_dotenv

    load_dotenv()


class TokenService:
    @classmethod
    def get(cls, key: str) -> Optional[str]:
        return os.getenv(key)

    @classmethod
    def create_client(cls) -> tweepy.OAuth2UserHandler:
        client_id = cls.get("x_clientid")
        client_secret = cls.get("x_clientsecret")
        return tweepy.OAuth2UserHandler(
            client_id=client_id,
            redirect_uri="https://xn--zon-oq8e.com/callback",
            scope=[
                "tweet.read",
                "tweet.write",
                "users.read",
                "offline.access",
            ],
            client_secret=client_secret,
        )
