#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]
from testlib import ActiveCheck  # type: ignore[import]

pytestmark = pytest.mark.checks


@pytest.mark.parametrize("params,expected_args", [
    ({
        "base_url": "some/path",
        "aggregation_name": "foo",
        "username": "bar",
        "credentials": "automation",
        "optional": {}
    }, ["-b", "some/path", "-a", "foo", "--use-automation-user"]),
])
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_bi_aggr_argument_parsing(params, expected_args):
    """Tests if all required arguments are present."""
    active_check = ActiveCheck("check_bi_aggr")
    assert active_check.run_argument_function(params) == expected_args
