#!/usr/bin/env python3
# =============================================================================
# Created On  : MAC OSX High Sierra 10.14.2 (18C54)
# Created On  : Python 3.7.2
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jan 25 13:44:00 PST8PDT 2019
# =============================================================================
"""THE MODULE HAS BEEN BUILD FOR CONVERTING ALL CHARACTERS TO HTML UNICODE."""
# =============================================================================

def fizzybuzzy():
    """Placeholder."""
    i = 1
    while i < 101:
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)
        i += 1

if __name__ == '__main__':
    fizzybuzzy()
