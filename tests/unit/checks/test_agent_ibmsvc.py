#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]
from testlib import SpecialAgent  # type: ignore[import]

pytestmark = pytest.mark.checks


@pytest.mark.parametrize('params,expected_args', [
    ({
        'infos': [
            'lshost', 'lslicense', 'lsmdisk', 'lsmdiskgrp', 'lsnode', 'lsnodestats', 'lssystem',
            'lssystemstats', 'lsportfc', 'lsenclosure', 'lsenclosurestats', 'lsarray', 'disks'
        ],
        'user': 'user',
        'accept-any-hostkey': True
    }, [
        "-u", "user", "--accept-any-hostkey", "-i",
        "lshost,lslicense,lsmdisk,lsmdiskgrp,lsnode,lsnodestats,lssystem,lssystemstats,lsportfc,lsenclosure,lsenclosurestats,lsarray,disks",
        "address"
    ]),
    ({
        'infos': [
            'lshost', 'lslicense', 'lsmdisk', 'lsmdiskgrp', 'lsnode', 'lsnodestats', 'lssystem',
            'lssystemstats', 'lsportfc', 'lsenclosure', 'lsenclosurestats', 'lsarray', 'disks'
        ],
        'user': 'user',
        'accept-any-hostkey': False
    }, ["-u", "user", "address"]),
])
@pytest.mark.usefixtures("config_load_all_checks")
def test_ibmsvc_argument_parsing(params, expected_args):
    """Tests if all required arguments are present."""
    agent = SpecialAgent('agent_ibmsvc')
    arguments = agent.argument_func(params, "host", "address")
    assert arguments == expected_args