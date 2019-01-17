#
# Flask-CDN
#
# Copyright (C) 2019 Boris Raicheff
# All rights reserved
#


from flask import current_app, url_for
from werkzeug.urls import url_parse, url_unparse


class CDN(object):
    """"""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('CDN_SCHEME', app.config['PREFERRED_URL_SCHEME'])
        if app.config.get('CDN_DOMAIN'):
            app.jinja_env.globals['url_for'] = cdn_url_for


def cdn_url_for(endpoint, **values):
    url = url_for(endpoint, **values)
    if endpoint == 'static':
        parts = url_parse(url, scheme=current_app.config['CDN_SCHEME'])
        parts.netloc = current_app.config['CDN_DOMAIN']
        url = url_unparse(parts)
    return url


# EOF
