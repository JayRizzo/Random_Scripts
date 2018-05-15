#!/usr/bin/env python3

# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.4 (17E199)
# Created By  : Jeromie Kirchoff
# Created Date: Mon May 14 21:46:03 PDT 2018
# =============================================================================
# Answer for: https://stackoverflow.com/a/23561726/1896134 PNG Archive
# NOTE: THIS WILL NOT CREATE THE DESTINATION FOLDER(S)
# =============================================================================

import os
import shutil

file_extensn = '.png'
mac_username = 'jkirchoff'

search_dir = '/Users/' + mac_username + '/Desktop/'
target_foldr = '/Users/' + mac_username + '/Pictures/Archive/'
ignore_fldrs = [target_foldr,
                '/Users/' + mac_username + '/Documents/',
                '/Users/' + mac_username + '/AnotherFolder/'
                ]

for subdir, dirs, files in os.walk(search_dir):
    for file in files:
        if subdir not in ignore_fldrs and file.endswith(file_extensn):
            # print('I would Move this file: ' + str(subdir) + str(file)
            #       # + "\n To this folder:" + str(target_foldr) + str(file)
            #       )

            filetomove = (str(subdir) + str(file))
            movingfileto = (str(target_foldr) + str(file))
            print("filetomove: " + str(filetomove))
            print("movingfileto: " + str(movingfileto))

            # =================================================================
            # IF YOU ARE HAPPY WITH THE RESULTS
            # UNCOMMENT THE SHUTIL TO MOVE THE FILES
            # =================================================================
            # shutil.move(filetomove, movingfileto)

            pass
        elif file.endswith(file_extensn):
            # print('Theres no need to move these files: '
            #       + str(subdir) + str(file))
            pass
        else:
            # print('Theres no need to move these files either: '
            #       + str(subdir) + str(file))
            pass
