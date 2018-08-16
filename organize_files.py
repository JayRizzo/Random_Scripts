#!/usr/bin/env python3
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon May 14 21:46:03 PDT 2018
# Updated Date: Mon August 15 22:34:03 PDT 2018
# =============================================================================
"""THE MODULE HAS BEEN BUILD FOR KEEPING YOUR FILES ORGANIZED."""
# Answer for: https://stackoverflow.com/a/50344578/1896134 PNG Archive
# NOTE: THIS WILL NOT CREATE THE DESTINATION FOLDER(S)
#
# Improvements THANKS TO:
#
# "Use endswith with multiple extensions"
# https://stackoverflow.com/a/22812835/1896134
#
# "Normalize a pathname by collapsing redundant separators"
# https://docs.python.org/3/library/os.path.html#os.path.normpath
#
# "Styling multi-line conditions in 'if' statements?"
# https://stackoverflow.com/a/181557/1896134
#
#
# "Python: Line that does not start with #"
# https://stackoverflow.com/a/34129925/1896134
#
# "What is the easiest way to get all strings that do not start with a char?"
# https://stackoverflow.com/a/6763438/1896134
# =============================================================================
from os import walk
from os import path
from shutil import move # noqa
import getpass
import click

mac_username = getpass.getuser()

includes_file_extensn = ([".jpg", ".gif", ".png", ".jpeg",
                          ])

# includes_file_extensn = ([".mp4", ".mpg", ".mpeg", ".swf", ".vob", ".wmv",
#                           ".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv",
#                           ".m2ts", ".mkv", ".mov",
#                           ])

search_dir = path.dirname('/Users/' + mac_username +
                          '/Documents/')

target_foldr = path.dirname('/Users/' + mac_username +
                            '/Pictures/Archive/')

# target_foldr = path.dirname('/Users/' + mac_username +
#                             '/Movies/')

exclude_foldr = set([target_foldr,
                     '.app',
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/GitHub/'),
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/Random/'),
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/Stupid_Folder/'),
                     ])

print("Exclude list: " + str(exclude_foldr))
print("Files found will be moved to this folder:" + str(target_foldr))

if click.confirm("Would you like to move files?"
                 "\n No? This will just list the files."
                 "\n Yes? This will Move your files to the target folder.\n",
                 default=False):
    # print('Do something if True?')
    question_moving = True
else:
    # print('Do something if False?')
    question_moving = False


def organize_files():
    """THE MODULE HAS BEEN BUILD FOR KEEPING YOUR FILES ORGANIZED."""
    for root, dir, files in walk(search_dir, topdown=True):
        for file in files:
            if (not (str(root) + '/').startswith(tuple(exclude_foldr))):
                if (file.endswith(tuple(includes_file_extensn))):
                    filetomove = path.normpath(str(root) + '/' +
                                               str(file))
                    movingfileto = path.normpath(str(target_foldr) + '/' +
                                                 str(file))
                    print('Files To Move: ' + str(filetomove))
                    # This is using the prompt you answered at the beginning
                    if question_moving is True:
                        print('Moving File: ' + str(filetomove) +
                              "\n To:" + str(movingfileto))
                        move(filetomove, movingfileto)
                        pass
                    else:
                        pass
                    pass
                else:
                    # print('Theres no need to move these files either: ' +
                    #       str(root) + str(file))
                    pass
            else:
                pass


if __name__ == '__main__':
    organize_files()
