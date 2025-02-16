"""
Defines project setup and initialization code

All setup code should be defined in the `configure` function
"""

import os
from contextlib import asynccontextmanager
import fastapi

from helpers.fastapi.config import settings, SETTINGS_ENV_VARIABLE

NAME = "Petriz"
SETTINGS_MODULE = "core.settings"
VERSION = "1.0.0"


def set_env_vars():
    """Set environment variables required for project setup"""
    os.environ.setdefault("FAST_API_APPLICATION_NAME", NAME)
    os.environ.setdefault("FAST_API_APPLICATION_VERSION", VERSION)
    os.environ.setdefault(SETTINGS_ENV_VARIABLE, SETTINGS_MODULE)


def initialize_project():
    """Initialize/configure project"""
    set_env_vars()
    settings.configure()

    from helpers.fastapi.routing import install_router
    from .endpoints import router
    from helpers.fastapi.apps import discover_apps

    for app in discover_apps():
        # Ensures that commands defined in each app are registered
        # in the commands registry on project setup
        app.commands

    # Install routers
    install_router(router, router_name="base_router")


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    """Application lifespan events"""
    from helpers.fastapi.sqlalchemy.setup import engine, bind_db_to_model_base
    from helpers.fastapi.sqlalchemy.models import ModelBase
    from helpers.fastapi.apps import configure_apps
    from helpers.fastapi.requests import throttling

    try:
        bind_db_to_model_base(db_engine=engine, model_base=ModelBase)
        await configure_apps()
        # Any setup code that needs to run before the application starts goes here
        async with throttling.configure(
            persistent=app.debug
            is False,  # Disables persistent rate limiting in debug mode
            redis=settings.REDIS_LOCATION,
        ):
            yield
    finally:
        pass
        # Perform additional cleanup here


def main(config: str = "APP") -> fastapi.FastAPI:
    """
    Configures and returns a FastAPI application instance
    for the project.

    :param config: name of configuration for FastAPI application in project settings
    :return: FastAPI application instance
    """
    initialize_project()

    # Ensure this environmental variables are set before anything is initialized
    # Hence, why top-level imports are avoided
    from helpers.fastapi.application import get_application

    app = get_application(**settings[config], lifespan=lifespan)
    return app
