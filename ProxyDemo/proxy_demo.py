#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Login:
    def __init__(self, user, pwd, ip):
        self.user = user
        self.pwd = pwd
        self.ip = ip
        self.session_id = ''
        self.last_time = ''

    def login(self):
        self.session_id = '3fcc2090b202c89598dcc64f3e036a17f80a77ec'

    def get_session_id(self):
        return self.session_id

    def set_last_time(self, last_time):
        self.last_time = last_time


class ProxyLogin:
    def __init__(self, user, pwd, ip):
        self.__l = Login(user, pwd, ip)

    def login(self):
        return self.__l.login()

    def get_session_id(self):
        return self.__l.get_session_id()

    def set_last_time(self, last_time):
        self.__l.set_last_time(last_time)


if __name__ == "__main__":
    pl = ProxyLogin("u", "123456", "127.0.0.1")
    print(pl.get_session_id())
    pl.login()
    print(pl.get_session_id())
