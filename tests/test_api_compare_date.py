#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: api-testing
@file: test_api_compare_date.py
@time: 2019/1/6 上午11:32
'''

import json
import requests, pytest
from utils import Log
from parameters import api_compare


@pytest.mark.usefixtures('base')
class TestAPICompareDate(object):
    log = Log().getlog('TestAPICompareDate')

    @pytest.mark.parametrize('gformat,before,after,res', api_compare.test_data_compare)
    def test_01_compare_date(self, gformat, before, after, res):
        params = {
            'timestamp': before,
            'target': after
        }
        self.log.info('gformat is {}, params timestamp is {} target is {}'.format(gformat, before, after))
        try:
            response = json.loads(requests.get('https://postman-echo.com/time/before', params).content)
        except Exception:
            response = ''
        self.log.info('content of api response: {}'.format(response))
        assert res == response
