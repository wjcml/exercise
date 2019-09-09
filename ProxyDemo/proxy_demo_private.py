#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Login:
    def __init__(self, user, pwd, ip):
        self.__user = user
        self.__pwd = pwd
        self.__ip = ip
        self.__session_id = ''
        self.__last_time = ''

    def login(self):
        self.__session_id = '3fcc2090b202c89598dcc64f3e036a17f80a77ec'

    def get_session_id(self):
        return self.__session_id

    def set_last_time(self, last_time):
        self.__last_time = last_time

    def get_last_time(self):
        return self.__last_time


# class ProxyLogin:
#     def __init__(self, user, pwd, ip):
#         self.l = Login(user, pwd, ip)
#
#     def login(self):
#         return self.l.login()
#
#     def get_session_id(self):
#         return self.l.get_session_id()
#
#     def set_last_time(self, last_time):
#         self.l.set_last_time(last_time)


if __name__ == "__main__":
    l = Login("user", "123456", "192.168.0.2")
    l.login()
    print(l.get_session_id())
    l.set_last_time("2019.09")
    print(l.get_last_time())
