import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET_12345')

class Development():
    """Configuration from Development."""
    DATABASE_NAME = os.environ['DATABASE_NAME']
    password = os.environ['password']
    postgres = os.environ['postgres']
    DEBUG = True

class TestingConfig(Config):
    """Configuration for Testing."""
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configuration for Staging."""
    DEBUG = False

class ProductionConfig(Config):
    """Configration for Production"""
    DEBUG = False
    TESTING = False
'''
app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging' : StagingConfig,
    'production' : ProductionConfig
}'''