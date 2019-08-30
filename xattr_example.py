#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Following Is An Example for xattr.

Answer for: https://stackoverflow.com/q/52403922/1896134
Showcasing a 'How-to' example.
"""
# =============================================================================

import xattr

print("{}".format(xattr.__file__))
# '/usr/local/lib/python3.7/site-packages/xattr/__init__.py'


def showww_me_the_meta(file_name):
    """Using Python's XATTR to list Key Meta Names for File."""
    print("Showing Initial Names & Values.")
    attrz = xattr.listxattr(file_name)
    result = ("A. Info Showcased Init: {}".format(attrz))
    print("{}".format(result))
    return result


def update_the_meta(file_name):
    """Using Python's XATTR to Update Key Meta Names for File."""
    xattr.setxattr(file_name, 'custom.comment',
                   'I tawt I taw a puddy tat!.'.encode('utf-8'))
    xattr.setxattr(file_name, 'Music.Artist',
                   'I did! '
                   'I did taw a puddy tat!'.encode('utf-8'))
    get_the_meta_values(file_name)
    return


def get_the_meta_values(file_name):
    """Example Looping thru keys to get the values."""
    print("B. Listing Meta for: {}".format(file_name))
    attrz = xattr.listxattr(file_name)
    print("")
    for i in reversed(attrz):
        abc = xattr.getxattr(file_name, i)
        result = ("{} : {}".format(i, abc))
        print("   {}".format(result))
    print("")
    return


def remove_the_meta(file_name):
    """Example of removing the keys added to the file."""
    xattr.removexattr(file_name, 'custom.comment')
    xattr.removexattr(file_name, 'Music.Artist')
    attrz = xattr.listxattr(file_name)
    result = ("C. Info Removed Meta: {}".format(attrz))
    print("{}".format(result))
    return result


if __name__ == '__main__':
    showww_me_the_meta('xattr_example.py')
    update_the_meta('xattr_example.py')
    remove_the_meta('xattr_example.py')
