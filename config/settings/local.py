from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "45.136.71.0"]

ADMIN_URL = "admin/"