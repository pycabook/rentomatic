class Config(object):
    """Base configuration."""


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'production'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""
    ENV = 'test'
    TESTING = True
    DEBUG = True
