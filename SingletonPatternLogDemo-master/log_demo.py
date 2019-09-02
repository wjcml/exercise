#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from sp_log import SpLog

n = 0
max_n = 100

while True:
    if n >= max_n:
        break

    sp_log = SpLog.get_ins("err.log")
    sp_log.info('序号：%d' % n)
    sp_log.close_file()

    n += 1

