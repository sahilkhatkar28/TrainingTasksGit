from starlette.config import Config


config = Config('.env')

GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')
GITHUB_CLIENT_ID = config('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = config('GITHUB_CLIENT_SECRET')
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


