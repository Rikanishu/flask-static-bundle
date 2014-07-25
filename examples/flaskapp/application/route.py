# encoding: utf-8

from application import app
from application.static import builder

from flask import render_template

@app.route('/')
def index():
    builder.collect_links()
    return render_template("index.html", statics=builder)