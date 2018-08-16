#!/usr/bin/env python3
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17E199)
# Created By  : Jeromie Kirchoff
# Created Date: Mon May 14 21:46:03 PDT 2018
# =============================================================================
"""THE MODULE HAS BEEN BUILD FOR."""
# =============================================================================
# IMPORTS
# =============================================================================
import re

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())   # 'alice-b@google.com' (the whole match)
    print(match.group(1))  # 'alice-b' (the username, group 1)
    print(match.group(2))  # 'google.com' (the host, group 2)
