#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore



checkname = 'liebert_cooling_status'


info = [
    [u'Fancy cooling device', u'awesome'],
]


discovery = {
    '': [
        (u'Fancy cooling device', {}),
    ],
}


checks = {
    '': [
        (u'Fancy cooling device', {}, [(0, "awesome", [])]),
    ],
}
