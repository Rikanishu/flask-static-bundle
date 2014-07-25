#!/usr/bin/env python
# encoding: utf-8

# use run.py <environment> for change environment
# available environments: production, development
if __name__ == "__main__":
    from application import app
    is_debug_enabled = app.config.get('DEBUG', False)
    app.run(debug=is_debug_enabled, use_reloader=is_debug_enabled)