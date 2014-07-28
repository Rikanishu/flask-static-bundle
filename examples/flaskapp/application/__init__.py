# encoding: utf-8

from __future__ import absolute_import

import sys
from flask import Flask


class ProdConf:
    DEBUG = False
    STATIC_BUNDLE_INPUT_PATH = "public/src"
    STATIC_BUNDLE_OUTPUT_PATH = "public/build"
    STATIC_BUNDLE_ENV = "production"

    # not recommend in production
    STATIC_BUNDLE_REWRITE = True


class DevConf(ProdConf):
    DEBUG = True
    STATIC_BUNDLE_ENV = "development"
    STATIC_BUNDLE_REWRITE = True


def current_conf():
    if len(sys.argv) > 1:
        if sys.argv[1] == "production":
            return ProdConf
    return DevConf


app = Flask(__name__, static_folder=None, template_folder='../templates')
app.config.from_object(current_conf())

from flask.ext.static_bundle import StaticManager
static_manager = StaticManager(app)

import application.route

