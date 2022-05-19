import os
class Config():

    SECRET_KEY = 'secretkey1'
    SQLALCHEMY_DATABASE_URI='postgresql://moringa:pass123@localhost/studentportal'
    SQLALCHEMY_TRACK_MODIFICATIONS='FALSE'
   
    
class ProdConfig(Config):
    DEBUG = False
    
class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql://moringa:pass123@localhost/studentportal'
    
class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig,
'development':DevConfig,
'production':ProdConfig
}