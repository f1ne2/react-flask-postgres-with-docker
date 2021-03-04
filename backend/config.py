import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRE_SQL") or \
                              'postgresql://postgres:SNekH2233@localhost:5432/quiz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
