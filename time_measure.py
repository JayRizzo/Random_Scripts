#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Thu Sep  5 00:00:00 2019 PST
# Last ModDate: Thu Sep 22 18:02:45 2022 CDT
# =============================================================================
"""
    Module Built to Convert Seconds, MilliSeconds, MicroSeconds or NanoSeconds to a Human Readable Time Format.
    File Name: time_measure.py

    Example:
        print(f"Example  (s) 13: {DurationFromSeconds(1234567890123)}")
            Example  (s) 13: ('039:0001:047:325:05:02:03', ' 39 Millennia,    1 Century,  47 Years,  325 Days,   5 Hours,   2 Minutes,   3 Seconds')
        print(f"Example (ms) 16: {DurationFromMilliSeconds(1234567890123456)}")
            Example (ms) 16: ('039:0001:047:325:05:02:03::456', ' 39 Millennia,    1 Century,  47 Years,  325 Days,   5 Hours,   2 Minutes,   3 Seconds,  456 MilliSeconds')
        print(f"Example (μs) 19: {DurationFromMicroSeconds(1234567890123456789)}")
            Example (μs) 19: ('039:0001:047:325:05:02:03::456::789', ' 39 Millennia,    1 Century,  47 Years,  325 Days,  5 Hours,  2 Minutes,  3 Seconds,  456 MilliSeconds,  789 MicroSeconds')
        print(f"Example (ns) 22: {DurationFromNanoSeconds(1234567890123456789012)}")
            Example (ns) 22: ('039:0001:047:325:05:02:03::456::789::012', ' 39 Millennia,    1 Century,  47 Years,  325 Days,  5 Hours,  2 Minutes,  3 Seconds,  456 MilliSeconds,  789 MicroSeconds,  12 NanoSeconds')

"""
# =============================================================================


def DurationFromSeconds(s):
    """
        Convert Seconds to Human Readable Time Format.

        INPUT : s (AKA: Seconds)
        OUTPUT: tuple(string TIMELAPSED, string SPOKENTIME) like format.
        OUTPUT Variables: TIMELAPSED, SPOKENTIME

        Example  Input: DurationFromSeconds(s)
        **"Millennium:Century:Years:Days:Hours:Minutes:Seconds"**
        Example Output: ('039:0001:047:325:05:02:03', ' 39 Millennia,    1 Century,  47 Years,  325 Days,   5 Hours,   2 Minutes,   3 Seconds')
        Call: DurationFromSeconds(1234567890123)
    """
    m, s        = divmod(s, 60)
    h, m        = divmod(m, 60)
    d, h        = divmod(h, 24)
    y, d        = divmod(d, 365)
    c, y        = divmod(y, 100)
    n, c        = divmod(c, 10)
    TIMELAPSED  = f"{n:03.0f}:{c:04.0f}:{y:03.0f}:{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
    SPOKENTIME  = f"{n: 3d} Millennia, {c: 4d} Century, {y: 3d} Years, {d: 4.0f} Days, {h: 3d} Hours, {m: 3d} Minutes, {s: 3d} Seconds"
    return TIMELAPSED, SPOKENTIME


def DurationFromMilliSeconds(ms):
    """
        Convert MilliSeconds to Human Readable Time Format.

        INPUT : ms (AKA: MilliSeconds)
        OUTPUT: tuple(string TIMELAPSED, string SPOKENTIME) like format.
        OUTPUT Variables: TIMELAPSED, SPOKENTIME

        Example  Input: DurationFromMilliSeconds(ms)
        **"Millennium:Century:Years:Days:Hours:Minutes:Seconds:MilliSeconds"**
        Example Output: ('0039:053:23:31:30', '  39 Years,   53 Days,  23 Hours,  31 Minutes,  30 Seconds,  123 MilliSeconds')
        Call: DurationFromMilliSeconds(1234567890123456)

    """
    s, ms       = divmod(ms, 1000)
    m, s        = divmod(s, 60)
    h, m        = divmod(m, 60)
    d, h        = divmod(h, 24)
    y, d        = divmod(d, 365)
    c, y        = divmod(y, 100)
    n, c        = divmod(c, 10)
    TIMELAPSED  = f"{n:03.0f}:{c:04.0f}:{y:03.0f}:{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}::{ms:03.0f}"
    SPOKENTIME  = f"{n: 3d} Millennia, {c: 4d} Century, {y: 3d} Years, {d: 4d} Days, {h: 3d} Hours, {m: 3d} Minutes, {s: 3d} Seconds, {ms: 3d} MilliSeconds"
    return TIMELAPSED, SPOKENTIME

