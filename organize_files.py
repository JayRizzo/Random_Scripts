#!/usr/bin/env python3
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon May 14 21:46:03 PDT 2018
# Updated Date: Mon August 15 22:34:03 PDT 2018
# =============================================================================
"""THE MODULE HAS BEEN BUILD FOR KEEPING YOUR FILES ORGANIZED."""
# Answer for "Moving specific file types with Python":
#   https://stackoverflow.com/a/50344578/1896134
# Answer for "Filtering os.walk() dirs and files":
#   https://stackoverflow.com/a/51871627/1896134
# NOTE: THIS WILL NOT CREATE THE DESTINATION FOLDER(S)
#
# Improvements THANKS TO:
#
# "Use endswith with multiple extensions"
#   https://stackoverflow.com/a/22812835/1896134
#
# "Normalize a pathname by collapsing redundant separators"
#   https://docs.python.org/3/library/os.path.html#os.path.normpath
#
# "Styling multi-line conditions in 'if' statements?"
#   https://stackoverflow.com/a/181557/1896134
#
#
# "Python: Line that does not start with #"
#   https://stackoverflow.com/a/34129925/1896134
#
# "What is the easiest way to get all strings that do not start with a char?"
#   https://stackoverflow.com/a/6763438/1896134
#
# Updated naming convention for `for loop` based on
# "Python os.walk skip directories with specific name instead of path"
#   https://stackoverflow.com/a/38928455/1896134
# =============================================================================

import getpass

from os import path
from os import walk
from shutil import move

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
    for dirpath, dirnames, filenames in walk(search_dir, topdown=True):
        for file in filenames:
            if (not (str(dirpath) + '/').startswith(tuple(exclude_foldr))):
                if (file.endswith(tuple(includes_file_extensn))):
                    filetomove = path.normpath(str(dirpath) + '/' +
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
                    #       str(dirpath) + str(file))
                    pass
            else:
                pass


if __name__ == '__main__':
    organize_files()
