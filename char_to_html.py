#!/usr/bin/env python3
# =============================================================================
# Created On  : MAC OSX High Sierra 10.13.6 (17G65)
# Created On  : Python 3.7.0
# Created By  : Jeromie Kirchoff
# Created Date: Mon May 14 21:46:03 PDT 2018
# =============================================================================
"""THE MODULE HAS BEEN BUILD FOR CONVERTING ALL CHARACTERS TO HTML UNICODE."""
# =============================================================================
import re


def cleantext(text):
    """
    THE MODULE HAS BEEN BUILD to Replace non-ASCII characters with...

    printable ASCII.
    Use HTML entities when possible.
    started from
    https://secure.hens-teeth.net/orders/knowledgebase/74/Cleaning-Special-Characters-from-Product-Text-Files.html
    https://www.toptal.com/designers/htmlarrows/
    http://www.thepunctuationguide.com/hyphen-and-dashes.html
    """
    # text = re.sub(r'[\x00-\x1f\x80-\xff]', ' ', text)
    # The line above is a hard-core line that strips everything else.
    text = re.sub(r'\x85', 'U+02026', text)  # replace ellipses
    text = re.sub(r'\x91', "‘", text)  # replace left single quote
    text = re.sub(r'\x92', "’", text)  # replace right single quote
    text = re.sub(r'\x93', '“', text)  # replace left double quote
    text = re.sub(r'\x94', '”', text)  # replace right double quote
    text = re.sub(r'\x95', '•', text)  # replace bullet
    text = re.sub(r'\x96', '-', text)  # replace bullet
    text = re.sub(r'\x99', 'U+02122', text)  # replace TM
    text = re.sub(r'\xae', 'U+000AE', text)  # replace (R)
    text = re.sub(r'\xb0', 'U+000B0', text)  # replace degree symbol
    text = re.sub(r'\xba', 'U+000B0', text)  # replace degree symbol
    text = re.sub(r'[\n|\r]+', ' ', text)  # remove embedded \n and \r

    return

if __name__ == '__main__':
    cleantext("\n")
