'''
Created on 2014-5-21

@author: KEVIN
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
        { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
        { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
        { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
        { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
        { 'name': 'QQ', 'url': 'https://graph.z.qq.com/moc2/me' },
        ]

#mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

#administrator list
ADMINS=['dkrose.random@gmail.com']
