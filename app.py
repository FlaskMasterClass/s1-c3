import os
import pathlib
import flask
from flask import Flask
from flask import current_app 

from flask.cli import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


from config import ProductionConfig
from config import DevelopmentConfig
from config import TestingConfig


profiles = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig(),
    'testing': TestingConfig()
}



def create_app(profile):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(profiles[profile])
    app.config.from_pyfile("config.py", silent=True)

    if profile != "testing":
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)

    try: # make sure the config folder exists
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app


if __name__ == '__main__':
    flask_env = os.environ.get("FLASK_ENV", default="development")
    app = create_app(flask_env)
    @app.route('/check')
    def var_check():
        return current_app.config['INSTANCE_VAR']
    @app.route('/check/env')
    def env_var_check():
        print(current_app.config['BING'])
        print(current_app.config['ENV_VAR'])
        print(current_app.config['APPLE'])
        return ''
    app.run()