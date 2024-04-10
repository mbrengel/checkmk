#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# type: ignore[list-item,import,assignment,misc,operator]  # TODO: see which are needed in this file


def scan_blade_modules(oid):
    return ("BladeCenter Management Module" in oid(".1.3.6.1.2.1.1.1.0") or
            "BladeCenter Advanced Management Module" in oid(".1.3.6.1.2.1.1.1.0") or
            "IBM Flex Chassis Management Module" in oid(".1.3.6.1.2.1.1.1.0") or
            "Lenovo Flex Chassis Management Module" in oid(".1.3.6.1.2.1.1.1.0"))


def scan_blade_power_modules(oid):
    return ("BladeCenter Management Module" in oid(".1.3.6.1.2.1.1.1.0") or
            "BladeCenter Advanced Management Module" in oid(".1.3.6.1.2.1.1.1.0"))