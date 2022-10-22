from environs import Env

env = Env()

IS_PRODUCTION = env.bool('PRODUCTION', False)

if not IS_PRODUCTION:
    env.read_env()

RELOAD = not IS_PRODUCTION

PORT = env.int('PORT')

PROJECT_NAME = 'my_template'

SQLALCHEMY_DATABASE_URL = (
    f'bigquery://{env.str("GCP_PROJECT")}/{env.str("GCP_DATASET")}'
)

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

SECRET_KEY = env.str('SECRET_KEY')

BACKEND_CORS_ORIGINS = env.list('BACKEND_CORS_ORIGINS', default=[])

API_V1_STR = '/api/v1'
