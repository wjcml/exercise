#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from happy_utils import HappyConfigBase


class Config(HappyConfigBase):
    """
    配置文件模板
    """
    def __init__(self):
        super().__init__()

        self.section = 'ghibli'
        self.listen = ''
        self.port = 0
        self.debug = True
        self.db_host = '127.0.0.1'
        self.db_port = 3306
        self.db_user = ''
        self.db_password = ''
        self.db_name = ''

