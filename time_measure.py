#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Module Built to measure ms or seconds to readable time format."""
# File Name: time_measure.py
# =============================================================================


def duration_from_seconds(s):
    """Module to get the convert Seconds to a time format."""
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    timelapsed = "{:03d}:{:02d}:{:02d}:{:02d}".format(int(d),
                                                      int(h),
                                                      int(m),
                                                      int(s))
    return timelapsed


duration_from_seconds(2492000)
# 028:20:13:20


def duration_from_secs_v2(s):
    """Module to get the convert milliseconds to a time format."""
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    timely = "{:03d} Days {:02d} Hours {:02d} Min {:02d} Sec".format(int(d),
                                                                     int(h),
                                                                     int(m),
                                                                     int(s))
    return timely


duration_from_secs_v2(2492000)
# 028 Days 20 Hours 13 Min 20 Sec


def duration_from_milliseconds(ms):
    """Module to get the convert milliseconds to a time format.

    'Days,Hours,Min,Sec: like format '.
    """
    s = ms / 1000
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    timely = "{:00d}:{:02d}:{:02d}:{:02d}".format(int(d),
                                                  int(h),
                                                  int(m),
                                                  int(s))
    return timely

duration_from_milliseconds(23362624)[1]
# 'Days,Hours,Min,Sec: 000:06:29:22'
