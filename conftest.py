#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: api-testing
@file: conftest.py
@time: 2019/1/6 上午11:26
'''

import pytest
from utils import Log


@pytest.fixture(scope='session', autouse=True)
def base():
    log = Log.getlog('Base')

    log.info('set up test')
    yield

    log.info('tear down test')