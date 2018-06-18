import os


CONFIG = {
    'base':'https://graph.facebook.com/v3.0',
    'node':'',
    'fields':'id, message, link, name, type, shares, reactions, created_time, comments.limit(0).summary(true).limit(0).summary(true)',
    'common':{
        'since':'',
        'until':'',
        'fetch':True,
        'result_directory': '__results__/crawling',
        'limit':50,
        'access_token':'EAACEdEose0cBAIvFV8ihrEELt98NdWcZBZCPTmHbkgEjPGmOq7oKZAJ4shqeNGF60YuOMp4smC8RghMvzDWGd7ZC0ESn4ImjiX1gnQdZCEPd5bZC0Gay5y3HnSDlNHG8rA2cOjGhgsmfr092jVgEDWmZACbwBuYuKnZBTMPKIT3NmZBAgFCagbH2WgV85oI4vUQDfWOsorud58QZDZD'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(**CONFIG['common']['result_directory'])

