"""Main application module"""
import os
import json
import jsend
import sentry_sdk
import falcon
from falcon_autocrud.middleware import Middleware
import sqlalchemy as sa
from . import routes

def start_service():
    """Start this service
    set SENTRY_DSN environmental variable to enable logging with Sentry
    """
    # Initialize Sentry
    sentry_sdk.init(os.environ.get('SENTRY_DSN'))

    # Database
    db_engine = sa.create_engine(os.environ.get('DATABASE_URL'))

    # Initialize Falcon
    api = falcon.API(
        middleware = [Middleware()]
    )
    routes.addRoutes(api, db_engine)
    api.add_sink(default_error, '')
    return api

def default_error(_req, resp):
    """Handle default error"""
    resp.status = falcon.HTTP_404
    msg_error = jsend.error('404 - Not Found')

    sentry_sdk.capture_message(msg_error)
    resp.body = json.dumps(msg_error)
