# config.py

class Config(object):
    """
    Common configurations
    """


    SECRET_KEY = '6c57827b5f83d30b51104a18e7bce497140540a56b13159286bfb9d97e4609bc'
    SQLALCHEMY_DATABASE_URI = 'postgres://inqemahooylwml:6c57827b5f83d30b51104a18e7bce497140540a56b13159286bfb9d97e4609bc@ec2-3-210-255-177.compute-1.amazonaws.com:5432/dcr2mtcqdg08c' #Use postgres/MySQL/SQLite::

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations to be used when building the app & running it locally
    """


    SECRET_KEY = '6c57827b5f83d30b51104a18e7bce497140540a56b13159286bfb9d97e4609bc'
    SQLALCHEMY_DATABASE_URI = 'postgres://inqemahooylwml:6c57827b5f83d30b51104a18e7bce497140540a56b13159286bfb9d97e4609bc@ec2-3-210-255-177.compute-1.amazonaws.com:5432/dcr2mtcqdg08c' #Use postgres/MySQL/SQLite::
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production configurations to be used when the app is deployed
    """

    DEBUG = True

config_options = {
'development':DevelopmentConfig,
'production':ProductionConfig,

}