def DurationFromMicroSeconds(μs):
    """
        Convert MicroSeconds to Human Readable Time Format.
        A MicroSecond is a unit of time in the International System of Units (SI) equal to one millionth (0.000001 or 10−6 or 1⁄1,000,000) of a second.
        Its symbol is μs, sometimes simplified to us when Unicode is not available.
        A microsecond is equal to 1000 nanoseconds or 1⁄1,000 of a millisecond.

        INPUT : ms (AKA: MilliSeconds)
        OUTPUT: tuple(string TIMELAPSED, string SPOKENTIME) like format.
        OUTPUT Variables: TIMELAPSED, SPOKENTIME

        Example  Input: DurationFromMicroSeconds(μs)
        **"Millennium:Century:Years:Days:Hours:Minutes:Seconds:MilliSeconds:MicroSeconds"**
        Example Output: ('0039:053:23:31:30:123:456', '  39 Years,  53 Days, 23 Hours, 31 Minutes, 30 Seconds,  123 MilliSeconds,  456 MicroSeconds')
        Call: DurationFromMicroSeconds(1234567890123456789)

    """
    ms, μs      = divmod(μs, 1000)
    s, ms       = divmod(ms, 1000)
    m, s        = divmod(s, 60)
    h, m        = divmod(m, 60)
    d, h        = divmod(h, 24)
    y, d        = divmod(d, 365)
    c, y        = divmod(y, 100)
    n, c        = divmod(c, 10)
    TIMELAPSED  = f"{n:03.0f}:{c:04.0f}:{y:03.0f}:{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}::{ms:03.0f}::{μs:03.0f}"
    SPOKENTIME  = f"{n: 3d} Millennia, {c: 4d} Century, {y: 3d} Years, {d: 4d} Days, {h: 2d} Hours, {m: 2d} Minutes, {s: 2d} Seconds, {ms: 3d} MilliSeconds, {μs: 3d} MicroSeconds"
    return TIMELAPSED, SPOKENTIME

def DurationFromNanoSeconds(ns):
    """
        Convert NanoSeconds to Human Readable Time Format.
        A NanoSeconds is a unit of time in the International System of Units (SI) equal to one millionth (0.000001 or 10−6 or 1⁄1,000,000) of a second.
        Its symbol is μs, sometimes simplified to us when Unicode is not available.
        A microsecond is equal to 1000 nanoseconds or 1⁄1,000 of a millisecond.

        INPUT : ms (AKA: MilliSeconds)
        OUTPUT: tuple(string TIMELAPSED, string SPOKENTIME) like format.
        OUTPUT Variables: TIMELAPSED, SPOKENTIME

        Example  Input: DurationFromNanoSeconds(ns)
        **"Millennium:Century:Years:Days:Hours:Minutes:Seconds:MilliSeconds:MicroSeconds:NanoSeconds"**
        Example Output: ('039:0001:047:325:05:02:03:456:789:012', ' 39 Millennia,    1 Century,  47 Years,  325 Days,  5 Hours,  2 Minutes,  3 Seconds,  456 MilliSeconds,  789 MicroSeconds,  12 NanoSeconds')
        DurationFromNanoSeconds(1234567890123456789012)
    """
    μs, ns      = divmod(ns, 1000)
    ms, μs      = divmod(μs, 1000)
    s, ms       = divmod(ms, 1000)
    m, s        = divmod(s, 60)
    h, m        = divmod(m, 60)
    d, h        = divmod(h, 24)
    y, d        = divmod(d, 365)
    c, y        = divmod(y, 100)
    n, c        = divmod(c, 10)
    TIMELAPSED  = f"{n:03.0f}:{c:04.0f}:{y:03.0f}:{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}::{ms:03.0f}::{μs:03.0f}::{ns:03.0f}"
    SPOKENTIME  = f"{n: 3d} Millennia, {c: 4d} Century, {y: 3d} Years, {d: 4d} Days, {h: 2d} Hours, {m: 2d} Minutes, {s: 2d} Seconds, {ms: 3d} MilliSeconds, {μs: 3d} MicroSeconds, {ns: 3d} NanoSeconds"
    return TIMELAPSED, SPOKENTIME


