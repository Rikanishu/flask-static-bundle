# flask-static-bundle #
**Flask extension for [static-bundle](http://github.com/rikanishu/static-bundle)**
---

### Installation ###

Via pip:
```
    pip install git+https://github.com/rikanishu/flask-static-bundle.git
```
or from sources
```
    python setup.py install
```

### Example ###

See **examples/flaskapp** for example of flask application which used this extension

### Config Keys ###

`STATIC_BUNDLE_INPUT_PATH` - Input path, development static root directory.
`STATIC_BUNDLE_OUTPUT_PATH` - Path for build in production env.
`STATIC_BUNDLE_ENV` - Current env ("development" / "production").
`STATIC_BUNDLE_REWRITE` - Rewrite static with standard route handler.
This option required creating app with option `static_folder=None`:
```
app = Flask(__name__, static_folder=None)
```
`STATIC_BUNDLE_REWRITE_URL` - Url for static rewrite, "/static/<filename>" by default