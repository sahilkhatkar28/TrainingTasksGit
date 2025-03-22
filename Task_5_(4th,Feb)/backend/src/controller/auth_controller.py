# BACKEND/src/controllers/auth_controller.py
from fastapi import APIRouter, Depends, HTTPException, status, Request
from authlib.integrations.starlette_client import OAuth, OAuthError
from src.config.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from src.services.auth_service import create_access_token
from src.models.user_model import User
from src.services.user_service import get_current_user

router = APIRouter()

oauth = OAuth()

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    client_kwargs={'scope': 'openid email profile'},
)

oauth.register(
    name='github',
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@router.get('/login/google')
async def google_login(request: Request):
    redirect_uri = request.url_for('google_auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get('/auth/google')
async def google_auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return {'error': error.error}
    user = await oauth.google.parse_id_token(request, token)
    access_token = create_access_token(data={"sub": user['email'], "name": user['name']})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/login/github')
async def github_login(request: Request):
    redirect_uri = request.url_for('github_auth')
    print(f"Redirect URI: {redirect_uri}") #print the uri
    return await oauth.github.authorize_redirect(request, redirect_uri)

@router.get('/auth/github')
async def github_auth(request: Request):
    try:
        token = await oauth.github.authorize_access_token(request)
    except OAuthError as error:
        return {'error': error.error}

    resp = await oauth.github.get('user', token=token)
    resp.raise_for_status()
    profile = resp.json()

    resp_email = await oauth.github.get('user/emails', token=token)
    resp_email.raise_for_status()
    emails = resp_email.json()
    primary_email = next((e['email'] for e in emails if e['primary']), emails[0]['email'])

    access_token = create_access_token(data={"sub": primary_email, "name": profile['name']})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/protected')
async def protected(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.name}! Your email is {current_user.email}"}