# encoding: utf-8

from __future__ import absolute_import
import sys
import os

# for testing

PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.append(PACKAGE_ROOT)

from flask import Flask

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
APP_PATH = os.path.join(ROOT_PATH, "application")

PUBLIC_STATIC_PATH = os.path.join(ROOT_PATH, "public")
SRC_PATH = os.path.join(PUBLIC_STATIC_PATH, "src")
BUILD_PATH = os.path.join(PUBLIC_STATIC_PATH, "build")


class ProdConf:
    DEBUG = False
    STATIC_BUNDLE_INPUT_PATH = SRC_PATH
    STATIC_BUNDLE_OUTPUT_PATH = BUILD_PATH
    STATIC_BUNDLE_ENV = "production"
    STATIC_BUNDLE_REWRITE = False


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

