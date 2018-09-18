#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Answer for https://stackoverflow.com/q/52360498/1896134."""
# =============================================================================


class MyIntroduction():
    """Doc PlaceHolder."""

    def __init__(self):
        """Doc PlaceHolder."""
        self.name = ""
        self.age = ""
        self.education = ""
        self.masters = ""
        self.interestarea = ""

    def set_info(self, name, age, education, masters, interestarea):
        """Doc PlaceHolder."""
        self.name = name
        self.age = age
        self.education = education
        self.masters = masters
        self.interestarea = interestarea

    def displayinformation(self):
        """Doc PlaceHolder."""
        a = {'name': self.name,
             'a': self.age,
             'e': self.education,
             'M': self.masters,
             'IA': self.interestarea
             }
        print(a)

a = MyIntroduction()
a.set_info('Jay', 453, 'SelfTaught', 'Making Stuff Up', 'Space Captain')
a.displayinformation()
