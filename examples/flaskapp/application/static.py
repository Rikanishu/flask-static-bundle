# encoding: utf-8

from application import static_manager
from static_bundle import (JsBundle,
                           CssBundle,
                           LessCompilerPrepareHandler)

css1 = CssBundle("static/css")
css1.add_file("example1.less")
css1.add_file("example2.css")

js1 = JsBundle("static/js")
js1.add_file("vendors/example1.js")
js1.add_file("vendors/example2.js")

js2 = JsBundle("static/js/include")
# modules depends on app.js
js2.add_file("app.js")
js2.add_directory("modules")

builder = static_manager.create_builder()
builder.create_group("Styles").add_bundle(css1)
builder.create_group("Vendors", minify=True).add_bundle(js1)
builder.create_group("Application", minify=True).add_bundle(js2)

