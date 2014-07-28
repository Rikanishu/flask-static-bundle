#!/usr/bin/env python
# encoding: utf-8

# this script run static build in output directory
# execute before production deploy
if __name__ == "__main__":
    from application.static import builder
    builder.make_build()
    print("Done")