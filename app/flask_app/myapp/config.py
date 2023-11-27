from environs import Env

env = Env()
env.read_env()


class Config(object):
    """Base configuration."""

    FLASK_APP = env.str("FLASK_APP", "app.py")
    POSTGRES_PORT = env.int("POSTGRES_PORT", 5432)
    POSTGRES_USER = env.str("POSTGRES_USER")
    POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
    POSTGRES_DB = env.str("POSTGRES_DB")
    POSTGRES_HOST = env.str("POSTGRES_HOST")
    # Add more common configurations as needed


class DevelopmentConfig(Config):
    """Development configurations."""

    DEBUG = True
    TESTING = True
    POSTGRES_DB = env.str("DEV_POSTGRES_DB", "dev_database")
    # Add development-specific configurations


class ProductionConfig(Config):
    """Production configurations."""

    DEBUG = False
    TESTING = False
    POSTGRES_DB = env.str("PROD_POSTGRES_DB", "prod_database")
    # Add production-specific configurations


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True
    POSTGRES_DB = env.str("TEST_POSTGRES_DB", "test_database")
    # Add testing-specific configurations
