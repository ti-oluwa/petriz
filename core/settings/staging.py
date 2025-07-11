import datetime
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import functools

from helpers.generics.utils.db import get_database_url
from helpers.fastapi import default_settings
from helpers.fastapi.exceptions.capture import ExceptionCaptor

load_dotenv(find_dotenv(".env.staging", raise_error_if_not_found=True))


BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

APPLICATION_NAME = os.getenv("FAST_API_APPLICATION_NAME")
APPLICATION_VERSION = os.getenv("FAST_API_APPLICATION_VERSION")
APP_DESCRIPTION = """
Petriz API provides endpoints for the extensive and customizable search 
of Petroleum related terms from a growing database of Petroleum and 
Energy related terminologies.
"""

APP = {
    "debug": DEBUG,
    "title": APPLICATION_NAME,
    "description": APP_DESCRIPTION,
    "version": APPLICATION_VERSION,
    "redoc_url": "/api/redoc",
    "docs_url": "/api/docs",
    "openapi_url": "/api/openapi.json",
    "contact": {"name": "Daniel Toluwalase Afolayan"},
    "license_info": {"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
}


DEFAULT_DEPENDENCIES = []


INSTALLED_APPS = [
    "api",
    "apps.tokens",
    "apps.accounts",
    "apps.clients",
    "apps.search",
    "apps.quizzes",
    "apps.audits",
]


get_driver_url = functools.partial(
    get_database_url,
    db_type="postgresql",
    db_name=str(os.getenv("DB_NAME")),
    db_user=str(os.getenv("DB_USER")),
    db_password=str(os.getenv("DB_PASSWORD")),
    db_host=str(os.getenv("DB_HOST")),
    db_port=str(os.getenv("DB_PORT")),
)


SQLALCHEMY = {
    "engine": {
        "url": get_driver_url(db_driver="psycopg2"),
        "future": True,
        "connect_args": {},
        "echo": False,
        "pool_size": 20,
        "max_overflow": 0,
        "pool_pre_ping": True,
        "pool_recycle": 3600,
    },
    "async_engine": {
        "url": get_driver_url(db_driver="asyncpg"),
        "future": True,
        "connect_args": {},
    },
    "sessionmaker": {
        "sync": {
            "autocommit": False,
            "autoflush": False,
            "future": True,
            "expire_on_commit": False,
        },
        "async": {
            "autocommit": False,
            "autoflush": False,
            "future": True,
            "expire_on_commit": False,
        },
    },
}


PASSWORD_SCHEMES = [
    "argon2",
    "pbkdf2_sha512",
    "md5_crypt",
]

PASSWORD_VALIDATORS = [
    *default_settings.PASSWORD_VALIDATORS,
    "apps.accounts.validators.min_password_length_validator",
]

TIMEZONE = "UTC"

AUTH_USER_MODEL = "accounts.Account"

MIDDLEWARE = [
    # "starlette.middleware.httpsredirect.HTTPSRedirectMiddleware",
    "helpers.fastapi.middleware.core.RequestProcessTimeMiddleware",
    "helpers.fastapi.sqlalchemy.middleware.AsyncSessionMiddleware",
    (
        "helpers.fastapi.auditing.middleware.ConnectionEventLogMiddleware",
        {
            "logger": "api.auditing.redis_cached_logger",
            "log_builder": "api.auditing.build_audit_log_entries",
            "excluded_paths": [
                r"^/api/openapi.json$",
                r"^/api/docs.*$",
                r"^/api/redoc.*$",
                r"^/api/v[1-9]{1,}/audits.+$",
                r"^/api/v[1-9]{1,}/?$",
                r"^/mcp.*$",
            ],
            "include_request": True,
            "include_response": True,
            "compress_body": True,
        },
    ),
    (
        "starlette.middleware.cors.CORSMiddleware",
        {
            "allow_origins": ["*"],
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        },
    ),
    (
        "starlette.middleware.gzip.GZipMiddleware",
        {
            "minimum_size": 1024 * 10,  # 10 KB
            "compresslevel": 9,
        },
    ),
    *default_settings.MIDDLEWARE,
    (
        "helpers.fastapi.response.middleware.FormatJSONResponseMiddleware",
        {
            "format": True,
            "formatter": "default",
            "excluded_paths": [
                r"^(?!/api/v).*$",
            ],
        },
    ),
]

EXCEPTION_HANDLERS = {
    **default_settings.EXCEPTION_HANDLERS,
    ExceptionCaptor.ExceptionCaptured: "core.exception_handling.formatted_exception_captured_handler",
}

OTP_LENGTH = 6

OTP_VALIDITY_PERIOD = 30 * 60

ALLOWED_HOSTS = ["*"]

BLACKLISTED_HOSTS = []

BLACKLISTED_IPS = []

MAILING = {
    "fastapi_mail": {
        "MAIL_SERVER": os.getenv("MAIL_SERVER"),
        "MAIL_PORT": os.getenv("MAIL_PORT"),
        "MAIL_STARTTLS": os.getenv("MAIL_USE_TLS"),
        "MAIL_SSL_TLS": os.getenv("MAIL_USE_SSL"),
        "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
        "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
        "MAIL_FROM": os.getenv("MAIL_FROM"),
        "MAIL_FROM_NAME": "Petriz",
        "USE_CREDENTIALS": True,
        "TEMPLATE_FOLDER": None,
        "SUPPRESS_SEND": False,
    }
}

REDIS_URL = os.getenv("REDIS_URL")

AUTH_TOKEN_VALIDITY_PERIOD = datetime.timedelta(days=30)

SENSITIVE_HEADERS = {
    "x-client-id",
    "x-client-secret",
    *default_settings.SENSITIVE_HEADERS,
}

LOG_CONNECTION_EVENTS = (
    os.getenv("LOG_CONNECTION_EVENTS", "False").lower() == "true"
)  # Enable/disable request event logging
AUDIT_LOGGING_BATCH_SIZE = 1000  # Number of entries to log in a single batch
AUDIT_LOGGING_INTERVAL = 60  # Interval in seconds to log entries

MAINTENANCE_MODE = {"status": False, "message": "default:techno"}

ANYIO_MAX_WORKER_THREADS: int = 100