if __name__ == '__main__':
    # print(f"Example  (s)  1: {DurationFromSeconds(1)}")
    # print(f"Example  (s)  2: {DurationFromSeconds(12)}")
    # print(f"Example  (s)  3: {DurationFromSeconds(123)}")
    # print(f"Example  (s)  4: {DurationFromSeconds(1234)}")
    # print(f"Example  (s)  5: {DurationFromSeconds(12345)}")
    # print(f"Example  (s)  6: {DurationFromSeconds(123456)}")
    # print(f"Example  (s)  7: {DurationFromSeconds(1234567)}")
    # print(f"Example  (s)  8: {DurationFromSeconds(12345678)}")
    # print(f"Example  (s)  9: {DurationFromSeconds(123456789)}")
    # print(f"Example  (s) 10: {DurationFromSeconds(1234567890)}")
    # print(f"Example  (s) 11: {DurationFromSeconds(12345678901)}")
    # print(f"Example  (s) 12: {DurationFromSeconds(123456789012)}")
    print(f"Example  (s) 13: {DurationFromSeconds(1234567890123)}")
    print("")
    # print(f"Example (ms)  1: {DurationFromMilliSeconds(1)}")
    # print(f"Example (ms)  2: {DurationFromMilliSeconds(12)}")
    # print(f"Example (ms)  3: {DurationFromMilliSeconds(123)}")
    # print(f"Example (ms)  4: {DurationFromMilliSeconds(1234)}")
    # print(f"Example (ms)  5: {DurationFromMilliSeconds(12345)}")
    # print(f"Example (ms)  6: {DurationFromMilliSeconds(123456)}")
    # print(f"Example (ms)  7: {DurationFromMilliSeconds(1234567)}")
    # print(f"Example (ms)  8: {DurationFromMilliSeconds(12345678)}")
    # print(f"Example (ms)  9: {DurationFromMilliSeconds(123456789)}")
    # print(f"Example (ms) 10: {DurationFromMilliSeconds(1234567890)}")
    # print(f"Example (ms) 11: {DurationFromMilliSeconds(12345678901)}")
    # print(f"Example (ms) 12: {DurationFromMilliSeconds(123456789012)}")
    # print(f"Example (ms) 13: {DurationFromMilliSeconds(1234567890123)}")
    # print(f"Example (ms) 14: {DurationFromMilliSeconds(12345678901234)}")
    # print(f"Example (ms) 15: {DurationFromMilliSeconds(123456789012345)}")
    print(f"Example (ms) 16: {DurationFromMilliSeconds(1234567890123456)}")
    print("")
    # print(f"Example (μs)  1: {DurationFromMicroSeconds(1)}")
    # print(f"Example (μs)  2: {DurationFromMicroSeconds(12)}")
    # print(f"Example (μs)  3: {DurationFromMicroSeconds(123)}")
    # print(f"Example (μs)  4: {DurationFromMicroSeconds(1234)}")
    # print(f"Example (μs)  5: {DurationFromMicroSeconds(12345)}")
    # print(f"Example (μs)  6: {DurationFromMicroSeconds(123456)}")
    # print(f"Example (μs)  7: {DurationFromMicroSeconds(1234567)}")
    # print(f"Example (μs)  8: {DurationFromMicroSeconds(12345678)}")
    # print(f"Example (μs)  9: {DurationFromMicroSeconds(123456789)}")
    # print(f"Example (μs) 10: {DurationFromMicroSeconds(1234567890)}")
    # print(f"Example (μs) 11: {DurationFromMicroSeconds(12345678901)}")
    # print(f"Example (μs) 12: {DurationFromMicroSeconds(123456789012)}")
    # print(f"Example (μs) 13: {DurationFromMicroSeconds(1234567890123)}")
    # print(f"Example (μs) 14: {DurationFromMicroSeconds(12345678901234)}")
    # print(f"Example (μs) 15: {DurationFromMicroSeconds(123456789012345)}")
    # print(f"Example (μs) 16: {DurationFromMicroSeconds(1234567890123456)}")
    # print(f"Example (μs) 17: {DurationFromMicroSeconds(12345678901234567)}")
    # print(f"Example (μs) 18: {DurationFromMicroSeconds(123456789012345678)}")
    print(f"Example (μs) 19: {DurationFromMicroSeconds(1234567890123456789)}")
    print("")
    # print(f"Example (ns)  1: {DurationFromNanoSeconds(1)}")
    # print(f"Example (ns)  2: {DurationFromNanoSeconds(12)}")
    # print(f"Example (ns)  3: {DurationFromNanoSeconds(123)}")
    # print(f"Example (ns)  4: {DurationFromNanoSeconds(1234)}")
    # print(f"Example (ns)  5: {DurationFromNanoSeconds(12345)}")
    # print(f"Example (ns)  6: {DurationFromNanoSeconds(123456)}")
    # print(f"Example (ns)  7: {DurationFromNanoSeconds(1234567)}")
    # print(f"Example (ns)  8: {DurationFromNanoSeconds(12345678)}")
    # print(f"Example (ns)  9: {DurationFromNanoSeconds(123456789)}")
    # print(f"Example (ns) 10: {DurationFromNanoSeconds(1234567890)}")
    # print(f"Example (ns) 11: {DurationFromNanoSeconds(12345678901)}")
    # print(f"Example (ns) 12: {DurationFromNanoSeconds(123456789012)}")
    # print(f"Example (ns) 13: {DurationFromNanoSeconds(1234567890123)}")
    # print(f"Example (ns) 14: {DurationFromNanoSeconds(12345678901234)}")
    # print(f"Example (ns) 15: {DurationFromNanoSeconds(123456789012345)}")
    # print(f"Example (ns) 16: {DurationFromNanoSeconds(1234567890123456)}")
    # print(f"Example (ns) 17: {DurationFromNanoSeconds(12345678901234567)}")
    # print(f"Example (ns) 18: {DurationFromNanoSeconds(123456789012345678)}")
    # print(f"Example (ns) 19: {DurationFromNanoSeconds(1234567890123456789)}")
    # print(f"Example (ns) 20: {DurationFromNanoSeconds(12345678901234567890)}")
    # print(f"Example (ns) 21: {DurationFromNanoSeconds(123456789012345678901)}")
    print(f"Example (ns) 22: {DurationFromNanoSeconds(1234567890123456789012)}")
    print("")


