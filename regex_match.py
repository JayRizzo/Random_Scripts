#!/usr/bin/env python3
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon August 15 22:00:03 PDT 2018
# =============================================================================
"""THE MODULE HAS BEEN BUILD TO TRY AND FIND EMAIL ADDRESSES IN RANDOM TEXT."""
# =============================================================================
# IMPORTS
# =============================================================================
import re

str = 'purple asdf-b@google.com monkey spacewasher Something (at) Yahoo (Dot com'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
# match = re.search(r'([\w.-]+)\s?\(?(at|AT)\)?\s?([\w.-]+)\s?\(?\s?(dot|DOT)\s?\)?\s?\(?(com|COM|us|US|nz|NZ|de|DE|uk|UK)\s?\)?\s?', str)
if match:
    print(match.group())   # 'asdf-b@google.com' (the whole match)
    print(match.group(1))  # 'asdf-b' (the username, group 1)
    print(match.group(2))  # 'google.com' (the host, group 2)
