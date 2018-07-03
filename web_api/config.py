import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = os.env.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        'host': os.env.get('HOST'),
        'port': int(os.env.get('PORT')),
        'maxPoolSize': 200
    }

class DevelopmentConfig(Config):
    Config.MONGODB_SETTINGS.update({
        'db': os.env.get('DEV_DATABASE')
    })

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}