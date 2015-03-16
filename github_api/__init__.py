from flask import Flask

from . import models
from .extensions import config, oauth, assets
from .views.repolister import repolister
from .views.users import users


DEBUG = True
SECRET_KEY = 'development-key'



def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.config['GITHUB'] = {
    'consumer_key': '4c80fa0cce999380369c',
    'consumer_secret': '4636bbe882615d4c121ac10a5a4173526c559fa2',
    }

    config.init_app(app)
    oauth.init_app(app)
    assets.init_app(app)

    app.register_blueprint(repolister)
    app.register_blueprint(users)

    return app
