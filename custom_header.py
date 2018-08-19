#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jeromie Kirchoff
# Created Date: Mon August 18 18:54:00 PDT 2018
# =============================================================================
"""The Module Has Been Build for An Example Of Custom Headers."""
# =============================================================================
# Answer for: https://stackoverflow.com/q/16220930/1896134
# =============================================================================
# STANDARD FIELDS
# =============================================================================
__author__ = 'Jeromie Kirchoff'
__copyright__ = 'Copyright 2018, Your Project'
__credits__ = ['Jeromie Kirchoff']
__license__ = 'MSU'  # Makin' Shi* Up!
__version__ = '1.0.1'
__maintainer__ = 'Jeromie Kirchoff'
__email__ = 'Jahomie04@gmail.com'
__status__ = 'Prototype'

# =============================================================================
# CUSTOM Fields
# =============================================================================
__course__ = 'cs108'
__teammates__ = ['Jeromie Kirchoff']
__laboratory__ = 'A13'
__date__ = '2018/08/18'
__username__ = 'JayRizzo'
__description__ = 'My First Project Program.'

# =============================================================================
# Showing the info each time the program is run.
# =============================================================================

print('# ' + '=' * 77)
print('Author: ' + __author__)
print('Teammates: ' + ', '.join(__teammates__))
print('Copyright: ' + __copyright__)
print('Credits: ' + ', '.join(__credits__))
print('License: ' + __license__)
print('Version: ' + __version__)
print('Maintainer: ' + __maintainer__)
print('Email: ' + __email__)
print('Status: ' + __status__)
print('Course: ' + __course__)
print('Laboratory: ' + __laboratory__)
print('Date: ' + __date__)
print('Username: ' + __username__)
print('Description: ' + __description__)
print('# ' + '=' * 77)


# RESULT
"""
$ python3 custom_header.py
# =============================================================================
Author: Jeromie Kirchoff
Teammates: Jeromie Kirchoff
Copyright: Copyright 2018, Your Project
Credits: Jeromie Kirchoff
License: MSU
Version: 1.0.1
Maintainer: Jeromie Kirchoff
Email: Jahomie04@gmail.com
Status: Prototype
Course: cs108
Laboratory: A13
Date: 2018/08/18
Username: JayRizzo
Description: My First Project Program.
# =============================================================================
"""
