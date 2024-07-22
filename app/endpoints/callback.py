from fastapi import APIRouter, HTTPException
import aiohttp
import tweepy

from ..services import TokenService

router = APIRouter()


@router.get("/callback")
async def callback(state: str, code: str):
    if state != "state":
        raise HTTPException(status_code=400)

    oauth_token = TokenService.create_client().fetch_token(
        f"https://xn--zon-oq8e.com/callback?state={state}&code={code}",
    )

    client = tweepy.Client(
        bearer_token=oauth_token,
        consumer_key=TokenService.get("x_consumerkey"),
        consumer_secret=TokenService.get("x_consumersecret"),
        access_token=TokenService.get("x_clientid"),
        access_token_secret=TokenService.get("x_clientsecretid"),
    )
