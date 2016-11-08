#!/usr/bin/ev python
#coding=utf-8

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
from handlers import WelcomeHandler,LoginHandler,IndexHandler,MainHandler




urls =[
    (r'/',WelcomeHandler,None,'derek_welcome'),
    (r'/login',LoginHandler,None,'derek_login'),
    (r'/index',IndexHandler,None,'derek_index'),
    (r'/main',MainHandler,None,'derek_main'),
       ]


settings={
    'template_path':os.path.join(os.path.dirname(__file__),'templates'),
    'static_path':os.path.join(os.path.dirname(__file__),'statics'),
    'debug':True,
    'cookie_secret': "HeavyMetalWillNeverDie",
    'login_url':'/login'
}

application = tornado.web.Application(urls,**settings)

if __name__ == "__main__":
    httpd = tornado.httpserver.HTTPServer(application)
    httpd.listen(8089)

    tornado.ioloop.IOLoop.instance().start()

    #this  is new 