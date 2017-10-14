class Config(object):
    """
    Configuration base, for all environments.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = "MINHACHAVESECRETA"
    CSRF_ENABLED = True

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
