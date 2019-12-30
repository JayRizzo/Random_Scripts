#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Following Is An Example for xattr.

Answer for: https://stackoverflow.com/q/52403922/1896134
Showcasing a 'How-to' example.
"""
# =============================================================================

import xattr
from getpass import getuser


class MetaModz(object):
    """Docstring for MetaModz."""

    def __init__(self, arg):
        """Docstring for MetaModz.__init__."""
        super(MetaModz, self).__init__()
        self.file_name = arg.__str__()
        self.attrz = []
        print("\n\nRunning File: {}\n".format(self.file_name))
        # '/usr/local/lib/python3.7/site-packages/xattr/__init__.py'

    def showww_me_the_meta(self):
        """Using Python's XATTR to list Key Meta Names for File."""
        attrz = xattr.listxattr(self.file_name)
        print("List All Meta Key's: {}".format(attrz))
        return attrz

    def update_the_meta(self):
        """Using Python's XATTR to Update Key Meta Names for File."""
        xattr.setxattr(self.file_name, 'custom.comment',
                       'I tawt I taw a puddy tat!.'.encode('utf-8'))
        xattr.setxattr(self.file_name, 'Music.Artist',
                       'I did! '
                       'I did taw a puddy tat!'.encode('utf-8'))
        print("Update Meta Key's Names for File: {}".format(self.file_name))
        return

    def update_file_owner(self):
        """Using Python's XATTR to Update Key Meta Names with owner info."""
        xattr.setxattr(self.file_name, 'custom.owner',
                       "{}".format(getuser()).encode('utf-8'))
        print("Update Meta Key's Names for File: {}".format(self.file_name))
        return

    def get_the_meta_values(self):
        """Example Looping thru keys to get the values."""
        print("Get The Meta for: {}".format(self.file_name))
        attrz = xattr.listxattr(self.file_name)
        print("")
        for i in reversed(attrz):
            abc = xattr.getxattr(self.file_name, i)
            result = ("{} : {}".format(i, abc))
            print("   {}".format(result))
        print("")
        return attrz

    def remove_the_meta(self):
        """Example of removing the keys added to the file."""
        print("Delete The Meta.")
        xattr.removexattr(self.file_name, 'custom.comment')
        attrz = xattr.listxattr(self.file_name)
        result = ("D. Info Removed Meta: {}".format(attrz))
        print("{}".format(result))
        print("The Meta Has Been Removed.")
        return result

    def remove_all_the_meta(self):
        """Example of removing the keys added to the file."""
        print("Deleting All Meta.")
        attrz = xattr.listxattr(self.file_name)
        for i in reversed(attrz):
            xattr.removexattr(self.file_name, i)
            print("    {}: Removed".format(i))
        print("")
        print("All Meta Has Been Removed.")
        return


if __name__ == '__main__':
    # use this to test
    a = MetaModz(xattr.__file__)

    # use this to select a file
    # a = MetaModz(input("Please Provide Absolute Path: "))

    # use this to explicitly run against a defined file.
    # a = MetaModz('~/Desktop/test.text')

    a.showww_me_the_meta()
    a.update_the_meta()
    a.update_file_owner()
    a.showww_me_the_meta()
    a.get_the_meta_values()
    a.remove_the_meta()
    a.showww_me_the_meta()
    a.remove_all_the_meta()
    a.showww_me_the_meta()
