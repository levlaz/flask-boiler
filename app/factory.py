# -*- coding: utf-8 -*-
"""
app.factory module

:copyright: (c) 2018 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from flask import Flask

from app.config import config

def create_app(config_name):
    """Flask application factory

    :param config_name: mapped class as found in app.config \
        defaults to DevelopmentConfig.

    :returns: The app flask application.
    """
    app = Flask('app')
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    # register blueprints
    from app.core import core
    app.register_blueprint(core)

    return app