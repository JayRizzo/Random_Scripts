#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""Module Built to To Read ID3 Track Data."""
# File Name: track_meta_id3.py
# =============================================================================
import time
from os import path
from eyed3 import id3
from eyed3 import load

CURRENT_HOME = path.expanduser('~')
SEARCH_DIR = path.join(CURRENT_HOME + "/Music/Music/Media.localized/Music/Thrice/Artist in the Ambulance/07 Hoods on Peregrine.mp3")  # noqa


def track_info(filename):
    """Module Built To Read ID3 Track Data."""
    tag = id3.Tag()
    tag.parse(filename)
    a = load(filename)
    print("# {}".format('=' * 78))
    print("Track Name:     {}".format(tag.title))
    print("Track Artist:   {}".format(tag.artist))
    print("Track Album:    {}".format(tag.album))
    print("Track Duration: {}".format(duration_from_seconds(a.info.time_secs)))
    print("Track Number:   {}".format(tag.track_num))
    print("Track BitRate:  {}".format(a.info.bit_rate))
    print("Track BitRate:  {}".format(a.info.bit_rate_str))
    print("Sample Rate:    {}".format(a.info.sample_freq))
    print("Mode:           {}".format(a.info.mode))
    print("# {}".format('=' * 78))
    print("Album Artist:         {}".format(tag.album_artist))
    print("Album Year:           {}".format(tag.getBestDate()))
    print("Album Recording Date: {}".format(tag.recording_date))
    print("Album Type:           {}".format(tag.album_type))
    print("Disc Num:             {}".format(tag.disc_num))
    print("Artist Origin:        {}".format(tag.artist_origin))
    print("# {}".format('=' * 78))
    print("Artist URL:         {}".format(tag.artist_url))
    print("Audio File URL:     {}".format(tag.audio_file_url))
    print("Audio Source URL:   {}".format(tag.audio_source_url))
    print("Commercial URL:     {}".format(tag.commercial_url))
    print("Copyright URL:      {}".format(tag.copyright_url))
    print("Internet Radio URL: {}".format(tag.internet_radio_url))
    print("Publisher URL:      {}".format(tag.publisher_url))
    print("Payment URL:        {}".format(tag.payment_url))
    print("# {}".format('=' * 78))
    print("Publisher: {}".format(tag.publisher))
    print("Original Release Date: {}".format(tag.original_release_date))
    print("Play Count: {}".format(tag.play_count))
    print("Tagging Date: {}".format(tag.tagging_date))
    print("Release Date: {}".format(tag.release_date))
    print("Terms Of Use: {}".format(tag.terms_of_use))
    print("isV1: {}".format(tag.isV1()))
    print("isV2: {}".format(tag.isV2()))
    print("BPM: {}".format(tag.bpm))
    print("Cd Id: {}".format(tag.cd_id))
    print("Composer: {}".format(tag.composer))
    print("Encoding date: {}".format(tag.encoding_date))
    print("# {}".format('=' * 78))
    print("Genre: {}".format(tag.genre.name))
    print("Non Std Genre Name: {}".format(tag.non_std_genre.name))
    print("Genre ID: {}".format(tag.genre.id))
    print("Non Std Genre ID: {}".format(tag.non_std_genre.id))
    print("LAME Tag:       {}".format(a.info.lame_tag))
    print("# {}".format('=' * 78))
    print("Header Version: {}".format(tag.header.version))
    print("Header Major Version: {}".format(tag.header.major_version))
    print("Header Minor Version: {}".format(tag.header.minor_version))
    print("Header Rev Version: {}".format(tag.header.rev_version))
    print("Header Extended: {}".format(tag.header.extended))
    print("Header Footer: {}".format(tag.header.footer))
    print("Header Experimental: {}".format(tag.header.experimental))
    print("Header SIZE: {}".format(tag.header.SIZE))
    print("Header Tag Size: {}".format(tag.header.tag_size))
    print("Extended Header Size: {}".format(tag.extended_header.size))
    print("# {}".format('=' * 78))
    print("File Name: {}".format(tag.file_info.name))
    print("File Tag Size: {}".format(tag.file_info.tag_size))
    print("File Tag Padding Size: {}".format(tag.file_info.tag_padding_size))
    print("File Read Only: {}".format(tag.read_only))
    print("File Size: {}".format(a.info.size_bytes))
    print("Last Modified: {}".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(tag.file_info.mtime))))
    print("Last Accessed: {}".format(time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(tag.file_info.atime))))
    print("# {}".format('=' * 78))


def duration_from_seconds(s):
    """Module to get the convert Seconds to a time like format."""
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
    return TIMELAPSED


track_info(SEARCH_DIR)



"""Example Result:
# ==============================================================================
Track Name:     Hoods on Peregrine
Track Artist:   Thrice
Track Album:    Artist in the Ambulance
Track Duration: 000:00:08:05
Track Number:   (7, 12)
Track BitRate:  (False, 56)
Track BitRate:  56 kb/s
Sample Rate:    22050
Mode:           Mono
# ==============================================================================
Album Artist:         Thrice
Album Year:           2003-03-20
Album Recording Date: 2003-03-20
Album Type:           None
Disc Num:             (1, 1)
Artist Origin:        None
# ==============================================================================
Artist URL:         None
Audio File URL:     None
Audio Source URL:   None
Commercial URL:     None
Copyright URL:      None
Internet Radio URL: None
Publisher URL:      None
Payment URL:        None
# ==============================================================================
Publisher: Island
Original Release Date: None
Play Count: None
Tagging Date: None
Release Date: None
Terms Of Use: None
isV1: False
isV2: True
BPM: None
Cd Id: None
Composer: Dustin Kensrue/Thrice
Encoding date: None
# ==============================================================================
Genre: Hard Rock
Non standard genre name: (79)
Non Std Genre Name: (79)
Genre ID: 79
Non standard genre name: (79)
Non Std Genre ID: None
LAME Tag:       {}
# ==============================================================================
Header Version: (2, 3, 0)
Header Major Version: 2
Header Minor Version: 3
Header Rev Version: 0
Header Extended: False
Header Footer: False
Header Experimental: False
Header SIZE: 10
Header Tag Size: 50115
Extended Header Size: 0
# ==============================================================================
File Name: /Users/jkirchoff/Music/Music/Media.localized/Music/Thrice/Artist in the Ambulance/07 Hoods on Peregrine.mp3
File Tag Size: 50125
File Tag Padding Size: 9148
File Read Only: False
File Size: 3438639
Last Modified: 2012-06-10 00:55:24
Last Accessed: 2021-01-01 22:23:06
# ==============================================================================
"""
