#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: api-testing
@file: api_compare.py
@time: 2019/1/6 下午4:38
'''

test_data_compare = [
    ('date', '2016-10-10', '2017-10-10', {'before': True}),
    ('timestamp', '1476057600', '1507593600', ''),
    ('datetime', '2016-10-10 00:00', '2017-10-10 00:00', {'before': True}),
    ('gyear', '2016', '2017', {'before': True}),
    ('gyearmonth', '2016-10', '2017-10', {'before': True}),
    ('gmonth', '--10', '--10', {'before': False}),
    ('gmonthday', '--10-10', '--10-10', {'before': False}),
    ('gday', '---10', '---10', {'before': False}),
    ('time', '00:00', '00:00', ''),
    ('au', '10/10/2016', '10/10/2017', {'before': True}),
    ('de', '10.10.2016', '10.10.2017', {'before': True}),
    ('zh', '2016年10月10日', '2017年10月10日', ''),
    ('kr', '2016년10월10일', '2017년10월10일', ''),
    ('uk', '10 10 2016', '10 10 2017', {'before': True}),
    ('empty', '', '', ''),
    ('leftempty', '', '2017-10-10', ''),
    ('rightempty', '2016-10-10', '', {'before': False}),
    ('text', '2016.Oct.10th', '2017.Oct.10th', '')
]
