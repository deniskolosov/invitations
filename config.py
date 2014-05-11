# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email support
MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'testpydev'
MAIL_PASSWORD = 'testpassword123'

ADMINS = ['testpydev@yandex.ru','cute.buzz@gmail.com']

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

