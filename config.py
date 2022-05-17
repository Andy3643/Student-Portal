import os
class Config():
    SECRET_KEY = 'secretkey1'
    SQLALCHEMY_DATABASE_URI=''
    
    
class ProdConfig(Config):
    DEBUG = False
    
class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=''
    
class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig,
'development':DevConfig,
'production':ProdConfig
}