# -*- coding: utf-8 -*-
"""
app.config module

Class based configuration objects for flask.

:copyright: (c) 2018 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
import os


class Config:
    """Base Configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Development Configuration."""
    DEBUG = True

    @staticmethod
    def init_app(app):
        Config.init_app(app)


class TestingConfig(Config):
    """Test Environment Configuration."""
    TESTING = True
    DEBUG = True

    @staticmethod
    def init_app(app):
        Config.init_app(app)


# node module export style object
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}