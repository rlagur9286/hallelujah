import json
import re
from django.utils.http import urlquote
import pymongo

# collection
def filter_getitem(value, arg):
    return value.get(arg, '')


def filter_getat(value, arg):
    try:
        return value[int(arg)]
    except Exception as e:
        return None


def filter_notinappend(a, b):
    if b not in a:
        a.append(b)
    return a


def filter_union(a, b):
    return set(a) | set(b)


def filter_featurs(items):
    if len(items) == 0: return ""
    for idx, item in enumerate(items[0].keys()):
        if idx == 0:
            result = "\"{}\"".format(item)
        else:
            result += ", \"{}\"".format(item)
    return "[{}]".format(result)


# math


def filter_divide(value, arg):
    return float(value) / float(arg)


def filter_mod(value, arg):
    return int(value) % int(arg)


def filter_min(a, b):
    return min(a, b)


def filter_max(a, b):
    return max(a, b)


# converting


def filter_int(value):
    return int(value)


def filter_float(a):
    return float(a)


# type


def filter_type(value):
    return str(type(value))


# str


def filter_endswith(value, arg):
    return value.endswith(arg)


def filter_quote(a):
    return urlquote(a)


# saturn-specific filters


# ------------------------------------------------------
# query classes
# ------------------------------------------------------
QCLASSES = {
    '0': 'BASIC',
    '1': 'NAVIGATION',
    '2': 'CATEGORY',
    '3': 'GEO_CAT',
    '4': 'HOST_PROP',
    '5': 'LONG',
    '6': 'VERY_LONG',
    '7': 'HIGHQC_ETC',
    '8': 'REFERENCE',
    '9': 'HOWTO',
    '10': 'PERSON',
    '11': 'PERSON_INFO'
}
def filter_qclass(value):
    return QCLASSES.get(value, 'NONE')


# ------------------------------------------------------
# cell background
# ------------------------------------------------------
LIST_PATTERN_DF = [
    r'.+_link$', r'^(?!boost|penalty).+_score$', r'.+_count$', r'.+_pv$', r'.+len$',
    'host_max_pr', 'arank', 'prank', 'is_curation', 'is_in_sitemap_file'
]
LIST_PATTERN_QDF = [r'^relevance.*', r'^qds.*', r'^mtr.*', r'^prox.*']
LIST_PATTERN_RRK = ['penalty_score', 'boost_score']
LIST_PATTERN_HL = [r'^colrank.*', 'source', 'page_type']

LIST_PATTERN_ALL = LIST_PATTERN_DF + LIST_PATTERN_QDF + LIST_PATTERN_RRK + LIST_PATTERN_HL
