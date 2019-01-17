#
# Flask-CDN
#
# Copyright (C) 2019 Boris Raicheff
# All rights reserved
#


from flask import current_app, url_for
from werkzeug.urls import url_parse, url_unparse


class CDN(object):
    """
    Flask-CDN

    :param app: Flask app to initialize with. Defaults to `None`.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    @staticmethod
    def init_app(app):
        app.config.setdefault('CDN_SCHEME', app.config['PREFERRED_URL_SCHEME'])
        if app.config.get('CDN_DOMAIN'):
            app.jinja_env.globals['url_for'] = _url_for


def _url_for(endpoint, **values):
    url = url_for(endpoint, **values)
    if endpoint == 'static':
        parts = url_parse(url)
        parts.scheme = current_app.config['CDN_SCHEME']
        parts.netloc = current_app.config['CDN_DOMAIN']
        url = url_unparse(parts)
    return url


# EOF
