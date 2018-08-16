#!/bin/bash
# =============================================================================
# MAC OSX HIGH SIERRA 10.13.4 (17E199)
# Terminal: Version: 2.8.2 64-Bit (Intel): Yes
# Terminal Location: /Applications/Utilities/Terminal.app
# =============================================================================
# Terminal CLEAN UP YOUR DOCUMENTS FOLDER.
# =============================================================================
# START WHAT IS BELIEVED TO BE EMPTY NOW.
# =============================================================================
echo 'Searching Documents for empty folders...'
find ~/Documents -type d -empty;

# =============================================================================
# SHOW & THEN REMOVE ALL MAC OS DS_Store FILES
# =============================================================================

echo 'Searching Documents for DS_Store files...'
find ~/Documents -type f -name ".DS_Store" -print;

echo 'Removing DS_Store files...'
find ~/Documents -type f -name ".DS_Store" -print -delete;

# =============================================================================
# SHOW & THEN REMOVE ALL MAC OS pyc FILES
# =============================================================================

echo 'Searching Documents for pyc files...'
find ~/Documents -type f -name ".pyc" -print;

echo 'Removing pyc files...'
find ~/Documents -type f -name ".pyc" -print -delete;

# =============================================================================
# SHOW & THEN REMOVE ALL MAC OS ZERO SIZED FILES
# =============================================================================
echo 'Searching Documents for ZERO file sized files...'
find ~/Documents -type f -empty;

echo 'Removing ZERO file sized files...'
find ~/Documents -type f -empty -delete;

# =============================================================================
# SHOW & THEN REMOVE Icon^M FILES
# USE THE ? MARK FOR EASE OF USE YOU CAN ALSO SUB 'CTRL + V & CTRL + M' FOR ^M
# =============================================================================

echo 'Searching Documents for Icon files...'
find ~/Documents -type f -name 'Icon?' -print;

echo 'Removing Icon files from Documents...'
find ~/Documents -type f -name 'Icon?' -print -delete;

# SEEMINGLY THE SAME AS
# find ~/Documents -type f -size 0 -print
# find ~/Documents -type f -size 0 -print -delete

# =============================================================================
# SHOWCASE NEW FOUND EMPTY FOLDERS
# =============================================================================
echo 'Showcasing new result of existing and new found empty folders...'
find ~/Documents -type d -empty;

echo 'Deleting result of empty folders...'
find ~/Documents -type d -empty -delete;

echo 'Showcasing the removal of said, 'empty folders'...'
find ~/Documents -type d -empty;

# =============================================================================
# SHOWCASE ALL COMMANDS
# =============================================================================

# echo 'Searching Documents for empty folders...'
# find ~/Documents -type d -empty;
# echo 'Searching Documents for DS_Store files...'
# find ~/Documents -type f -name ".DS_Store" -print;
# echo 'Removing DS_Store files...'
# find ~/Documents -type f -name ".DS_Store" -print -delete;
# echo 'Searching Documents for pyc files...'
# find ~/Documents -type f -name ".pyc" -print;
# echo 'Removing pyc files...'
# find ~/Documents -type f -name ".pyc" -print -delete;
# echo 'Searching Documents for ZERO file sized files...'
# find ~/Documents -type f -empty;
# echo 'Removing ZERO file sized files...'
# find ~/Documents -type f -empty -delete;
# echo 'Searching Documents for Icon files...'
# find ~/Documents -type f -name 'Icon?' -print;
# echo 'Removing Icon files from Documents...'
# find ~/Documents -type f -name 'Icon?' -print -delete;
# echo 'Showcasing new result of existing and new found empty folders...'
# find ~/Documents -type d -empty;
# echo 'Deleting result of empty folders...'
# find ~/Documents -type d -empty -delete;
# echo 'Showcasing the removal of said, 'empty folders'...'
# find ~/Documents -type d -empty;
