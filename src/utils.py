import random
import re
import string
import time
from functools import lru_cache
from src.const import *
import requests

regex_name = '^[A-Za-z_][A-Za-z0-9_]*'
regex_username = '^[A-Za-z][A-Za-z0-9]*'


def is_valid_name(str, max_length=NAME_MAX_LENGTH, min_length=0):
    if str is None:
        return False

    if len(str) > max_length or len(str) < min_length:
        return False

    if re.search(regex_name, str):
        return True
    else:
        return False


def is_valid_username(str, max_length=20, min_length=0):
    if str is None:
        return False

    if len(str) > max_length or len(str) < min_length:
        return False

    if re.search(regex_name, str):
        return True
    else:
        return False


def validate_phone(phone):
    if phone is None:
        return None

    result = re.sub('\D', '', phone)

    if len(str) == PHONE_LENGTH:
        return result

    return None


def is_url_image(image_url):

    r = requests.head(image_url)
    if r.headers[CONTENT_TYPE] in IMAGE_FORMATS:
        return True
    return False


def random_string(length=None):
    if length is None:
        length = random.randint(5, 20)

    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k=length)))


def get_current_datetime():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def get_username_from_email(email):
    return email.split("@")[0]


def equal(thing1, thing2):
    if str(thing1) == str(thing2):
        return True
    return False


def lev_dist(string1, string2):
    '''
    This function will calculate the levenshtein distance between two input
    strings a and b

    params:
        a (String) : The first string you want to compare
        b (String) : The second string you want to compare

    returns:
        This function will return the distnace between string a and b.

    example:
        a = 'stamp'
        b = 'stomp'
        lev_dist(a,b)
        >> 1.0
    '''

    @lru_cache(None)  # for memorization
    def min_dist(s1, s2):

        if s1 == len(string1) or s2 == len(string2):
            return len(string1) - s1 + len(string2) - s2

        # no change required
        if string1[s1] == string2[s2]:
            return min_dist(s1 + 1, s2 + 1)

        return 1 + min(
            min_dist(s1, s2 + 1),      # insert character
            min_dist(s1 + 1, s2),      # delete character
            min_dist(s1 + 1, s2 + 1),  # replace character
        )

    return min_dist(0, 0)
