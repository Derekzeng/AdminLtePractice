#!/usr/bin/ev python
#coding=utf-8

import tornado
import tornado.web
import datetime
import functools
from collections import namedtuple

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def _format_date(self,date):
        return  date.strftime('%Y-%m-%d')

    def get_template_namespace(self):
        namespaces = super(BaseHandler,self).get_template_namespace()
        User = namedtuple('User','name,date')
        user =User(name=self.current_user,date=datetime.datetime.now())
        namespaces.update(user=user)
        return namespaces


class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        if username:
            self.set_secure_cookie("user",username)


        next = self.get_argument("next")
        if next:
            self.redirect(self.reverse_url(next))

        # self.redirect('/login')



    def get(self, *args, **kwargs):
        self.render("login.html",next='derek_main')

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("index.html")

class WelcomeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write('''
            <html>
              <h1>欢迎你光临本系统,please login:</h1>
              <a href='/login'><strong>Login to system</strong></a>
            </html>
        ''')

class NewWelcomeHandler21(BaseHandler):
    def post(self, *args, **kwargs):
        pass

class MainHandler(BaseHandler):
    def post(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        self.render("main/view.html")