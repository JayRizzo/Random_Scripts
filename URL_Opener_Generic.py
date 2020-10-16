#!/usr/bin/env python3
# =============================================================================
# Created On  :
# Created On  : Python 3.8.1
# Created By  : Jeromie Kirchoff
# Created Date: Mon October 15 21:00:00 PDT 2020
# Updated Date: Mon October 15 21:00:00 PDT 2020
# =============================================================================
from pyautogui import prompt
import logging
import re
import webbrowser

# Create and configure logger
logging.basicConfig(filename='foo.log',
                    format='%(asctime)s_%(levelname)s:    %(message)s', datefmt='%Y%m%d__%H%M%S',
                    filemode='a+',   # create/append/write to same file every time
                    # filemode='w',  # Write to new file every time.
                    level=logging.DEBUG)
FOO_LOGGER = logging.getLogger('simple_example')


class URLOpener:
    """Prompt & iterate thru any urls with numbers in the URL.."""

    def __init__(self):
        """Defaults."""
        FOO_LOGGER.info("BEGIN")
        self.list_of_ints = prompt(
            text='Launch URLs By List Of ID(s) (Comma or space separated):',
            title='Launch Browser By ID')
        self.clean_list = re.findall(r'\d+', self.list_of_ints)
        self.chrome_path_win = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe {}"
        self.chrome_path_mac = 'open -a /Applications/Google\\ Chrome.app'
        self.chrome_path_lnx = '/usr/bin/google-chrome'
        self.target_url_begin = 'https://Your_URL.hereTo/SomePath'
        self.target_url_end = 'someotherpathafter_variable'

    def main(self):
        """Open Urls in Succession in chrome"""
        for line in self.clean_list:
            target_url = "{}/{}/{}".format(self.target_url_begin,
                                           line, self.target_url_end)
            FOO_LOGGER.debug("target_url: {}".format(target_url))
            FOO_LOGGER.debug(
                "self.chrome_path_win: {}".format(self.chrome_path_win))
            webbrowser.get(self.chrome_path_win).open(target_url)



if __name__ == "__main__":
    x = URLOpener()
    x.main()

FOO_LOGGER.info("END")
