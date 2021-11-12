import os

class Config:
    TESTING = False
    ENV_VAR = os.environ.get('ENV_VAR', 'default')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'default')
    FLASK_APP = os.environ.get('FLASK_APP', 'default')
    FLASK_CONFIG = os.environ.get('FLASK_CONFIG', 'default')

class ProductionConfig(Config):
    FAV_FLOWER = 'rose'

class DevelopmentConfig(Config):
    FAV_FLOWER = 'sunflower'

class TestingConfig(Config):
    FAV_FLOWER = 'moonlight petal'
    TESTING = True