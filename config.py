import os


CONFIG = {
    'base':'https://graph.facebook.com/v3.0',
    'node':[('jtbcnews'), ('chosun')],
    'fields':'id, message, link, name, type, shares, reactions, created_time, comments.limit(0).summary(true).limit(0).summary(true)',
    'common':{
        'since':'2017-01-01',
        'until':'2018-12-31',
        'fetch':True,
        'result_directory': '__results__/crawling',
        'limit':50,
        'access_token':'EAACEdEose0cBAJbehvcIozibZBeIngZBJL7dMJP9Yjvs8z0JUQtoXezW6lwwlfzNyK3BBZCs3F4FR1alBVaZBWCurbZAgmelFdK66iFKIhL2tECX1PlLWZBLfMqrzcafEjVpX8zrKZCoIYnVzKoswoZC4xC5uvOn6hKunB8I2woGY8At26MnxsZB9B3sJ1TbQrPm8ESUaOFmuIgZDZD'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(**CONFIG['common']['result_directory'])

