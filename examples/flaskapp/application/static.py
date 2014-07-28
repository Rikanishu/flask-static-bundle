# encoding: utf-8

from application import static_manager
from static_bundle import (JsBundle,
                           CssBundle)

css1 = CssBundle("css")
css1.add_file("example1.less")
css1.add_file("example2.css")

js1 = JsBundle("js")
js1.add_file("vendors/example1.js")
js1.add_file("vendors/example2.js")

js2 = JsBundle("js/include")
# modules depends on app.js
js2.add_file("app.js")
js2.add_directory("modules")

builder = static_manager.create_builder()
builder.create_asset("Styles").add_bundle(css1)
builder.create_asset("Vendors", minify=True).add_bundle(js1)
builder.create_asset("Application", minify=True).add_bundle(js2)