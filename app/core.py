# -*- coding: utf-8 -*-
"""
app.core module

Core of application.

:copyright: (c) 2018 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from flask import Blueprint

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/')
def index():
    return 'you have reached the core'