"""
    Definitions:
       Nanoseconds: A nanosecond (ns) is a unit of time in the International System of Units (SI) equal to one billionth of a second, that is, 1⁄1 000 000 000 of a second, or 10−9 seconds.
                    The term combines the SI prefix nano- indicating a 1 billionth submultiple of an SI unit (e.g. nanogram, nanometre, etc.) and second, the primary unit of time in the SI.
                    A nanosecond is equal to 1000 picoseconds or 1⁄1000 microsecond. Time units ranging between 10−8 and 10−7 seconds are typically expressed as tens or hundreds of nanoseconds.
      Microseconds: A microsecond is a unit of time in the International System of Units (SI) equal to one millionth (0.000001 or 10−6 or 1⁄1,000,000) of a second.
                    Its symbol is μs, sometimes simplified to us when Unicode is not available.
      MilliSeconds: A millisecond (from milli- and second; symbol: ms) is a unit of time in the International System of Units (SI) equal to one thousandth (0.001 or 10−3 or 1/1000) of a second
                    and to 1000 microseconds.  A unit of 10 milliseconds may be called a centisecond, and one of 100 milliseconds a decisecond, but these names are rarely used.
                    To help compare orders of magnitude of different times, this page lists times between 10−3 seconds and 100 seconds (1 millisecond and one second).
           Seconds: The second (symbol: s) is the unit of time in the International System of Units (SI), historically defined as 1⁄86400 of a day –
                    this factor derived from the division of the day first into 24 hours, then to 60 minutes and finally to 60 seconds each (24 × 60 × 60 = 86400).
                    The current and formal definition in the International System of Units (SI) is more precise:
           Minutes: This article is about the unit of time. For angle and right ascension, see Minute and second of arc.
                    For the written record of a meeting, see Minutes. For other uses of the word, see Minute (disambiguation).
                    A digital clock showing zero hours and one minute The minute is a unit of time usually equal to 1/60 (the first sexagesimal fraction) of an hour, or 60 seconds.
                    In the UTC time standard, a minute on rare occasions has 61 seconds, a consequence of leap seconds (there is a provision to insert a negative leap second,
                    which would result in a 59-second minute, but this has never happened in more than 40 years under this system). Although not an SI unit,
                    the minute is accepted for use with SI units.  The SI symbol for minute or minutes is min (without a dot).
                    The prime symbol is also sometimes used informally to denote minutes of time.
             Hours: An hour (symbol: h;[1] also abbreviated hr) is a unit of time conventionally reckoned as 1⁄24 of a day and scientifically reckoned between 3,599 and 3,601 seconds,
                    depending on the speed of Earth's rotation. There are 60 minutes in an hour, and 24 hours in a day.
                    The hour was initially established in the ancient Near East as a variable measure of 1⁄12 of the night or daytime.
                    Such seasonal, temporal, or unequal hours varied by season and latitude. Equal or equinoctial hours were taken as 1⁄24 of the day as measured from noon to noon;
                    The minor seasonal variations of this unit were eventually smoothed by making it 1⁄24 of the mean solar day.
                    Since this unit was not constant due to long term variations in the Earth's rotation,
                    the hour was finally separated from the Earth's rotation and defined in terms of the atomic or physical second.
              Days: Generally, a day is roughly the time of one rotation of the Earth (about 24 hours) or one rotation of other large astronomical objects.
                    In everyday life, the word "day" often refers to a solar day, which is the length between two solar noons or times the Sun reaches the highest point.
                    The word "day" may also refer to daytime, a time period when the location receives direct and indirect sunlight.
                    On Earth, as a location passes through its day, it experiences morning, noon, afternoon, evening, and night.
                    The effect of a day is vital to many life processes, which is called the circadian rhythm.
             Years: A year or annus is the orbital period of a planetary body, for example, the Earth, moving in its orbit around the Sun. Due to the Earth's axial tilt,
                    the course of a year sees the passing of the seasons, marked by change in weather, the hours of daylight, and, consequently, vegetation and soil fertility.
                    In temperate and subpolar regions around the planet, four seasons are generally recognized: spring, summer, autumn and winter.
                    In tropical and subtropical regions, several geographical sectors do not present defined seasons; but in the seasonal tropics, the annual wet and dry seasons are recognized and tracked.
                    A calendar year is an approximation of the number of days of the Earth's orbital period, as counted in a given calendar.
                    The Gregorian calendar, or modern calendar, presents its calendar year to be either a common year of 365 days or a leap year of 366 days, as do the Julian calendars.
                    For the Gregorian calendar, the average length of the calendar year (the mean year) across the complete leap cycle of 400 years is 365.2425 days (97 out of 400 years are leap years).
           Century: A century is a period of 100 years. Centuries are numbered ordinally in English and many other languages.
                    The word century comes from the Latin centum, meaning one hundred. Century is sometimes abbreviated as c.
                    A centennial or centenary is a hundredth anniversary, or a celebration of this, typically the remembrance of an event which took place a hundred years earlier.
        Millennium: A millennium (plural millennia or millenniums) is a period of one thousand years, sometimes called a kiloannum (ka), or kiloyear (ky).
                    Normally, the word is used specifically for periods of a thousand years that begin at the starting point (initial reference point) of the calendar in consideration (typically the year "1")
                    and at later years that are whole number multiples of a thousand years after the start point.
"""
