from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer

from jwt import PyJWKClient
import jwt
from typing import Annotated
from pydantic import BaseModel

from .configs import get_setings

settings = get_setings()

oauth_2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl=settings.token_url,
    authorizationUrl=settings.authorization_url,
    refreshUrl=settings.refresh_url,
)


class User(BaseModel):
    sub: str
    name: str
    email: str


async def valid_access_token(
    access_token: Annotated[str, Depends(oauth_2_scheme)]
):
    url = settings.token_certs
    jwks_client = PyJWKClient(url)

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(access_token)
        data = jwt.decode(
            access_token,
            signing_key.key,
            algorithms=["RS256"],
            audience="510a48a7-4114-4fef-8240-a19307a8c450",
            options={"verify_exp": True},
        )
        return data
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Not authenticated")


async def get_user(
        json: Annotated[dict, Depends(valid_access_token)]
):
    return User(**json)
