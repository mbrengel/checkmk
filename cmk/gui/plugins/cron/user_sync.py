#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.gui.userdb as userdb
from cmk.gui.plugins.cron import register_job

register_job(userdb.execute_userdb_job)
register_job(userdb.execute_user_profile_cleanup_job)
